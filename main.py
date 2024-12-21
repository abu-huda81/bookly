from fastapi import FastAPI
from user.models import User as UserModel, Note as NoteModel
from product.models import Product as ProductModel, Image as ImageModel
from category.models import Category as CategoryModel
from core.database import engine, Base, get_db


app = FastAPI()


# database:
Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup():
    get_db()


@app.on_event("shutdown")
async def shutdown():
    await engine.dispose()
    

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
