# CENG113 PROGRAMMING BASICS  
## Homework 4

Write a python program to take a customer's order and create a receipt. When the program is executed, product information and prices will be read from the attached "menu.txt" file, which must be in the same directory as your python source code. Then, each product should be defined as an instance of the “Menu” class you will define, and menu related operations should be performed using this class.

In the product selection, there should be a gradual flow by first selecting the category, then the product name, and finally the product portion. When the order is completed, a receipt containing all products and the total price must be created.

The first line of the “menu.txt” file contains the labels of the product attributes, and the attribute columns are separated by "; ". No changes should be made in the sent .txt file and the product features (category, product name, etc.) should not be hard coded in your code.

Please handle invalid inputs and make your output as clear as possible. Briefly explain the functions and operations you define with comment lines in your source code.

---

### Example Output:

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
--------------------  
Product Categories  

1. Fries  
2. Milkshake  
3. Salads  
4. Sandwiches or Wrap  
5. Sauce  
6. Side  

Please select category: 6  
--------------------  
Products in Side  

1. Chicken & Cheddar Baked Potato  
2. Sour Cream & Chive Baked Potato  

Please select name: 2  
--------------------  
Sour Cream & Chive Baked Potato Portions  

1. Regular  

Please select portion: 1  
--------------------  

1. Add New  
2. Checkout  

Please select an operation: 1  
--------------------  
Product Categories  

1. Fries  
2. Milkshake  
3. Salads  
4. Sandwiches or Wrap  
5. Sauce  
6. Side  

Please select category: 5  
--------------------  
Products in Sauce  

1. Chilli  

Please select name: 1  
--------------------  
Chilli Portions  

1. Large  
2. Small  

Please select portion: 2  
--------------------  

1. Add New  
2. Checkout  

Please select an operation: 2  
----------------------------------------------------------------------  

Patty with Cheese                       3/4 lb              $5.59  
Sour Cream & Chive Baked Potato         Regular             $0.99  
Chilli                                  Small               $0.99  

----------------------------------------------------------------------  
Total:                                                      $7.57
```
