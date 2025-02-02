# src/models.py
from pydantic import BaseModel

class CreateTodoRequest(BaseModel):
    id: int  # Todo 항목의 고유 ID
    contents: str  # Todo 항목의 내용
    is_done: bool  # Todo 항목의 완료 여부