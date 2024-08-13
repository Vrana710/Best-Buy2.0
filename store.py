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
        Calculates the total quantity of all products in the store.

        Returns:
            int: The total quantity of all products in the store.
        """
        return sum(product.quantity for product in self.product_list if product.is_active())


    def get_all_products(self) -> list:
        """
        Retrieves a list of all active products in the store.

        Returns:
            list: A list of active Product objects in the store.
        """
        return [product for product in self.product_list if product.is_active()]

    def order(self, shopping_list: list) -> float:
        """
        Processes an order from the shopping list, updating quantities and calculating total cost.

        Args:
            shopping_list (list): A list of tuples, where each tuple contains a Product object and a quantity.

        Returns:
            float: The total cost of the order.

        Raises:
            ValueError: If any product in the order has insufficient quantity.
        """
        total_cost = 0
        for product, quantity in shopping_list:
            total_cost += product.buy(quantity)
        return total_cost
