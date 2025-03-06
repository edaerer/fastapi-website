from pydantic import BaseModel


class ProductWithoutPydantic:
    def __init__(self, name:str, price:float, in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock


class ProductWithPydantic(BaseModel):
    name: str
    price: float
    in_stock: bool


if __name__ == "__main__":

    str_data = {
        "name": "Product",
        "price": "100",
        "in_stock": "False"
    }

    p1 = ProductWithoutPydantic(name=str_data.get("name"), price=str_data.get("price"), in_stock=str_data.get("in_stock"))
    print(type(p1.name), type(p1.price), type(p1.in_stock)) # output: <class 'str'> <class 'str'> <class 'str'>
    print(p1.name, p1.price, p1.in_stock) # output: Product 100 False

    p2 = ProductWithPydantic(name=str_data.get("name"), price=str_data.get("price"), in_stock=str_data.get("in_stock"))
    print(type(p2.name), type(p2.price), type(p2.in_stock)) # output: <class 'str'> <class 'float'> <class 'bool'>
    print(p2.name, p2.price, p2.in_stock) # output: Product 100 False

    # Pydantic object initialization shortcut
    p3 = ProductWithPydantic(**str_data)