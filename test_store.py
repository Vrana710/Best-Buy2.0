import pytest
from store import Store
from products import Product


def test_store_initialization():
    product1 = Product(name="Product 1", price=100, quantity=10)
    product2 = Product(name="Product 2", price=200, quantity=20)
    store = Store(product_list=[product1, product2])
    assert len(store.product_list) == 2


def test_store_add_remove_product():
    store = Store(product_list=[])
    product = Product(name="Product", price=100, quantity=10)
    store.add_product(product)
    assert len(store.product_list) == 1
    store.remove_product(product)
    assert len(store.product_list) == 0


def test_store_get_total_quantity():
    product1 = Product(name="Product 1", price=100, quantity=10)
    product2 = Product(name="Product 2", price=200, quantity=20)
    store = Store(product_list=[product1, product2])
    assert store.get_total_quantity() == 30


def test_store_order():
    product1 = Product(name="Product 1", price=100, quantity=10)
    product2 = Product(name="Product 2", price=200, quantity=20)
    store = Store(product_list=[product1, product2])
    total_price = store.order([(product1, 5), (product2, 2)])
    assert total_price == 900  # 5 * 100 + 2 * 200
    assert product1.quantity == 5
    assert product2.quantity == 18
