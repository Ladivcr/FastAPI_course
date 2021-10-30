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

__comment was taken by Javier Almarza Bucarey__

_
