from fastapi import APIRouter
from application.schemas.Stats import PopularBookResponse, ActiveUserResponse, OverviewResponse
from application.crud.Stats import Stats
from typing import List


router=APIRouter(prefix='',tags=['Stats'])

stats=Stats()

@router.get("/stats/users/active", response_model=List[ActiveUserResponse])
def getActiveUsers():
    return stats.getActiveUsers()

@router.get("/stats/books/popular", response_model=List[PopularBookResponse])
def getPopularBooks():
    return stats.getPopularBooks()

@router.get("/stats/overview",  response_model=OverviewResponse)
def getOverview():
    return stats.getOverview()