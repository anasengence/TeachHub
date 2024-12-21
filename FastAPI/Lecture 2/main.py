from fastapi import FastAPI
import models, database

app = FastAPI()

@app.on_event("startup")
def on_startup():
    models.create_db_and_tables()


@app.post("/blog")
def create_blog(blog: models.Blog, session: database.SessionDep):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog

@app.get("/blog/{id}")
def get_blog(id: int, session: database.SessionDep):
    blog = session.get(models.Blog, id)
    return blog