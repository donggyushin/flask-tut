# Env

python=3.13.2 <br />
pip=25.0.1 <br />
Docker version=28.0.2 <br />

# Docker

## create docker image

```
docker build -t {image_name} .
```

## run docker container

```
# Run container with existing code
docker run -dp {host_port}:{container_port} {image_name}
# Run container with volume(host folder synced with container folder)
docker run -dp {host_port}:{container_port} -w /app -v "$(pwd):/app" {image_name}
```

```
	•	-d → 백그라운드 모드로 컨테이너 실행 (터미널 점유 안 함)
	•	-p {호스트포트}:{컨테이너포트} → 호스트의 포트를 컨테이너 포트에 연결
	•	-w /app → 컨테이너의 작업 디렉터리를 /app으로 설정
	•	-v "$(pwd):/app" → 현재 디렉터리를 컨테이너의 /app에 볼륨 마운트 (양방향 파일 공유 가능)
```

### Using Docker Compose

```
docker compose up
```

# Install Packages

```
pip install -r requirements.txt
```

### Requirements.txt

```
pip freeze > requirements.txt
```

현재 가상환경에 설치된 모든 패키지(Flask 포함)의 버전 정보가 requirements.txt에 기록됩니다.
