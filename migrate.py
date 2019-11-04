
# ================================== BELOW IS HOW WE MIGRATE DATA & HANDLE ANY CHANGES IN DATABASE ===================================


# ================================== HANDLING ANY CHANGES IN DATABASE ===================================
import peeweedbevolve
from orm_practise import db

if __name__ == '__main__':
    db.evolve(ignore_tables={'base_model'})


# ================================== MIGRATE DATA : RUN BELOW CODE LINE BY LINE IN PYTHON REPL (SHELL. THE PYTHON TERMINAL) ===================================
# # create instance of new Store
# meng_store = Store(name='Meng camera store')

# # save the new camera store into database
# meng_store.save()


# # update two new warehouses, with `store=meng_store` as foreignKey
# wh_one = Warehouse(location="5 Jalan Damansara", store=meng_store)
# wh_one.save()

# wh_two = Warehouse(location="5 Jalan Cempaka", store=meng_store)
# wh_two.save()

# # update a product in wh_two as foreignKey
# prod_one = Product(name="Sony RX100",
#                    description='Sony decent camera', warehouse=wh_two)
# prod_one.save()
