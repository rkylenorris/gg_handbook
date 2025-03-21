from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..declarative_base import Base

class Race(Base):
    __tablename__ = 'races'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    traits = relationship("RacialTrait", back_populates='Race')
    
class RacialTrait(Base):
    __tablename__ = 'racial_traits'
    
    id = Column(Integer, primary_key=True, index=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    name = Column(String)
    description = Column(String)

class SubRace(Base):
    __tablename__ = 'subraces'
    
    id = Column(Integer, primary_key=True, index=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    name = Column(String)
    description = Column(String)
    traits = relationship("RacialTrait", back_populates='SubRace')
    
class RaceSkillBonus(Base):
    __tablename__ = 'race_skill_bonuses'
    
    id = Column(Integer, primary_key=True, index=True)
    race_id = Column(Integer, ForeignKey('races.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    bonus = Column(Integer) # bonus to the skill
    description = Column(String) # description of why the bonus is given