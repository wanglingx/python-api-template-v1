from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="template")
import controller.endpoint

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
