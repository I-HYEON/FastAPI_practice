from fastapi import APIRouter, Body
from .models import CreateTodoRequest
from .db import todo_data

router = APIRouter()

@router.get("/")
def health_check_handler():
    """헬스 체크 핸들러"""
    return {"ping": "pong"}

@router.get("/todos")
def get_todos_handler(order: str | None = None):
    """모든 Todo 항목을 가져오는 핸들러"""
    ret = list(todo_data.values())
    if order == "DESC":
        return ret[::-1]  # 내림차순 정렬
    return ret

@router.get("/todos/{todo_id}")
def get_todo_handler(todo_id: int):
    """특정 Todo 항목을 가져오는 핸들러"""
    return todo_data.get(todo_id, {})

@router.post("/todos")
def create_todo_handler(request: CreateTodoRequest):
    """새로운 Todo 항목을 생성하는 핸들러"""
    todo_data[request.id] = request.dict()
    return todo_data[request.id]

@router.patch("/todos/{todo_id}")
def update_todo_handler(
        todo_id: int,
        is_done: bool = Body(..., embed=True)
):
    """특정 Todo 항목을 업데이트하는 핸들러"""
    if todo_id in todo_data:
        todo_data[todo_id]["is_done"] = is_done
        return todo_data[todo_id]
    return {}