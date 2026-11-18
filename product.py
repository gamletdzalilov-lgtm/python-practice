class Product:
    def __init__(self,name,price):
        if not isinstance(name,str) or len(name.strip())==0:
            raise ValueError ('введите имя')
        self.name=name
        if not isinstance(price, (int,float)) or isinstance(price,bool) or price<0:
            raise ValueError ('Введите число не меньше 0')
        self.price=price
    def __str__(self):
        return f'Товар: {self.name}, цена: {self.price} руб.'   
    def __repr__(self):
        return f'Product(name={self.name!r}, price={self.price!r})'
    def to_dict(self):
        q={}
        q['name']=self.name
        q['price']=self.price
        return q
    @classmethod
    def from_dict(cls, data):
        if not isinstance(data, dict):
                raise ValueError("Ожидается словарь с данными товара")
        if "name" not in data or "price" not in data:
            raise ValueError("В словаре отсутствуют ключи 'name' или 'price'")
        return cls(data["name"], data["price"])
