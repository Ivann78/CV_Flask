from flask import Flask, render_template, request, redirect, jsonify, json
from urllib.request import urlopen
import sqlite3
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

app = Flask(__name__) #creating flask app name

@app.errorhandler(404) 
def not_found(e): 
  return render_template("404.html") 

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")


@app.route('/lecture')
def lecture():
    return render_template("lecture.html")

@app.route('/authentification')
def authentification():
    return render_template("authentification.html")

@app.route('/fiche_client/<int:client_id>')
def fiche_client():
    return render_template("fiche_client.html")

# Création d'une nouvelle route pour la lecture de la BDD
@app.route("/consultation")
def ReadBDD():
    conn = sqlite3.connect('/home/ivann/www/flask/database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/enregistrer_client')
def enregistrer_client():
    return render_template("enregistrer_client.html")

@app.route('/post/<int:post_id>')
def get_post(post_id):
    conn = sqlite3.connect('/home/ivann/www/flask/database.db')
    post = conn.execute('SELECT * FROM livres WHERE id = ?', (post_id,)).fetchone()
    conn.close()

    # Si la publication avec l'ID spécifié n'est pas trouvée, renvoie une réponse 404 Not Found
    if post is None:
        return jsonify(error='Post not found'), 404

    # Convertit la publication en un format JSON
    json_post = {'id': post['id'], 'title': post['title'], 'auteur': post['auteur']}
    
    # Renvoie la réponse JSON
    return jsonify(post=json_post)

if(__name__ == "__main__"):
    app.run()
