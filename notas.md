# ¿Qué es FastAPI?

- El framework mas veloz para el desarrollo web con Python. 
  Enfocado para realizar APIs, es el mas rápido en lo que respecta
  a la velocidad del servidor superando a Node.Js y a GO.
  Fue creado por Sebastian Ramirez, es de código abierto y
  se encuentra en Github, es usado por empresas como Uber,
  Windows, Netflix y Office.

  __comment was taken by Edkar Chachati - Platzi__

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


