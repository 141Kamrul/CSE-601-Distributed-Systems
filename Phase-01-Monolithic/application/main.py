from fastapi import FastAPI
from application.api.User import router as user_router
from application.api.Book import router as book_router
from application.database.Session import session_instance
from sqlalchemy  import  text
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


@app.get("/")
async def root():
    return {"message": "Hello, world!"}
