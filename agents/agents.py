# =========================================
# FILE: agents/agents.py
# =========================================

from crewai import Agent
from langchain_google_genai import (
    ChatGoogleGenerativeAI
)

from dotenv import load_dotenv
import os

from tools.order_tools import (
    parse_orders_tool,
    match_products_tool,
    generate_reports_tool
)

load_dotenv()

# ----------------------------------------
# GEMINI MODEL
# ----------------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv(
        "GOOGLE_API_KEY"
    ),
    temperature=0
)

# ----------------------------------------
# SINGLE LIGHTWEIGHT AGENT
# ----------------------------------------

automation_agent = Agent(
    role="Automation Agent",

    goal=(
        "Coordinate WhatsApp "
        "order automation workflow."
    ),

    backstory=(
        "You coordinate deterministic "
        "Python automation services."
    ),

    tools=[
        parse_orders_tool,
        match_products_tool,
        generate_reports_tool
    ],

    llm=llm,

    verbose=True
)