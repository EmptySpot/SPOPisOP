from pymongo import MongoClient
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Onjuist1!"
)

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Onjuist1!",
    database = "SPopdracht"
)

client = MongoClient('mongodb://localhost:27017/')
db = client.huwebshop
col = db.products
ses = db.sessions
pro = db.profiles

products = col.find({})
sessions = ses.find({})
profiles = pro.find({})
cursor = database.cursor()


def branden():
    values = []
    for i in range(0, 100):
        if 'brand' in products[i]:
            if products[i]['brand'] not in values:
                values.append(products[i]['brand'])
    values.remove(None)
    for i in values:
        h = (i,)
        query = """INSERT INTO Brands (brand_name) VALUES (%s)"""

        cursor.execute(query, h)


def producten():
    values = []
    for i in range(0, 100):
        if '_id' in products[i]:
            if (products[i]['_id'],) not in values:
                id = products[i]['_id']
        if 'name' in products[i]:
            if (products[i]['name']) not in values:
                name = products[i]['name']
        if 'gender' in products[i]:
            gender = products[i]['gender']
        else:
            gender = 'unisex'
        if 'selling_price' in products[i]['price']:
            selling_price = products[i]['price']['selling_price']
        if 'brand' in products[i]:
            brand = products[i]['brand']
        else:
            brand = 'geen merk'
        if 'category' in products[i]:
            category = products[i]['category']
        else:
            category = 'geen category'
        values.append([id, name, gender, selling_price, brand, category])
    print(values)

    query = """INSERT INTO products (Product_id, Product_name, Gender, Prijs, BrandsBrands, CategorieCategorie) VALUES (%s, %s, %s, %s, %s, %s)"""

    cursor.executemany(query, values)


def categorien():
    values = []
    getal = 0

    for i in range(0, 100):
        if 'sub_category' in products[i]:
            if (products[i]['sub_category'], products[i]['sub_sub_category']) not in values:
                catego = str(getal)
                sub = products[i]['sub_category']
                subsub = products[i]['sub_sub_category']
                values.append((sub, subsub))
    valueses = []

    for i in values:
        getal += 1
        value = (getal, ) + i
        valueses.append(value)

    query = """INSERT INTO Categorie (Categorie, Subcategorie, Subsubcategorie) VALUES (%s, %s, %s)"""

    cursor.executemany(query, valueses)

def profielen():
    values = []

    for i in range(0, 100):
        if '_id' in profiles[i]:
            if (profiles[i]['_id'],) not in values:
                split = str(profiles[i]['_id'])
                values.append((split,))

    query = """INSERT INTO profiles (profiles_id) VALUES (%s)"""

    cursor.executemany(query, values)


def buiden():
    values = []

    for i in range(0, 100):
        id = str(profiles[i]['_id'])
        buid = profiles[i]['buids']
        for j in range(len(buid)):
            values.append((str(buid[j]), id))
    print(values)
    query = """INSERT INTO Buids (buids, profilesProfiles_id) VALUES (%s, %s)"""

    cursor.executemany(query, values)

def sessies():
    values = []
    for i in range(0, 100):
        if '_id' in sessions[i] and 'buid' in sessions[i]:
            id = sessions[i]['_id']
            print(id)
            buid = sessions[i]['buid'][0]
            print(buid)
            values.append((id, buid))
    print(values)
    query = """INSERT INTO Sessions (Session_id, BuidsBuids) VALUES (%s, %s)"""
    cursor.executemany(query, values)


def orders():
    values = []

    for i in range(0, 100):
        if 'brand' in products[i]:
            if (products[i]['brand'],) not in values:
                values.append((products[i]['brand'],))

    query = """INSERT INTO Brands (brand_name)
                                VALUES 
                                (%s)"""

    cursor.executemany(query, values)

profielen()
buiden()
sessions()
branden()
categorien()
producten()

database.commit()
cursor.close()

if database.is_connected():
    database.close()

print(cursor.rowcount, "records inserted")
print('Klaar')