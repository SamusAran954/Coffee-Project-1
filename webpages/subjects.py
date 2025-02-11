import streamlit as st


def subjects_page():

    # noinspection SqlNoDataSourceInspection
    st.header(f"Select subject from {st.session_state.school} for training!")
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Biology"):
        st.session_state.subject = "Biology"
        st.session_state.page = "training_modes"
        st.rerun()

    if st.button("Chemistry"):
        st.session_state.subject = "Chemistry"
        st.session_state.page = "training_modes"
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "modes"
        st.rerun()