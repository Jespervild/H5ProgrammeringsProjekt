import unittest
from WebshopMain import DatabaseObject

#class MyTestCase(unittest.TestCase):
   # def test_something(self):
     #   self.assertEqual(True, False)


#if __name__ == '__main__':
   # unittest.main()


class ConnectionUnittest(unittest.TestCase):
    methods = database_Methods()
    connection = methods.connect_DB()

    def test_conn(self):
        connection = database_Methods().connect_DB()
        self.assertIsNotNone(connection)
        connection.close()
