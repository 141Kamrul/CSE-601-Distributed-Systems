#!/bin/bash

echo "Activating virtual environment..."
source phase-01-myvenv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Running FastAPI app..."
uvicorn application.main:app --reload
