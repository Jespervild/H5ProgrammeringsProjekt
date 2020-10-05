from WebshopMain import DatabaseObject
from Classes import ProductClass
from Classes import OrderDetailsClass

import TextMenuFunctions
import time
import sys


#def Main_menu():
#    print("****MAIN MENU****")
#    #time.sleep(1)
#    print()
#                        #Nedenunder defineres main menuen, selve teksten#
#    choice = input("""
#                      A: View Table
#                      B: Update Table
#                      Q: Quit/Log Out
#
#                      Enter your choice: """)
#        #Nedenunder defineres de forskellige valg i menuen#
#    if choice == "A" or choice =="a":
#        select_product()
#    elif choice == "B" or choice =="b":
#        update.stock()
#    elif choice=="Q" or choice=="q":
#        sys.exit
#    else:
#        print("You must only select either A,B or Q.")
#        print("Please try again")
#        menu()

def menu():
    print("***MAIN MENU***")
    time.sleep(1)

    choice = input(TextMenuFunctions.Main_menu_options())

    if choice == "A" or choice =="a":
        Table = input(TextMenuFunctions.Table_choice_menu())

        if Table == "A" or Table =="a":
            Table_option = input(TextMenuFunctions.Product_choice_menu())

            if Table_option == "A" or Table_option =="a": #Product Insert Menu
                parameters = TextMenuFunctions.Product_parameter_options()
                instance = ProductClass(parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6])
                instance.Product_sql_insert()
                time.sleep(1)
                print("Following has been inserted: ProductCode: {} ProductName: {} ProductLine: {} ProductDescription: {} ProductVendor: {} BuyPrice: {} QuantityInStock: {}".format(parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6]))
                time.sleep(1)
                menu()

            elif Table_option == "B" or Table_option=="b": #Product Update Menu
                parameters = TextMenuFunctions.Product_parameter_options()
                instance = ProductClass(parameters[0],parameters[1],parameters[2],parameters[3],parameters[4],parameters[5],parameters[6])
                instance.Product_sql_update()
                time.sleep(1)
                print("Following has been updated: ProductCode: {} ProductName: {} ProductLine: {} ProductDescription: {} ProductVendor: {} BuyPrice: {} QuantityInStock: {}".format(ProductCode,ProductName,ProductLine,ProductDescription,ProductVendor,BuyPrice,QuantityInStock))
                time.sleep(1)
                menu()

            elif Table_option == "C" or Table_option =="c": #Product Delete Menu
                parameter = TextMenuFunctions.Product_delete_parameter()
                instance = ProductClass(parameter,'ProductName',20,'QuantityInStock',100,'BuyPrice',2000)
                instance.Product_sql_delete()
                time.sleep(1)
                print("Following row has been deleted: {} ".format(parameter))
                time.sleep(1)
                menu()

            elif Table_option == "D" or Table_option =="d": #Product Show rows
                parameter = TextMenuFunctions.Product_select_parameter()
                instance = ProductClass(parameter,'ProductName',20,'QuantityInStock',100,'BuyPrice',2000)
                row = instance.Product_sql_select()
                print (row)

            elif Table_option == "Q" or Table_option =="q":
                menu()
        elif Table == "B" or Table =="b":
            Table_option = input(TextMenuFunctions.OrderDetails_choice_menu())
            if Table_option == "A" or Table_option =="a": # OrderDetails Insert Menu
                parameters = TextMenuFunctions.OrderDetails_parameter_options()
                instance = OrderDetailsClass(parameters[0], parameters[1], parameters[2])
                instance.OrderDetails_sql_insert()
                time.sleep(1)
                print("Following has been inserted: OrderDetails: {} QuantityOrdered: {} PriceEach: {}".format(parameters[0], parameters[1], parameters[2]))
                time.sleep(1)
                menu()

            elif Table_option == "B" or Table_option =="b": #OrderDetails Update Menu
                parameters = TextMenuFunctions.OrderDetails_parameter_options()
                instance = OrderDetailsClass(parameters[0], parameters[1], parameters[2])
                instance.OrderDetails_sql_update()
                time.sleep(1)
                print("Following has been updated: OrderDetails: {} QuantityOrdered: {} PriceEach: {}".format(parameters[0], parameters[1], parameters[2]))
                time.sleep(1)

            elif Table_option == "C" or Table_option =="c": #OrderDetails Delete Menu
                parameters = TextMenuFunctions.OrderDetails_delete_parameter()
                instance = OrderDetailsClass(parameters,2,2)
                instance.OrderDetails_sql_update()
                time.sleep(1)
                print("Following has been updated: OrderDetails: {} QuantityOrdered: {} PriceEach: {}".format(parameters[0], parameters[1], parameters[2]))
                time.sleep(1)



        elif Table == "Q" or Table =="a":
            menu()
    elif choice == "A" or choice =="q":
        sys.exit()
