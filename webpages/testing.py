import streamlit as st


def load_answer_images(q, school, subject):

    option_letter = "A"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['A']
    if q['answers']['A'].strip() == "":
        st.image(f"resources/images/{school}-{subject}-{q['id']}-{option_letter.lower()}.png")

    option_letter = "B"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['B']
    if q['answers']['B'].strip() == "":
        st.image(f"resources/images/{school}-{subject}-{q['id']}-{option_letter.lower()}.png")

    option_letter = "C"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['C']
    if q['answers']['C'].strip() == "":
        st.image(f"resources/images/{school}-{subject}-{q['id']}-{option_letter.lower()}.png")

    option_letter = "D"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['D']
    if q['answers']['D'].strip() == "":
        st.image(f"resources/images/{school}-{subject}-{q['id']}-{option_letter.lower()}.png")


def load_checkboxes_and_images(q, school, subject):

    selected_answers = []

    # Checkboxes
    option_letter = "A"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['A']
    if st.checkbox(f"{option_letter}. {q['answers']['A']}", key=f"{subject}_q{q['id']}_A"):
        selected_answers.append("A")

    option_letter = "B"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['B']
    if st.checkbox(f"{option_letter}. {q['answers']['B']}", key=f"{subject}_q{q['id']}_B"):
        selected_answers.append("B")

    option_letter = "C"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['C']
    if st.checkbox(f"{option_letter}. {q['answers']['C']}", key=f"{subject}_q{q['id']}_C"):
        selected_answers.append("C")

    option_letter = "D"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['D']
    if st.checkbox(f"{option_letter}. {q['answers']['D']}", key=f"{subject}_q{q['id']}_D"):
        selected_answers.append("D")

    # Images
    load_answer_images(q, school, subject)

    return selected_answers


def load_submitted_checkboxes_and_images(user_answers_boolean, correct_answers_boolean, actual_score, q, school, subject):

    option_letter = "A"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['A']
    if user_answers_boolean[0] == correct_answers_boolean[0]:
        st.checkbox(f"{option_letter}. {q['answers']['A']} ✅", key=f"{subject}_q{q['id']}_A", disabled=True, value=user_answers_boolean[0])
        actual_score += 1
    else:
        st.checkbox(f"{option_letter}. {q['answers']['A']} ❌", key=f"{subject}_q{q['id']}_A", disabled=True, value=user_answers_boolean[0])
        if st.session_state.school == "LFUK":
            actual_score -= 1

    option_letter = "B"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['B']
    if user_answers_boolean[1] == correct_answers_boolean[1]:
        st.checkbox(f"{option_letter}. {q['answers']['B']} ✅", key=f"{subject}_q{q['id']}_B", disabled=True, value=user_answers_boolean[1])
        actual_score += 1
    else:
        st.checkbox(f"{option_letter}. {q['answers']['B']} ❌", key=f"{subject}_q{q['id']}_B", disabled=True, value=user_answers_boolean[1])
        if st.session_state.school == "LFUK":
            actual_score -= 1

    option_letter = "C"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['C']
    if user_answers_boolean[2] == correct_answers_boolean[2]:
        st.checkbox(f"{option_letter}. {q['answers']['C']} ✅", key=f"{subject}_q{q['id']}_C", disabled=True, value=user_answers_boolean[2])
        actual_score += 1
    else:
        st.checkbox(f"{option_letter}. {q['answers']['C']} ❌", key=f"{subject}_q{q['id']}_C", disabled=True, value=user_answers_boolean[2])
        if st.session_state.school == "LFUK":
            actual_score -= 1

    option_letter = "D"
    if st.session_state.school == "LFUK":
        option_letter = q['answer_mapping']['D']
    if user_answers_boolean[3] == correct_answers_boolean[3]:
        st.checkbox(f"{option_letter}. {q['answers']['D']} ✅", key=f"{subject}_q{q['id']}_D", disabled=True, value=user_answers_boolean[3])
        actual_score += 1
    else:
        st.checkbox(f"{option_letter}. {q['answers']['D']} ❌", key=f"{subject}_q{q['id']}_D", disabled=True, value=user_answers_boolean[3])
        if st.session_state.school == "LFUK":
            actual_score -= 1

    # Images
    load_answer_images(q, school, subject)

    return actual_score


