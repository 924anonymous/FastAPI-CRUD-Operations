# FastAPI-CRUD-Operations
CURD operations using FastAPI

Pakcage's Used:
  - fastapi  --> pip install fastapi
  - uvicorn  --> pip install uvicorn
  - pydantic --> pip install pydantic
  - json
  
To execute the project run following command in terminal
  "uvicorn fapi_app:app --reload"

The command "uvicorn fapi_app:app --reload" refers to:
  - fapi_app: the file fapi_app.py (the Python "module").
  - app: the object created inside of fapi_app.py with the line app = FastAPI().
  - --reload: make the server restart after code changes. Only use for development.
  
To access documentation or to try out API's after executing the above command use the following URL.
  "http://127.0.0.1:8000/docs"
