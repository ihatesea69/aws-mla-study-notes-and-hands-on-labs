import re
import json
import os

# Configuration
SOURCE_FILE = r"c:\Users\LENOVO\Desktop\aws-mla-study-notes-and-hands-on-labs\65 Mock Test.txt"
JSON_OUTPUT = r"c:\Users\LENOVO\Desktop\aws-mla-study-notes-and-hands-on-labs\docs\assets\questions.json"
MARKDOWN_OUTPUT = r"c:\Users\LENOVO\Desktop\aws-mla-study-notes-and-hands-on-labs\docs\practice-exams\exam-01.md"
DELETE_FILES = [
    r"c:\Users\LENOVO\Desktop\aws-mla-study-notes-and-hands-on-labs\docs\practice-exams\exam-02.md"
]

def parse_questions_new_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by "Q" followed by digits at start of line or after newline
    # Regex: \nQ\d+ or ^Q\d+
    # But some might have spaces? Let's check the file content looked like "Q1\nCâu hỏi:..."
    
    # We can split by regex \nQ\d+(\r?\n|$)
    chunks = re.split(r'\nQ\d+(?:\r?\n|$)', text)
    
    # The first chunk is header or empty
    if "uvTổng hợp" in chunks[0] or not chunks[0].strip():
        chunks.pop(0)

    # Note: re.split consumes the delimiter. We might lose Q number if we don't capture it.
    # Alternative: iterate line by line or use finditer.
    # Let's try a regex that captures the full block.
    
    # Pattern:
    # Q<id>
    # Câu hỏi: <text>
    # <Options>
    # Đáp án đúng: ...
    
    questions = []
    
    # We will iterate through the text using a state machine approach or regex blocks because split is tricky with capturing.
    # Actually, simpler: finding all starts "Q<number>"
    
    starts = [m.start() for m in re.finditer(r'^Q\d+\s*$', text, re.MULTILINE)]
    starts.append(len(text)) # End of file
    
    for i in range(len(starts) - 1):
        block = text[starts[i]:starts[i+1]].strip()
        lines = block.split('\n')
        
        try:
            # Line 0 is like "Q1" or "Q1 "
            q_id_match = re.search(r'Q(\d+)', lines[0])
            if q_id_match:
                q_id = int(q_id_match.group(1))
            else:
                q_id = i + 1
            
            content = '\n'.join(lines[1:])
            
            # Extract Question Text
            # Starts with "Câu hỏi:"
            # Ends before the first Option "*"
            
            # Regex for parts
            # 1. Question Text
            q_text_match = re.search(r'Câu hỏi:(.*?)(?=\n\*|\nĐáp án đúng:)', content, re.DOTALL)
            if not q_text_match:
                # Fallback: maybe no "Câu hỏi:" prefix in some? Or options start differently?
                # Based on file, "Câu hỏi:" seems consistent.
                print(f"Skipping Q{q_id}: 'Câu hỏi:' not found or format issue.")
                continue
                
            q_text = q_text_match.group(1).strip()
            
            # 2. Options & Answer Parsing
            # We need to scan the content line by line to handle multi-line options
            
            # Split content into lines to process statefully
            lines_content = content.replace('\r\n', '\n').split('\n')
            
            current_section = "question"
            q_text_lines = []
            options_map = {} # { "A": ["line1", "line2"], ... }
            current_opt_id = None
            answer_line_index = -1
            
            # Find where "Đáp án đúng:" starts to stop option parsing
            for idx, line in enumerate(lines_content):
                if "Đáp án đúng:" in line:
                    answer_line_index = idx
                    break
            
            # If we found answer line, restrict content processing up to that point for Q&Options
            # But wait, answer itself might be multi-line.
            # Let's process systematically.
            
            full_answer_text = ""
            
            for idx, line in enumerate(lines_content):
                strip_line = line.strip()
                
                # Check for Answer trigger
                if "Đáp án đúng:" in line:
                    current_section = "answer"
                    # Capture the part after the colon
                    ans_part = line.split("Đáp án đúng:", 1)[1].strip()
                    full_answer_text += ans_part
                    continue
                
                if current_section == "answer":
                    full_answer_text += " " + strip_line
                    continue
                
                # Check for Option trigger
                # Pattern: * A. text or * A.text or *A. text
                # We also need to handle cases where it might just be "A." without star if the format varies, 
                # but based on file it seems to use *.
                opt_match = re.match(r'^\*\s*([A-E])\.?\s*(.*)', strip_line)
                if opt_match:
                    current_section = "option"
                    current_opt_id = opt_match.group(1)
                    options_map[current_opt_id] = [opt_match.group(2).strip()]
                    continue
                
                # Check for Question text (start)
                if "Câu hỏi:" in line:
                    # Logic handled previously? No, we are iterating `content` which already stripped Q ID.
                    # But `content` was `\n'.join(lines[1:])` from previous logic.
                    # In `lines_content`, this line exists.
                    # We might have "Câu hỏi: Blah..."
                    q_text_part = line.split("Câu hỏi:", 1)[1].strip()
                    q_text_lines.append(q_text_part)
                    continue
                
                # Handling continuations
                if current_section == "question":
                    if strip_line: # ignore empty lines if we want, or keep them
                         q_text_lines.append(strip_line)
                elif current_section == "option":
                    if strip_line and current_opt_id:
                        options_map[current_opt_id].append(strip_line)
            
            # Reconstruct
            q_text = ' '.join(q_text_lines).strip()
            
            options = []
            for opt_id in sorted(options_map.keys()):
                # Join lines with space
                opt_text = ' '.join(options_map[opt_id]).strip()
                options.append({
                    "id": opt_id,
                    "text": opt_text
                })
            
            # Parse Answer
            explanation = full_answer_text.strip()
            correct_option = "?"
            # Try to extract leading letter
            # Typically "D. Optimize..."
            # Remove any leading punctuation or space
            clean_ans = explanation.lstrip(" .:")
            match_letter = re.match(r'^([A-E])[\.\s]', clean_ans)
            if match_letter:
                correct_option = match_letter.group(1)
            elif len(clean_ans) == 1 and clean_ans in "ABCDE":
                correct_option = clean_ans 

            questions.append({
                "id": q_id,
                "question": q_text,
                "options": options,
                "answer": correct_option,
                "explanation": explanation
            })
            
        except Exception as e:
            print(f"Error parsing Q at index {i}: {e}")
            
    return questions

