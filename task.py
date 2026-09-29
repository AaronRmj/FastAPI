from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

# 3 modeles pour task

# on utilise task pour afficher les taches
class Task(BaseModel):
    id: int
    title: str = None
    description: Optional[str] = None
    completed: Optional[bool] = None


#on l'utilise pour créer des taches
class TaskCreate(BaseModel):
    title: str = None
    description: Optional[str] = None


#on l'utilise pour put et update les tasks
class TaskUpdate(BaseModel):
    id: int
    title: str = None
    descrption: Optional[str] = None
    completed: Optional[bool] = None