# Todo App

FastAPI를 사용하여 간단한 Todo 애플리케이션을 구현. 애플리케이션은 CRUD(Create, Read, Update, Delete) 기능을 제공하며 현재는 더미 데이터를 사용하고 있습니다. 추후 실제 데이터베이스와 연결할 예정입니다.

## 프로젝트 구조
```
src/
├── db.py # 더미 데이터 및 데이터베이스 연결 설정
├── main.py # FastAPI 애플리케이션의 진입점
├── models.py # Pydantic 모델 정의
└── routes.py # API 라우트 정의
```

## 설치 및 실행

1. **환경 설정**: Python 3.7 이상이 설치되어 있어야 합니다. 가상 환경을 설정하는 것이 좋습니다.

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. **필요한 패키지 설치**:

   ```bash
   pip install fastapi uvicorn
   ```

3. **애플리케이션 실행**:

   ```bash
   uvicorn src.main:app --reload
   ```

   애플리케이션이 실행되면, 기본적으로 `http://127.0.0.1:8000`에서 접근할 수 있습니다.

## API 엔드포인트

- `GET /`: 헬스 체크 핸들러
- `GET /todos`: 모든 Todo 항목을 가져옵니다.
- `GET /todos/{todo_id}`: 특정 Todo 항목을 가져옵니다.
- `POST /todos`: 새로운 Todo 항목을 생성합니다.
- `PATCH /todos/{todo_id}`: 특정 Todo 항목을 업데이트합니다.

## 예제

### 모든 Todo 항목 가져오기
```bash
curl -X GET "http://127.0.0.1:8000/todos"
```

```bash
curl -X POST "http://127.0.0.1:8000/todos" -H "Content-Type: application/json" -d '{"id": 4, "contents": "새로운 할 일", "is_done": false}'
```


### 특정 Todo 항목 업데이트하기
```bash
curl -X PATCH "http://127.0.0.1:8000/todos/4" -H "Content-Type: application/json" -d '{"is_done": true}'
```


## 향후 계획

- 실제 데이터베이스와 연결하여 데이터를 영구적으로 저장할 수 있도록 구현할 예정입니다.
- UI 라이브러리를 사용하여 사용자 인터페이스를 개선할 계획입니다.
