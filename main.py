import streamlit as st

from webpages.home import home_page
from webpages.modes import modes_page
from webpages.subjects import subjects_page
from webpages.training_modes import training_modes_page
from webpages.custom_range import custom_range_page
from webpages.training import training_page
from webpages.topics import topics_page
from webpages.testing import testing_page


if 'is_test_submitted' not in st.session_state:
    st.session_state.is_test_submitted = False
if 'return_clicks' not in st.session_state:
    st.session_state.return_clicks = 0


# Main page logic
if 'page' not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "modes":
    modes_page()
elif st.session_state.page == "subjects":
    subjects_page()
elif st.session_state.page == "training_modes":
    training_modes_page()
elif st.session_state.page == "custom_range":
    custom_range_page()
elif st.session_state.page == "topics":
    topics_page()
elif st.session_state.page == "training":
    training_page()
elif st.session_state.page == "testing":
    testing_page()