import streamlit as st


def home_page():

    st.header("Welcome to the SuliX testing program!")
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("Select school for the base of testing!")

    if st.button("SZU"):
        st.session_state.school = "SZU"
        st.session_state.page = "modes"
        st.rerun()

    if st.button("LFUK"):
        st.session_state.school = "LFUK"
        st.session_state.page = "modes"
        st.rerun()