# This is the Python backend for Generative AI (ChatGPT) functions of the project
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # load env vars from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask import send_file

app = Flask(__name__, template_folder='.')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/docs")
def docs():
    return render_template("docs.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/work")
def work():
    return render_template("work.html")

@app.route("/entertainment")
def entertainment():
    return render_template("entertainment.html")

@app.route("/social")
def social():
    return render_template("social.html")

@app.route("/develop")
def develop():
    return render_template("home.html")

@app.route("/search")
def search():
    return render_template("search.html")

# app.route for angrybirds

@app.route("/chrome")
def chrome():
    return render_template("/static/appListings/chrome/index.html")

# app.route for discord, disneyplus, everynote, ...

@app.route("/pycharm")
def pycharm():
    return render_template("/static/appListings/pycharm/index.html")

@app.route("/resolve")
def resolve():
    return render_template("/static/appListings/resolve/index.html")

# app.route for slack, snapchat

@app.route("/steam")
def steam():
    return render_template("/static/appListings/steam/index.html")

# app.route for tiktok, twitter

@app.route("/vscode")
def vscode():
    return render_template("/static/appListings/vscode/index.html")

@app.route('/manifest.json')
def serve_manifest():
    return send_file('manifest.json', mimetype='application/manifest+json')


@app.route('/sw.js')
def serve_sw():
    return send_file('sw.js', mimetype='application/javascript')


@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    completion = client.chat.completions.create(# You can switch this to `gpt-4` if you have access to that model.
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "You know a lot about tech. Do not answer any math questions. Please answer the following question(s) only if it is related to tech: " + message}])
    response = completion.choices[0].message.content
    return response


if __name__ == "__main__":
    app.run(debug=True)
