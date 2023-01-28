from sqlalchemy import select, text 
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine

from discord.interactions import Interaction 

from classes.models import Character, User


def check_is_character_owner(method):
    '''Cog's method decorator for accesing only character owners'''

    def decorate(self, *args, **kwargs):
        database:Engine = self.database
        interaction:Interaction = kwargs['interaction']
        character_name = kwargs['character_name']
        
        with Session(self.database) as session:
            owner_id_query = select(Character.user_id).where(Character.name == character_name)
            owner_id = session.execute(owner_id_query).first()[0]
            
            if not owner_id == interaction.user.id:
                raise PermissionError('Доступ запрещен: это не ваш персонаж')
        
        return method(self, *args, **kwargs)
    return  decorate


def check_is_admin(method):
    '''Cog's method decorator for accesing only admin'''

    def decorate(self, *args, **kwargs):
        database:Engine = self.database
        interaction:Interaction = kwargs['interaction']
        
        with Session(self.database) as session:
            user_type_query = select(User.type).where(User.id == interaction.user.id)
            user_type = session.execute(user_type_query).first()[0]
            
            if user_type != 'admin':
                raise PermissionError('Доступ запрещен: Вы не администратор')
        
        return method(self, *args, **kwargs)
    return  decorate

