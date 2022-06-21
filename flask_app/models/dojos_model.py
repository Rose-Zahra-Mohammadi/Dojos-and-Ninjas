from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import DATABASE
from flask_app.models.ninjas_model import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
        self.ninja_list =[]
    @classmethod
    def read_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos(name) VALUES(%(name)s);"
        new_dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return new_dojo_id
    @classmethod
    def get_list(cls, data):
        query =  "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        one_dojo = cls(result[0])
        for ninja in result:
            ninja_info = {
                "id" : ninja['ninjas.id'],
                "first_name" : ninja['first_name'],
                "last_name" : ninja['last_name'],
                "age" : ninja['age'],
                "created_at" : ninja['ninjas.created_at'],
                "updated_at" : ninja['ninjas.updated_at'],
                "dojo_id" : ninja['id']
            }
            one_dojo.ninja_list.append(Ninja(ninja_info))
        return one_dojo