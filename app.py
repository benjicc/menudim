from flask import Flask
from flask import render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('men.html')

@app.route('/cr')
def cr():
    return render_template('ibm.html')

@app.route('/cp4d')
def cp4d():
    return redirect("https://ui.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/cp4d")

@app.route('/backup')
def backup():
    return redirect("https://pxbackup.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/")

@app.route('/iks')
def iks():
    return redirect("https://iks-ocp.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/iks")

@app.route('/ocp')
def ocp():
    return redirect("https://iks-ocp.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/ocp")

@app.route('/ml')
def ml():
    return redirect("https://ui-monitoring.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/VATLA?")

@app.route('/ms')
def ms():
    return redirect("https://ui-monitoring.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/VLG?")

@app.route('/cga')
def cga():
    return redirect("https://ui-ga.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/uiga")

@app.route('/core')
def core():
    return redirect("https://ui-cr.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
