from fastapi import FastAPI

# Instancia de FASTAPI
app = FastAPI() # Esta variable va a contener a toda nuestra aplicación 


# Path Operations Decorator
@app.get("/")
def home():
    return {"Hello": "World"}
