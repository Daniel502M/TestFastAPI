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

print("Hello Samvel and Edmond, how are you?")
print("What are you doing now?")
print("Today is sunny")
print("I am working now")

@app.get("/fine")
def get_text():
    return "fine"
