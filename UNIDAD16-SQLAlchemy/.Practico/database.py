import sqlalchemy as db
from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Database():
    '''Database is the class with everything related to connecting to the DB and running DDL/DML transactions.
    '''

    engine = db.create_engine('postgresql://user_test:test_password@localhost/test')
    Session = sessionmaker(bind=engine)
    session = Session()

    def __init__(self):
        self.connection = self.engine.connect()
        print("DB instance created")

    def fetchByQuery(self, query):
        '''fetchByQuery runs a select for the query argument.

        Args:
            query (string): the query itself that will be ran. e.g. "table WHERE column < 2"
        '''

        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        
        for data in fetchQuery.fetchall():
            print(data)

    def fetchUserByName(self):
        '''fetchUserByName fetches all users in table Customer by name.
        '''

        meta = MetaData()
        customer = Table('customer', meta, Column('name'))
        data = self.connection.execute(customer.select())

        for cust in data:
            print(cust)

    def fetchAllUsers(self):
        '''fetchAllUsers fetches all users from table Customer.
        '''
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)
            
    def saveData(self, customer):
        self.session.add(customer)
        self.session.commit()

class Customer(Base):
    '''Customer is the class for returning Customer objects from rows in the Customer table.

    Args:
        Base (class): importing the Base module is necessary in order to map objects in the DB.

    Returns:
        _type_: Customer row from Customer table.
    '''
    __tablename__ = 'customer'
    name = Column(String, primary_key=True)
    age = Column(Integer)
    email = Column(String)
    address = Column(String)
    zip_code = Column(String)


    def __repr__(self):
        return "<Customer (name='%s', age='%s', email='%s', address='%s', zip_code='%s')>" % (self.name, self.age, self.email, self.address, self.zip_code) 

        
Database().fetchAllUsers()