from flask import Flask
from flask_restful import Resource, Api
from classes.Movie_to_API import Movie_to_API
from classes.Links_to_API import Links_to_API
from classes.Tags_to_API import Tags_to_API
from classes.Ratings_to_API import Ratings_to_API
from classes.HelloWorld import HelloWorld
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from app.html_content import html_content
from app.primality_test import primality_test

app = Flask(__name__)
api = Api(app)


api.add_resource(HelloWorld, "/")
api.add_resource(Movie_to_API, "/movies")
api.add_resource(Links_to_API, "/links")
api.add_resource(Tags_to_API, "/tags")
api.add_resource(Ratings_to_API, "/ratings")

@app.get("/prime/{number}")
def check_number(number):
    html = html_content(primality_test(number))
    return number #HTMLResponse(content=html, status_code=200)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)
