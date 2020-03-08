# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class Item(Base):
    __tablename__ = 'item'


    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'   : self.description,
           'id'            : self.id,
       }



engine = create_engine('mysql+pymysql://<user>:<password>@<yourDB_hostservername>:3306/<yourDB>')
 

Base.metadata.create_all(engine)





#SQLALCHEMY_DATABASE_URI = ('mysql+pymysql://<user>:<password>@<yourDB_hostservername>:3306/<yourDB>')

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

#SQLALCHEMY_POOL_RECYCLE = 3600

#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
