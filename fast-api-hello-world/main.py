#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path
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
        name: Optional[str] = Query(
            None, min_length=1,
            max_length=50,
            title = "Person Name", 
            description="This is the person name. It's between 1 and 50 characters"
            ),

        age: int = Query(
            ...,
            title="Person Age",
            description="This is the person age. It's required"
            ) # Query parameter obligatorio
        ):
    return {name: age}

# Validaciones: Path Parameters

#TODO: Si tenemos dos enpoints que son iguales, python va a tomar el primero dado que lee de izquierda a derecha
# y de arriba hacia abajao linea por linea
@app.get("/person/detail/{person_id}")
def show_person(
        person_id: int = Path(
            ...,
            gt=0,
            title="Person Id", 
            description="This is the person Id. It's greater than zero and it's requiered"
            )

        ):
    return {person_id: "It exists!"}

