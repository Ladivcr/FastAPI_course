#Python
from typing import Optional
from enum import Enum # crear enumeraciones de str

#Pydantic
from pydantic import BaseModel
from pydantic import Field


#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

# Instancia de FASTAPI
app = FastAPI() # Esta variable va a contener a toda nuestra aplicación 

# Models
class HairColor(Enum):
    white = "White"
    brown = "Brown"
    black = "Black"
    blonde = "Blonde"
    red = "Red"


class Location(BaseModel):
    city: str = Field(
            ...,
            min_length=1,
            max_length=60
            )
    state: str = Field(
            ...,
            min_length=1,
            max_length=50
            )
    country: str = Field(
            ...,
            min_length=1,
            max_length=50
            )


class Person(BaseModel):
    # TODO: También es posible usar el parametro "example" en Field
    # para pasar un caso de ejemplo y probar el endpoint
    first_name: str = Field(
            ...,
            min_length=1,
            max_length=50
            )
    last_name: str = Field(
            ...,
            min_length=1,
            max_length=50
            )
    age: int = Field(
            ...,
            gt=0,
            le=115,
            )
    hair_color: Optional[HairColor] = Field(default=None) # Si nos pasan un valor dado que es opcional, esperamos un str
    is_married: Optional[bool] = Field(default=None) # Por defecto es un null que en python es un None

    # TODO: Automatizar la prueba de los endpoints
    # TODO: Debemos poner el primer valor igual a example
    # ya que swaggerUI así lo requiere
    class Config: 
        schema_extra = {
                "example": {
                    "first_name": "Facundo",
                    "last_name": "Garcia Martoni",
                    "age": 21,
                    "hair_color": "blonde",
                    "is_married": False
                }
        }

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
            description="This is the person name. It's between 1 and 50 characters",
            example="Sofi"
            ),

        age: int = Query(
            ...,
            title="Person Age",
            description="This is the person age. It's required",
            example = 21
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
            description="This is the person Id. It's greater than zero and it's requiered",
            example=123
            )

        ):
    return {person_id: "It exists!"}


# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
        person_id: int = Path(
            ...,
            title="Person ID", 
            description = "This is the person ID", 
            gt=0,
            example = 123
            ),
        person: Person = Body(...),
        location: Location = Body(...)
        
    ):

    # Unimos diccionarios
    results = person.dict()
    results.update(location.dict())

    return results



