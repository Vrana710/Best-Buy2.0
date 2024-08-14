from products import Product


class Store:
    """
    A class to represent a store containing products.

    Attributes:
        product_list (list): A list of Product objects available in the store.
    """

    def __init__(self, product_list: list):
        """
        Constructs all the necessary attributes for the store object.

        Args:
            product_list (list): A list of Product objects available in the store.
        """
        self.product_list = product_list

    def add_product(self, product: Product):
        """
        Adds a product to the store's inventory.

        Args:
            product (Product): The product to add.
        """
        self.product_list.append(product)

    def remove_product(self, product: Product):
        """
        Removes a product from the store's inventory.

        Args:
            product (Product): The product to remove.
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all active products in the store.

        Returns:
            int: Total quantity of active products.
        """
        return sum(product.quantity for product in self.product_list if product.is_active())

    def get_all_products(self) -> list:
        """
        Returns a list of all active products in the store.

        Returns:
            list: A list of active Product objects.
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes an order and returns the total price.

        Args:
            shopping_list (list): A list of tuples containing products and quantities to purchase.

        Returns:
            float: Total price of the order.
        """
        total_price = 0
        for product, quantity in shopping_list:
            try:
                total_price += product.buy(quantity)
            except ValueError as e:
                print(f"Could not process order for {product.name}: {e}")
        return total_price
