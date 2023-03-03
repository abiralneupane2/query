from sqlalchemy import create_engine

from schema import Base


engine = create_engine("sqlite:///xyz.sqlite", echo=True)


if __name__=="__main__":
    Base.metadata.create_all(engine)