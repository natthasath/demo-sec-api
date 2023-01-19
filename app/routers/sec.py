from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import JSONResponse
from app.models.model_sec import ConfigSchema
from app.services.service_sec import SecService

router = APIRouter(
    prefix="/sec",
    tags=["SEC"],
    responses={404: {"message": "Not found"}}
)

@router.post("/config")
async def config(data: ConfigSchema = Depends(ConfigSchema)):
    return SecService().config(data.fund_factsheet)

@router.get("/fund/amc")
async def get_fund_amc(request: Request):
    key = request.cookies.get("fund_factsheet")
    return SecService().get_fund_amc(key, f'https://api.sec.or.th/FundFactsheet/fund/amc')

@router.post("/fund/search")
async def get_fund_search(request: Request, name: str):
    key = request.cookies.get("fund_factsheet")
    return SecService().get_fund_search(key, f'https://api.sec.or.th/FundFactsheet/fund', name)