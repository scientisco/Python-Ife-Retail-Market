


#============PYTHON IFE RETAIL MARKET PROJECT BY ADEYINKA ANEES ADEDAYO=======================
#NOTE: Password to login as Admin is within the code  = LINE 398



#ITEMS
items=['Sugar',                   'Bread(sliced)',             'Bread(unsliced)',
       'Egg',                     'Three crown(tin)',          'Peak milk(tin)',
       'Peak milk(sachet)',       'Bournvita(sachet)',         'Milo(tin)',
       'Peak milk(Large Sachet)', 'Milo(Large Satchet)',       'Bournvita(Large Sachet)', 
       'Custard(small sachet)',   'Corn flakes(small sachet)', 'Golden morn(small sachet)',
       'Detergent(small Wawu)',   'Detergent(small Aerial)',   'Detergent(Big Wawu)',
       'Detergent(Big Aerial)',   'Corn flakes(big sachet)',   'Golden morn(Large sachet)',
       'Sprite(small)',           'Pepsi(small)',              'Fanta(small)',
       'Lacasera(small)',         'Sprite(big)',               'Pepsi(big)',
       'Fanta(big)',              'Lacasera(big)',             'Coke(big)'
       ]
#QUANTITY OF ITEMS
AvailableQty = [131, 311, 299,
                545, 201, 230,
                791, 611, 367,
                889, 934, 758,
                383, 647, 121,
                198, 354, 323,
                222, 341, 458,
                134, 674, 757,
                127, 956, 374,
                267, 786, 546
                ]
#PRICE OF ITEMS
Price = [50,  200, 150,
         50,  150, 120,
         50,  50,  500,
         700, 700, 100,
         200, 150, 100,
         120, 115, 200,
         250, 750, 650,
         80,  80,  80,
         80,  150, 150,
         150, 150, 150
         ]
total_Items = len(items)
discount = 0
total_price = 0
Cart = []
Cost = []
Quantity = []
Admin = None
Customer = []
total_gain = []




#An inbuilt function for admin to change the price of any of the items.
def ChangepriceOfItem(goods,new_price):
    if goods in items:
        Price[items.index(goods)] = new_price
        print('='*70)
        print(' '*20,"ITEM'S PRICE CHANGED !!!")
        print('Item: ',goods,' '*10,'New Price:', Price[items.index(goods)])
        print('='*70)
        intro2()
    else:
        print('Item is not available')
        pass

#An inbuilt function for admins to add more items.
def AddItems(goods,Qty,price):
    items.append(goods)

    AvailableQty.append(Qty)
    Price.append(price)
    print('*'*70)
    print(' '*20,'NEW ITEM ADDED !!!')
    print('Item: ',goods,' '*10, 'Qty: ',Qty,' '*10, 'Price:', Price[items.index(goods)])
    print('*'*70)
    intro2()
    
            



