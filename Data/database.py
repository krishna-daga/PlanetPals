from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task, TaskCompletion, Score

engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
