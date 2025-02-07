from fastapi import FastAPI
from config import settings
from src.jobs.api import router as jobs_router
from src.users.api import router as users_router
from config.database import Base, engine
from fastapi.responses import JSONResponse
from src.users.exceptions import UserNotFound

app = FastAPI(
    title=settings.PROJECT_NAME, debug=settings.DEBUG, version=settings.VERSION
)

app.include_router(jobs_router, prefix="/api/v1/jobs", tags=["jobs"])
app.include_router(users_router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.exception_handler(UserNotFound)
async def user_not_found_exception_handler(request, exc):
    return JSONResponse(
        status_code=404,
        content={"message": f"User with id {exc.user_id} not found"},
    )