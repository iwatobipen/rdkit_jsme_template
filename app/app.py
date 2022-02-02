from flask import Flask
from flask import request
from flask import url_for
from flask import Blueprint
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form

from rdkit import Chem
from wtforms.validators import DataRequired
from wtforms import StringField

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()

class Smiles( Form ):
    smi = StringField( "- mol to smiles", validators=[ DataRequired() ] )

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method=="POST":
        print(456)
        print(request.form['smiles'])
    return render_template('templates.html')


if __name__=="__main__":
    app.run(debug=True)