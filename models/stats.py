from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base



class Ability(Base):

    __tablename__ = "abilities"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    level_cap = Column(Integer) # max level for the ability
    cost = Column(Integer) # skill point cost
    skills = relationship("Skill", back_populates="ability")
    milestones = relationship("AbilityMilestone", back_populates="ability")
    
class AbilityMilestone(Base):
    __tablename__ = "ability_milestones"
    
    id = Column(Integer, primary_key=True, index=True)
    ability_id = Column(Integer, ForeignKey('abilities.id'))
    level = Column(Integer)
    description = Column(String)
    choices = relationship("AMChoice", back_populates="ability_milestone")

class AMChoice(Base):
    __tablename__ = "am_choices"
    
    id = Column(Integer, primary_key=True, index=True)
    ability_milestone_id = Column(Integer, ForeignKey('ability_milestones.id'))
    description = Column(String)
    
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    ability_id = Column(Integer, ForeignKey('abilities.id'))
    score_calc = Column(String) # formula for calculating the score from the ability score
    milestones = relationship("SkillMilestone", back_populates="skill")
    
class SkillMilestone(Base):
    __tablename__ = "skill_milestones"
    
    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    level = Column(Integer)
    description = Column(String)
    choices = relationship("SMChoice", back_populates="skill_milestone")

class SMChoice(Base):
    __tablename__ = "sm_choices"
    
    id = Column(Integer, primary_key=True, index=True)
    skill_milestone_id = Column(Integer, ForeignKey('skill_milestones.id'))
    description = Column(String)