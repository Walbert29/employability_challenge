import uvicorn

from controller.user import user_router
from fastapi import FastAPI

app = FastAPI(
    title="Employability Api",
    description="API to interact with users and vacancies ",
    version="1.0.0",
)

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)