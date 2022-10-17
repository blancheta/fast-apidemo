from fastapi import FastAPI

app = FastAPI()
v1 = FastAPI()


@v1.get("/api/users")
def read_main():
    return {"message": "Hello World from api v1"}


v2 = FastAPI()


@v2.get("/api/users")
def read_sub():
    return {"message": "Hello World from  api v2"}


app.mount("/api/v1", v1)
app.mount("/api/v2", v2)