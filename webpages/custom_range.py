import streamlit as st

from utils.dataloader import load_data


def check_if_range_is_correct(start, end, selected_size):

    if start > end:
        st.write("[ERROR] - Start is greater than end")
        return False

    if selected_size > (end-start+1):
        st.write("[ERROR] - Selected size is greater than the interval")
        return False

    return True


def get_max_possible_range():

    if st.session_state.school == "SZU":
        if st.session_state.subject == "Biology":
            return 1090
        else:
            return 1200

    if st.session_state.school == "LFUK":
        return 1000


def custom_range_page():

    st.header(f"Enter the range of questions for {st.session_state.subject} {st.session_state.school}!")
    st.markdown("<hr>", unsafe_allow_html=True)

    # Determine available range
    max_possible_value = get_max_possible_range()

    range_start = st.number_input("From:", min_value=1, max_value=max_possible_value, step=1)

    range_end = st.number_input("To:", min_value=1, max_value=max_possible_value, step=1, value=max_possible_value)

    possible_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    selected_size = st.selectbox("How many questions would you like?", possible_sizes)

    if st.button("Start"):
        if check_if_range_is_correct(range_start, range_end, selected_size):
            load_data(start=range_start, end=range_end, size=selected_size)
            st.session_state.page = "training"
            st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "training_modes"
        st.rerun()
