def Main_menu_options():
    return("""
                      A: Edit Tables or show rows
                      B: Show whole tables
                      Q: Quit

                      Enter your choice: """)

def Table_choice_menu():
    return("""
                      A: Product
                      B: Order Details
                      Q: Back to main menu

                      Enter your choice: """)

def Product_choice_menu():
    return("""
                      A: Insert
                      B: Update
                      C: Delete
                      D: Show rows
                      Q: Back to main menu

                      Enter your choice: """)

def Product_parameter_options():
        parameters = []
        parameters.append(input("Product Code?"))
        parameters.append(input("Product Name?"))
        parameters.append(input("Product Line?"))
        parameters.append(input("Product Description?"))
        parameters.append(input("Product Vendor?"))
        parameters.append(input("Buy Price?"))
        parameters.append(input("Quantity In Stock?"))
        return parameters

def Product_delete_parameter():
    ProductCode = input("Which ProductCode is to be deleted?")
    return ProductCode

def Product_select_parameter():
    ProductCode = input("Which ProductCode row would you like to view?")
    return ProductCode

def OrderDetails_choice_menu():
    return("""
                      A: Insert
                      B: Update
                      C: Delete
                      D: Show rows
                      Q: Back to main menu

                      Please enter your choice: """)

def OrderDetails_parameter_options():
        parameters = []
        parameters.append(input("Which Order Details?"))
        parameters.append(input("Quantity Ordered?"))
        parameters.append(input("Price Each?"))
        return parameters

def OrderDetails_delete_parameter():
    OrderDetails = input("Which Order Detail is to be deleted?")
    return OrderDetails
