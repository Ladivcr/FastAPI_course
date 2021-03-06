# FastAPI_course
---
¿qué es un servidor? -> Ambas opciones son correctas
starlette -> Es un framework de desarrollo web pero de bajo nivel, python toma a starlette y le agrega funcionalidades. FastAPI es un 
starlette con esteroides

¿qué es openapi? -> Es una especificación, un conjunto de reglas 
que permite definir algo. Permite definir como crear, como visualizar,
APIS. Es un conjunto de reglas que me permiten decir si una API esta ien o no. 

Swagger, SwaggerUX y REDOC son apoyos para openapi para ver
la api 

¿Con cuál de las siguientes operations no deberías enviar jamás un request body?
-> DELETE NO ES 

# ¿Qué es FastAPI?

- El framework mas veloz para el desarrollo web con Python. 
  Enfocado para realizar APIs, es el mas rápido en lo que respecta
  a la velocidad del servidor superando a Node.Js y a GO.
  Fue creado por Sebastian Ramirez, es de código abierto y
  se encuentra en Github, es usado por empresas como Uber,
  Windows, Netflix y Office.

  __comment was taken by Edkar Chachati - Platzi__

**Instalar FastAPI**
> pip install fastapi uvicorn 

# Ubicación de FastaPI en el ecosistema de Python 

FastAPI utiliza otros frameworks dentro de si para funcionar
  - **Uviconr:** Es una libreria de Python que funciona de servidor, 
  es decir, permite que cualquier computadora se convierta en servidor. 
  
  - **Starlette**: Es un framework de desarrollo web de bajo nivel, para desarrollar
  aplicaciones. 
  
  - **Pydantic:** Es un framework que permite trabajar con datos similar a pandas, 
  pero este te permite usar modelos los cuales aprovecara FastAPI para crear 
  la API. 

  __comment was taken by Edkar Chachati - Platzi__


# Inicializar la aplicación 

> Ejecutar el comando: *uvicorn main:app --reload*

Donde _main_ es el nombre del archivo y _app_ es el nombre de la variable que contiene nuestra aplicación 
y _--reload_ Es un modificador que funciona como hot reloading, es decir, provocamos un efecto en la app y
podemos ver los cambios que hemos hecho. 

# Documentación interactiva de una API

FastAPI también está parado sobre los hombros de OpenAPI, el cual es un conjunto de reglas que permite 
trabajar con APIs. FastAPI funciona sobre un programa de Swagger el cual es Swagger UI, que permite
mostrar la API documentada. 

- Acceder a la documentación interactiva con Swagger UI: {localhost}/docs
- Acceder a la documentación interactiva con Redoc: {localhost}/redoc

__comment was taken by Pedro Alvarado García - Platzi__ 


## OAS3 
> Open API Specification
Es la documentación que viene de base con FastAPI


# Path Operations 

## ¿Qué es un path?

- Un path es lo mis que un route o endpoints y es todo aquello que vaya después de nuestro dominio 
a la derecha del mismo. 

## ¿Qué son las operations?

No son más que la combinación de rutas o endpoints con métodos http utilizando decoradores y funciones. **

- Un operations es exactamente lo mismo que un método http y tenemos las siguinetes más populates: 
> - GET: Obtener
> - POST: Crear
> - PUT & Patch: Modificar-Actualizar
> - DELETE: Eliminar
y otros métoso como: OPTIONS, HEAD, PATCH...


__comment was taken by Eduardo Enrique Morales Martinez - Platzi__

## Otros métodos

- Options: Devuelve un header adicional llamado allow que contiene los métodos http que pueden utilizarse
en ese endpoint 
- Head: Devuelve info sobre el documento, más no el documento en sí 
- Patch: Hacer modificaciones parciales al documento **A diferencia de PUT que permiete cambiar el documento 
entero**
- Trace: Nos permite observar que esta pasando en la petición y nos devuelve nuestro input con propositos de debugging

__comment was taken by Sebastián Andrade - Platzi__

