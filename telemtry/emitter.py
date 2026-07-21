import json
import os
from datetime import datetime, timezone

from .schema import SupplyChainEvent

def emit (event_name, status="success", metadata=None):
    event = SupplyChainEvent(
        timestamp=datetime.now(timezone.utc).isoformat(),
        event=event_name,
        repo=os.getenv("GITHUB_REPOSITORY"),
        run_id=os.getenv("GITHUB_RUN_ID"),
        sha=os.getenv("GITHUB_SHA"),
        branch=os.getenv("GITHUB_REF_NAME"),
        actor=os.getenv("GITHUB_ACTOR"),
        status=status,
        metadata = metadata or {}
    )
    print(json.dumps(event.__dict__))

#this emitter takes the supply chain event and emits it to the console in JSON format, which can be captured by GitHub Actions and used for further processing or analysis. The metadata field can be used to include additional information about the event, such as the name of the workflow or the name of the job that generated the event.
#the emitter is filled with the current timestamp, the name of the event, the repository name, the run ID, the commit SHA, the branch name, the actor (user) who triggered the event, and the status of the event (success or failure). The metadata field is optional and can be used to include additional information about the event.