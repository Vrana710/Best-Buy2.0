import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount


def test_create_product():
    # Test normal product creation
    product = Product(name="Test Product", price=100, quantity=10)
    assert product.name == "Test Product"
    assert product.price == 100
    assert product.quantity == 10
    assert product.is_active() is True

    # Test invalid product creation
    with pytest.raises(ValueError):
        Product(name="", price=100, quantity=10)
    with pytest.raises(ValueError):
        Product(name="Test Product", price=-10, quantity=10)
    with pytest.raises(ValueError):
        Product(name="Test Product", price=100, quantity=-10)


def test_product_activation():
    product = Product(name="Test Product", price=100, quantity=10)
    product.deactivate()
    assert product.is_active() is False
    product.activate()
    assert product.is_active() is True


def test_product_purchase():
    product = Product(name="Test Product", price=100, quantity=10)
    total_price = product.buy(5)
    assert total_price == 500
    assert product.quantity == 5
    with pytest.raises(ValueError):
        product.buy(6)


def test_product_with_promotion():
    # Create product and promotion
    promotion = PercentDiscount(name="10% off", percent=10)
    product = Product(name="Test Product", price=100, quantity=10, promotion=promotion)

    # Test buying with promotion
    total_price = product.buy(5)
    assert total_price == 450  # 10% off of 500


def test_non_stocked_product():
    non_stocked_product = NonStockedProduct(name="Non-Stocked Product", price=200)
    assert non_stocked_product.quantity == 0
    total_price = non_stocked_product.buy(3)
    assert total_price == 600  # 3 * 200


def test_limited_product():
    limited_product = LimitedProduct(name="Limited Product", price=50, quantity=100, maximum=5)
    with pytest.raises(ValueError):
        limited_product.buy(6)  # Exceeds the maximum purchase limit
    total_price = limited_product.buy(5)
    assert total_price == 250  # 5 * 50
