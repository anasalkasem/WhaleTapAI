from models.models import Base
from models.database import engine

def init_db():
    Base.metadata.create_all(bind=engine)