Tenemos en nuestro main.py: @app.get("/") -> Lo cual corresponde a: PATH OPERATION DECORATIO 
y def home(): return {"hello": "world"} a PATH OPERATION FUNCTION

# Path Parameters

Los parámetros de ruta son partes variables de una ruta URL. Por lo general, se utulizan para señalar
un recurso específico dentro de una colección, como un usuario idetificado por ID. Una URL puede tener varios
parámetros de ruta.

__comment was taken by Duvan Jose Botello Ramirez - Platzi__

> **CADA VEZ QUE DEFINO UN PATH PARAMETER DEBO DE PASARLO DE MANERA OBLIGATORIA**

# Query Parameters

- Un Query Parameter es un conjunto de elementos opcionales, los cuales son añadidos al finalizar la ruta
con el objetivo de definir contenido o acciones en la url, estos elementos se añaden después de un _?_
para agregar más query parameters utilizamos _&_

__comment was taken by Jeiber Ignacio Jimenez Bojaca - Platzi__


# Request Body y Response Body 

Debes saber que bajo el protocolo **HTTP** existe una comunicación entre el usuario y el servidor. 
Esta comunicación está compuesta por cabeceras (headers) y un cuerpo (body). Por lo mismo, se tienen dos
direcciones en la comunicación entre el cliente y el servidor, se definen de la siguiente manera: 

- **Request:** Cuando el cliente solicita/pide datos al servidor
- **Responde:** Cuando el servidor responde al cliente

**Request Body** 
Con lo anterior mencionado, Request Body viene a ser el cuerpo (body) de una solicitud de cliente al servidor. 

**Response Body**
Con lo anterior mencionado, **Response Body** viene a ser el cuerpo (body) de una **respuesta** del servidor al cliente. 

__comment was taken by Javier Almarza Bucarey - Platzi__

# MODELS

- Documentación oficial: https://fastapi.tiangolo.com/tutorial/sql-databases/

Un modelo es la representación de una entidad en código, al menos de una manera descriptiva. 

**¿Cómo luce un modelo dentro de FastAPI?**

Modelo pydantic para validar datos: 

```
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True

```

Un modelo para mapear los datos a la base de datos
(ORM, SQLalchemy)

```
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
```

__comment was taken by Duvan Jose Botello Ramirez - Platzi__

# VALIDACIONES

Las validaciones tal como se definen, nos sirven para comprobar si son correctos los parámetros
entregados en cada una de las peticiones. Estas validaciones funcionan restringiendo o indicando el 
formato de entrega en cada una de las peticiones. 

**Query Parameters**
Entonces se definen las validaciones para las Query Parameters para definir un estándar de consulta 
y especificar cómo se debe entregar los datos. 

**EJ**
Se define la siguiente consulta: 
```
https://domain.com/user/detail?nombre=Manolo&edad=20
```

Como validaciones tendríamos que limitar el tamaño de caracteres que pueden tener el atributo "nombre"
(50>largo>1), además de limitar los valores para "edad" (300>edad>0)

```
# Validaciones.
@mi_app.get("/user/detail") # Ruta para realizar la consulta.
def mostrar_usuario(
	#Opcional.
	nombre: Optional[str] = Query(None, min_length=1, max_length=50),
	# Obligatorio.
	edad: int = Query(...)
   ):

   return {nombre: edad};
```

__comment was taken by Javier Almarza Bucarey - Platzi__

# Más sobre validaciones

Para especificar las validaciones, debemos pasarle como parámetros a la función **Query** lo que necesitamos validar. 

- Para tipos de datos **str:**

> - max_length: Para especificar el tamaño máximo de la cadena
> - min_length: Para especificar el tamaño minimo de la cadena
> - regex: Para especificar expresiones regulares

- Para tipos de datos **int:**
> - ge: (greater or equal than >=) Para especificar que el valor debe ser mayor o igual 
> - le: (less or equal than <=) Para especificar que el valor debe ser menor o igual 
> - gt: (greater than >) Para especificar que el valor debe ser mayor
> - lt: (less than <) Para especificar que el valor debe ser menor 

