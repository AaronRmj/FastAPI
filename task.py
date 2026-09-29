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


# BD fictif
db_task: list[Task] = [
    Task(id=1, title= "faire du sport", description= "Footing du matin", completed=False)
    Task(id=2, title= "cuisiner", description= "apprendre un plat", completed=True)
]


# CRUD

#lister toutes les tâches
@app.get("/tasks", response_model= list[Task])
def get_all_tasks():
    return db_task


#creer un nouveau taches
@app.post("/tasks", response_model=Task, status_code=201)
def create_task(tache: TaskCreate):

    new_id = max([t.id for t in db_task], default=0) + 1

    new_task = Task(
        id=new_id,
        title = tache.title
        description=tache.description=
        completed=False
    )


    #sauvegarder dans la liste 
    db_task.append(new_task)

    return new_task


