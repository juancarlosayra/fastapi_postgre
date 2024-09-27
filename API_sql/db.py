from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import BASE

db_user: str = 'postgres'
db_port: int = 5432
db_password: str = 'gatopirata99'
db_host: str = 'localhost'

uri: str = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/fastapi-pg'

engine = create_engine(uri)
BASE.metadata.create_all(bind=engine)

#Session

session = sessionmaker(bind=engine, autoflush=True)

db_session = session()

try:
  connection = engine.connect()
  connection.close()
  print('Connected')
except Exception as e:
  print(f'Error: {str(e)}')