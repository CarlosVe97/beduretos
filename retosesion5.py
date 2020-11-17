#Sesión 5: Consultas en Mongo DB
#RETO 1-3
#Carlos Alejandro Velázquez Valdez
#Email: carlosvelazquezv2@gmail.com
#Data Science Bedu

#1
#Usando la base de datos sample_airbnblistingsAndReviews, realiza los siguientes filtros:

#Propiedades que no permitan fiestas.
client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"(no fiestas|no parties)(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Propiedades que admitan mascotas.
#NOTA: encontré que en amenities tambien especifican si se puede o no tener mascotas y busqué en ambas

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    '$or': [
        {
            'amenities': re.compile(r"pets allowed(?i)")
        }, {
            'house_rules': re.compile(r"pets allowed")
        }
    ]
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

# Propiedades que no permitan fumadores.
client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"(No smoking|no smokers)(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Propiedades que no permitan fiestas ni fumadores.
client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'house_rules': re.compile(r"(No smoking.*no parties|no parties.*no smoking)(?i)")
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#Usando la colección sample_airbnb.listingsAndReviews, agrega un filtro que permita obtener todas las publicaciones que tengan 50 o más comentarios, que la valoración sea mayor o igual a 80, que cuenten con conexión a Internet vía cable y estén ubicada en Brazil
client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    '$and': [
        {
            'address.country_code': 'BR'
        }, {
            'amenities': re.compile(r"ethernet(?i)")
        }, {
            'number_of_reviews': {
                '$gte': 50
            }
        }, {
            'review_scores.review_scores_rating': {
                '$gte': 80
            }
        }
    ]
}

result = client['sample_airbnb']['listingsAndReviews'].find(
  filter=filter
)

#3
#Usando la colección sample_airbnb.listingsAndReviews, mediante el uso de agregaciones, encontrar el número de publicaciones que tienen conexión a Internet, sea desde Wifi o desde cable (Ethernet).


client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_airbnb']['listingsAndReviews'].aggregate([
    {
        '$match': {
            'amenities': {
                '$in': [
                    'Internet', 'Ethernet'
                ]
            }
        }
    }, {
        '$count': 'total_publicaciones_internet'
    }
])
