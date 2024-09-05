# CENG113 Homework 4: Customer Order and Receipt Generator

## Overview

This project is a Python program designed to handle customer orders and generate a receipt based on a predefined menu. The menu information, such as product categories, names, and prices, is dynamically loaded from a `menu.txt` file. No hardcoding of menu items is involved.

## Features

- **Dynamic Menu Loading**: Reads product information from the `menu.txt` file, which includes attributes such as category, product name, portions, and prices.
- **Menu Class**: Implements a `Menu` class to handle product details and related operations.
- **User Input Flow**:
  1. Select a product category.
  2. Choose a product from the category.
  3. Pick a portion size for the selected product.
  4. Option to add more products or checkout.
- **Receipt Generation**: When checkout is selected, a receipt is printed with the product details and total price.
- **Input Validation**: Handles invalid inputs and prompts the user to try again for valid selections.
  
## Example Program Output

```
Product Categories
1. Fries
2. Milkshake
3. Salads
4. Sandwiches or Wrap
5. Sauce
6. Side
Please select product category: 4
--------------------
Products in Sandwiches or Wrap
1. Chicken Wrap
2. Kids Cheeseburger
3. Patty with Beef
4. Patty with Cheese
Please select product name: 4
--------------------
Patty with Cheese Portions
1. 1/2 lb
2. 1/4 lb
3. 3/4 lb
Please select product portion: 3
--------------------
1. Add New
2. Checkout
Please select an operation: 1
```

### Example Receipt

```
---------------------------------------------------------
Patty with Cheese                  3/4 lb          $5.59
Sour Cream & Chive Baked Potato     Regular         $0.99
Chilli                              Small           $0.99
---------------------------------------------------------
Total:                                            $7.57
```
