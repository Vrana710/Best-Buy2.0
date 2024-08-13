class Promotion:
    """
    Base class for all promotions.
    """

    def __init__(self, name: str):
        """
        Constructs all the necessary attributes for the promotion object.

        Args:
            name (str): The name of the promotion.
        """
        self._name = name

    @property
    def name(self) -> str:
        """Returns the name of the promotion."""
        return self._name

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the promotion to the product for a given quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The total price after applying the promotion.
        """
        return product.price * quantity


class SecondHalfPrice(Promotion):
    """
    A promotion where the second item is half price.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the second half-price promotion to the product for a given quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The total price after applying the promotion.
        """
        full_price_quantity = quantity // 2 + quantity % 2
        half_price_quantity = quantity // 2
        return full_price_quantity * product.price + half_price_quantity * product.price * 0.5


class ThirdOneFree(Promotion):
    """
    A promotion where the third item is free.
    """

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the third one free promotion to the product for a given quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The total price after applying the promotion.
        """
        full_price_quantity = quantity - (quantity // 3)
        return full_price_quantity * product.price


class PercentDiscount(Promotion):
    """
    A promotion with a percentage discount.
    """

    def __init__(self, name: str, percent: float):
        """
        Constructs all the necessary attributes for the percentage discount promotion object.

        Args:
            name (str): The name of the promotion.
            percent (float): The percentage discount to apply.
        """
        super().__init__(name)
        self._percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        """
        Applies the percentage discount promotion to the product for a given quantity.

        Args:
            product (Product): The product to apply the promotion to.
            quantity (int): The quantity of the product to apply the promotion to.

        Returns:
            float: The total price after applying the promotion.
        """
        discount = self._percent / 100.0
        return product.price * quantity * (1 - discount)
