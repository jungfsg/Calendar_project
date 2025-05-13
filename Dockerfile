FROM infiniflow/ragflow:v0.15.0-slim

WORKDIR /server

# 필요한 Python 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# PYTHONPATH 설정
ENV PYTHONPATH=/server

# 서비스 포트 노출
EXPOSE 8080

# RagFlow의 기본 entrypoint를 사용하고 FastAPI 앱을 실행
ENTRYPOINT ["python3"]
CMD ["-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"] 