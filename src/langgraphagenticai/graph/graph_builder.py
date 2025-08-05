from langgraph.graph import StateGraph, START, END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot import BasicChatbotNode



## This workflow will get triggered once we have user inputs from UI and
## our LLM is loaded
class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langgraph.
        The method initializes a chatbot node using `BasicChatbotNode` class
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph
        """
        
        ## basic chatbot node
        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        ## Build graph
        self.graph_builder.add_node('chatbot', self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, 'chatbot')
        self.graph_builder.add_edge('chatbot', END)
        