import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.LLMs.openaillm import OpenAILLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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
    if user_message:
        try:
            ## Configure LLM
            if user_input.get('selected_llm') == 'Groq':

                obj_llm_config = GroqLLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()
                
            else:
                obj_llm_config = OpenAILLM(user_controls_input=user_input)
                model = obj_llm_config.get_llm_model()

            if not model:
                st.error('❌ Error: Model could not be initialised!')
                return
            
            ## Initialise and setup the graph based on use case
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error('❌ Error: No usecase selected')
            
            #Graph builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f'❌ Error: Graph setup failed - {e}')
        except Exception as e:
            return ValueError(f'❌ Error occured with an exception: {e}')
            