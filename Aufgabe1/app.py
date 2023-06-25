from flask import Flask, render_template, request, flash
from DataHandler import DataHandler

app = Flask(__name__)
app.secret_key = '93fa92ddbc680464e4d294cb9b0a1ba5'
dataHandler = DataHandler()


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route("/WebAPP", methods=["POST", "GET"])
def webapp():
    if(request.method == "POST"):
        ip=request.form["ip"]
        ipLookup = dataHandler.getCoordinates(ip)
        if (len(ipLookup) == 1):
           flash("No matching IP was found")
        else:
            latitude, longitude = ipLookup
            flash("latitude: "+latitude+" | longitude: "+longitude)
    return render_template("webapp.html")

@app.route("/API", methods=["POST", "GET"])
def api():
    try:
        argument = request.args.get('ip')
    except:
        return {"error":"No Parameter 'ip' was found"}
    ipLookup = dataHandler.getCoordinates(argument)

    result={}
    try:
        ip, latitude, longitude = ipLookup
    except ValueError:
        latitude =""
        longitude =""
    result["data"]={}
    result["data"]["ip"] = ip
    result["data"]["latitude"] = latitude
    result["data"]["longitude"] = longitude
    return result

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
