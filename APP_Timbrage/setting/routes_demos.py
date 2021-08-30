"""
    Fichier : routes_demos.py
    Auteur : OM 2021.03.16
    Pour faire des tests divers et variés, avec la notion de "routes" avec FLASK
"""

from flask import render_template
from APP_Timbrage import obj_mon_application
from APP_Timbrage.erreurs.msg_erreurs import *
from APP_Timbrage.erreurs.exceptions import *
from flask import url_for