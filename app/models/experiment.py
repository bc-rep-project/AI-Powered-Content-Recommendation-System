from pydantic import BaseModel
from typing import Dict, List, Optional
from datetime import datetime
from enum import Enum

class ExperimentStatus(str, Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"

class ExperimentVariant(BaseModel):
    id: str
    name: str
    description: str
    config: Dict[str, any]
    traffic_percentage: float

class ExperimentMetrics(BaseModel):
    variant_id: str
    clicks: int = 0
    impressions: int = 0
    conversions: int = 0
    total_revenue: float = 0.0
    avg_session_duration: float = 0.0
    user_satisfaction: float = 0.0
    
    @property
    def ctr(self) -> float:
        """Calculate Click-Through Rate."""
        return self.clicks / self.impressions if self.impressions > 0 else 0
    
    @property
    def conversion_rate(self) -> float:
        """Calculate Conversion Rate."""
        return self.conversions / self.clicks if self.clicks > 0 else 0

class Experiment(BaseModel):
    id: str
    name: str
    description: str
    status: ExperimentStatus
    variants: List[ExperimentVariant]
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    metrics: Dict[str, ExperimentMetrics] = {}
    
    class Config:
        use_enum_values = True

class UserAssignment(BaseModel):
    user_id: str
    experiment_id: str
    variant_id: str
    assigned_at: datetime = datetime.utcnow()

class ExperimentEvent(BaseModel):
    user_id: str
    experiment_id: str
    variant_id: str
    event_type: str  # e.g., "impression", "click", "conversion"
    metadata: Dict[str, any] = {}
    timestamp: datetime = datetime.utcnow() 