# question 2
def grocery():
    while True:  
        try:
            # Budget should be integer or float .
            budget = float(input("Enter your budget : ")) 
            f= budget  
        
        
        except ValueError: 
            print("print number as amount!!") 
            continue
        else: 
            break
    #  d is dictionary to store product , quantity and price

    dict1 ={"name":[], "quantity":[], "priceofproduct":[]} 
    #converting to list 
    li= list(dict1.values()) 
    name = li[0] # value of "name" from dictionary 'dict1' in variable
    quantity = li[1] # value of "quantity" from dictionary 'dict1' in variable
    price = li[2] # value of "price" from dictionary 'dict1' in a variable
  
    # This loop terminates when user select option '2'  
    while True: 
        try: 
            choice = int(input("1.Add an Item \n2.Exit \nEnter your choice : ")) 
        except ValueError: 
            print("\nERROR: Choose only digits either 1 or 2 ") 
            continue
        else: 
        
            if choice == 1 and f>0:  # if user selects option '1' and budget is greater than 0      
                  
                productname = input("Enter product name : ")   
                quant = input("Enter quantity : ") 
            
                pr = float(input("Enter price of the product : ")) # price should be in integer or float   
  
                if pr>f: # if price of product is greater than budget
                    print("\nCan't buy the product(because budget left is "+ str(f)+")")  
                    continue
  
                else: 
                 
                    if productname in name:   # if product name already in list
                    
                        index = name.index(productname)   
                        quantity.remove(quantity[index])  
                        price.remove(price[index])   # remove price from "price" index of the product
  
                   
                        quantity.insert(index, quant)  # insert new value given by user earlier     
   
                        price.insert(index, pr)    
  
                        #remaining amount
                        f = budget-sum(price)    
  
                        print("\namount left", f) 
                    else: 
                    
                        name.append(productname) # append value of in "name", "quantity", "price"   
   
                        quantity.append(quant)    
                        price.append(pr)     
                        f = budget-sum(price)    
  
                        print("\namount left", f) 
   
            elif f<= 0:  
                print("\nBudget is over")  
            else:
            
                break
        

    print("\nAmount left is : Rs.", f)  
    if f in price:  
        print("\nAmount left can buy you a", name[price.index(f)])   
  
    print("\n\n\nGROCERY LIST is :") 
  

    for j in range(len(name)):  
        print(name[j], quantity[i], price[i])







grocery()


