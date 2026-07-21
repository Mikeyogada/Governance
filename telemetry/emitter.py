import json
import os
import sys
from datetime import datetime, timezone

from .schema import SupplyChainEvent
from routing.router import route

def emit (event_name, status="success", metadata=None):
    """
    Build and emit a standard supply chain telemetry event.
    """

    print ("==================== Emitting Supply Chain Telemetry Event ==================== ")
    event = SupplyChainEvent(
        timestamp=datetime.now(timezone.utc).isoformat(),
        event=event_name,
        repo=os.getenv("GITHUB_REPOSITORY"),
        workflow=os.getenv("GITHUB_WORKFLOW"),
        run_id=os.getenv("GITHUB_RUN_ID"),
        sha=os.getenv("GITHUB_SHA"),
        branch=os.getenv("GITHUB_REF_NAME"),
        actor=os.getenv("GITHUB_ACTOR"),
        status=status,
        metadata = metadata or {}
    )
    print ("==============Event Details=====================")
    print(json.dumps(event.__dict__, indent=2))  # Emit the event as a JSON object to the console
    return event

if __name__ == "__main__":

    print ("====================Telemetry emitter started=====================")
    print (f"Arguments received: {sys.argv[1:]}")
        
    if len(sys.argv) < 2:
        raise SystemExit(
            "Usage: python -m telemetry.emitter <event_name> [status] [metadata_json]"
        )
    metadata = None

    if len(sys.argv) > 3:
        metadata = json.loads(sys.argv[3])


    #emit(
    #    sys.argv[1],
    #    sys.argv[2] if len(sys.argv) > 2 else "success",
    #    metadata=metadata,
    #)
    event = emit(
        event_name=sys.argv[1],
        status=sys.argv[2] if len(sys.argv) > 2 else "success",
        metadata=metadata,
    )

    print ("====================Routing event to adapters=====================")
    route(event)
    print ("====================Routing completed=====================")

    print ("====================Telemetry emitter completed=====================")

#this emitter takes the supply chain event and emits it to the console in JSON format, which can be captured by GitHub Actions and used for further processing or analysis. The metadata field can be used to include additional information about the event, such as the name of the workflow or the name of the job that generated the event.
#the emitter is filled with the current timestamp, the name of the event, the repository name, the run ID, the commit SHA, the branch name, the actor (user) who triggered the event, and the status of the event (success or failure). The metadata field is optional and can be used to include additional information about the event.