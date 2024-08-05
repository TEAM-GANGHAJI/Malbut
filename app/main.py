from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


from api.user import user_router
from api.auth import auth_router
from api.learning import learning_router
from api.conversation import conversation_router

app.include_router(user_router.router)
app.include_router(auth_router.router)
app.include_router(learning_router.router)
app.include_router(conversation_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)