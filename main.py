from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "Hello"


@app.get("/users")
def get_all_users():
    return []

@app.get("/posts")
def get_all_posts():
    return []