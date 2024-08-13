# Best Buy 2.0 Tech Store

## Overview
This project is a simulation of a store inventory system called **Best Buy 2.0**. The system allows users to interact with a store, manage inventory, apply promotions, and process orders.


## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Vrana710/best-buy2.0.git 
   cd best-buy2.0
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```


## Usage

To run the store simulation, execute the following command:

```bash
python3 main.py
```

Follow the on-screen menu to interact with the store:

1. **List all products in the store**: Displays a list of all active products with their details.
2. **Show total amount in store**: Shows the total quantity of items available in the store.
3. **Make an order**: Allows you to select products and specify quantities to order.
4. **Quit**: Exits the program.

## Project Structure

The codebase is organized into several modules:

- **main.py**: The entry point of the application. Sets up the store inventory and starts the interactive menu.

- **products.py**: Defines the `Product`, `NonStockedProduct`, and `LimitedProduct` classes, which represent different types of products available in the store.

- **store.py**: Contains the `Store` class, which manages the list of products and handles operations like adding/removing products, calculating total quantities, and processing orders.

- **promotions.py**: Defines the `Promotion` base class and specific promotion types like `SecondHalfPrice`, `ThirdOneFree`, and `PercentDiscount`.

- **tests**: Contains unit tests for the project.

  - **test_product.py**: Tests for product-related functionalities.
  - **test_store.py**: Tests for store-related functionalities.

## Tests

To run the tests, use the following command:

```bash
python3 -m pytest test_product.py
python3 -m pytest test_store.py
```

This command will execute the unit tests in the `tests` directory and display the results.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to contact me at [ranavarsha710@gmail.com](mailto:ranavarsha710@gmail.com).
