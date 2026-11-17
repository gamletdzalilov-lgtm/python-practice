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

def save_product(product,filename):
    product=product.to_dict()
    with open(filename,'w',encoding="utf-8") as file:
        json.dump(product, file, ensure_ascii=False, indent=4)

def load_products(filename):
    try:
        with open(filename,'r',encoding="utf-8") as file:
            data=json.load(file)
    except FileNotFoundError:
        print('Файл не найден')        
        return []
    except json.JSONDecodeError as error:
        print(f"повреждённый JSON: строка {error.lineno}, столбец {error.colno}: {error.msg}")
        return []
    if not isinstance(data,dict):
        print ('data должен быть словарем')
        return []
    if "products" not in data:
        print(f'неверная структура: нет ключа products в файле {filename}')
        return []
    if not isinstance(data["products"], list):
        return "неверная структура: 'products' должен быть списком"     
    for i in data:
            for j in i:

                if not isinstance(i,dict):
                    print(f'Для {'i'} Нужен словарь')
                    continue
                if i!=('name','price'):
                    continue
            data.append((data['name'],data['price']))    
            

    

def input_product():
    while True:
        try:
            name=(input('Введите название товара - '))
            price=float(input('Введите стоимость - '))
            q=Product(name,price)
        except ValueError as e:
            print('Ошибка:', e)
        else:
            return q  

# 1. Создаём корзину и добавляем товары
cart = ShoppingCart()
cart.add_product(Product("Клавиатура", 3500))
cart.add_product(Product("Мышь", 1500))
assert cart.get_total_price() == 5000

# 2. Проверяем сохранение чека (save_receipt)
cart.save_receipt("receipt.txt")
with open("receipt.txt", "r", encoding="utf-8") as f:
    receipt_text = f.read()

assert "Клавиатура" in receipt_text
assert "Товаров: 2" in receipt_text
assert "Итого: 5000 руб." in receipt_text

# 3. Проверяем пустую корзину и её чек
empty_cart = ShoppingCart()
empty_cart.save_receipt("empty_receipt.txt")
with open("empty_receipt.txt", "r", encoding="utf-8") as f:
    assert "Итого: 0 руб." in f.read()

# 4. Проверяем сохранение и загрузку JSON
cart.save_to_json("cart.json")
restored_cart = ShoppingCart.load_from_json("cart.json")
assert restored_cart.get_total_price() == 5000

print("Все проверки прошли успешно!")



            