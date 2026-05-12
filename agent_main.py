# =========================================
# FILE: agent_main.py
# =========================================

import os

os.environ["ANONYMIZED_TELEMETRY"] = "False"
os.environ["CHROMA_TELEMETRY"] = "False"
os.environ["CHROMA_SERVER_NOFILE"] = "65535"
os.environ["CHROMA_DB_IMPL"] = "duckdb+parquet"

from crewai import Crew, Task

from agents.agents import (
    automation_agent
)

from core.media_handler import (
    move_whatsapp_images
)

# ----------------------------------------
# SINGLE LIGHTWEIGHT TASK
# ----------------------------------------

workflow_task = Task(
    description="""
    Execute the WhatsApp order
    automation workflow.

    Steps:
    1. Parse orders
    2. Match products
    3. Generate reports
    """,

    expected_output="""
    Orders processed successfully
    and reports generated.
    """,

    agent=automation_agent
)

# ----------------------------------------
# CREW
# ----------------------------------------

crew = Crew(
    agents=[automation_agent],

    tasks=[workflow_task],

    memory=False,
    cache=False,

    verbose=True
)


def run_agents():

    # -----------------------------------
    # STEP 0: MOVE IMAGES
    # -----------------------------------

    move_whatsapp_images()

    # -----------------------------------
    # RUN CREW
    # -----------------------------------

    result = crew.kickoff()

    return result


if __name__ == "__main__":

    result = run_agents()

    print("\n✅ FINAL RESULT")
    print(result)