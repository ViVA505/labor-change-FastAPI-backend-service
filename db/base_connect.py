from databases import Database
#create_engine - будем использовать для подключение к бд, MetaData - контейнер(обьект) который содержить необходимую информацию для орн таблицы
from sqlalchemy import create_engine,MetaData
from core.config import DATABASE_URL

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)