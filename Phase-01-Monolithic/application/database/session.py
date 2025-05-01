from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv


class Session:
    _engine=None
    _session_factory=None
    meta=MetaData()


    def __init__(self):
        database_url=getenv('DATABASE_URL')
        if not database_url:
            raise ValueError("DATABASE_URL is not set in the environment variables.")

        self._engine=create_engine(database_url,echo=True)
        self._session_factory=sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False
            )
        self.meta.bind=self._engine
        

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
        self.meta.create_all(self._engine)


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
        with cls.get_session() as session:
            instance=session.get(model_cls, id)
            if not instance:
                return None

            for key, value in updates.items():
                if key != "id":  
                    setattr(instance, key, value)
            session.commit()
            session.refresh(instance)
            return instance