**EJ**

```
# Validaciones de un nombre de usuario 
Query(None, min_length=1, max_length=50)):
```

Es posible dotar de mayor contexto a nuestra documentación. Se deben usar los parámetros **title**
y **description**.

- title: Para definir un titulo al parámetro
- description: Para especificar una descripción al parámetro

**EJ**

```
# Validaciones para un identificador
Query(None, title="ID del usuario", description="El ID se consigue entrando a las configuraciones del perfil");

```

__comment was taken by Javier Almarza Bucarey - Platzi__

# Validaciones: Models

**Diferencia Path, Query Parameters and Request Body**

- Usamos Path Parameters cuando por ejemplo se trata de un id y esas cosas, como variables etc.
- Usamos Requests Body para enviar información que tiene formato de un modelo
- Usamos Query Parameters para solicitar información opcional del servidor

Para validar modelos tomamos uso de las clases de Pydantic Field que funiona igual a las validaciones
que ya hemos hecho con Path, Query y Body

```
from pydantic import BaseModel, Field

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    age: int = Field(
        ...,
        gt=0,
        le=110
    )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)

```

Puedes ver que hair_color ya tiene un tipo distinto a String, esto lo hacemos para validar
que tenga un campo permitido haciendo otra clase usando Enum


```
from enum import Enum

class HairColor(Enum):
    white: str = 'white'
    black: str = 'black'
    brown: str = 'brown'
    red: str = 'red'
    blonde: str = 'blonde'
    tinted: str = 'tinted'
```

Aquí tenemos enumerados algunos colores de pelo y ahora cada vez que alguien trate de ingresar
un valor que no se encuentra en nuestra clase que hereda de Enum, le arrojará un error 422 Unprocessable Entity 
con el siguien mensaje: 

```
{
  "detail": [
    {
      "loc": [
        "body",
        "person",
        "hair_color"
      ],
      "msg": "value is not a valid enumeration member; permitted: 'white', 'black', 'brown', 'red', 'blonde', 'tinted'",
      "type": "type_error.enum",
      "ctx": {
        "enum_values": [
          "white",
          "black",
          "brown",
          "red",
          "blonde",
          "tinted"
        ]
      }
    }
  ]
}
```

__comment was taken by Edkar Chachati - Platzi__

# Tipos de Datos Especiales

**Clásicos**

- str
- int
- float 
- bool

**Exóticos**

- Enum
- HttpUrl: Valida que lo que se recibe es una url 
- FilePath: Valida que lo que se recibe es un path para un archivo
- DirectoryPath: Valida que lo que se recibe es un path para un directorio
- EmailStr: Valida que lo que se recibe es un email
- PaymentCardNumber: Valida que lo que se recibe es una tarjeta
- IPvAnyAdress: Valida que lo que se recibe es una IP 
- NegativeFloat: Valida que lo que se recibe es un flotante negativo
- PositiveFloat: Valida que lo que se recibe es un flotante positivo  
- NegativeInt: Valida que lo que se recibe es un entero negativo 
- PositiveInt: Valida que lo que se recibe es un entero positivo

> Más tipos de datos: https://pydantic-docs.helpmanual.io/usage/types/#pydantic-types

**Ejemplo de uso de datos Exóticos por un estudiante de Platzi**

