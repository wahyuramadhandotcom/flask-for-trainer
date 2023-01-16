from flask import Flask, render_template
from datetime import date


app = Flask(__name__)
list_pendaftar = ["orang 1", 'orang 2', 'orang 3', "orang 4"]
@app.route("/")
def welcome():
    return {
        "message" : "Welcome to my Website"
    }
@app.route("/pendaftar")
def pendaftar():
    today = date.today()
    return render_template ("list_pendaftar.html", lp=list_pendaftar, tgl = today)
    

@app.route('/addPeserta/<nama>')
def addPeserta(nama):
    list_pendaftar.append(nama)
    return {
        "message" : f"Pendaftaran berhasil! {list_pendaftar}"
    }
@app.route('/delete/<nama>')
def deletePeserta(nama):
    list_pendaftar.remove(nama)
    return {
        "message" : f"berhasil di hapus! {list_pendaftar}"
    }

@app.route("/home/<nama>")
def home(nama):
    name = nama
    return render_template ("home.html", name=nama)

@app.route("/about")
def about():
    return render_template ("about.html")

if "__main__" == __name__:
    app.run(debug=True, port=2000)