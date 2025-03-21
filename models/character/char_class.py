from models.declarative_base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class CharClass(Base):
    __tablename__ = 'char_classes'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    hit_die = Column(Integer) # size of the hit die
    proficiencies = relationship("ClassProficiency", back_populates='char_class')
    features = relationship("ClassFeature", back_populates='char_class')
    
class ClassProficiency(Base):
    __tablename__ = 'class_proficiencies'
    
    id = Column(Integer, primary_key=True, index=True)
    char_class_id = Column(Integer, ForeignKey('char_classes.id'))
    proficiency_type = Column(String) # type of proficiency (e.g. skill, tool, weapon, armor)
    