```
"""
Program: Reto 1; uso de tipos de datos exóticos.

Description: Simulación de endpoint encargado de registrar una compra en una tienda online.

Author: Jose Noriega <josenoriega723@gmail.com>

Last Update: 2021-10-26 

"""

import re
from datetime import date
from typing import Dict
from typing import Any

# Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from pydantic import PaymentCardNumber
from pydantic.validators import str_validator
from pydantic.types import PaymentCardBrand

# Fast API
from fastapi import FastAPI
from fastapi import Body


app = FastAPI()

PHONE_REGEXP = re.compile(r'^\+?[0-9]{1,3}?[0-9]{6,14}$')

# Custom Types


class PhoneNumber(str):
    """Phone number type"""

    @classmethod
    def __get_validators__(cls) -> Dict[str, Any]:
        yield str_validator
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        field_schema.update(
            pattern=r'^\+?[0-9]+$',
            example=['+541112345678'],
            format='phone-number',
        )

    @classmethod
    def validate(cls, value: str) -> str:
        if not isinstance(value, str):
            raise TypeError('Phone number must be a string')

        match = PHONE_REGEXP.search(value)

        if not match:
            raise ValueError('Phone number must be a valid phone number')

        return value

    def __repr__(self) -> str:
        return f'PhoneNumber({super().__repr__()})'


# Models


class Person(BaseModel):
    name: str = Field(...,
                      min_length=2,
                      max_length=50,
                      title='Name',
                      description='The name of the person that will receive the package.',
                      example='John Doe')

    email: EmailStr = Field(...,
                            title='Email',
                            description='The email of the person that will receive the package.')

    phone: PhoneNumber = Field(...,
                               title='Phone',
                               description='The phone number of the person that will receive the package.')


class Product(BaseModel):
    """Product model"""

    name: str = Field(...,
                      min_length=2,
                      max_length=50,
                      title='Name',
                      description='The name of the product.',
                      example='Laptop')


class PaymentMethod(BaseModel):
    """Payment method model"""

    card_number: PaymentCardNumber = Field(...,
                                      title='Number',
                                      description='The number of the payment card.',
                                      example='1234567890123456')

    expiration_month: int = Field(...,
                                  title='Expiration month',
                                  description='The expiration month of the payment card.',
                                  ge=1,
                                  le=12,
                                  example=12)

    expiration_year: int = Field(...,
                                 title='Expiration year',
                                 description='The expiration year of the payment card.')

    @property
    def brand(self) -> PaymentCardBrand:
        """Returns the brand of the payment card"""
        return self.card_number.brand

    @property
    def expired(self) -> bool:
        """Returns if the payment card is expired"""

        today = date.today()
        expiration_date = date(year=self.expiration_year,
                               month=self.expiration_month,
                               day=1)

        return today > expiration_date


class Address(BaseModel):
    """Address model"""

    street: str = Field(...,
                        min_length=2,
                        max_length=50,
                        title='Street',
                        description='The street of the address.')

    city: str = Field(...,
                      min_length=2,
                      max_length=50,
                      title='City',
                      description='The city of the address.')

    country: str = Field(...,
                         min_length=2,
                         max_length=50,
                         title='Country',
                         description='The country of the address.')

# Endpoints

@app.post('/order')
def add_order(
    person: Person = Body(...,),
    product: Product = Body(...,),
    address: Address = Body(...,),
    payment_method: PaymentMethod = Body(...,),
):
    """Registers a new order"""

    return {
        'person': person,
        'product': product,
        'address': address,
        'payment_method': {
            'brand': payment_method.brand,
            'last4': payment_method.card_number.last4,
            'mask': payment_method.card_number.masked,
            'expired': payment_method.expired,
        }
    }

```


**Request Body**

```
{
    "person": {
        "name": "John Doe",
        "email": "john@emai.com",
        "phone": "+52638107905"
    },
    "address": {
        "street": "Street",
        "city": "City",
        "country": "Country"
    },
    "product": {
        "name": "Macbook Pro"
    },
    "payment_method": {
        "card_number":"4242424242424242",
        "expiration_month": 12,
        "expiration_year": 2050
    }
 
}
```

**Response Body**

```
{
    "person": {
        "name": "John Doe",
        "email": "john@emai.com",
        "phone": "+52638107905"
    },
    "product": {
        "name": "Macbook Pro"
    },
    "address": {
        "street": "Street",
        "city": "City",
        "country": "Country"
    },
    "payment_method": {
        "brand": "Visa",
        "last4": "4242",
        "mask": "424242******4242",
        "expired": false
    }
}
```
