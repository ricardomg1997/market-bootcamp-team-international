from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.product import product_router
from routers.user import user_router
app = FastAPI()
app.title = "Family products market with FastAPI"
app.version = "0.0.1"



app.add_middleware(ErrorHandler)
app.include_router(product_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)



products = [
    {
		"id": 1,
		"name": "leche",
		"about": "Leche entera",
		"year": "2024",
		"units": 7,
		"category": "lacteos"
	},
    {
		"id": 2,
		"name": "leche",
		"about": "Leche deslactosada",
		"year": "2023",
		"units": 7,
		"category": "lacteos"
	}
]

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')



