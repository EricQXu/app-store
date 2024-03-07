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
    return render_template("develop.html")

@app.route("/search")
def search():
    return render_template("search.html")





# appListings

@app.route("/angrybirds")
def angrybirds():
    return render_template("/static/appListings/angrybirds/index.html")

@app.route("/chrome")
def chrome():
    return render_template("/static/appListings/chrome/index.html")

@app.route("/discord")
def discord():
    return render_template("/static/appListings/discord/index.html")

@app.route("/disneyplus")
def disneyplus():
    return render_template("/static/appListings/disneyplus/index.html")

@app.route("/evernote")
def evernote():
    return render_template("/static/appListings/evernote/index.html")

@app.route("/garageband")
def garageband():
    return render_template("/static/appListings/garageband/index.html")

@app.route("/googledocs")
def googledocs():
    return render_template("/static/appListings/googledocs/index.html")

@app.route("/googlesheets")
def googlesheets():
    return render_template("/static/appListings/googlesheets/index.html")

@app.route("/googleslides")
def googleslides():
    return render_template("/static/appListings/googleslides/index.html")

@app.route("/hbomax")
def hbomax():
    return render_template("/static/appListings/hbomax/index.html")

@app.route("/illustrator")
def illustrator():
    return render_template("/static/appListings/illustrator/index.html")

@app.route("/instagram")
def instagram():
    return render_template("/static/appListings/instagram/index.html")

@app.route("/microsoft365")
def microsoft365():
    return render_template("/static/appListings/microsoft365/index.html")

@app.route("/microsoftexcel")
def microsoftexcel():
    return render_template("/static/appListings/microsoftexcel/index.html")

@app.route("/microsoftonenote")
def microsoftonenote():
    return render_template("/static/appListings/microsoftonenote/index.html")

@app.route("/microsoftpowerpoint")
def microsoftpowerpoint():
    return render_template("/static/appListings/microsoftpowerpoint/index.html")

@app.route("/microsofttodo")
def microsofttodo():
    return render_template("/static/appListings/microsofttodo/index.html")

@app.route("/microsoftword")
def microsoftword():
    return render_template("/static/appListings/microsoftword/index.html")

@app.route("/netflix")
def netflix():
    return render_template("/static/appListings/netflix/index.html")

@app.route("/notion")
def notion():
    return render_template("/static/appListings/notion/index.html")

@app.route("/photoshop")
def photoshop():
    return render_template("/static/appListings/photoshop/index.html")

@app.route("/premierepro")
def premierepro():
    return render_template("/static/appListings/premierepro/index.html")

@app.route("/pycharm")
def pycharm():
    return render_template("/static/appListings/pycharm/index.html")

@app.route("/resolve")
def resolve():
    return render_template("/static/appListings/resolve/index.html")

@app.route("/slack")
def slack():
    return render_template("/static/appListings/slack/index.html")

@app.route("/snapchat")
def snapchat():
    return render_template("/static/appListings/snapchat/index.html")

@app.route("/steam")
def steam():
    return render_template("/static/appListings/steam/index.html")

@app.route("/tiktok")
def tiktok():
    return render_template("/static/appListings/tiktok/index.html")

@app.route("/twitter")
def twitter():
    return render_template("/static/appListings/twitter/index.html")

@app.route("/vscode")
def vscode():
    return render_template("/static/appListings/vscode/index.html")






# Installable PWA routing

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
