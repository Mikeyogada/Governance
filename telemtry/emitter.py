import json
import os
import sys
from datetime import datetime, timezone

from .schema import SupplyChainEvent

def emit (event_name, status="success", metadata=None):
    """
    Build and emit a standard supply chain telemetry event.
    """

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
    print(json.dumps(event.__dict__, indent=2))  # Emit the event as a JSON object to the console

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python -m telemetry.emitter <event_name> [status] [metadata_json]"
        )

    emit(
        sys.argv[1],
        sys.argv[2] if len(sys.argv) > 2 else "success",
        json.loads(sys.argv[3]) if len(sys.argv) > 3 else None,
    )

#this emitter takes the supply chain event and emits it to the console in JSON format, which can be captured by GitHub Actions and used for further processing or analysis. The metadata field can be used to include additional information about the event, such as the name of the workflow or the name of the job that generated the event.
#the emitter is filled with the current timestamp, the name of the event, the repository name, the run ID, the commit SHA, the branch name, the actor (user) who triggered the event, and the status of the event (success or failure). The metadata field is optional and can be used to include additional information about the event.