from fastapi import FastAPI
from application.api.User import router as user_router
from application.api.Book import router as book_router
from application.api.Loan import router as loan_router
from application.api.Stats import router as stats_router
from application.database.Session import session_instance
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],  #origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

session_instance.create_tables()

app.include_router(user_router)
app.include_router(book_router)
app.include_router(loan_router)
app.include_router(stats_router)


@app.get("/")
async def root():
    return {"message": "Application Running at localhost"}