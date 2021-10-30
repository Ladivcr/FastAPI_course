#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
# Instancia de FASTAPI
app = FastAPI() # Esta variable va a contener a toda nuestra aplicación 

# Models

class Person(BaseModel): 
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None # Si nos pasan un valor dado que es opcional, esperamos un str
    is_married: Optional[bool] = None # Por defecto es un null que en python es un None


# Path Operations Decorator
@app.get("/")
def home():
    return {"Hello": "World"}

# Request and Response Body
@app.post("/person/new")
def create_person(person: Person = Body(...)): # El triple punto indica que es obligatorio
   return Person

# Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
        name: Optional[str] = Query(None, min_length=1, max_length=50),
        age: int = Query(...) # Query parameter obligatorio
        ):
    return {name: age}
