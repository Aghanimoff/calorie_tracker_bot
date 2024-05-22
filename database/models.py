from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    chat_id = Column(String, nullable=False)
    entries = relationship("Entry", back_populates="user")

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(Date)
    calories = Column(Integer)
    description = Column(String)
    user = relationship("User", back_populates="entries")

def create_db():
    """ Создать базу данных и таблицы, если они не существуют """
    engine = create_engine('sqlite:///calorie_tracker.db')
    Base.metadata.create_all(engine)

def get_session():
    """ Получить сессию для выполнения операций с базой данных """
    engine = create_engine('sqlite:///calorie_tracker.db')
    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind=engine)
    return Session()
