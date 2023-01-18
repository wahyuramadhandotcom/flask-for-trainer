from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Peserta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    alamat = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    umur = db.Column(db.Integer())

    def __repr__(self) -> str:
        return self.name

@app.route("/pendaftar")
def pendaftar():
    today = date.today()
    list_peserta = Peserta.query.all()
    return render_template ("list_pendaftar.html", lp=list_peserta, tgl = today)

@app.route('/add_peserta') #menampilkan template form
def add_peserta():
    return render_template("daftar_pendaftar.html")

@app.route('/add_peserta/save', methods=['POST']) #save
def save_peserta():
    if request.method=='POST':
        f_nama = request.form.get("nama")
        f_alamat = request.form.get("alamat")
        f_gender = request.form.get("gender")
        f_umur = request.form.get("umur")
        p = Peserta(name=f_nama, alamat=f_alamat, gender=f_gender, umur=f_umur)
        db.session.add(p)
        db.session.commit()
        return redirect('/pendaftar')
@app.route('/pendaftar/<id>/delete')
def delete_peserta(id):
    obj =Peserta.query.filter_by(id=id).first()
    db.session.delete(obj)
    db.session.commit()
    return redirect ('/pendaftar')




if "__main__" == __name__:
    app.run(debug=True, port=2000)