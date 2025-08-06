from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_tavily import TavilySearch
from langchain_community.tools import ArxivQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    # search tool
    search = TavilySearch(max_results=2)
    # arxiv tool
    api_wrapper_arxiv = ArxivAPIWrapper(top_k_results=2, doc_content_chars_max=500)
    arxiv = ArxivQueryRun(api_wrapper=api_wrapper_arxiv)
    tools = [search, arxiv]
    return tools

def create_tool_node(tools):
    """
    Creates and returns a tool node for the graph
    """
    return ToolNode(tools)