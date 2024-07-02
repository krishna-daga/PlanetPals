from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date, Text
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    house_id = Column(Integer, ForeignKey('house.house_id'))
    total_points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC))
    house = relationship("House", back_populates="users")
    tasks = relationship("UserTasks", back_populates="user")

class UserTasks(Base):
    __tablename__ = 'user_tasks'
    user_task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    task_id = Column(Integer, ForeignKey('tasks.task_id'), nullable=False)
    date = Column(Date, nullable=False, default=datetime.utcnow)
    user = relationship("User", back_populates="tasks")
    task = relationship("Tasks")

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False, unique=True)

class House(Base):
    __tablename__ = 'house'
    house_id = Column(Integer, primary_key=True)
    house_name = Column(String, nullable=False, unique=True)
    total_points = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    users = relationship("User", back_populates="house")

class Tasks(Base):
    __tablename__ = 'tasks'
    task_id = Column(Integer, primary_key=True)
    task_name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.category_id'))
    points = Column(Integer, nullable=False)
    difficulty_level = Column(Text, nullable=False)
    date = Column(Date, nullable=False, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category = relationship("Category", back_populates="tasks")
