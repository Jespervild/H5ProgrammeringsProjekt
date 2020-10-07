

import pyodbc #Forbindelsen til SQL-databasen
from tabulate import tabulate
#Import af funktioner


class DatabaseObject:
    def __init__(self):
        self.cursor = self.conn.cursor()
        self.conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=THINOTE20-JPK;'
                      'Database=WebshopDB;'
                      'Trusted_Connection=yes;')
    def show_table(self, table):
            self.cursor.execute("SELECT * FROM " + table)
            tabledescriptions = []
            tablerows = []
            for row in self.cursor:
                tablerows.append(row)
            for column in self.cursor.description:
                tabledescriptions.append(column[0])
        print(tabulate(tablerows, headers=tabledescriptions))

    def sql_query(self, query, control):
        if control == None:
            self.cursor.execute(query)
            self.conn.commit()
        else:
            self.cursor.execute(query)
            data = self.cursor.fetchone()
            return data

    def print_object(self):
        print(self.conn.getinfo())

   # def select_product(self):
   #     self.cursor.execute('SELECT * FROM WebshopDB.dbo.Product')
   #     for row in self.cursor:
   #         print(row)

   # def select_profiles(self):
   #     self.cursor.execute('SELECT * FROM WebshopDB.dbo.Profiles')
   #     for row in self.cursor:
   #         print(row)

   # def select_orders(self):
   #     self.cursor.execute('SELECT * FROM WebshopDB.dbo.Orders')
   #     for row in self.cursor:
   #         print(row)

   # def select_orderdetails(self):
   #     self.cursor.execute('SELECT * FROM WebshopDB.dbo.OrderDetails')
   #     for row in self.cursor:
   #         print(row)

    #def InsertInto(self):
        #self.cursor.execute('''
                #INSERT INTO WebshopDB.dbo.Profile (ProfileID, FirstName, LastName)
                #VALUES
                #('''),
                #('''),
                #(''')
        #self.conn.commit()

   # def update_profiles(self):
   #     self.cursor.execute('''
   #             UPDATE WebshopDB.dbo.Profiles
   #             SET ProfilePassword = 13371337,City = 'Aalborg Øst'
   #             WHERE ProfileID = '2'
   #             ''')
   #     self.conn.commit()

   # def update_product(self):
   #     ProductName = input("ProductName")
   #     self.cursor.execute('''
   #             UPDATE WebshopDB.dbo.Product
   #             SET ProductName = '{}'
   #             WHERE ProductCode = '2'
   #             '''.format(ProductName))
   #     self.conn.commit()

   # def update_stock(self):
   #     Stock = input("Stock")
   #     self.cursor.execute('''
   #             UPDATE WebshopDB.dbo.Stock
   #             SET QuantityInStock = '{}'
   #             WHERE ProductCode = '2'
   #             '''.format(Stock))
   #     self.conn.commit()


#db=DatabaseObject()
#db.update()
#db.select_product()
#db.select_profiles()
#db.select_orders()
#db.select_orderdetails()
#db.update_stock()
#db.update_product()

