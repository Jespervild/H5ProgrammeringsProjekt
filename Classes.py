from DatabaseObject import DatabaseObject

class ProductClass(DatabaseObject):

    def __init__(self, ProductCode, ProductName, ProductLine, ProductDescription, ProductVendor, BuyPrice, QuantityInStock):
        database_Methods.__init__(self)
        self.ProductCode = ProductCode
        self.ProductName = ProductName
        self.ProductLine = ProductLine
        self.ProductDescription = ProductDescription
        self.ProductVendor = ProductVendor
        self.BuyPrice = BuyPrice
        self.QuantityInStock = QuantityInStock

    def Product_sql_insert(self):
        sql = "INSERT INTO Product (ProductCode, ProductName, ProductLine, ProductDescription, ProductVendor, BuyPrice, QuantityInStock) Values (" + str(self.ProductCode) + ", '" + self.ProductName + "', " + str(self.ProductLine) + ", '" + self.ProductDescription + "', " + str(self.ProductVendor) + ", '" + self.BuyPrice + "', " + str(self.QuantityInStock) + ")"
        self.sql_query(sql, None)

    def Product_sql_update(self):
        sql = "UPDATE Product SET ProductCode =" + " " + str(self.ProductCode) + ", " + "Product Name =" + " '" + self.ProductName + "', " + "Product Line =" + " " + str(self.ProductLine) + ", " + "Product Description =" + " '" + self.ProductDescription + "', " + "Product Vendor =" + " " + str(self.ProductVendor) + ", " + "Buy Price =" + " '" + self.BuyPrice + "', " + "Quantity In Stock =" + " " + str(self.QuantityInStock) + " " + "WHERE ProductCode =" +" "+ str(self.ProductCode)+""
        self.sql_query(sql, None)

    def Product_sql_delete(self):
        sql = "DELETE FROM Product WHERE ProductCode =" + " " + str(self.ProductCode)
        self.sql_query(sql, None)

    def Product_sql_select(self):
        sql = "SELECT * FROM Product Where ProductCode =" + " " + str(self.ProductCode)
        row = self.sql_query(sql, True)
        return row

    def print_object(self):
        print(self.ProductName)


#Product_sql_update()
#Product_sql_insert()
#Product_sql_delete()

class OrderDetailsClass(DatabaseObject):

    def __init__(self, LocationID, QuantityOrdered, PriceEach):
        database_Methods.__init__(self)
        self.OrderDetails = OrderDetails
        self.QuantityOrdered = QuantityOrdered
        self.PriceEach = PriceEach

    def OrderDetails_sql_insert(self):
        sql = "INSERT INTO OrderDetails (OrderDetails,QuantityOrdered,PriceEach) Values (" + str(self.OrderDetails) + ", '" + str(self.QuantityOrdered) + "', " + str(self.PriceEach) + ")"
        self.sql_query(sql, None)

    def OrderDetails_sql_update(self):
        sql = "UPDATE OrderDetails SET OrderDetails =" + " " + str(self.OrderDetails) + ", " + "QuantityOrdered =" + " " + str(self.QuantityOrdered) + ", " + "PriceEach =" + " " + str(self.PriceEach) + "WHERE OrderDetails =" + " " + str(self.OrderDetails)
        self.sql_query(sql, None)

    def OrderDetails_sql_delete(self):
        sql = "DELETE FROM OrderDetails WHERE OrderDetails =" + " " + str(self.OrderDetails)
        self.sql_query(sql, None)

#OrderDetails_sql_insert()
#OrderDetails_sql_update()
#OrderDetails_sql_delete()


