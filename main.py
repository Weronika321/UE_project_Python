from flask import Flask
from flask_restful import Resource, Api
# from app.PrimalityTestToAPI import PrimalityTestToAPI
# from classes.Links_to_API import Links_to_API
# from classes.Tags_to_API import Tags_to_API
# from classes.Ratings_to_API import Ratings_to_API
# from classes.HelloWorld import HelloWorld
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse


app = Flask(__name__)
api = Api(app)


# api.add_resource(HelloWorld, "/")
# api.add_resource(PrimalityTestToAPI, "/prime/<number>")
# api.add_resource(PrimalityTestToAPI, '/bar', endpoint='bar')

# api.add_resource(Movie_to_API, "/movies")
# api.add_resource(Links_to_API, "/links")
# api.add_resource(Tags_to_API, "/tags")
# api.add_resource(Ratings_to_API, "/ratings")
@app.get("/")
def start():
    return ""

@app.get("/prime/{number}", response_class=HTMLResponse)
def check_number(number):
    # html = html_content(primality_test(number))
    return number #HTMLResponse(content=html, status_code=200)


# @app.get("/picture/{filename}", response_class=FileResponse)
# def invert_image(filename):
#     # img = invert_colors(os.path.abspath(filename))
#     # img.save(app.const.img_name)
#     return os.path.abspath(app.const.img_name)


# @app.get("/auth")
# def read_current_user(username: str = Depends(get_current_username)):
#     # time = datetime.datetime.now().strftime("%H:%M")
#     # html = html_content(f"Godzina logowania: {time}")
#     return HTMLResponse(content=html, status_code=200)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")  # app.run(debug=True)