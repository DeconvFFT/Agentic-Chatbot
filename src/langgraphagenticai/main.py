import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI





def load_langgraph_agentic_ai_app():
    """
    Creates and loads an agentic AI app powered by Langgraph and streamlit UI.
    This function initialises the UI, handles user input, configures the LM model,
    sets up the graph based on the selected usecase, and displays the output while
    implementing exception handling for robustness
     
    """
    
    ## load ui
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error('❌ Failed to load user input from UI')
        return
    user_message = st.chat_input('Enter your message!')
    # if user_message:
    #     try:
            