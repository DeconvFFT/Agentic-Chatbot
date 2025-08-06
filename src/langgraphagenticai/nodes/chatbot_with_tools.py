from src.langgraphagenticai.state.state import State

class ChatbotwithTools:
    """
    Chatbot logic enhanced with tool logic
    """
    def __init__(self, model):
        self.llm = model
        
    def process(self, state:State)->dict:
        """
        Process the input state and generates a response with tool integration

        Args:
            state (State): The current state of the graph

        Returns:
            dict: Messages appended with tool response
        """
        user_input = state.model_dump()['messages'][-1] if state.model_dump()['messages'] else ''
        llm_response = self.llm.invoke([{'role':'user', 'content':user_input}])
        
        # simulate tool specific logic
        tool_response = f"Tool integration for: '{user_input}'"
        return {'messages': [llm_response, tool_response]}
    
    def create_chatbot(self, tools):
        """
        Returns a chatbot node function
        """
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response

            Args:
                state (State): The current state of the graph
            """
            return {'messages': [llm_with_tools.invoke(state.model_dump()['messages'])]}
        return chatbot_node
        