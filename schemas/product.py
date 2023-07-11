from pydantic import BaseModel, Field
from typing import Optional

class Product(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=3, max_length=80)
    about: str = Field(min_length=3, max_length=50)
    year: int = Field(ge=2023)
    units:float = Field(ge=1)
    category:str = Field(min_length=3, max_length=80)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Mi producto",
                "about": "Producto lacteo",
                "year": 2023,
                "units": 9,
                "category" : "Lacteos"
            }
        }