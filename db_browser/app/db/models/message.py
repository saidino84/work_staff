from sqlalchemy import Column, Integer,ForeignKey,String
from sqlalchemy.orm import relationship
from  app.db import Base

class Message(Base):
    '''
    corpo
    pessoa_id
    '''
    
    __tablename__='message'
    id = Column(Integer, primary_key=True)
    # no constructor do ForeignKey('parent.id') {introduza o nome da tabela.id}
    corpo=Column(String)
    pessoa_id=Column(Integer,ForeignKey('pessoa.id'))
    pessoa =relationship('Pessoa')