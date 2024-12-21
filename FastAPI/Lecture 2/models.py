from sqlmodel import Field, Session, SQLModel, create_engine, select
import database

class Blog(SQLModel, table=True):
    # autoincrement = True
    id: int | None = Field(default=None, primary_key=True , index=True)
    title: str
    body: str



def create_db_and_tables():
    SQLModel.metadata.create_all(database.engine)