def save_json(questions, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(questions)} questions to JSON.")

def save_markdown(questions, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# Practice Exam 01\n\n")
        f.write("!!! info \"Exam Details\"\n")
        f.write(f"    - **Total Questions**: {len(questions)}\n")
        f.write(f"    - **Estimated Time**: ~{len(questions) * 2} minutes\n")
        f.write(f"    - **Passing Score**: 72%\n\n")
        
        for q in questions:
            f.write(f"## Question {q['id']}\n\n")
            f.write(f"{q['question']}\n\n")
            
            # Use a list for options to ensure proper separation
            for opt in q['options']:
                # Bold the Option ID (A, B, C...) for visibility
                f.write(f"- **{opt['id']}.** {opt['text']}\n")
            
            f.write("\n")
            
            # Use MkDocs Admonition (collapsible) for the answer
            f.write("??? success \"Reveal Answer\"\n")
            f.write(f"    **Correct Answer: {q['answer']}**\n\n")
            
            # Handle explanation indentation for Admonition
            if q['explanation']:
                # Indent every line of explanation by 4 spaces
                explanation_indented = q['explanation'].replace('\n', '\n    ')
                f.write(f"    {explanation_indented}\n")
            else:
                f.write("    No detailed explanation provided.\n")
                
            f.write("\n---\n\n")
            
    print(f"Saved {len(questions)} questions to Markdown.")

def cleanup_files():
    for fpath in DELETE_FILES:
        if os.path.exists(fpath):
            try:
                os.remove(fpath)
                print(f"Deleted old file: {fpath}")
            except Exception as e:
                print(f"Error deleting {fpath}: {e}")

if __name__ == "__main__":
    if os.path.exists(SOURCE_FILE):
        qs = parse_questions_new_format(SOURCE_FILE)
        save_json(qs, JSON_OUTPUT)
        save_markdown(qs, MARKDOWN_OUTPUT)
        cleanup_files()
    else:
        print(f"Source file not found: {SOURCE_FILE}")