#An inbuilt function to compute goods purchased per customer and displays a
#receipt for printing.
#Same Code for:
#(b). Write a test program, that communicates with the buyer,
#taking note of the following:
def PurchaseGoods():
    Cart = []
    Cost = []
    Quantity = []
    VAT = 0
    total_price = 0
    bonus = 0
    print('*'*70)
    print(' '*30,'PURCHASE ITEMS !!!')
    
    print('*'*70)
    CustomerName = str(input("\nWhat's your Name? "))
    Customer.append(CustomerName)
    validNo = False
    validQtyNo = False
    validItems = False
    QtyAvail = False
    valid = False
    while validNo ==False:
        try:
            NoOfItems = int(input('\nHow many type of items do you want to buy? '))
            validNo = True
        except ValueError:
             print('Invalid Number!!!')
    
        
    for i in range(NoOfItems):
        while valid == False:
            while validItems ==False:
                try:
                    goods = str(input('\nWhat item do you want: '))
                    print('Price of', goods,'is: #', Price[items.index(goods)])
                    print('Available Qty of',goods,'is:', AvailableQty[items.index(goods)])
                    validItems = True
                except ValueError:
                    print('Item not available!!!')
                    
                    
            while validQtyNo ==False:
                try:
                    Qty = int(input('How many of the item do you want to buy? '))
                    validQtyNo = True
                except ValueError:
                    print('Invalid Number!!!')

            validItems = False  #To start question: "What item do you want" for next item)
                
            
            if (goods in items)and (goods not in Cart):   
                
                if Qty >0 :

                    if AvailableQty[items.index(goods)] >= Qty:
                        QtyAvail = True
                        priceOfItem = Price[items.index(goods)]*Qty
                        AvailableQty[items.index(goods)] -= Qty
                        print(Qty,'Qty of', goods,'is: #', priceOfItem)
                        Cart.append(goods)
                        Cost.append(priceOfItem)
                        Quantity.append(Qty)
                        print('Available Qty Remaining: ', AvailableQty[items.index(goods)])
                        total_price += priceOfItem
                        valid = True
                    elif AvailableQty[items.index(goods)] == 0:
                        print(goods,'Is out of stock!!!')
                    else:
                        print('\nThe quantity of',goods,'you ordered is not available!!\n')
                        print('Available Qty Remaining: ', AvailableQty[items.index(goods)])
                       
                else:
                    print('Invalid Qty')
            elif (goods in Cart) :
                print('Item already added, Choose another Item!!!')
                validQtyNo = False
                validItems = False
                valid = False
                continue
            else:
                print('Item is not available!!!')
                validQtyNo = False
                validItems = False
                valid = False
                continue
            
            validQtyNo = False   #=====To ask for a valid Qty of the next item
        valid = False   #=======To keep looping till a valid Item is entered

        
    if len(Cart) < 5:
        VAT = total_price*0.2  #20% VAT for items less than 5
    elif len(Cart) > 10:
        VAT = total_price*0.3  #30% VAT for items greater than 10
    if len(Cart) > 10 and min(Cost)>= 100:
        
        bonus = 800            #bonus goods for items greater than 10 and minimum price is #100
    else:
        bonus = 0

    def reciept():  #=======RECIEPT FOR PRINTING============
        print('='*70)
        print('~'*30, 'RECIEPT', '~'*30)
        print('='*70)
        print('Name : ',CustomerName)
        print('S/N', ' '*5, 'Item Purchased', ' '*15, 'QTY', ' '*10, 'Price(#)')
        for j in range(len(Cart)):
            spaces = len(Cart[j])
            if j <9 and Quantity[j]<10:
                print(j+1, ' '*10, Cart[j], ' '*(30 - spaces),Quantity[j],' '*15,'#', Cost[j], sep='')
            elif j <9 and Quantity[j]<100:
                print(j+1, ' '*10, Cart[j], ' '*(30 - spaces),Quantity[j],' '*14,'#', Cost[j], sep='')
            elif j <9 and Quantity[j]>=100:
                print(j+1, ' '*10, Cart[j], ' '*(30 - spaces),Quantity[j],' '*13,'#', Cost[j], sep='')
            elif j <99 and Quantity[j]<100:
                print(j+1, ' '*9, Cart[j], ' '*(30 - spaces),Quantity[j],' '*15,'#', Cost[j], sep='')
            elif j >=100 and Quantity[j]>100:
                print(j+1, ' '*8, Cart[j], ' '*(30 - spaces),Quantity[j],' '*15,'#', Cost[j], sep='')
               


        print('Total:',' '*50,'#',total_price, sep='')
        print('\nVAT : #',VAT, sep='')
        print('Discount: ', discount, '%', sep='')
        print('Bonus Goods: #', bonus, sep='')
        payment = total_price + VAT
        print('Total payment is: #',  payment, sep='')
        total_gain.append(payment)
        print('\nThanks for shopping with us, See you next time')
        print('='*70)
        intro2()

