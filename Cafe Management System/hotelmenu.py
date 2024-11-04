#Defining the menu of restaurant 
menu ={
    "Pizza":200,
    "Pasta":50,
    "Burger":160,
    "Salad":80,
    "Coffee":500,
    "Paratha" : 80,
}

print("Welcome to  Resturant")
for item, price in menu.items():
    print(f"{item}: Rs{price}")

order_total=0
another_order ="Yes"

while another_order.capitalize()=="Yes":
    item_1 = input("Enter the name of item you want to order :").capitalize()
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to your order")
    else:
        print(f"Ordered item {item_1} is not available yet")
    another_order=input("Do you want to add another iteam ? (Yes/No) :").capitalize()

print(f"The total amount of item to pay is {order_total}")



