from classes.models import Base, User, Character, Stats, BodyPart, Item
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == '__main__':
    database_engine = create_engine("sqlite:///roleplay.db")
    Base.metadata.create_all(database_engine)

    with Session(database_engine) as session:
        beaver = User(id=354177140087980042, type='admin')
        margarita = Character(name='Маргарита', type='Человек', user=beaver)
        margaritas_stats = Stats(fortitude=10, temperance=10, justice=10, character=margarita)
        margaritas_health = [BodyPart(type='head', health_points=10,
                                    max_health_points=10, character=margarita),
		                     BodyPart(type='body', health_points=10,
                                    max_health_points=10, character=margarita),
		                     BodyPart(type='left_arm', health_points=10,
                                    max_health_points=10, character=margarita),
		                     BodyPart(type='right_arm', health_points=10,
                                    max_health_points=10, character=margarita),
		                     BodyPart(type='left_leg', health_points=10,
                                    max_health_points=10, character=margarita),
		                     BodyPart(type='right_leg', health_points=10,
                                    max_health_points=10, character=margarita),
                             BodyPart(type='sanity', health_points=10,
                                    max_health_points=10, character=margarita),]
        margaritas_items = [Item(type='Ankh', amount=100, name='Анкх',
                                 description='Основная валюта города', character=margarita),
                            Item(type='Moonrock', amount=20, name='Лунный камень',
                                 description='Сигнатурный продукт корпорации М, очень ценный, если найти кому сбыть',
                                 character=margarita)]

        session.add_all([beaver, margarita, margaritas_stats])
        session.bulk_save_objects(margaritas_health)
        session.bulk_save_objects(margaritas_items)
        session.commit()

