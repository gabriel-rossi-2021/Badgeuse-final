import sys

import pymysql
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import logging
import hashlib

from werkzeug.security import check_password_hash

from APP_Timbrage import obj_mon_application
from APP_Timbrage.database.connect_db_context_manager import MaBaseDeDonnee
from APP_Timbrage.database.database_tools import Toolsbd


@obj_mon_application.route("/", methods=['GET', 'POST'])
@obj_mon_application.route("/login", methods=['GET', 'POST'])
def login():
    objet_connectbd = Toolsbd()
    connect_mabd = objet_connectbd.connect_database()
    curseur_mabd = connect_mabd.cursor()

     # Message de sortie si quelque chose ne va pas ...
    msg = ''
    # Vérifiez si des requêtes POST "nom d'utilisateur" et "mot de passe" existent (formulaire soumis par l'utilisateur)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        # Cherche si il trouve le nom d'utilisateur en BDD
        curseur_mabd.execute('SELECT * FROM t_identification WHERE nom_utilisateur = %s', (username,))
        # Retourne le résultat
        account = curseur_mabd.fetchone()


        if account:
            password_rs = account['mot_de_passe']
            print(password_rs)
            # Check le Hash de la BDD
            if check_password_hash(password_rs, password):
                # Créer les sessions
                session['loggedin'] = True
                session['id'] = account['id_identification']
                session['username'] = account['nom_utilisateur']
                session['FK_role'] = account['fk_role']
                # Redirige sur le panel d'administration
                return redirect(url_for('homepage', order_by='ASC', id_horaire_sel=3))

            else:
                msg = 'Nom d\'utilisateur ou mot de passe incorrect'
        else:
            msg = 'Non d\'utilisateur ou mot de passae incorrect'
    # Afficher le formulaire de connexion avec un message (le cas échéant)
    return render_template('index.html', msg=msg)
@obj_mon_application.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('login'))
    flash("Vous n'êtes pas connecté ! ", "danger")
