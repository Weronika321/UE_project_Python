from flask import Flask
from flask_restful import Resource, Api
from classes.Movie_to_API import Movie_to_API
from classes.Links_to_API import Links_to_API
from classes.Tags_to_API import Tags_to_API
from classes.Ratings_to_API import Ratings_to_API
from classes.HelloWorld import HelloWorld


app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(Movie_to_API, "/movies")
api.add_resource(Links_to_API, "/links")
api.add_resource(Tags_to_API, "/tags")
api.add_resource(Ratings_to_API, "/ratings")

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)