#=========================Confirm Purchase of goods===============================================
    actions = False
    print(' '*25, 'YOU GOODS ARE :\n')
    print('S/N',' '*5, 'Item', ' '*30, ' Quantity',' '*8,' Price(#)')
    print('='*75)
    for i in range(len(Cart)):
        if i <9 and Quantity[i]< 10:
            print(i+1,' '*5, Cart[i], ' '*(30-len(Cart[i])), ' '*10, Quantity[i],' '*12,"#", Cost[i])
        elif i <9 and Quantity[i]< 100:
            print(i+1,' '*5, Cart[i], ' '*(30-len(Cart[i])), ' '*9, Quantity[i],' '*12,"#", Cost[i])
        elif i <9 and Quantity[i]>= 100:
            print(i+1,' '*5, Cart[i], ' '*(30-len(Cart[i])), ' '*8, Quantity[i],' '*12,"#", Cost[i])
        elif i <99 and Quantity[i]<100:
            print(i+1,' '*5, Cart[i], ' '*(30-len(Cart[i])), ' '*10, Quantity[i],' '*12,"#", Cost[i])
        elif i >=100 and Quantity[i]>= 100:
            print(i+1,' '*5, Cart[i], ' '*(30-len(Cart[i])), ' '*10, Quantity[i],' '*12,"#", Cost[i])
        
    print('Total:',' '*60,'# ',total_price, sep='')
    print('\nVAT : #',VAT, sep='')
    print('Discount: ', discount, '%', sep='')
    print('Bonus Goods: #', bonus, sep='')
    payment = total_price + VAT 
    print('Total payment is: #',  payment, sep='')
    ans = str(input('\nDo You Want To Continue Purchase? :\n1. Yes\n2. No\nEnter: '))
    while actions == False:
        if ans == '1':
            print(' '*22,'Transaction Successful!!!')
            actions = True
            reciept()
        elif ans == '2':
            actions = True
            if actions == True:
                print(' '*22,'Transaction Unsuccessful!!!')
                print('+'*70,'\n')
            else:
                actions = False
            reply = str(input('Do you want to start purchase all over: \n1. Yes \n2. No (Main Menu) \n3.Exit \nEnter: '))
            if reply == '1' or reply == 'Yes':
                PurchaseGoods()

            elif reply == '2' or reply == 'No':
                
                intro()  
            elif reply == '3' or reply == 'Exit':

                exit()
            else:
                actions = False
                print('Invalid action!!')
                
        else:
            actions = False
            print('Invalid action!!!')
            ans = str(input('\nDo You Want To Continue Purchase? :\n1. Yes\n2. No\nEnter: '))

            

#============An inbuilt function that updates stock after an item has been purchased.================
def AvailableItems():
    print('*'*70)
    print(' '*25, 'AVAILABLE ITEMS')
    print('*'*70)
    print('S/N',' '*5, 'Item',' '*15, 'AvailableQty: ', ' '*6, 'Price')
    
    for i in range(len(items)):
        space = len(items[i])
        if i <9 and AvailableQty[i]>100:
            print(i+1,' '*5, items[i], ' '*(30-space), AvailableQty[i], ' '*15,'#', Price[i], sep='')
        elif i <9 and AvailableQty[i]<10:
            print(i+1,' '*4, items[i], ' '*(30-space), AvailableQty[i], ' '*16,'#', Price[i], sep='')
        elif i <99 and AvailableQty[i]<10:
            print(i+1,' '*4, items[i], ' '*(30-space), AvailableQty[i], ' '*17,'#', Price[i], sep='')
        elif i<99 and AvailableQty[i]<100:
            print(i+1,' '*4, items[i], ' '*(30-space), AvailableQty[i], ' '*16,'#', Price[i], sep='')
        elif i<99 and AvailableQty[i]<1000:
            print(i+1,' '*4, items[i], ' '*(30-space), AvailableQty[i], ' '*15,'#', Price[i], sep='')
        elif i<99 and AvailableQty[i]>=1000:
            print(i+1,' '*4, items[i], ' '*(30-space), AvailableQty[i], ' '*14,'#', Price[i], sep='')
        else:
            print(i+1,' '*3, items[i], ' '*(30-space), AvailableQty[i], ' '*15,'#', Price[i], sep='')

    print('*'*70)

#==============An inbuilt function that takes record of total gain per day.========================  
def gain():
    print('~'*70)
    print('-'*25, 'TOTAL GAIN = ', sum(total_gain),'-'*25)
    print('~'*70)