def testing_page():

    st.header(f"{st.session_state.school} {st.session_state.subject} Test")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Biology")
    st.markdown("<hr>", unsafe_allow_html=True)

    if 'user_b_answers' not in st.session_state:
        st.session_state.user_b_answers = []
    if 'user_c_answers' not in st.session_state:
        st.session_state.user_c_answers = []

    # The test is just initialized, there are no results
    if not st.session_state.is_test_submitted:
        for idx, q in enumerate(st.session_state.b_questions):

            if st.session_state.school == "SZU":
                school = "szu"
            else:
                school = "lfuk"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-b-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")

            selected_answers = load_checkboxes_and_images(q, school, "b")

            st.session_state.user_b_answers.append({"question_id": q['id'], "selected_answers": selected_answers})
            st.markdown("<hr>", unsafe_allow_html=True)

        st.subheader("Chemistry")
        st.markdown("<hr>", unsafe_allow_html=True)

        for idx, q in enumerate(st.session_state.c_questions):

            if st.session_state.school == "SZU":
                school = "szu"
            else:
                school = "lfuk"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-ch-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")

            selected_answers = load_checkboxes_and_images(q, school, "ch")

            st.session_state.user_c_answers.append({"question_id": q['id'], "selected_answers": selected_answers})
            st.markdown("<hr>", unsafe_allow_html=True)

        if st.button("Submit"):
            st.session_state.user_b_answers = {item['question_id']: item['selected_answers'] for item in st.session_state.user_b_answers}
            st.session_state.user_c_answers = {item['question_id']: item['selected_answers'] for item in st.session_state.user_c_answers}
            st.session_state.is_test_submitted = True
            st.rerun()
    # The user submitted his answers
    else:

        index_to_letter = ['A', 'B', 'C', 'D']
        actual_score = 0
        max_possible_score = 0

        for idx, q in enumerate(st.session_state.b_questions):

            user_b_answers_text = st.session_state.user_b_answers[q['id']]
            user_b_answers_boolean = [(element in user_b_answers_text) for element in index_to_letter]
            correct_b_answers_boolean = st.session_state.b_answers[str(q['id'])]

            max_possible_score += 4

            if st.session_state.school == "SZU":
                school = "szu"
            else:
                school = "lfuk"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-b-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")

            actual_score = load_submitted_checkboxes_and_images(user_b_answers_boolean, correct_b_answers_boolean, actual_score, q, school, "b")

            st.markdown("<hr>", unsafe_allow_html=True)

        st.subheader("Chemistry")
        st.markdown("<hr>", unsafe_allow_html=True)

        for idx, q in enumerate(st.session_state.c_questions):

            user_c_answers_text = st.session_state.user_c_answers[q['id']]
            user_c_answers_boolean = [(element in user_c_answers_text) for element in index_to_letter]
            correct_c_answers_boolean = st.session_state.c_answers[str(q['id'])]

            max_possible_score += 4

            if st.session_state.school == "SZU":
                school = "szu"
            else:
                school = "lfuk"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-ch-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")

            actual_score = load_submitted_checkboxes_and_images(user_c_answers_boolean, correct_c_answers_boolean, actual_score, q, school, "ch")

            st.markdown("<hr>", unsafe_allow_html=True)

        st.write(f"Score: {actual_score}/{max_possible_score}")
        st.write(f"Success rate: {round((actual_score / max_possible_score) * 100, 2)}%")

        st.markdown("<hr>", unsafe_allow_html=True)

        if st.button("Return to Home Page"):
            st.session_state.return_clicks += 1

            if st.session_state.return_clicks == 1:
                st.write("[INFO] - Click once more to return to Home Page")
                st.write("[ALERT] - Your results will be lost")
                st.write("[RECOMMENDATION] - To save your results print out the page")

            if st.session_state.return_clicks == 2:
                st.session_state.page = "home"

                # Clearing cookies
                del st.session_state.is_test_submitted
                del st.session_state.school
                del st.session_state.subject
                del st.session_state.b_answers
                del st.session_state.b_questions
                del st.session_state.user_b_answers
                del st.session_state.c_answers
                del st.session_state.c_questions
                del st.session_state.user_c_answers
                del st.session_state.return_clicks

                st.rerun()