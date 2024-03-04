# This is the Python backend for Generative AI (ChatGPT) functions of the project
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # load env vars from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from dotenv import load_dotenv
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/get_response")
def get_response():
    message = request.args.get("message")
    completion = client.chat.completions.create(# You can switch this to `gpt-4` if you have access to that model.
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": message}])
    response = completion.choices[0].message.content
    return response


if __name__ == "__main__":
    app.run(debug=True)
