from fastapi import FastAPI

from endpoins import users_handlers,auth,jobs_handler
from db.base_connect import database
import uvicorn
app = FastAPI()

app = FastAPI(title="Employment exchange")
app.include_router(users_handlers.router, prefix="/users", tags=["users"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(jobs_handler.router, prefix="/jobs", tags=["jobs"])

#делаем декоратор get(чуточку rest api)
@app.get("/")
async def root():
    return {"message": "Hello World"}
#startup - выполняет при включение сервера
@app.on_event('startup')
async def startup():
    await database.connect()
#shutdown -  выполняет при выключение сервака
@app.on_event('shutdown')
async def shutdown():
    database.disconnect()


#автомат.сервер
if __name__ == '__main__':
    uvicorn.run('main:app',port=8000,host='0.0.0.0',reload=True)
