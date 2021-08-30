"""
    Fichier : gestion_genres_crud.py
    Auteur : OM 2021.03.16
    Gestions des "routes" FLASK et des données pour les genres.
"""
import sys

import pymysql
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from APP_Timbrage import obj_mon_application
from APP_Timbrage.database.connect_db_context_manager import MaBaseDeDonnee
from APP_Timbrage.erreurs.exceptions import *
from APP_Timbrage.erreurs.msg_erreurs import *
from APP_Timbrage.utils.utils import si_user_login

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher
    
    Test : ex : http://127.0.0.1:5005/genres_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_identification_sel = 0 >> tous les genres.
                id_identification_sel = "n" affiche le genre dont l'id est "n"
"""

@obj_mon_application.route("/homepage/<string:order_by>/<int:id_horaire_sel>", methods=['GET', 'POST'])
@si_user_login
def homepage(order_by, id_horaire_sel):
    if request.method == "GET":
        try:
            try:
                # Renvoie une erreur si la connexion est perdue.
                MaBaseDeDonnee().connexion_bd.ping(False)
            except Exception as erreur:
                flash(f"Dans Gestion genres ...terrible erreur, il faut connecter une base de donnée", "danger")
                print(f"Exception grave Classe constructeur GestionGenres {erreur.args[0]}")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            with MaBaseDeDonnee().connexion_bd.cursor() as mc_afficher:
                if order_by == "ASC" and id_horaire_sel == 0:
                    strsql_horaire_afficher = """SELECT id_horaires, date_et_heure_horaires FROM t_horaires ORDER BY id_horaires ASC"""
                    mc_afficher.execute(strsql_horaire_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_horaire_selected_dictionnaire = {"value_id_horaire_selected": id_horaire_sel}
                    strsql_horaire_afficher = """SELECT id_horaires, date_et_heure_horaires FROM t_horaires WHERE id_horaires= %(value_id_horaire_selected)s"""

                    mc_afficher.execute(strsql_horaire_afficher, valeur_id_horaire_selected_dictionnaire)
                else:
                    strsql_horaire_afficher = """SELECT id_horaires, date_et_heure_horaires FROM t_horaires ORDER BY id_horaires DESC"""

                    mc_afficher.execute(strsql_horaire_afficher)

                data_horaire = mc_afficher.fetchall()

                print("data_horaire ", data_horaire, " Type : ", type(data_horaire))

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # Envoie la page "HTML" au serveur.
    return render_template("home.html", data=data_horaire)
