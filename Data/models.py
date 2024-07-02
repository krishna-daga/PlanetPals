from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    level = Column(Integer, default=1)
    xp = Column(Integer, default=0)
    scores = relationship('Score', backref='user', lazy=True)

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    score = Column(Integer, nullable=False)

class TaskCompletion(Base):
    __tablename__ = 'task_completions'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    proof_image_url = Column(String(200), nullable=False)
    completed_at = Column(DateTime, nullable=False, default=datetime.utcnow)

class Score(Base):
    __tablename__ = 'scores'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    total_score = Column(Integer, default=0)
