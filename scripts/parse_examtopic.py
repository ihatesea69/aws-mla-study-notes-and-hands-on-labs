#!/usr/bin/env python3
"""
Parser for Examtopic format exam questions.
Parses the "Dump MLA-C01 Examtopic Detail Explain Vietnamese" format.
"""

import re
import json
import os

def parse_examtopic_questions(filepath):
    """Parse questions from Examtopic format file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by "Question #:" pattern
    question_blocks = re.split(r'Question #:\s*(\d+)', content)
    
    questions = []
    i = 1  # Start from index 1 (skip header before first question)
    
    while i < len(question_blocks) - 1:
        q_num = int(question_blocks[i].strip())
        q_text = question_blocks[i + 1]
        i += 2
        
        # Detect question type
        q_type = "multiple_choice"
        required_answers = 1
        
        if re.search(r'Select (?:and order|TWO|THREE|two|three)', q_text, re.IGNORECASE):
            if re.search(r'(?:Select and order|order the)', q_text, re.IGNORECASE):
                q_type = "ordering"
                match = re.search(r'(?:order|Select)\s+(?:THREE|three|3)', q_text)
                required_answers = 3 if match else 3
            elif re.search(r'Select (?:TWO|two|2)', q_text, re.IGNORECASE):
                q_type = "multiple_response"
                required_answers = 2
            elif re.search(r'Select (?:THREE|three|3)', q_text, re.IGNORECASE):
                q_type = "multiple_response"
                required_answers = 3
        
        # Check for matching questions
        if re.search(r'(?:Select the correct .* term|Select the correct .* for each)', q_text, re.IGNORECASE):
            if not re.search(r'\*\s*[A-E]\.', q_text):  # No A/B/C/D options
                q_type = "matching"
        
        # Extract question text (before options)
        question_match = re.search(r'(?:Case [Ss]tudy\s*-?\s*)?(.*?)(?=\*\s*[A-E]\.|Options List:|Analysis)', q_text, re.DOTALL)
        question_text = ""
        if question_match:
            question_text = question_match.group(1).strip()
            # Clean up
            question_text = re.sub(r'^Câu hỏi:\s*', '', question_text)
            question_text = re.sub(r'^Scenario:\s*', '', question_text)
            question_text = re.sub(r'^Task:\s*', '', question_text)
            question_text = re.sub(r'\s+', ' ', question_text).strip()
        
        # Extract options
        options = []
        option_matches = re.findall(r'\*\s*([A-E])\.\s*(.+?)(?=\*\s*[A-E]\.|Dưới đây|Answer\s*:|Đáp án)', q_text, re.DOTALL)
        
        for opt_id, opt_text in option_matches:
            opt_text = re.sub(r'\s+', ' ', opt_text).strip()
            options.append({"id": opt_id, "text": opt_text})
        
        # Extract answer
        answer = "?"
        answer_match = re.search(r'Answer\s*:\s*(?:Option\s*)?([A-E])', q_text)
        if answer_match:
            answer = answer_match.group(1)
        else:
            # Try Vietnamese format
            answer_match = re.search(r'Đáp án\s*(?:đúng)?:\s*(?:Option\s*)?([A-E])', q_text)
            if answer_match:
                answer = answer_match.group(1)
        
        # For multiple response, try to find multiple answers
        if q_type == "multiple_response":
            # Look for patterns like "A and C" or multiple letters in answer section
            multi_match = re.search(r'Answer\s*:\s*.*?([A-E]).*?(?:and|,)\s*([A-E])', q_text, re.IGNORECASE)
            if multi_match:
                answer = f"{multi_match.group(1)},{multi_match.group(2)}"
        
        # Extract explanation
        explanation = ""
        explain_match = re.search(r'Explain:\s*(.*?)(?=Summary:|References:|Question #:|$)', q_text, re.DOTALL)
        if explain_match:
            explanation = explain_match.group(1).strip()
            # Clean up bullet points
            explanation = re.sub(r'\*\s*', '', explanation)
            explanation = re.sub(r'\s+', ' ', explanation).strip()
            # Limit length
            if len(explanation) > 2000:
                explanation = explanation[:2000] + "..."
        
        # For ordering questions, extract the correct order
        if q_type == "ordering":
            order_match = re.search(r'Thứ tự chính xác.*?(?:1\.\s*.*?2\.\s*.*?3\.\s*)', q_text, re.DOTALL)
            if order_match:
                # Extract step numbers
                steps = re.findall(r'(\d+)\.\s*(.+?)(?=\d+\.|$)', order_match.group(0), re.DOTALL)
                if steps:
                    answer = ",".join([s[0] for s in steps])
        
        question_obj = {
            "id": q_num,
            "type": q_type,
            "required_answers": required_answers,
            "question": question_text if question_text else f"Question {q_num}",
            "options": options,
            "answer": answer,
            "explanation": explanation
        }
        
        questions.append(question_obj)
    
    return questions


def save_questions_json(questions, output_path, start_id=66):
    """Save questions to JSON, adjusting IDs."""
    # Adjust IDs to continue from existing questions
    for i, q in enumerate(questions):
        q["id"] = start_id + i
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(questions)} questions to {output_path}")


def merge_with_existing(existing_path, new_questions, output_path):
    """Merge new questions with existing JSON file."""
    with open(existing_path, 'r', encoding='utf-8') as f:
        existing = json.load(f)
    
    # Get max ID from existing
    max_id = max(q["id"] for q in existing)
    
    # Adjust new question IDs
    for i, q in enumerate(new_questions):
        q["id"] = max_id + 1 + i
    
    # Merge
    merged = existing + new_questions
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    
    print(f"Merged {len(new_questions)} new questions. Total: {len(merged)}")
    return merged


def save_exam_markdown(questions, output_path, exam_title, start_idx=0, count=65):
    """Save a subset of questions as exam markdown."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    exam_questions = questions[start_idx:start_idx + count]
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"# {exam_title}\n\n")
        f.write("!!! info \"Exam Details\"\n")
        f.write(f"    - **Total Questions**: {len(exam_questions)}\n")
        f.write(f"    - **Estimated Time**: ~{len(exam_questions) * 2} minutes\n")
        f.write(f"    - **Passing Score**: 72%\n\n")
        
        for i, q in enumerate(exam_questions):
            f.write(f"## Question {i + 1}\n\n")
            f.write(f"{q['question']}\n\n")
            
            # Type badge for special questions
            if q['type'] == 'multiple_response':
                f.write(f"!!! warning \"Select {q['required_answers']}\"\n\n")
            elif q['type'] == 'ordering':
                f.write(f"!!! info \"Ordering\"\n\n")
            elif q['type'] == 'matching':
                f.write(f"!!! info \"Matching\"\n\n")
            
            # Options
            for opt in q['options']:
                f.write(f"- **{opt['id']}.** {opt['text']}\n")
            
            f.write("\n")
            
            # Answer section
            f.write("??? success \"Reveal Answer\"\n")
            f.write(f"    **Correct Answer: {q['answer']}**\n\n")
            
            if q['explanation']:
                exp_lines = q['explanation'].split('\n')
                for line in exp_lines:
                    f.write(f"    {line}\n")
            else:
                f.write("    No detailed explanation provided.\n")
            
            f.write("\n---\n\n")
    
    print(f"Saved {len(exam_questions)} questions to {output_path}")


