from crewai import Task
from agents.agents import (
    ingestion_agent,
    parsing_agent,
    vision_agent,
    order_agent,
    reporting_agent
)

ingest_task = Task(
    description="Ingest WhatsApp export data",
    agent=ingestion_agent
)

parse_task = Task(
    description="Parse chat and extract orders",
    agent=parsing_agent
)

vision_task = Task(
    description="Match images with catalog",
    agent=vision_agent
)

order_task = Task(
    description="Create structured orders",
    agent=order_agent
)

report_task = Task(
    description="Generate final reports",
    agent=reporting_agent
)