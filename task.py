from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

#instancer fastapi
app = FastAPI()

#Creation des modeles

#afficher une task
class Task(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: bool | None = None


db_tasks: list[Task] = [
    Task(id=1, title="Faire du sport", description="gotta run 6 miles", completed=False),
    Task(id=2, title="Cuisiner", description="apprendre un nouveau plat", completed=False),
]


# lire toutes les taches
@app.get("/tasks/", response_model=list[Task])
def get_all_tasks():
    return db_tasks


#creer un nouveau tache
@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(tache: TaskCreate):
    new_id = max([t.id for t in db_tasks], default= 0) + 1
    new_task = Task (
        id = new_id,
        title = tache.title,
        description= tache.description,
        completed = False
    )

    db_tasks.append(new_task)
    return new_task


#chercher une seul tache
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in db_tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code= 404, detail="Not found")


#modifier une tache
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_update: TaskUpdate):
    for task in db_tasks:
        if task.id == task_id:
            if task_update.title is not None:
                task.title = task_update.title
            if task_update.description is not None:
                task.description = task_update.description
            if task_update.completed is not None:
                task.completed = task_update.completed
            return task

    raise HTTPException(status_code=404, detail="Erreur lors de la modification")


# suppression
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index_tache , tache in enumerate(db_tasks):
        if tache.id == task_id:
            db_tasks.pop(index_tache)
            return 
    raise HTTPException(status_code=404, detail="Introuvable")
