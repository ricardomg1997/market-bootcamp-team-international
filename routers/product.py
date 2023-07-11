from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.product import Product as ProductModel
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from services.product import ProductService
from schemas.product import Product

product_router = APIRouter()

#Obtener productos
@product_router.get('/products', tags=['products'], response_model=List[Product], status_code=200, dependencies=[Depends(JWTBearer())])
def get_products() -> List[Product]:
    db = Session()
    result = ProductService(db).get_products()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
#Obtener producto por id
@product_router.get('/products/{id}', tags=['products'], response_model=Product)
def get_product_by_id(id: int = Path(ge=1, le=2000)) ->     Product:
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
#Obtener producto por categoria
@product_router.get('/products/', tags=['products'], response_model=List[Product])
def get_products_by_category(category: str = Query(min_length=2, max_length=50)) -> List[Product]:
    db = Session()
    result = ProductService(db).get_product_by_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    #data = [ item for item in products if item['category'] == category ]
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
#Crear Producto
@product_router.post('/products', tags=['products'], response_model=dict, status_code=201)
def create_product(product: Product) -> dict:
    db = Session()
    ProductService(db).create_product(product)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado el producto"})
#Editar Producto
@product_router.put('/products/{id}', tags=['products'], response_model=dict, status_code=200)
def update_product(id: int, product: Product)-> dict:
    db = Session()
    result = ProductService(db).get_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    ProductService(db).update_product(id, product)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el producto"})
#Eliminar producto
@product_router.delete('/products/{id}', tags=['products'], response_model=dict, status_code=200)
def delete_product(id: int)-> dict:
    db = Session()
    result = result = ProductService(db).delete_product(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el producto"})