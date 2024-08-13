from products import Product, NonStockedProduct, LimitedProduct
from store import Store
import promotions

def setup_inventory():
    """
    Sets up the initial stock of inventory for the store.

    This function creates a list of Product objects with 
    predefined names, prices, and quantities.
    It then initializes a Store object with this list of products.

    Returns:
        Store: A Store object initialized with the predefined list of products.
    """
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    ]
    return Store(product_list)


def start(store: Store):
    """
    Starts the interactive store menu for the user to interact with the store.

    The function provides a menu with options to list all products, 
    show the total amount of items in the store,
    make an order, or quit the menu. 
    It continuously prompts the user for input until the user chooses to quit.

    Args:
        store (Store): The store object containing 
                        the inventory and methods to interact with it.

    Returns:
        None
    """
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            # List all products
            products = store.get_all_products()
            print("\n------")
            for idx, product in enumerate(products, start=1):
                print(f"{idx}. {product.show()}")
            print("------")

        elif choice == "2":
            # Show total amount in store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")

        elif choice == "3":
            # Make an order
            products = store.get_all_products()
            order_list = []
            while True:
                print("\n------")
                for idx, product in enumerate(products, start=1):
                    print(f"{idx}. {product.show()}")
                print("------")
                
                try:
                    print("When you want to finish order, enter empty text.")
                    product_choice = input("Which product # do you want? ").strip()
                    if product_choice == '':
                        break
                    product_idx = int(product_choice) - 1
                    if product_idx < 0 or product_idx >= len(products):
                        print("Invalid product number.")
                        continue
                    quantity = int(input(f"What amount do you want? ").strip())
                    if quantity <= 0:
                        print("Quantity must be greater than 0.")
                        continue

                    product = products[product_idx]
                    order_list.append((product, quantity))
                    print("Product added to list!")

                except ValueError:
                    print("Error adding product!")
            
            if order_list:
                try:
                    total_cost = store.order(order_list)
                    print(f"********\nOrder made! Total payment: ${total_cost}")
                except Exception as e:
                    print(f"Error processing order: {e}")

        elif choice == "4":
            print("Thank you for visiting Best Buy 2.0. Goodbye!")
            break

        else:
            print("Error with your choice! Try again!")


if __name__ == "__main__":
    best_buy = setup_inventory()

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list = best_buy.get_all_products()
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    start(best_buy)
