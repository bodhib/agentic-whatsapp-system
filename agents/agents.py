from crewai import Agent
from tools.ingestion_tool import ingest_whatsapp_data
from tools.parsing_tool import parse_orders
from tools.vision_tool import match_product
from tools.order_tool import create_order
from tools.reporting_tool import generate_report

from dotenv import load_dotenv
load_dotenv()

# from langchain_google_genai import ChatGoogleGenerativeAI

# # 🔥 Gemini LLM
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     temperature=0.3
# )

# ✅ Use Gemini via LiteLLM (this works with CrewAI)
llm = "gemini/gemini-2.5-flash"

ingestion_agent = Agent(
    role="Data Ingestion Agent",
    goal="Load WhatsApp data and prepare images for processing",
    backstory="You are responsible for collecting and organizing raw WhatsApp data and media files before processing.",
    tools=[ingest_whatsapp_data],
    llm=llm,
    verbose=True
)

parsing_agent = Agent(
    role="Parsing Agent",
    goal="Extract structured order data from WhatsApp chats",
    backstory="You specialize in transforming messy chat conversations into structured data suitable for analysis.",
    tools=[parse_orders],
    llm=llm,
    verbose=True
)

vision_agent = Agent(
    role="Vision AI Agent",
    goal="Accurately match product images with catalog items",
    backstory="You are an expert in computer vision and use AI models to identify products from images with high accuracy.",
    tools=[match_product],
    llm=llm,
    verbose=True
)

order_agent = Agent(
    role="Order Processing Agent",
    goal="Create structured orders with unique IDs and timestamps",
    backstory="You handle business logic to convert extracted data into finalized orders with proper tracking.",
    tools=[create_order],
    llm=llm,
    verbose=True
)

reporting_agent = Agent(
    role="Reporting Agent",
    goal="Generate business reports and summaries from processed orders",
    backstory="You analyze processed order data and generate reports that help businesses understand performance.",
    tools=[generate_report],
    llm=llm,
    verbose=True
)