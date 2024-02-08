from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///research.db")
Base = declarative_base()


class CancerResearch(Base):
    # only initial creation of course no version control of schemas or anything like alembic
    __tablename__ = "cancer_research_versioned"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    year_last_updated = Column(Integer)
    version_number = Column(Integer)


Base.metadata.create_all(engine)
