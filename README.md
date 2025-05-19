# Calendar Server

FastAPI 기반의 캘린더 서버 애플리케이션입니다.
플러터 코드는 다음 레포지토리를 참고해주세요.
https://github.com/jungfsg/Calender

## 실행 명령어
```bash
# 백엔드
python run_chroma.py
python -m uvicorn app.main:app --reload --port 8000

# 플러터
flutter run -d chrome
```

## 기능

- LLM을 활용한 텍스트 기반 일정 추출
- 벡터 데이터베이스를 활용한 컨텍스트 관리
- STT/TTS 지원 (구현 예정)
- 이미지 OCR 처리 (구현 예정)
- Google Calendar 연동 (구현 예정)

## 설치 방법

1. 의존성 설치:
```bash
pip install -r requirements.txt
```

2. 환경 변수 설정:
`.env` 파일을 생성하고 다음 변수들을 설정하세요:
```env
OPENAI_API_KEY=your_api_key
GOOGLE_CALENDAR_CREDENTIALS=path_to_credentials.json
VLLM_MODEL_PATH=path_to_model
```

3. ChromaDB 서버 실행:
```bash
chroma run --path /path/to/chromadb
```

4. vLLM 서버 실행:
```bash
python -m vllm.entrypoints.openai.api_server --model path_to_model --port 8000
```

5. FastAPI 서버 실행:
```bash
uvicorn app.main:app --reload
```

## API 엔드포인트

### 일정 처리
- POST `/api/v1/calendar/process`
  - 텍스트 입력을 처리하여 일정 정보를 추출합니다.

### 컨텍스트 관리
- POST `/api/v1/calendar/context`
  - 새로운 컨텍스트를 벡터 저장소에 추가합니다.

## 개발 예정 기능

- [ ] STT/TTS 서비스 통합
- [ ] 이미지 OCR 처리
- [ ] Google Calendar API 연동
- [ ] 사용자 인증 시스템
- [ ] 실시간 알림 시스템 
