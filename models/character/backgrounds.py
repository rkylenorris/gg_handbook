from models.declarative_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Background(Base):
    __tablename__ = 'backgrounds'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    features = relationship("BackgroundFeature", back_populates='background')
    
class BackgroundFeature(Base):
    __tablename__ = 'background_features'
    
    id = Column(Integer, primary_key=True, index=True)
    background_id = Column(Integer, ForeignKey('backgrounds.id'))
    name = Column(String)
    description = Column(String)

class BackgroundSkillBonus(Base):
    __tablename__ = 'background_skill_bonuses'
    
    id = Column(Integer, primary_key=True, index=True)
    background_id = Column(Integer, ForeignKey('backgrounds.id'))
    skill_id = Column(Integer, ForeignKey('skills.id'))
    bonus = Column(Integer) # bonus to the skill
    description = Column(String) # description of why the bonus is given

class BackgroundToolProficiency(Base):
    __tablename__ = 'background_tool_proficiencies'
    
    id = Column(Integer, primary_key=True, index=True)
    background_id = Column(Integer, ForeignKey('backgrounds.id'))
    tool_id = Column(Integer, ForeignKey('tools.id'))
    description = Column(String) # description of why the proficiency is given

class BackgroundStartingTools(Base):
    __tablename__ = 'background_starting_tools'
    
    id = Column(Integer, primary_key=True, index=True)
    background_id = Column(Integer, ForeignKey('backgrounds.id'))
    tool_id = Column(Integer, ForeignKey('tools.id'))
    quantity = Column(Integer) # number of tools
    description = Column(String) # description of why the tool is given