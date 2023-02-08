import uvicorn
from fastapi import FastAPI

from src.controller.application import application_router
from src.controller.employability import employability_router
from src.controller.user import user_router
from src.controller.vacancy import vacancy_router

app = FastAPI(
    title="Employability Api",
    description="API to interact with users and vacancies ",
    version="1.0.0",
)

# Router User
app.include_router(user_router)

# Router Vacancy
app.include_router(vacancy_router)

# Router Employability
app.include_router(employability_router)

# Router Application
app.include_router(application_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
