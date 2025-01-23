from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from client import CmfClient
from utils import get_example, process_uf_data


templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="", tags=["UF Variation"])

@router.get("/uf-variation/year/{year}", responses={200: get_example("uf_variation")})
def get_uf_variation_data_per_year(year: int) -> dict:

    client = CmfClient()

    ok, response = client.get(path=f'uf/{year}')
    if not ok:
        raise HTTPException(status_code=400, detail=response)

    return process_uf_data(response.get('UFs'))

@router.get("/uf-variation", response_class=HTMLResponse, include_in_schema=False)
async def show_uf_variation_page(request: Request):
    return templates.TemplateResponse("uf_variation_form.html", {"request": request})

@router.get("/uf-variation/data/", response_class=HTMLResponse, include_in_schema=False)
async def show_uf_variation_data_page(request: Request, year: int):
    data = get_uf_variation_data_per_year(year)
    return templates.TemplateResponse("uf_variation_data.html", {"request": request, "data": data, "year": year})
