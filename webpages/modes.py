import streamlit as st

from utils.dataloader import load_test_data


def modes_page():

    st.header(f"Select mode for {st.session_state.school}!")
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Training"):
        st.session_state.page = "subjects"
        st.rerun()

    if st.button("Testing"):
        load_test_data()
        st.session_state.page = "testing"
        st.session_state.subject = "Complete"
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "home"
        st.rerun()