import streamlit as st


def training_modes_page():

    st.header(f"Select training mode for {st.session_state.subject} {st.session_state.school}!")
    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Custom range"):
        st.session_state.page = "custom_range"
        st.rerun()

    if st.button("Select topics"):
        st.session_state.page = "topics"
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "subjects"
        st.rerun()