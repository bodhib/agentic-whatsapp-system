from crewai import Crew
from tasks import ingest_task, parse_task, vision_task, order_task, report_task

crew = Crew(
    tasks=[ingest_task, parse_task, vision_task, order_task, report_task],
    verbose=True
)