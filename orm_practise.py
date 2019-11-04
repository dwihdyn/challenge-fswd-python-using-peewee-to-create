# showing how can we implement the .txt schema (https://ondras.zarovi.cz/sql/demo/)
# ================================== CREATING NEW TABLE ===================================
import datetime
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase


# connect psql to this python code
db = PostgresqlExtDatabase('orm_practise_dev')


# db parent, make code tidier

class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime.datetime.now)
    updated_at = pw.DateTimeField(default=datetime.datetime.now)

    # stores the current time when data being created/updated
    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)

    # let python know to put in each class as the new table
    class Meta:
        database = db
        legacy_table_names = False


# store table
class Store(BaseModel):
    name = pw.CharField(unique=True)

    def __repr__(self):
        return f"Store name is {self.name}"


# warehouse table | indexing warehouse to make sure that each store ONLY has one warehouse
class Warehouse(BaseModel):
    # indexed warehouse store, dont need to do index=true, as foreignKey are indexed already by default
    store = pw.ForeignKeyField(Store, backref='warehouses', unique=True)
    location = pw.TextField()


# product table | indexed on product name
class Product(BaseModel):
    name = pw.CharField(index=True)  # indexed product name.
    description = pw.TextField()
    warehouse = pw.ForeignKeyField(Warehouse, backref='products')
    color = pw.CharField(null=True)


# connect db to python & create `orm_practise.db`
db.connect()


# create the tables that we defined in python
db.create_tables([Store, Warehouse, Product])


print(" ")
print('orm_practise.py have successfully imported')
print(" ")
