from crewai.tools import BaseTool
from pydantic import BaseModel
from typing import Any, Type


class AgentDiscoveryToolInput(BaseModel):
    pass


class AgentDiscoveryTool(BaseTool):
    name: str = "agent_goal_discovery_tool"
    description: str = (
        "This provides list of Agents with corresponding goals"
    )
    args_schema: Type[BaseModel] = AgentDiscoveryToolInput

    def _run(self, **kwargs: Any) -> dict:
        return {
            "product_agent": "This provides services for all product related queries",
            "purchase_agent": "This provides services for all purchase related queries",
            "order_status_agent": "This provides services for all order status related queries"
        }
