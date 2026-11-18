import json
from product import Product
from cart import ShoppingCart




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
        print( "неверная структура: 'products' должен быть списком")
        return []
    products=[]
    skipped=[]
    for item in data['products']:
        if not isinstance(item,dict): 
            skipped.append(f'{item} не словарь')
            continue
        missing=[]
        for key in ('name','price'):
            if key not in item:
                missing.append(key)
        if len(missing)!=0:
            skipped.append(f'Нет ключей: {", ".join(missing)}')
            continue

        try:
            product = Product.from_dict(item)
            products.append(product)
        except ValueError as error:
            skipped.append(f'Ошибка валидации для {item}: {error}')  
    print(f'Загружено: {len(products)}, пропущено: {len(skipped)}')   
    for skip in skipped:
            print(f" - {skip}")        
    return products
            

    

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
assert len(load_products("products.json")) == 2
assert load_products("нет_такого_файла.json") == []
print("Все проверки прошли успешно!")



            