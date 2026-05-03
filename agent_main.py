from crewai import Crew, Task

from agents.agents import (
    ingestion_agent,
    parsing_agent,
    vision_agent,
    order_agent,
    reporting_agent
)

# -------------------------------
# TASKS (FIXED WITH expected_output)
# -------------------------------

ingest_task = Task(
    description="Load WhatsApp export data from data/whatsapp_export and organize images",
    expected_output="Confirmation message with number of images ingested",
    agent=ingestion_agent
)

parse_task = Task(
    description="Parse chat.txt from data/whatsapp_export and extract structured order data including customer, message, and image",
    expected_output="List of structured order dictionaries",
    agent=parsing_agent
)

vision_task = Task(
    description="Match product images with catalog using AI and return high-confidence matches only",
    expected_output="List of matched products with confidence scores",
    agent=vision_agent
)

order_task = Task(
    description="Create structured orders with order_id, timestamp, product, and price",
    expected_output="List of finalized order records",
    agent=order_agent
)

report_task = Task(
    description="Generate Excel reports from processed orders",
    expected_output="Confirmation that reports are generated successfully",
    agent=reporting_agent
)

# -------------------------------
# CREW
# -------------------------------

crew = Crew(
    agents=[
        ingestion_agent,
        parsing_agent,
        vision_agent,
        order_agent,
        reporting_agent
    ],
    tasks=[
        ingest_task,
        parse_task,
        vision_task,
        order_task,
        report_task
    ],
    verbose=True
)

# -------------------------------
# RUN
# -------------------------------

def run():
    result = crew.kickoff()
    print("\n✅ Agent execution complete")
    print(result)


if __name__ == "__main__":
    run()