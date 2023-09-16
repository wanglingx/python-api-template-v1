from __main__ import app
from controller.process import Process
from models.models import *
from flask import  render_template,request


@app.route('/<template>')
def route_template(template):
        if not template.endswith('.html'):
            template += '.html'
        # Detect the current page
        segment = get_segment(request)
        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("/" + template, segment=segment)

def get_segment(request):
    try:
        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'
        return segment

    except:
        return None

@app.route("/")
def index():
    name = "สวัสดีอาจารย์และเพื่อนๆทุกๆคน"
    return render_template("index.html", name=name)


# example get value by models
# @app.route("/test", methods=['POST'])
# def test():
#     RegistrySchema.registry_id = request.form.get('registry_id')
#     return render_template("index.html")
