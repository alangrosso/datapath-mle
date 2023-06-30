from fastapi import FastAPI
from routers.routes import router

app = FastAPI()

# Incluir routes
app.include_router(router)