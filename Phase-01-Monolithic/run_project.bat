@echo off
echo Activating virtual environment...
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
call newvenv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

echo Running FastAPI app...
uvicorn application.main:app --reload
