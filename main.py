from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import uf_variation


app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": 0},
    title="Variacion UF"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(uf_variation.router)
