#!/usr/bin/python
from flask import Flask, request, jsonify
from flask_sse import sse
from datetime import datetime
import string
app = Flask(__name__)

port=31337
templatefilename = "template.html"

rundate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
values = {
        'date': rundate
}

with open(templatefilename) as data_file:
        template = data_file.read()
db_template = string.Template(template)

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route("/")
def hello():
    dashboard_html = db_template.substitute(values)
    return dashboard_html

@app.route("/send", methods=["GET"])
def send_message():
  div_id =  request.args.get("id")
  div_html = request.args.get("html")
  print div_id, div_html
  sse.publish({"div_id": div_id, "div_html": div_html}, type='dbuiupdate')
  return "Message sent!"

if __name__ == '__main__':
#app.run(host='0.0.0.0',port=port,debug=True)
  app.run(host='0.0.0.0',port=port,threaded=True)
  print "App running..."
