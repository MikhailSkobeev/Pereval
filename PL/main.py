from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from PL.pereval.DateBase import models
from PL.pereval.DateBase.dateb import engine
from PL.pereval import user, post
from PL.pereval.AUTH.AUTH import authentication


app = FastAPI()
app.include_router(user.router)
app.include_router(authentication.router)
app.include_router(post.router)


@app.get("/")
def root():
    return "Hello people!"


models.Base.metadata.create_all(engine)

app.mount("/images", StaticFiles(directory="images"), name="images")