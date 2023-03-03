from sqlalchemy import create_engine

from src.schema import Base


engine = create_engine("sqlite:///xyz.sqlite", echo=True)



if __name__=="__main__":
    """
    Creates an empty db based on specification
    in schema.py
    """
    Base.metadata.create_all(engine)