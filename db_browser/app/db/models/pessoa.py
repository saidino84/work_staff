from app.db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column,String,Integer

from app.db.models.message import Message

class Pessoa(Base):
    '''nome:str,
       email:str,
       idade:int,
    '''
    __tablename__='pessoa'
    id=Column(Integer,primary_key=True)
    nome=Column(String)
    email=Column(String)
    idade=Column(Integer)
    messages=relationship(Message,backref='message')
    
    def __repr__(self) -> str:
        return f"Pessoa({self.nome})"