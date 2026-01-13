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

def detect_question_type(q_text):
    """
    Detect question type based on keywords in question text.
    Returns: (type, required_answers)
    """
    text_lower = q_text.lower()
    
    # Ordering questions
    if "select and order" in text_lower:
        # Extract number: "Select and order THREE" -> 3
        match = re.search(r'select and order (\w+)', text_lower)
        if match:
            word = match.group(1)
            num_map = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
            count = num_map.get(word, 3)
        else:
            count = 3
        return ("ordering", count)
    
    # Multiple Response questions
    if "select two" in text_lower:
        return ("multiple_response", 2)
    if "select three" in text_lower:
        return ("multiple_response", 3)
    
    # Default: Multiple Choice
    return ("multiple_choice", 1)


def parse_questions_new_format(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    questions = []
    
    # Find all question starts "Q<number>"
    starts = [m.start() for m in re.finditer(r'^Q\d+\s*$', text, re.MULTILINE)]
    starts.append(len(text))  # End of file
    
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
            q_text_match = re.search(r'Câu hỏi:(.*?)(?=\n\*|\n\d+\.\t|\nĐáp án đúng:)', content, re.DOTALL)
            if not q_text_match:
                print(f"Skipping Q{q_id}: 'Câu hỏi:' not found or format issue.")
                continue
                
            q_text = q_text_match.group(1).strip()
            
            # Detect question type
            q_type, required_answers = detect_question_type(q_text)
            
            # Split content into lines to process statefully
            lines_content = content.replace('\r\n', '\n').split('\n')
            
            current_section = "question"
            q_text_lines = []
            options_map = {}  # { "A": ["line1", "line2"], ... }
            ordering_steps = []  # For ordering questions: [{"step": 1, "text": "..."}, ...]
            current_opt_id = None
            current_step_num = None
            full_answer_text = ""
            
            for idx, line in enumerate(lines_content):
                strip_line = line.strip()
                
                # Check for Answer trigger
                if "Đáp án đúng:" in line:
                    current_section = "answer"
                    ans_part = line.split("Đáp án đúng:", 1)[1].strip()
                    full_answer_text += ans_part
                    continue
                
                if current_section == "answer":
                    full_answer_text += " " + strip_line
                    continue
                
                # Check for Option trigger (Multiple Choice / Multiple Response)
                opt_match = re.match(r'^\*\s*([A-E])\.?\s*(.*)', strip_line)
                if opt_match:
                    current_section = "option"
                    current_opt_id = opt_match.group(1)
                    options_map[current_opt_id] = [opt_match.group(2).strip()]
                    continue
                
                # Check for Ordering step trigger: "1.	Step text" or "1.  Step text"
                step_match = re.match(r'^(\d+)\.\s+(.*)', strip_line)
                if step_match and q_type == "ordering":
                    current_section = "ordering_step"
                    current_step_num = int(step_match.group(1))
                    step_text = step_match.group(2).strip()
                    ordering_steps.append({"step": current_step_num, "text": step_text})
                    continue
                
                # Check for Question text (start)
                if "Câu hỏi:" in line:
                    q_text_part = line.split("Câu hỏi:", 1)[1].strip()
                    q_text_lines.append(q_text_part)
                    continue
                
                # Handling continuations
                if current_section == "question":
                    if strip_line:
                        q_text_lines.append(strip_line)
                elif current_section == "option":
                    if strip_line and current_opt_id:
                        options_map[current_opt_id].append(strip_line)
                elif current_section == "ordering_step":
                    if strip_line and ordering_steps:
                        ordering_steps[-1]["text"] += " " + strip_line
            
            # Reconstruct question text
            q_text = ' '.join(q_text_lines).strip()
            
            # Build options list
            options = []
            if q_type == "ordering" and ordering_steps:
                # For ordering: use steps as options
                for step in ordering_steps:
                    options.append({
                        "id": str(step["step"]),
                        "text": step["text"]
                    })
            else:
                # Standard A/B/C/D options
                for opt_id in sorted(options_map.keys()):
                    opt_text = ' '.join(options_map[opt_id]).strip()
                    options.append({
                        "id": opt_id,
                        "text": opt_text
                    })
            
            # Parse Answer
            explanation = full_answer_text.strip()
            correct_answer = "?"
            
            if q_type == "ordering":
                # For ordering, answer is the sequence like "1,2,3" or parsed from "Step 1:..., Step 2:..."
                # The answer format in source is: "1. Step 1: ..., 2. Step 2: ..."
                # We'll store the correct order as comma-separated step numbers
                step_order = re.findall(r'Step (\d+):', explanation)
                if step_order:
                    correct_answer = ",".join(step_order)
                else:
                    correct_answer = ",".join([str(s["step"]) for s in ordering_steps])
            elif q_type == "multiple_response":
                # Extract multiple letters from patterns like:
                # "A. ... AND C. ..." or "A and B" or "A. ... AND B. ..."
                # Look for pattern: Letter followed by "." and later "AND" followed by another Letter
                # Search in the entire explanation text
                
                # First try to find explicit "AND" pattern
                and_pattern = re.findall(r'\b([A-E])\.\s.*?AND\s+([A-E])\.', explanation, re.IGNORECASE | re.DOTALL)
                if and_pattern:
                    # Flatten tuples and get unique letters
                    letters = list(and_pattern[0])  # e.g., ('A', 'C')
                    correct_answer = ",".join(letters)
                else:
                    # Fallback: find all standalone letters at start of sentences
                    letters = re.findall(r'(?:^|\.\s+)([A-E])\.', explanation)
                    if len(letters) >= required_answers:
                        correct_answer = ",".join(letters[:required_answers])
                    else:
                        # Last resort: find all letters in first 200 chars
                        letters = re.findall(r'\b([A-E])\b', explanation[:200])
                        correct_answer = ",".join(letters[:required_answers]) if letters else "?"
            else:
                # Single choice
                clean_ans = explanation.lstrip(" .:")
                match_letter = re.match(r'^([A-E])[\.\s]', clean_ans)
                if match_letter:
                    correct_answer = match_letter.group(1)
                elif len(clean_ans) >= 1 and clean_ans[0] in "ABCDE":
                    correct_answer = clean_ans[0]

            questions.append({
                "id": q_id,
                "type": q_type,
                "required_answers": required_answers,
                "question": q_text,
                "options": options,
                "answer": correct_answer,
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
            
            # Add question type badge
            if q['type'] == "multiple_response":
                f.write(f"!!! warning \"Select {q['required_answers']}\"\n\n")
            elif q['type'] == "ordering":
                f.write(f"!!! warning \"Ordering - Arrange {q['required_answers']} Steps\"\n\n")
            
            f.write(f"{q['question']}\n\n")
            
            # Render options based on type
            if q['type'] == "ordering":
                for opt in q['options']:
                    f.write(f"- **Step {opt['id']}.** {opt['text']}\n")
            else:
                for opt in q['options']:
                    f.write(f"- **{opt['id']}.** {opt['text']}\n")
            
            f.write("\n")
            
            # Use MkDocs Admonition (collapsible) for the answer
            f.write("??? success \"Reveal Answer\"\n")
            f.write(f"    **Correct Answer: {q['answer']}**\n\n")
            
            # Handle explanation indentation for Admonition
            if q['explanation']:
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
