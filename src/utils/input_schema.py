"""
    Module full of schemas for API? calls
    - Company
    - MainRequiest (to be changed)
"""

import os
from pydantic import BaseModel, Field

class Company(BaseModel):
    company_name: str = Field(
        description="Company name"
    )
    
    company_url: str | None = Field(
        description="Company URL adress"
    )
    
    location: str | None = Field(
        description="Country the company has headquarters"
    )
    
    industry: str | None = Field(
        description="Industry the company operates"
    )
    
    #
    # Here is specified 5 as default queries (will be also changed)
    query_amount: int | None = Field(
        default=5,
        description="Number of queries to execute/generate"
    )
    
    #
    # Will add more itf

class MainRequest(BaseModel):
    pass
