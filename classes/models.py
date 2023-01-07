from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy_utils.types.choice import ChoiceType
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
	__tablename__ = 'users'

	TYPES = [('user', 'User'),
	         ('admin', 'Admin')]

	id = Column(Integer, primary_key=True)
	type = Column(ChoiceType(TYPES))

	characters = relationship("Character", back_populates="user", cascade="all, delete-orphan")

	def __repr__(self):
		return f"User(id={self.id!r}, fullname={self.type!r})"


class Character(Base):
	__tablename__ = 'characters'

	TYPES = [('human', 'Human'),
	         ('distortion', 'Distortion')]

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(100))
	type = Column(ChoiceType(TYPES))
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

	user = relationship(User, back_populates="characters")
	stats = relationship('Stats', back_populates="character")
	skills = relationship('Skill', back_populates="character")
	traits = relationship('Trait', back_populates="character")
	weaknesses = relationship('Weakness', back_populates="character")
	body_parts = relationship('BodyPart', back_populates="character")
	items = relationship('Item', back_populates="character")
	extra_info = relationship('ExtraInfo', back_populates="character")

	def __repr__(self):
		return f"Character(id={self.id}, name={self.user}, type={self.type}, user={self.user})"


class Skill(Base):
	__tablename__ = 'skills'

	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(100))
	description = Column(Text)
	character_id = Column(Integer, ForeignKey("characters.id"))

	character = relationship('Character', back_populates="skills")


class Trait(Base):
	__tablename__ = 'traits'

	id = Column(Integer, primary_key=True, autoincrement=True)
	text = Column(Text)
	character_id = Column(Integer, ForeignKey("characters.id"))

	character = relationship('Character', back_populates="traits")


class Weakness(Base):
	__tablename__ = 'weaknesses'

	id = Column(Integer, primary_key=True, autoincrement=True)
	text = Column(Text)
	character_id = Column(Integer, ForeignKey("characters.id"))

	character = relationship('Character', back_populates="weaknesses")


class BodyPart(Base):
	__tablename__ = 'body_parts'

	id = Column(Integer, primary_key=True, autoincrement=True)
	type = Column(String(50))
	health_points = Column(Integer)
	max_health_points = Column(Integer)
	character_id = Column(Integer, ForeignKey("characters.id"))

	character = relationship('Character', back_populates="body_parts")


class Item(Base):
	__tablename__ = 'items'

	id = Column(Integer, primary_key=True, autoincrement=True)
	type = Column(String(50))
	amount = Column(Integer)
	name = Column(String(100))
	description = Column(Text)
	character_id = Column(Integer, ForeignKey("characters.id"))

	character = relationship('Character', back_populates="items")


class Stats(Base):
	__tablename__ = 'stats'

	prudence = Column(Integer)
	fortitude = Column(Integer)
	temperance = Column(Integer)
	justice = Column(Integer)
	character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

	character = relationship('Character', back_populates="stats")


class ExtraInfo(Base):
	__tablename__ = 'extra_info'

	job = Column(String(100))
	ideology = Column(String(50))
	biography = Column(Text)
	character_id = Column(Integer, ForeignKey("characters.id"), primary_key=True)

	character = relationship('Character', back_populates="extra_info")
