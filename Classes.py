from WebshopMain import DatabaseObject
#Import af DatabaseObject, som er SQL forbindelse & Queries

class ProductClass(DatabaseObject): #ProductClass med nedarvning af DatabaseObject, som er SQL forbindelse

    def __init__(self, ProductCode, ProductName, ProductLine, ProductDescription, ProductVendor, BuyPrice,
                 QuantityInStock):    # Alle rows i tabellen "Product"
        DatabaseObject.__init__(self)
        self.ProductCode = ProductCode
        self.ProductName = ProductName
        self.ProductLine = ProductLine
        self.ProductDescription = ProductDescription
        self.ProductVendor = ProductVendor
        self.BuyPrice = BuyPrice
        self.QuantityInStock = QuantityInStock

    def product_sql_insert(self): #Insert into Product Query
        sql = "INSERT INTO Product (ProductCode, ProductName, ProductLine, ProductDescription, ProductVendor, BuyPrice, QuantityInStock) Values (" + str(
            self.ProductCode) + ", '" + self.ProductName + "', " + str(
            self.ProductLine) + ", '" + self.ProductDescription + "', " + str(
            self.ProductVendor) + ", '" + self.BuyPrice + "', " + str(self.QuantityInStock) + ")"
        self.sql_query(sql, None)

    def product_sql_update(self): #Update Product Query
        sql = "UPDATE Product SET ProductCode =" + " " + str(
            self.ProductCode) + ", " + "Product Name =" + " '" + self.ProductName + "', " + "Product Line =" + " " + str(
            self.ProductLine) + ", " + "Product Description =" + " '" + self.ProductDescription + "', " + "Product Vendor =" + " " + str(
            self.ProductVendor) + ", " + "Buy Price =" + " '" + self.BuyPrice + "', " + "Quantity In Stock =" + " " + str(
            self.QuantityInStock) + " " + "WHERE ProductCode =" + " " + str(self.ProductCode) + ""
        self.sql_query(sql, None)

    def product_sql_delete(self): #Delete Product Query
        sql = "DELETE FROM Product WHERE ProductCode =" + " " + str(self.ProductCode)
        self.sql_query(sql, None)

    def product_sql_select(self): #Select Product Query
        sql = "SELECT * FROM Product Where ProductCode =" + " " + str(self.ProductCode)
        row = self.sql_query(sql, True)
        return row

    def print_object(self):
        print(self.ProductName)


# product_sql_update()
# product_sql_insert()
# product_sql_delete()

class OrderDetailsClass(DatabaseObject):

    def __init__(self, OrderNumber, QuantityOrdered, PriceEach): #Her defineres rows i tabellen "OrderDetails"
        DatabaseObject.__init__(self)
        self.OrderNumber = OrderNumber
        self.QuantityOrdered = QuantityOrdered
        self.PriceEach = PriceEach

    def orderDetails_sql_insert(self):   #OrderDetails insert into Query
        sql = "INSERT INTO OrderDetails (OrderNumber,QuantityOrdered,PriceEach) Values (" + str(
            self.OrderNumber) + ", '" + str(self.QuantityOrdered) + "', " + str(self.PriceEach) + ")"
        self.sql_query(sql, None)

    def orderDetails_sql_update(self):   #OrderDetails update Query
        sql = "UPDATE OrderDetails SET OrderDetails =" + " " + str(
            self.OrderNumber) + ", " + "QuantityOrdered =" + " " + str(
            self.QuantityOrdered) + ", " + "PriceEach =" + " " + str(
            self.PriceEach) + "WHERE OrderDetails =" + " " + str(self.OrderNumber)
        self.sql_query(sql, None)

    def orderDetails_sql_delete(self):   #OrderDetails delete Query
        sql = "DELETE FROM OrderDetails WHERE OrderDetails =" + " " + str(self.OrderNumber)
        self.sql_query(sql, None)

# OrderDetails_sql_insert()
# OrderDetails_sql_update()
# OrderDetails_sql_delete()
