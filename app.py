from flask import Flask

app = Flask(__name__)
list_pendaftar = []
@app.route("/")
def welcome():
    return {
        "message" : "Welcome to my Website"
    }
@app.route("/pendaftar")
def pendaftar():
    return {
        "Pendaftar" : list_pendaftar
    }

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

if "__main__" == __name__:
    app.run(debug=True, port=2000)