#Sesión 6: Agregaciones
#RETO 1-3
#Carlos Alejandro Velázquez Valdez
#Email: carlosvelazquezv2@gmail.com
#Data Science Bedu


#Reto 1
    {
        '$match': {
            'property_type': 'House'
        }
    }, {
        '$match': {
            'bedrooms': {
                '$gte': 1
            }
        }
    }, {
        '$addFields': {
            'costo_recamara': {
                '$divide': [
                    '$price', '$bedrooms'
                ]
            }
        }
    }, {
        '$group': {
            '_id': '$address.country', 
            'total_price': {
                '$sum': '$costo_recamara'
            }, 
            'count': {
                '$sum': 1
            }
        }
    }, {
        '$addFields': {
            'costo_por_recamara': {
                '$divide': [
                    '$total_price', '$count'
                ]
            }
        }
    }, {
        '$project': {
            '_id': 1, 
            'costo_por_recamara': 1
        }
    }
])

#Reto 2


client = MongoClient('mongodb+srv://usuarioBedu:***@clusterbedutest.k1w71.mongodb.net/test?authSource=admin&replicaSet=atlas-d8xikc-shard-0&connectTimeoutMS=600000&socketTimeoutMS=6000000&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
result = client['sample_mflix']['comments'].aggregate([
    {
        '$lookup': {
            'from': 'users', 
            'localField': 'email', 
            'foreignField': 'email', 
            'as': 'info_usuario'
        }
    }, {
        '$addFields': {
            'user_object': {
                '$arrayElemAt': [
                    '$info_usuario', 0
                ]
            }
        }
    }, {
        '$addFields': {
            'correo': '$user_object.email'
        }
    }, {
        '$addFields': {
            'password': '$user_object.password'
        }
    }, {
        '$project': {
            '_id': 0, 
            'name': 1, 
            'email': 1, 
            'password': 1
        }
    }
])

#Reto 3
# Se comentó que no es necesario adjuntar evidencia de este reto ya que es simplemente generar el view.
# Se generó en la pantalla de agregaciones, se le da click a SAVE -> CREATE A VIEW Y se le asigna un nombre.