#============AFTER LOGIN IN THIS SHOWS: Prompts user to make an action ============================
def start():
    action = str(input('\nWhat action do you want to perform: '))
    i = 0
    while True:
        
        if action == '1' or action == 'Available Items' :
            AvailableItems()
            intro2()
            action = str(input('\nWhat action do you want to perform: '))
        elif action == '2' or action == 'Purchase Items':
            PurchaseGoods()
            action = str(input('\nWhat action do you want to perform: '))
        elif action == '3' or action == 'Change Price Of Item':
            if Admin == True:
                ValidItemPrice = False
                goods = str(input("Which Item's price do you want to change: "))
                
                while ValidItemPrice==False:
                    try:
                        new_price = int(input('New Price: '))
                        ValidItemPrice=True
                    except ValueError:
                        print('Invalid Number')
                        
                ChangepriceOfItem(goods, new_price)
                action = str(input('\nWhat action do you want to perform: '))
            else:
                print('This action is for only Admins!')
                break
        elif action == '4' or action == 'Add Item':
            if Admin == True:
                ValidItemQty = False
                goods = str(input("Which Item do you want to add to stock? "))
                while ValidItemQty==False:
                    try:
                        Qty = int(input('How many of the item do you want to add? '))
                        ValidItemQty=True
                    except ValueError:
                        print('Invalid Number')
                
                while ValidItemQty==True:
                    try:
                        price = int(input('How much is the item: '))
                        ValidItemQty=False
                    except ValueError:
                        print('Invalid Number')
                
                ValidItemQty=False
                    
                AddItems(goods,Qty,price)
                
                action = str(input('\nWhat action do you want to perform: '))
            else:
                print('This action is for only Admins!')
                break
        elif action == '5' or action == 'Check Gain':
            if Admin == True:
                gain()
                action = str(input('\nWhat action do you want to perform: '))
                
            else:
                print('This action is for only Admins!')
                break
        elif action == '6' or action == 'Exit':
            
            print('Thanks for shopping with us\nThe window will close shortly!!!')
            exit()
        elif action == '7' or action == 'Main Menu':
            intro()
            
        else:
           print('Invalid Action!!!')
           intro2()
           action = str(input('\nWhat action do you want to perform: '))
           
          
#===============MAIN MENU (Login)============================================================
#Test Program that communicates with the buyer
def intro():
    global Admin     #global so that other functions can access it especially purchasGoods()
    print('~'*70)
    print(' '*4, 'Welcome to Python Ife Retail Market Project by Adeyinka Anees')
    print('~'*70)
    print(' 1. Admins enter password("scientisco")\n 2. Non Admins enter "NONE"\n 3. Enter "Exit" to quit')
    pswd = 'scientisco'  #======Password for Admins =======================!!!!!!!!!!!!!!!!!!
    password = str(input('Enter Password : '))
    while password != pswd or 'NONE':
        if password == pswd:
            Admin = True
            print('-'*70)
            print(' '*20,'DISPLAYING AS ADMIN',' '*20)
            print('-'*70)
            intro2()
            start()
        elif password == 'NONE' or password == 'None':
            Admin = False
            print('-'*70)
            print(' '*20,'DISPLAYING AS CUSTOMER',' '*20)
            print('-'*70)
            intro2()
            start() #Test Program that communicates with the buyer
        elif password == 'EXIT' or password == 'Exit':
            quit()
        else:
            print('Wrong Password!!!')
            Admin = False
            password = str(input('Enter Password : '))

#====================INSTRUCTION FOR USER ===============================================
def intro2():
    print('\n1. Available Items')
    print('2. Purchase Items')
    print('3. Change Price Of Item')
    print('4. Add Item')
    print('5. Check Gain')
    print('6. Exit')
    print('7. Main Menu')
    print('+'*70)



#===============Starts Program=========    
intro()




#Thank you python Ife for the wonderful tutorials you gave us.
#This Project made me realize what i could do with Python
#Now i even understand why error handling is useful and I was able to think outside the box well enough
#========================CREDITS=========================================================#
#ALL CODED BY ANEES
#IG: scientisco
#FB: scientisco
#Phone: 08083400714





