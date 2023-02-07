import uvicorn

from controller.user import user_router
from controller.vacancy import vacancy_router
from fastapi import FastAPI

app = FastAPI(
    title="Employability Api",
    description="API to interact with users and vacancies ",
    version="1.0.0",
)
# Router User
app.include_router(user_router)

#router Vacancy
app.include_router(vacancy_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)