if __name__ == "__main__":
    # Parse new questions
    input_file = "Dump MLA-C01 Examtopic Detail Explain Vietnamse 1 - 145.txt"
    
    print(f"Parsing {input_file}...")
    new_questions = parse_examtopic_questions(input_file)
    print(f"Parsed {len(new_questions)} questions")
    
    # Merge with existing
    existing_json = "docs/assets/questions.json"
    merged = merge_with_existing(existing_json, new_questions, existing_json)
    
    # Generate Exam 02 and Exam 03 markdown
    # Find where new questions start
    new_start = len(merged) - len(new_questions)
    
    # Exam 02: first 65 new questions
    save_exam_markdown(
        merged, 
        "docs/practice-exams/exam-02.md",
        "Practice Exam 02",
        start_idx=new_start,
        count=65
    )
    
    # Exam 03: next 65 questions
    save_exam_markdown(
        merged,
        "docs/practice-exams/exam-03.md", 
        "Practice Exam 03",
        start_idx=new_start + 65,
        count=65
    )
    
    # Remaining questions (if any) go to exam-04
    remaining = len(new_questions) - 130
    if remaining > 0:
        save_exam_markdown(
            merged,
            "docs/practice-exams/exam-04.md",
            "Practice Exam 04 (Bonus Questions)",
            start_idx=new_start + 130,
            count=remaining
        )
    
    print("Done!")
