import unittest
from WebshopMain import DatabaseObject

class ConnectionUnittest(unittest.TestCase):
    methods = DatabaseObject()
    connection = methods.connect_DB()

    def test_conn(self):
        connection = DatabaseObject().connect_DB()
        self.assertIsNotNone(connection)
        connection.close()


#class MyTestCase(unittest.TestCase):
   # def test_something(self):
     #   self.assertEqual(True, False)


#if __name__ == '__main__':
   # unittest.main()
