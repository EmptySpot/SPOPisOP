from pymongo import MongoClient
import mysql.connector
#Deze versie is uploaden we pas 20 voor 12, maar doordat we de om voor 10 uur geuploade versie willen laten staan hebben we een extra bestand aangemaakt
database = mysql.connector.connect( # Connecten met de database
    host = "localhost",
    user = "root",
    passwd = input('Wat is je wachtwoord?: '),
    database = input('In welke database wil je alle data zetten?: ')
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


def branden(): # Maakt de "Brand" aan
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


def producten(): # Maakt table 'Products' aan
    values = []                # Hieronder ziet het er wat indrukwekkend uit maar we zogen er hier alleen voor dat we alle
    for i in range(0, 100):    # Waarden voor elke kolom in 'values' zetten
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


def categorien(): # Maakt table 'Categorie' aan
    values = []

    for i in range(0, 100):
        if 'sub_category' in products[i]:
            if (products[i]['sub_category'], products[i]['sub_sub_category']) not in values: # Voorkomt dezelfde sub_category - sub_sub_category combinatie
                sub = products[i]['sub_category']
                subsub = products[i]['sub_sub_category']
                values.append((sub, subsub))
    valueses = []

    getal = 0
    for i in values: # Zo kon ik de Primairy key (Categorie) er in zetten
        getal += 1
        value = (getal, ) + i
        valueses.append(value)

    query = """INSERT INTO Categorie (Categorie, Subcategorie, Subsubcategorie) VALUES (%s, %s, %s)"""

    cursor.executemany(query, valueses)

def profielen(): # Maakt de tabel 'profiles' aan
    values = []

    for i in range(0, 100):
        if '_id' in profiles[i]:
            if (profiles[i]['_id'],) not in values:
                split = str(profiles[i]['_id'])
                values.append((split,))

    query = """INSERT INTO profiles (profiles_id) VALUES (%s)"""

    cursor.executemany(query, values)


def buiden(): # Maakt de tabel 'Buids' aan
    values = []

    for i in range(0, 100): # Er zijn soms meerdere buids voor één profiel, zo delen we ze op
        if 'buids' in profiles[i]:
            id = str(profiles[i]['_id'])
            buid = profiles[i]['buids']
            for j in range(len(buid)):
                values.append((str(buid[j]), id))
    query = """INSERT INTO Buids (buids, profilesProfiles_id) VALUES (%s, %s)"""

    cursor.executemany(query, values)

def sessies(): # Maakt de table 'Sessions' aan
               # Sessies werkt nu niet door te korte range, maar als je alles zou implementeren zou het wel werken
    values = []
    for i in range(0, 100):
        if '_id' in sessions[i] and 'buid' in sessions[i]:
            id = sessions[i]['_id']
            buid = sessions[i]['buid'][0]
            values.append((id, buid))
    query = """INSERT INTO Sessions (Session_id, BuidsBuids) VALUES (%s, %s)"""
    cursor.executemany(query, values)


def Besteld(): # Maakt de tabel 'Order' aan
    values = []
                              # Door de tekort aan range in 'sessies' zal deze functie niet goed werken, maar als je alles zou implementeren zou het werken
    for i in range(0, 100):   # Haalt hier alle producten id's van een sessie eruit
        if 'order' in sessions[i]:
            if (sessions[i]['order'],) not in values:
                x = sessions[i]['order']['products']
                for item in x:
                    z = (item['id'])
                    values.append([sessions[i]['_id'], z])

    query = """INSERT INTO Besteld (SessionsSession_id, ProductProduct_id) VALUES (%s, %s)"""

    cursor.executemany(query, values)


profielen()
buiden()
sessies()
branden()
categorien()
producten()
Besteld()

database.commit()
cursor.close()

if database.is_connected():
    database.close()
