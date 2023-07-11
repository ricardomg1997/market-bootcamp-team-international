from models.product import Product as ProductModel
from schemas.product import Product

class ProductService:
    def __init__(self, db) -> None:
        self.db = db
    
    def get_products(self):
        result = self.db.query(ProductModel).all()
        return result
    
    def get_product(self, id):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        return result
    
    def get_product_by_category(self, category):
        result = self.db.query(ProductModel).filter(ProductModel.category == category).all()
        return result
    
    def create_product(self, product: Product):
        new_product = ProductModel(**product.dict())
        self.db.add(new_product)
        self.db.commit()
        return
    
    def update_product(self, id: int, data: Product):
        product = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        product.name = data.name
        product.about = data.about
        product.year = data.year
        product.units = data.units
        product.category = data.category
        self.db.commit()
        return
    
    def delete_product(self, id: int):
        result = self.db.query(ProductModel).filter(ProductModel.id == id).first()
        self.db.delete(result)
        self.db.commit()
        return result