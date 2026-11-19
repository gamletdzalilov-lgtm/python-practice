
from product import Product
from cart import ShoppingCart
from loaders import load_products




if __name__ == "__main__":
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



                