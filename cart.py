from product import Product
import json
class ShoppingCart:
    def __init__(self):
        self.products=[]
    def add_product(self,product):
        if not isinstance(product,Product):
            raise ValueError('Неподходящий объект')
        self.products.append(product)
    def get_total_price(self):
        total=0
        for i in self.products:
            total+=i.price
        return total
    def save_receipt(self,filename):
        with open(filename,'w',encoding='utf-8') as f:
            f.write('Чек \n')
            for i in self.products:
                f.write(f'{i} \n')
            f.write(f'Товаров: {len(self.products)}\n')    
            f.write(f'Итого: {self.get_total_price()} руб.')    
    def __str__(self):
        return f'Корзина: товаров — {len(self.products)}, сумма — {self.get_total_price()} руб. ' 
    def save_to_json(self, filename):
        data=[]
        for i in self.products:
            
            data.append(i.to_dict())
        with open(filename,'w',encoding='utf-8') as file:
            json.dump(data,file, ensure_ascii=False, indent=4) 
    @classmethod
    def load_from_json(cls, filename):
        with open(filename,'r', encoding='utf-8') as file:
            data=json.load(file)
        if not isinstance(data, list):
            raise ValueError ("Нужен список")    
        cart=cls()
        for item in data:
            product = Product.from_dict(item)
            cart.add_product(product)
        return cart    
