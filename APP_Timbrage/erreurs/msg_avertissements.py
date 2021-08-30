"""
    Fichier : msg_avertissements.py
    Auteur : OM 2021.05.02

    Messages d'avertissement. Souvent à caractère informatif.
    Certains peuvent sembler être abrupts.

"""
from flask import render_template
from APP_Timbrage import obj_mon_application


@obj_mon_application.route("/avertissement_sympa_pour_geeks")
def avertissement_sympa_pour_geeks():
    # Envoie la page "HTML" au serveur.
    return render_template("Origines_collaborateurs/avertissement_projet.html")

@obj_mon_application.route("/information_sur_table_crud")
def information_sur_table_crud():
    # Envoie la page "HTML" au serveur.
    return render_template("details/avertissement_projet.html")