from . import base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from contextlib import contextmanager


@contextmanager
def sessionScope(connectionString):
    engine = create_engine(connectionString, echo=False)
    base.Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    Session.configure(bind=engine)

    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
