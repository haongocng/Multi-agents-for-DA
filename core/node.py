from typing import Any
from langchain_core.messages import AIMessage, HumanMessage, BaseMessage,ToolMessage
from openai import InternalServerError
from core.state import State
import logging
import json
import re
import os
from pathlib import Path
from langchain.agents import AgentExecutor

logger = logging.getLogger(__name__)

def agent_node(state: State, agent: AgentExecutor, name: str) -> dict:
    """
    Process an agent's action and update the state accordingly.
    This function has been modified for the new workflow.
    """
    logger.info(f"Processing agent: {name}")
    try:
        # The agent's prompt template is designed to pick up relevant fields from the state.
        result = agent.invoke(state)
        logger.debug(f"Agent {name} result: {result}")
        
        # Ensure output is a string
        output = result.get("output", str(result)) if isinstance(result, dict) else str(result)
        
        # Create a new message from the agent's output
        ai_message = AIMessage(content=output, name=name)
        
        # Update the list of messages and the sender
        state["messages"].append(ai_message)
        state["sender"] = name
        
        # *** MODIFIED SECTION: Update the state with the specific report from each agent ***
        if name == "DataExplorer":
            state["eda_report"] = output
            logger.info("State updated with EDA Report.")
        elif name == "DataStatistic":
            state["statistic_report"] = output
            logger.info("State updated with Statistic Report.")
        elif name == "DataCluster":
            state["cluster_report"] = output
            logger.info("State updated with Cluster Report.")
        elif name == "DataVisualization":
            state["visualization_report"] = output
            logger.info("State updated with Visualization Report.")
        elif name == "HypothesisGenerator":
            state["hypothesis_report"] = output
            logger.info("State updated with Hypothesis Report.")
        elif name == "Reasoner":
            state["reasoning_report"] = output
            logger.info("State updated with Reasoning Report.")
        elif name == "QualityReview":
            state["total_summary_report"] = output
            logger.info("State updated with Total Summary Report.")
        elif name == "Synthesis":
            state["final_report"] = output
            logger.info("State updated with Final Insights Report.")
            
        logger.info(f"Agent {name} processing completed")
        return state

    except Exception as e:
        logger.error(f"Error occurred while processing agent {name}: {str(e)}", exc_info=True)
        error_message = AIMessage(content=f"Error in agent {name}: {str(e)}", name="error")
        return {"messages": state.get("messages", []) + [error_message]}



def human_choice_node(state: State) -> State:
    """
    Handle human input to choose the next step in the process.
    If regenerating hypothesis, prompt for specific areas to modify.
    """
    logger.info("Prompting for human choice")
    print("Please choose the next step:")
    print("1. Regenerate hypothesis")
    print("2. Continue the research process")
    
    while True:
        choice = input("Please enter your choice (1 or 2): ")
        if choice in ["1", "2"]:
            break
        logger.warning(f"Invalid input received: {choice}")
        print("Invalid input, please try again.")
    
    if choice == "1":
        modification_areas = input("Please specify which parts of the hypothesis you want to modify: ")
        content = f"Regenerate hypothesis. Areas to modify: {modification_areas}"
        state["hypothesis"] = ""
        state["modification_areas"] = modification_areas
        logger.info("Hypothesis cleared for regeneration")
        logger.info(f"Areas to modify: {modification_areas}")
    else:
        content = "Continue the research process"
        state["process"] = "Continue the research process"
        logger.info("Continuing research process")
    
    human_message = HumanMessage(content=content)
    
    state["messages"].append(human_message)
    state["sender"] = 'human'
    
    logger.info("Human choice processed")
    return state

def note_agent_node(state: State, agent: AgentExecutor, name: str) -> State:
    # This node can be kept if you decide to use the NoteTaker agent for debugging or state management
    # For simplicity in the new workflow, it's not strictly required.
    pass

logger.info("Agent processing node module initialized")