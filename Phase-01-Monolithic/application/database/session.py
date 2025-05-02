from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from dotenv import load_dotenv
from contextlib import contextmanager
from application.database.Base import Base

class _Session:
    _engine=None
    _session_factory=None
    meta=MetaData()


    def __init__(self):
        load_dotenv()
        database_url=getenv('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL is not set in the environment variable")

        self._engine=create_engine(database_url,echo=True)
        self._session_factory=sessionmaker(
            bind=self._engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
            )
        self.meta.bind=self._engine
        _Session._engine=self._engine
        
    @contextmanager
    def get_session(self):
        session=self._session_factory()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_tables(self):
        Base.metadata.create_all(bind=self._engine)


    def read_all(self, model_cls):
        with self.get_session() as session:
            return session.query(model_cls).all()


    def read_one(self, model_cls, id):
        with self.get_session() as session:
            return session.get(model_cls,id)


    def write(self, tableElement):
        with self.get_session() as session:
            session.add(tableElement)
            session.commit()
            session.refresh(tableElement)
            return tableElement


    def delete(self, model_cls, id):
        with self.get_session() as session:
            instance=session.get(model_cls,id)
            if not instance:
                return False
            session.delete(instance)
            session.commit()
            return True


    def update(self, model_cls, id, updates):
        with self.get_session() as session:
            instance=session.get(model_cls, id)
            if not instance:
                return None

            for key, value in updates.dict(exclude_unset=True).items():
                if key != "id":  
                    setattr(instance, key, value)
            session.commit()
            session.refresh(instance)
            return instance


session_instance=_Session()