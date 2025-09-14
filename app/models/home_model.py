from pydantic import BaseModel
from typing import List, Optional

class UniversityOverview(BaseModel):
    name: str
    description: str
    image_url: str
    established: str
    faculties: List[str]
    programs_count: int
    campus: str
    buildings: List[str]
    vision: str

class PresidentMessage(BaseModel):
    greeting: str
    image_url: str
    content: str
    closing: str
    president_name: str

class HomeScreen(BaseModel):
    welcome: Optional[str] = None  
    university: UniversityOverview 
    president_message: PresidentMessage 
    fromDB: bool= False