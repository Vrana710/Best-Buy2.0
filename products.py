from promotions import Promotion


class Product:
    """
    A class to represent a product available in the store.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product available.
        active (bool): The status of the product's availability.
        promotion (Promotion): The promotion applied to the product, if any.
    """


    def __init__(self, name: str, price: float, quantity: int, promotion=None):
        """
        Constructs all the necessary attributes for the product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
            promotion (Promotion): The promotion applied to the product.

        Raises:
            ValueError: If name is empty or if price or quantity are negative.
        """
        if not name or price < 0 or quantity < 0:
            raise ValueError("Invalid parameters for product creation.")
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion = promotion


    @property
    def name(self) -> str:
        """Returns the name of the product."""
        return self._name


    @property
    def price(self) -> float:
        """Returns the price of the product."""
        return self._price


    @price.setter
    def price(self, value: float):
        """
        Sets the price of the product.

        Args:
            value (float): The price to set.

        Raises:
            ValueError: If the price is negative.
        """
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value


    @property
    def quantity(self) -> int:
        """Returns the quantity of the product."""
        return self._quantity


    @quantity.setter
    def quantity(self, value: int):
        """
        Sets the quantity of the product. If quantity reaches 0, deactivates the product.

        Args:
            value (int): The quantity to set.

        Raises:
            ValueError: If the quantity is negative.
        """
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()


    @property
    def promotion(self) -> Promotion:
        """Returns the promotion applied to the product."""
        return self._promotion


    @promotion.setter
    def promotion(self, promo: Promotion):
        """
        Sets the promotion applied to the product.

        Args:
            promo (Promotion): The promotion to apply.
        """
        self._promotion = promo


    def set_promotion(self, promo: Promotion):
        """
        Sets the promotion applied to the product.

        Args:
            promo (Promotion): The promotion to apply.
        """
        self.promotion = promo


    def is_active(self) -> bool:
        """
        Checks if the product is active.

        Returns:
            bool: True if the product is active, False otherwise.
        """
        return self._active


    def activate(self):
        """Activates the product."""
        self._active = True


    def deactivate(self):
        """Deactivates the product."""
        self._active = False


    def show(self) -> str:
        """
        Returns a string that represents the product.

        Returns:
            str: A string representation of the product.
        """
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}{promo}"


    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product, updating the quantity and returning the total price.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is less than or equal to 0, or more than the available quantity.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise ValueError("Not enough quantity available.")
        
        # Apply promotion if available
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        return total_price


    def __str__(self):
        """Returns a string representation of the product using the show method."""
        return self.show()


    def __gt__(self, other):
        """Compares products by price."""
        if not isinstance(other, Product):
            raise ValueError("Can only compare products.")
        return self.price > other.price


class NonStockedProduct(Product):
    """
    A class to represent a non-stocked product in the store.

    Inherits from the Product class, but has no quantity attribute.
    """


    def __init__(self, name: str, price: float):
        """
        Constructs all the necessary attributes for the non-stocked product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
        """
        super().__init__(name, price, quantity=0)


    def show(self) -> str:
        """
        Returns a string that represents the non-stocked product.

        Returns:
            str: A string representation of the product.
        """
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}{promo}"


    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the non-stocked product, returning the total price.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is less than or equal to 0.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        # Apply promotion if available
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        return total_price


class LimitedProduct(Product):
    """
    A class to represent a product with a purchase limit in the store.

    Inherits from the Product class, but has a maximum purchase quantity.
    """


    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        """
        Constructs all the necessary attributes for the limited product object.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product.
            maximum (int): The maximum purchase quantity for the product.
        """
        super().__init__(name, price, quantity)
        self._maximum = maximum

    @property
    def maximum(self) -> int:
        """Returns the maximum purchase quantity for the product."""
        return self._maximum


    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the limited product, updating the quantity and returning the total price.

        Args:
            quantity (int): The quantity to buy.

        Returns:
            float: The total price of the purchase.

        Raises:
            ValueError: If the quantity is less than or equal to 0, more than the available quantity, or more than the maximum allowed.
        """
        if quantity > self.maximum:
            raise ValueError(f"Cannot purchase more than {self.maximum} of this item.")
        return super().buy(quantity)


    def show(self) -> str:
        """
        Returns a string that represents the limited product.

        Returns:
            str: A string representation of the product.
        """
        promo = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price}, Limited to {self.maximum} per order, Quantity: {self.quantity}{promo}"
