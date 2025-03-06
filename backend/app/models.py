from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    objectives = relationship("Objective", back_populates="owner")
    expenses = relationship("Expense", back_populates="owner")

class Objective(Base):
    __tablename__ = 'objectives'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    target_amount = Column(Float)
    current_amount = Column(Float, default=0.0)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="objectives")

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    date = Column(Date)
    owner_id = Column(Integer, ForeignKey('users.id'))

    owner = relationship("User", back_populates="expenses")