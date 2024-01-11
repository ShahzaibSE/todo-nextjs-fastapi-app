from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import DeclarativeMeta

"""
The declarative_base class is a factory function that returns a new base class for declarative class definitions. 
It is used to define a mapping between your Python classes and database tables.
"""

class CustomBase:
    # automatically generate table name.
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() 
    
Base: DeclarativeMeta = declarative_base(cls=CustomBase)

