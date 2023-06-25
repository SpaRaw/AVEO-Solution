from flask import Flask, request, render_template, flash
import DataHandler

app = Flask(__name__)
app.secret_key = '93fa92ddbc680464e4d294cb9b0a1ba5'
dh = DataHandler.DataHandler()
@app.route("/")
def main():
    return render_template("index.html")

@app.route("/WebAPP", methods=["POST", "GET"])
def web():
    if request.method == "POST":
        argument = request.form.get("name")
        name, gender, percent = dh.getNameInformation(argument)
        percent = str(float(percent) * 100.0)+" %"
        flash(f"name: {name} | gender: {gender} | {percent}")

    return render_template("webapp.html")

@app.route("/API")
def api():
    argument = request.args.get('name')
    response={}
    name, gender, percent = dh.getNameInformation(argument)
    percent = float(percent) * 100.0
    response["response"]={}
    response["response"]["name"]=name
    response["response"]["gender"]=gender
    response["response"]["percentage"]=str(percent)+" %"
    return response


if __name__ == "__main__":

    app.run(host="localhost", port=8081)
