import streamlit as st
import json
import random

def load_questions(questions_file_path):
    with open(questions_file_path, mode='r', encoding='utf-8') as json_file:
        questions_data = json.load(json_file)
    print(f"Data successfully loaded from {questions_file_path}")
    return questions_data


def load_answers(answers_file_path):
    with open(answers_file_path, "r") as file:
        answers_data = json.load(file)
    print(f"Data successfully loaded from {answers_file_path}")
    return answers_data


def load_questions_and_answers():
    questions, answers = None, None
    if st.session_state.school == "SZU":
        if st.session_state.subject == "Biology":
            questions = load_questions("resources/szu_biology_questions.json")
            answers = load_answers("resources/szu_biology_answers.json")
        if st.session_state.subject == "Chemistry":
            answers = load_answers("resources/szu_chemistry_answers.json")
            questions = load_questions("resources/szu_chemistry_questions.json")
    if st.session_state.school == "LFUK":
        if st.session_state.subject == "Biology":
            questions = load_questions("resources/lfuk_biology_questions.json")
            answers = load_answers("resources/lfuk_biology_answers.json")
        if st.session_state.subject == "Chemistry":
            answers = load_answers("resources/lfuk_chemistry_answers.json")
            questions = load_questions("resources/lfuk_chemistry_questions.json")
    return questions, answers


def load_data(start=None, end=None, size=None):
    questions, answers = load_questions_and_answers()

    filtered_questions = [item for item in questions if start <= item['id'] <= end]
    selected_questions = random.sample(filtered_questions, min(size, len(filtered_questions)))
    selected_questions.sort(key=lambda x: x['id'])
    selected_ids = {str(item['id']) for item in selected_questions}
    selected_answers = {key: value for key, value in answers.items() if key in selected_ids}

    st.session_state.answers = selected_answers
    st.session_state.questions = selected_questions


def select_random_answers(questions, correct_answers, num_options=4):
    selected_questions = []
    selected_correct_answers = {}

    for question in questions:
        q_id = str(question["id"])
        all_options = list(question["answers"].items())
        selected_options = sorted(random.sample(all_options, num_options))

        original_keys = sorted([opt[0] for opt in selected_options])
        new_keys = [chr(ord('A') + i) for i in range(num_options)]

        answer_mapping = dict(zip(new_keys, original_keys))
        renamed_answers = {new_keys[i]: selected_options[i][1] for i in range(num_options)}
        correct_values = [correct_answers[q_id][ord(original_keys[i]) - ord('A')] for i in range(num_options)]

        selected_questions.append({
            "id": question["id"],
            "question": question["question"],
            "answers": renamed_answers,
            "answer_mapping": answer_mapping
        })
        selected_correct_answers[q_id] = correct_values

    return selected_questions, selected_correct_answers


def load_test_data():
    st.session_state.subject = "Biology"
    b_questions, b_answers = load_questions_and_answers()
    st.session_state.subject = "Chemistry"
    c_questions, c_answers = load_questions_and_answers()

    if st.session_state.school == "SZU":
        number_of_questions = 80
    else:
        number_of_questions = 100

    # Biology
    selected_b_questions = random.sample(b_questions, number_of_questions)
    selected_b_questions.sort(key=lambda x: x['id'])
    selected_b_ids = {str(item['id']) for item in selected_b_questions}
    selected_b_answers = {key: value for key, value in b_answers.items() if key in selected_b_ids}

    if st.session_state.school == "LFUK":
        selected_b_questions, selected_b_answers = select_random_answers(selected_b_questions, selected_b_answers)

    st.session_state.b_questions = selected_b_questions
    st.session_state.b_answers = selected_b_answers

    # Chemistry
    selected_c_questions = random.sample(c_questions, number_of_questions)
    selected_c_questions.sort(key=lambda x: x['id'])
    selected_c_ids = {str(item['id']) for item in selected_c_questions}
    selected_c_answers = {key: value for key, value in c_answers.items() if key in selected_c_ids}

    if st.session_state.school == "LFUK":
        selected_c_questions, selected_c_answers = select_random_answers(selected_c_questions, selected_c_answers)

    st.session_state.c_questions = selected_c_questions
    st.session_state.c_answers = selected_c_answers
