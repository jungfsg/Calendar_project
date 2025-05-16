# 프로젝트 설정 및 실행 가이드

이 문서는 서버와 Flutter 클라이언트의 설정 및 실행 방법을 안내합니다.


## 0. 추가 라이브러리 설치

```python
import sys
import subprocess

# 패키지 설치
subprocess.check_call([sys.executable, "-m", "pip", "install", "FlagEmbedding"])

# 설치 후 다시 임포트해야 할 수 있음
import importlib
importlib.invalidate_caches()

# 이제 패키지 사용 가능
from FlagEmbedding import ...
```




## 1. 프로젝트 클론

```bash
# GitHub Desktop 사용
1. GitHub Desktop 실행
2. File > Clone Repository 클릭
3. URL 탭에서 https://github.com/jungfsg/Calendar_project.git 입력
4. 원하는 로컬 경로 선택 후 'Clone' 클릭
```

## 2. FastAPI 서버 실행 (Docker)

### 도커 이미지 빌드

```bash
# 프로젝트 루트 디렉토리에서
docker build -t calender-server .
```

### 도커 컨테이너 실행

```bash
# 개발 모드 실행 (소스 코드 변경 실시간 반영)
docker run -p 8080:8080 -v ${PWD}/app:/server/app calender-server
```

### 주요 사항
- 서버 접속: http://localhost:8080
- API 문서: http://localhost:8080/docs
- `app` 디렉토리 내 코드 수정이 실시간으로 반영됨

## 3. Flutter 클라이언트 실행

### 의존성 설치 및 캐시 정리
프로젝트 위치가 변경되었거나 처음 설정하는 경우 아래 명령어를 실행하세요:

```bash
# Calender 디렉토리에서 실행
cd Calender
flutter clean
flutter pub get
```

### 앱 실행

```bash
# 웹 브라우저에서 실행
flutter run -d chrome

# 윈도우 앱으로 실행
flutter run -d windows
```

## 4. 주의사항

### 도커 관련
- Flutter 프로젝트는 도커 이미지에 포함되지 않습니다 (`.dockerignore`에 설정됨)
- 도커 컨테이너 내에서 직접 코드를 수정하지 마세요 (변경사항이 호스트에 반영되지 않음)

### Flutter 관련
- 위치 변경 후 문제 발생 시 `flutter clean` 후 `flutter pub get` 실행
- 의존성 추가 시 `pubspec.yaml` 파일 수정 후 `flutter pub get` 실행

## 5. 유용한 명령어

### 도커 관련
```bash
# 실행 중인 컨테이너 확인
docker ps

# 컨테이너 로그 확인
docker logs <container_id>

# 컨테이너 중지
docker stop <container_id>
```

### Flutter 관련
```bash
# Flutter 환경 진단
flutter doctor

# 사용 가능한 디바이스 확인
flutter devices
``` 
