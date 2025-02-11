import streamlit as st
import re

from utils.dataloader import load_data


def determine_data_parameters(topic, size):
    match = re.search(r'\[(\d+)-(\d+)]', topic)
    start = int(match.group(1))
    end = int(match.group(2))
    if (end-start+1) < size:
        size = end-start+1
    return start, end, size


def topics_page():

    # noinspection SqlNoDataSourceInspection
    st.header(f"Select a Topic from {st.session_state.subject} {st.session_state.school}!")
    st.markdown("<hr>", unsafe_allow_html=True)

    topics = None
    if st.session_state.school == "LFUK":
        if st.session_state.subject == "Biology":
            topics = ["Cell [1-140]", "Genetics [141-521]", "Microbiology [522-588]", "Human [589-940]", "Ecosystem [941-1000]"]
        elif st.session_state.subject == "Chemistry":
            topics = ["Inorganic [1-257]", "Calculations [258-357]", "Organic [358-666]", "Biochemistry [667-1000]"]
    if st.session_state.school == "SZU":
        if st.session_state.subject == "Biology":
            topics = ["Cell [1-332]", "Botanics [333-451]", "Genetics [452-643]", "Animals [644-783]", "Human [784-1090]"]
        elif st.session_state.subject == "Chemistry":
            topics = ["Inorganic [1-354]", "Organic [355-764]", "Biochemistry [765-1093]", "Calculations [1094-1200]"]

    selected_topic = st.selectbox("Select a topic for training!", topics)

    possible_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    selected_size = st.selectbox("How many questions would you like?", possible_sizes)

    if st.button("Start"):
        range_start, range_end, selected_size = determine_data_parameters(selected_topic, selected_size)
        load_data(start=range_start, end=range_end, size=selected_size)
        st.session_state.page = "training"
        st.rerun()

    st.markdown("<hr>", unsafe_allow_html=True)

    if st.button("Back"):
        st.session_state.page = "training_modes"
        st.rerun()