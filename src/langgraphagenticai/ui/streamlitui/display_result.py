import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        
    def display_result_on_ui(self):
        usecase = self.usecase
        graph = self.graph
        user_message = self.user_message
        if usecase == 'Basic Chatbot':
            for event in graph.stream({'messages': ('user', user_message)}):
                for value in event.values():
                    
                    with st.chat_message('user'):
                        st.write(user_message)
                    with st.chat_message('assistant'):
                        st.write(value['messages'].content)
        elif usecase == 'Chatbot With Tools':
            inital_state = {'messages': [user_message]}
            res = graph.invoke(inital_state)
            for message in res['messages']:
                if type(message) == HumanMessage:
                    with st.chat_message('user'):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message('ai'):
                        st.write('Tool Call Started')
                        st.write(message.content)
                        st.write('Tool Call ended')
                elif type(message) == AIMessage and message.content:
                    with st.chat_message('assistant'):
                        st.write(message.content)
        elif usecase == 'AI News Summary':
            frequency = self.user_message
            with st.spinner("Fetching and summarising news... ⏳"):
                result = graph.invoke({'messages':frequency})
                print(f'result : {result}')

                try:
                    ## read the markdown file:
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()
                    
                    # display the markdown content on streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError as fne:
                    st.error(f'❌ News not generated or file not found: {fne}')
                except Exception as e:
                    st.error(f'⚠️ An error occured:  {e}')
        
            