from product import Product
import pytest
def test_to_dict():
    tea = Product("Чай", 100)
    assert tea.to_dict() == {"name": "Чай", "price": 100}

def test_create_product():
    tea = Product("Чай", 100)
    assert tea.name == "Чай"
    assert tea.price == 100    
def test_negative_price():
    with pytest.raises(ValueError):
        Product("Сахар", -5)    
def test_empty_name():
    with pytest.raises(ValueError):
        Product('',10)
def test_bool_price():
    with pytest.raises(ValueError):
        Product('Кола',True)
def test_zero_price():
    burger=Product('бургер',0)
    assert burger.price==0                        
def test_from_dict():
            coffee=Product.from_dict({'name':'кофе','price':20})
            assert coffee.name =='кофе'
            assert coffee.price ==20