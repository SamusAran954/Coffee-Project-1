import streamlit as st

def training_page():

    st.header(f"{st.session_state.school} {st.session_state.subject} Test")
    st.markdown("<hr>", unsafe_allow_html=True)

    if 'user_answers' not in st.session_state:
        st.session_state.user_answers = []

    # The test is just initialized, there are no results
    if not st.session_state.is_test_submitted:
        for idx, q in enumerate(st.session_state.questions):

            if st.session_state.school == "SZU":
                school = "szu"
            else:
                school = "lfuk"

            if st.session_state.subject == "Chemistry":
                subject = "ch"
            else:
                subject = "b"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")
            selected_answers = []

            if st.checkbox(f"A. {q['answers']['A']}", key=f"q{q['id']}_A"):
                selected_answers.append("A")
            if st.checkbox(f"B. {q['answers']['B']}", key=f"q{q['id']}_B"):
                selected_answers.append("B")
            if st.checkbox(f"C. {q['answers']['C']}", key=f"q{q['id']}_C"):
                selected_answers.append("C")
            if st.checkbox(f"D. {q['answers']['D']}", key=f"q{q['id']}_D"):
                selected_answers.append("D")

            if st.session_state.school == "LFUK":
                if st.checkbox(f"E. {q['answers']['E']}", key=f"q{q['id']}_E"):
                    selected_answers.append("E")
                if st.checkbox(f"F. {q['answers']['F']}", key=f"q{q['id']}_F"):
                    selected_answers.append("F")
                if st.checkbox(f"G. {q['answers']['G']}", key=f"q{q['id']}_G"):
                    selected_answers.append("G")
                if st.checkbox(f"H. {q['answers']['H']}", key=f"q{q['id']}_H"):
                    selected_answers.append("H")

            if q['answers']['A'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-a.png")
            if q['answers']['B'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-b.png")
            if q['answers']['C'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-c.png")
            if q['answers']['D'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-d.png")
            if st.session_state.school == "LFUK":
                if q['answers']['E'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-e.png")
                if q['answers']['F'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-f.png")
                if q['answers']['G'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-g.png")
                if q['answers']['H'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-h.png")

            st.session_state.user_answers.append({"question_id": q['id'], "selected_answers": selected_answers})
            st.markdown("<hr>", unsafe_allow_html=True)

        if st.button("Submit"):
            st.session_state.user_answers = {item['question_id']: item['selected_answers'] for item in st.session_state.user_answers}
            st.session_state.is_test_submitted = True
            st.rerun()
    # The user submitted his answers
    else:

        if st.session_state.school == "SZU":
            index_to_letter = ['A', 'B', 'C', 'D']
        else:
            index_to_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        number_of_all_answers = 0
        number_of_correct_answers = 0

        for idx, q in enumerate(st.session_state.questions):

            user_answers_text = st.session_state.user_answers[q['id']]
            user_answers_boolean = [(element in user_answers_text) for element in index_to_letter]

            correct_answers_boolean = st.session_state.answers[str(q['id'])]
            # correct_answers_text = [index_to_letter[i] for i, value in enumerate(correct_answers_boolean) if value]

            if st.session_state.school == "SZU":
                school = "szu"
                number_of_all_answers += 4
            else:
                school = "lfuk"
                number_of_all_answers += 8

            if st.session_state.subject == "Chemistry":
                subject = "ch"
            else:
                subject = "b"

            if q['question'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}.png")
            else:
                st.subheader(f"{q['id']}. {q['question']}")

            if user_answers_boolean[0] == correct_answers_boolean[0]:
                st.checkbox(f"A. {q['answers']['A']} ✅", key=f"q{q['id']}_A", disabled=True, value= user_answers_boolean[0])
                number_of_correct_answers += 1
            else:
                st.checkbox(f"A. {q['answers']['A']} ❌", key=f"q{q['id']}_A", disabled=True, value= user_answers_boolean[0])

            if user_answers_boolean[1] == correct_answers_boolean[1]:
                st.checkbox(f"B. {q['answers']['B']} ✅", key=f"q{q['id']}_B", disabled=True, value= user_answers_boolean[1])
                number_of_correct_answers += 1
            else:
                st.checkbox(f"B. {q['answers']['B']} ❌", key=f"q{q['id']}_B", disabled=True, value= user_answers_boolean[1])

            if user_answers_boolean[2] == correct_answers_boolean[2]:
                st.checkbox(f"C. {q['answers']['C']} ✅", key=f"q{q['id']}_C", disabled=True, value= user_answers_boolean[2])
                number_of_correct_answers += 1
            else:
                st.checkbox(f"C. {q['answers']['C']} ❌", key=f"q{q['id']}_C", disabled=True, value= user_answers_boolean[2])

            if user_answers_boolean[3] == correct_answers_boolean[3]:
                st.checkbox(f"D. {q['answers']['D']} ✅", key=f"q{q['id']}_D", disabled=True, value= user_answers_boolean[3])
                number_of_correct_answers += 1
            else:
                st.checkbox(f"D. {q['answers']['D']} ❌", key=f"q{q['id']}_D", disabled=True, value= user_answers_boolean[3])

            if st.session_state.school == "LFUK":

                if user_answers_boolean[4] == correct_answers_boolean[4]:
                    st.checkbox(f"E. {q['answers']['E']} ✅", key=f"q{q['id']}_E", disabled=True, value= user_answers_boolean[4])
                    number_of_correct_answers += 1
                else:
                    st.checkbox(f"E. {q['answers']['E']} ❌", key=f"q{q['id']}_E", disabled=True, value= user_answers_boolean[4])

                if user_answers_boolean[5] == correct_answers_boolean[5]:
                    st.checkbox(f"F. {q['answers']['F']} ✅", key=f"q{q['id']}_F", disabled=True, value= user_answers_boolean[5])
                    number_of_correct_answers += 1
                else:
                    st.checkbox(f"F. {q['answers']['F']} ❌", key=f"q{q['id']}_F", disabled=True, value= user_answers_boolean[5])

                if user_answers_boolean[6] == correct_answers_boolean[6]:
                    st.checkbox(f"G. {q['answers']['G']} ✅", key=f"q{q['id']}_G", disabled=True, value= user_answers_boolean[6])
                    number_of_correct_answers += 1
                else:
                    st.checkbox(f"G. {q['answers']['G']} ❌", key=f"q{q['id']}_G", disabled=True, value= user_answers_boolean[6])

                if user_answers_boolean[7] == correct_answers_boolean[7]:
                    st.checkbox(f"H. {q['answers']['H']} ✅", key=f"q{q['id']}_H", disabled=True, value= user_answers_boolean[7])
                    number_of_correct_answers += 1
                else:
                    st.checkbox(f"H. {q['answers']['H']} ❌", key=f"q{q['id']}_H", disabled=True, value= user_answers_boolean[7])

            if q['answers']['A'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-a.png")
            if q['answers']['B'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-b.png")
            if q['answers']['C'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-c.png")
            if q['answers']['D'].strip() == "":
                st.image(f"resources/images/{school}-{subject}-{q['id']}-d.png")
            if st.session_state.school == "LFUK":
                if q['answers']['E'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-e.png")
                if q['answers']['F'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-f.png")
                if q['answers']['G'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-g.png")
                if q['answers']['H'].strip() == "":
                    st.image(f"resources/images/{school}-{subject}-{q['id']}-h.png")

            st.markdown("<hr>", unsafe_allow_html=True)

        st.write(f"Score: {number_of_correct_answers}/{number_of_all_answers}")
        st.write(f"Success rate: {round((number_of_correct_answers / number_of_all_answers) * 100, 2)}%")

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
                del st.session_state.answers
                del st.session_state.questions
                del st.session_state.user_answers
                del st.session_state.return_clicks

                st.rerun()