from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.api.calendar import router as calendar_router

settings = get_settings()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 운영 환경에서는 구체적인 도메인을 지정해야 합니다
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Calendar Server API"}

# 라우터 등록
app.include_router(calendar_router, prefix=f"{settings.API_V1_STR}/calendar", tags=["calendar"])

# 추후 라우터들이 여기에 추가될 예정입니다
# from app.api import some_router
# app.include_router(some_router, prefix=settings.API_V1_STR) 

# 마운트 제대로 됐는지 확인
# 확인
# 깃헙 데스크탑이 잘 보고 있는지 확인