from sqlalchemy import create_engine,delete
from sqlalchemy.orm import sessionmaker
from app.db import Base
from app.db.models.message import Message
from app.db.models.pessoa import Pessoa
from typing import List


class Repository:
    def __init__(self):
        self.db=Base
        self.engine=create_engine('sqlite:///app_db.db')
        self.init_platforms_create_tables()
    def init_platforms_create_tables(self):
        
        Base.metadata.create_all(self.engine)
        Session=sessionmaker(bind=self.engine)
        self.session=Session()
        
    def create_or_update_pessoa(self,name:str,email:str,idade:int,id=0):
        if(id ==0):
            pessoa=Pessoa(
                nome=name,
                email=email,
                idade=idade
            )
            self.session.add(pessoa)
            self.session.commit()
        
            return 'User Added Sucessfuly'
        self.session.query(Pessoa).filter(Pessoa.id==id).update(
            {
            Pessoa.idade:idade,
            Pessoa.nome:name,
            Pessoa.email:email
            
            }
            )
        self.session.commit()
        return 'Updateded '
    def delete_pessoa(self,id):
        print(f'you typed {id}')
        u=self.session.query(Pessoa).filter_by(id=id).first()
        if u:
            print(f'user caucth {u.nome}')
            self.session.delete(u)
            self.session.commit()
            print('deletions sucessfull on')
        else:
            print('No user found')
    def get_users(self)->List[Pessoa]:
        users:List[Pessoa]=self.session.query(Pessoa).all()
        
        return users
    
    def get_user_by_id(self,id:int)->Pessoa:
        user:Pessoa= self.session.query(Pessoa).filter_by(id=id).first()  # type: ignore
        return user

    def get_user_messages(self,id:int)->list[str]:
        messages=self.get_user_by_id(id).messages;
        print('[MESSAGES]',messages)
        return messages

    def list_of_user_ids(self)->list[int]:
        return [i.id for i in self.get_users()] #type:ignore
    
    def add_message(self,message:str,user_id:int)->None:
        message=Message(corpo=message,pessoa_id=user_id)
        self.session.add(message)
        self.session.commit()
        print('message set')
        