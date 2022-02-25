from pymongo import MongoClient


# connection to mongo db
class MongoDBConnection:

    """This class implement connection to server with mogo db
        return connection object for work
        Close connection after work with it
    """

    def __init__(self):
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient("mongodb+srv://Andron:07201975@mydb.xw8ow.mongodb.net/myDB?retryWrites=true&w=majority")

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
