import streamlit as st
import os
from src.langgraphagenticai.ui.uiconfigfile import Config


class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title=" 🤖 "+ self.config.get_page_title(), layout='wide')
        st.header(" 🤖 " + self.config.get_page_title())
    
        with st.sidebar:
            
            # get LLM options 
            llm_options = self.config.get_llm_options()
            use_case_options = self.config.get_usecase_options()
            
            ## LLM selection
            self.user_controls['selected_llm'] = st.selectbox('Select an LLM', llm_options)
            
            ## Model selection
            model_options = []
            if self.user_controls['selected_llm'] == 'Groq':
                model_options = self.config.get_groq_model_options()
                os.environ['GROQ_API_KEY'] = self.user_controls['GROQ_API_KEY'] = st.session_state['GROQ_API_KEY'] = st.text_input('API key', type='password')
                
                ## validate api key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning('⚠️ Please enter your Groq API key. Don\'t have one? Create one here: https://console.groq.com/keys')
            elif self.user_controls['selected_llm'] == 'OpenAI':
                model_options = self.config.get_openai_model_options()
                os.environ['OPENAI_API_KEY'] = self.user_controls['OPENAI_API_KEY'] = st.session_state['OPENAI_API_KEY'] = st.text_input('API key', type='password')
                ## validate api key
                if not self.user_controls['OPENAI_API_KEY']:
                    st.warning('⚠️ Please enter your OPENAI API key. Don\'t have one? Create one here: https://platform.openai.com/api-keys')
            self.user_controls['selected_model'] = st.selectbox('Select a Model', model_options)
            
            ## select a use case
            self.user_controls['selected_usecase'] = st.selectbox('Select a Usecase', use_case_options)
            
            ## When use clicks on Chatbot with tools
            if self.user_controls['selected_usecase'] == 'Chatbot With Tools' or self.user_controls['selected_usecase'] == 'AI News Summary':
                os.environ['TAVILY_API_KEY'] = self.user_controls['TAVILY_API_KEY'] = st.session_state['TAVILY_API_KEY'] = st.text_input('TAVILY API KEY', type='password')
                
                # validate api key
                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning('⚠️ Please enter your TAVILY API KEY. Don\'t have one? Create one here: https://app.tavily.com/home')
                    
            if self.user_controls['selected_usecase'] == 'AI News Summary':
                st.subheader('🗞️ AI news explorer')
                with st.sidebar:
                    timeframe = st.selectbox(
                        "📅 Select a Time frame",
                        ["Daily", "Weekly", "Monthly"],
                        index=0
                    )
                if st.button("🔍 Fetch Latest AI News", use_container_width=True):
                    st.session_state.isFetchButtonClicked = True
                    st.session_state.timeframe = timeframe
        return self.user_controls
    
    