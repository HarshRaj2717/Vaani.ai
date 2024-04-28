from dataclasses import dataclass
from typing import Optional

from bson.objectid import ObjectId
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter()

@router.get("/students", response_model=dict)
async def list_students(
    country: Optional[str] = Query(None), age: Optional[int] = Query(None)
):
    filter = {}
    if country:
        filter["address.country"] = {"$regex": f"^{country}$", "$options": "i"}
    if age:
        filter["age"] = {"$gte": age}
    students = list_serialize(collection.find(filter))
    return {"data": students}
