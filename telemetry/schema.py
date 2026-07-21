from dataclasses import dataclass,field #dataclasses are used to define simple classes for storing data
from typing import Dict, Optional #typing is used for type hints, Dict is used to define a dictionary type, and Optional is used to indicate that a value can be None
from datetime import datetime #datetime is used to work with dates and times

@dataclass
class SupplyChainEvent:
    timestamp: str
    event: str
    repo: str
    workflow: str
    run_id: str
    sha: str
    branch: str
    actor: str
    status: str
    metadata: Optional[Dict[str, str]] = field(default_factory=dict) #metadata is an optional dictionary that can store additional information about the event

#this defines a function that takes a dictionary as input and returns a SupplyChainEvent object
#used to convert a dictionary representation of a supply chain event into a SupplyChainEvent object