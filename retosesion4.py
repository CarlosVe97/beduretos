#Sesión 4: Fundamentos de MongoDB
#RETO 1-2
#Carlos Alejandro Velázquez Valdez
#Email: carlosvelazquezv2@gmail.com
#Data Science Bedu 

#Usando la base de datos sample_mflix, proyecta los datos que se solicitan.
#Fecha, nombre y texto de cada comentario.


client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'date': 1,
    'name': 1,
    'text': 1,
    '_id': 0
}

result = client['sample_mflix']['comments'].find(
  filter=filter,
  projection=project
)

#Título, elenco y año de cada película.

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1,
    'cast': 1,
    'year': 1,
    '_id': 0
}

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project
)

#Nombre y contraseña de cada usuario.
client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'name': 1,
    'password': 1,
    '_id': 0
}

result = client['sample_mflix']['users'].find(
  filter=filter,
  projection=project
)


#Usando la base de datos sample_mflix, agrega proyeccciones, filtros, ordenamientos y límites que permitan contestar las siguientes preguntas.

#¿Qué comentarios ha hecho Greg Powell?

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    'name': 'Greg Powell'
}

result = client['sample_mflix']['comments'].find(
  filter=filter
)

#¿Qué comentarios han hecho Greg Powell o Mercedes Tyler?

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={
    '$or': [
        {
            'name': 'Greg Powell'
        }, {
            'name': 'Mercedes Tyler'
        }
    ]
}

result = client['sample_mflix']['comments'].find(
  filter=filter
)

# ¿Cuál es el máximo número de comentarios en una película?

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'num_mflix_comments': 1, 
    'title': 1, 
    '_id': 0
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=1

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit

# ¿Cuál es título de las cinco películas más comentadas?

client = MongoClient('mongodb+srv://usuarioBedu:testBEDU@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
filter={}
project={
    'title': 1, 
    '_id': 0
}
sort=list({
    'num_mflix_comments': -1
}.items())
limit=5

result = client['sample_mflix']['movies'].find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)
