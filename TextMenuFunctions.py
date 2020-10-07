def main_menu_options():
    return ("""
                      A: Edit Tables or show rows
                      B: Show whole tables
                      Q: Quit

                      Enter your choice: """)


def table_choice_menu():
    return ("""
                      A: Product
                      B: Order Details
                      Q: Back to main menu

                      Enter your choice: """)


def product_choice_menu():
    return ("""
                      A: Insert
                      B: Update
                      C: Delete
                      D: Show rows
                      Q: Back to main menu

                      Enter your choice: """)


def orderDetails_choice_menu():
    return ("""
                      A: Insert
                      B: Update
                      C: Delete
                      D: Show rows
                      Q: Back to main menu

                      Please enter your choice: """)


def product_delete_parameter():
    ProductCode = input("Which ProductCode is to be deleted?")
    return ProductCode


def product_select_parameter():
    ProductCode = input("Which ProductCode row would you like to view?")
    return ProductCode

def orderDetails_delete_parameter():
    OrderDetails = input("Which Order Detail is to be deleted?")
    return OrderDetails


def orderDetails_parameter_options():
    parameters = []
    parameters.append(input("Which Order Details?"))
    parameters.append(input("Quantity Ordered?"))
    parameters.append(input("Price Each?"))
    return parameters


def product_parameter_options():
    parameters = []
    parameters.append(input("Product Code?"))
    parameters.append(input("Product Name?"))
    parameters.append(input("Product Line?"))
    parameters.append(input("Product Description?"))
    parameters.append(input("Product Vendor?"))
    parameters.append(input("Buy Price?"))
    parameters.append(input("Quantity In Stock?"))
    return parameters
