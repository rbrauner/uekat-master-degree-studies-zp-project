#!/usr/bin/env bash

source venv/bin/activate

uvicorn src.app.app:app --reload
