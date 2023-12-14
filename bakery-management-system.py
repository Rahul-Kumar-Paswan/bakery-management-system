def add_orders():
    while True :
        cake = list(map(str,input("ENTER WHICH CAKE YOU WANT :").split()))
        quantity = list(map(int,input("ENTER QUANTITY :").split()))
        for i in range(len(cake)):
            if cake[i] not in bill :
                bill.update({cake[i]:0})
                order.update({cake[i]:quantity[i]})
                temp = menu[cake[i]]*quantity[i]
                bill[cake[i]] = bill[cake[i]] + temp 
            else :
                temp = menu[cake[i]] * quantity[i]
                bill[cake[i]] = temp + bill[cake[i]]
                order[cake[i]] = order[cake[i]] + quantity[i]

        q = int(input("DO YOU WNAT ANYTHING PRESS 1 ELSE 0 :"))
        if q == 1:
            continue
        elif q == 0 :
            break
        else:
            print("INVALID INPUT")
            break

def view_orders():
    sum=0
    line='__'
    space=' '
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
    pass

def save_to_excel():
    pass


# menu = {'Classic Chocolate Cake':30,'Vanilla Bean Celebration Cake':40,'Red Velvet Delight':45,'Lemon Blueberry Bliss':35,'Cookies and Cream Dream Cake':35}
menu = {'a':30,'b':40,'c':45,'d':35,'e':35}
bill = {}
order = {}

print("MENU : ",menu)
print('1. ADD ORDERS')
print('2. VIEW ORDERS')
print('3. UPDATE ORDERS')
print('4. SAVE TO EXCEL')
print('5. EXIT')

while True:
    options = int(input('ENTER YOUR OPTIONS:'))
    if options == 1:
        add_orders()
    elif options == 2:
        view_orders()
    elif options == 3:
        update_orders()
    elif options == 4:
        save_to_excel()
    elif options == 5:
        exit()
    else:
        print('ENTER VALID OPTIONS')
