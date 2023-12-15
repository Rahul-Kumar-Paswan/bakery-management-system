import pandas as pd
import datetime  

def add_orders():
    while True:
        global cus_name 
        global cake 
        cus_name = input('ENTER CUSTOMER NAME: ')
        cake = list(map(str, input("ENTER WHICH CAKE YOU WANT: ").split()))
        quantity = list(map(int, input("ENTER QUANTITY: ").split()))
        
        for i in range(len(cake)):
            if cake[i] not in bill:
                bill.update({cake[i]: 0})
                order.update({cake[i]: quantity[i]})
                temp = menu[cake[i]] * quantity[i]
                bill[cake[i]] = bill[cake[i]] + temp
            else:
                temp = menu[cake[i]] * quantity[i]
                bill[cake[i]] = temp + bill[cake[i]]
                order[cake[i]] = order[cake[i]] + quantity[i]

        q = int(input("DO YOU WANT ANYTHING ELSE? PRESS 1 ELSE 0: "))
        if q == 1:
            continue
        elif q == 0:
            print('ORDER ADDED SUCCESSFULLY !!!')
            print(order)
            print(bill)
            break
        else:
            print("INVALID INPUT")
            break


def view_orders():
    sum=0
    line='__'
    space=' '
    global current_date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{line*40}")
    print(f"CUSTOMER NAME : {cus_name} {space:7} ORDERID : {space:13} DATE : {current_date}")
    print(f"{line*40}")
    print(f" CAKE {space:5} QUANTITY {space:5} COST_OF_EACH_CAKE {space:5} TOTAL_COST_OF_EACH _CAKE")
    print(f"{line*40}")
    for i in bill:
        sum=sum+bill[i]
        print(f"| {i:15} {order[i]} {' '*15} {menu[i]} {' '*20} {bill[i]} ")

    print(f"{line*40}")
    print(f"{' '*45}TOTAL AMOUNT : {sum}")
    print(f"{line*40}")


def update_orders():

    cake_to_update = input("ENTER THE CAKE YOU WANT TO UPDATE :")

    if cake_to_update in order:
        print(order)
        print('PRESS 1 TO CHANGE QUANTITY , 2 TO REMOVE ITEM , PRESS 3 TO GO BACK TO PREVIOUS OPTIONS')
        update_option = int(input('ENTER OPTION :'))
        if update_option == 1:
            new_quantity = int(input(f"Enter the new quantity for {cake_to_update}: "))
            order[cake_to_update] = new_quantity
            bill[cake_to_update] = new_quantity * menu[cake_to_update]
        elif update_option == 2:
            order.pop(cake_to_update)
            bill.pop(cake_to_update)
        elif update_option == 3:
            return
        else:
            print('INVALID OPTION')

        print(f"{cake_to_update} updated successfully!")
    else:
        print(f"{cake_to_update} not found in the order. Please add it first.")


def cancel_order():
    confirm_cancellation = int(input("ENTER 1 TO CANCEL YOUR ORDER ELSE PRESS 0 :"))
    if confirm_cancellation == 1:
        order.clear()
        bill.clear()
    elif confirm_cancellation == 0:
        return
    else:
        print('INVALID OPTION')



def save_to_excel():
    # Create a DataFrame with the order details
    order_df = pd.DataFrame({
                             'CUSTOMER NAME': [cus_name]*len(order),
                             'CAKE': list(order.keys()),
                             'QUANTITY': list(order.values()),
                             'COST PER CAKE': [menu[cake] for cake in order.keys()],
                             'TOTAL COST': list(bill.values()),
                             'DATE': [current_date]*len(order)})

    # Save the DataFrame to an Excel file
    file_name = input("Enter the Excel file name to save (without extension): ")
    file_path = f"{file_name}.xlsx"
    order_df.to_excel(file_path, index=False)

    print(f"Order details saved to {file_path}")




# menu = {'Classic Chocolate Cake':30,'Vanilla Bean Celebration Cake':40,'Red Velvet Delight':45,'Lemon Blueberry Bliss':35,'Cookies and Cream Dream Cake':35}
menu = {'a':30,'b':40,'c':45,'d':35,'e':35}
bill = {}
order = {}

while True:
    print("MENU : ",menu)
    print('1. ADD ORDERS')
    print('2. VIEW ORDERS')
    print('3. UPDATE ORDERS')
    print('4. CANCEL ORDER')
    print('5. SAVE TO EXCEL')
    print('6. EXIT')
    options = int(input('ENTER YOUR OPTIONS:'))
    if options == 1:
        add_orders()
    elif options == 2:
        view_orders()
    elif options == 3:
        update_orders()
    elif options == 4:
        cancel_order()
    elif options == 5:
        save_to_excel()
    elif options == 6:
        exit()
    else:
        print('ENTER VALID OPTIONS')
