from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de datos para el elemento
class Item(BaseModel):
    id: int
    name: str

# Base de datos ficticia
db = []

# Ruta para crear un nuevo elemento
@app.post("/items/")
def create_item(item: Item):
    db.append(item)
    return item

# Ruta para obtener todos los elementos
@app.get("/items/")
def get_items():
    return db
