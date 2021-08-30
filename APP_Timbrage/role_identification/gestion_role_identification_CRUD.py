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
from werkzeug.security import generate_password_hash

from APP_Timbrage import obj_mon_application
from APP_Timbrage.database.connect_db_context_manager import MaBaseDeDonnee
from APP_Timbrage.erreurs.exceptions import *
from APP_Timbrage.erreurs.msg_erreurs import *
from APP_Timbrage.role_identification.gestion_role_identification_wtf_forms import FormWTFAjouterCollaborateur
from APP_Timbrage.role_identification.gestion_role_identification_wtf_forms import FormWTFUpdateIdentification
from APP_Timbrage.role_identification.gestion_role_identification_wtf_forms import FromWTFDeleteIdentification
from APP_Timbrage.utils.utils import si_user_login
from APP_Timbrage.utils.utils import is_admin

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /genres_afficher

    Test : ex : http://127.0.0.1:5005/genres_afficher

    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_identification_sel = 0 >> tous les genres.
                id_identification_sel = "n" affiche le genre dont l'id est "n"
"""


@obj_mon_application.route("/role_identification_afficher/<string:order_by>/<int:id_role_identification_sel>",
                           methods=['GET', 'POST'])
@si_user_login
@is_admin
def role_identification_afficher(order_by, id_role_identification_sel):
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
                if order_by == "ASC" and id_role_identification_sel == 0:
                    strsql_identification_afficher = """SELECT id_identification, nom_utilisateur,mot_de_passe, courriel, fk_role FROM t_identification ORDER BY id_identification ASC"""
                    mc_afficher.execute(strsql_identification_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_identification_selected_dictionnaire = {
                        "value_id_identification_selected": id_role_identification_sel}
                    strsql_identification_afficher = """SELECT id_identification, nom_utilisateur,mot_de_passe, courriel, fk_role FROM t_identification WHERE id_identification= %(value_id_identification_selected)s"""

                    mc_afficher.execute(strsql_identification_afficher, valeur_id_identification_selected_dictionnaire)
                else:
                    strsql_identification_afficher = """SELECT id_identification, nom_utilisateur,mot_de_passe,courriel, fk_role FROM t_identification ORDER BY id_identification DESC"""

                    mc_afficher.execute(strsql_identification_afficher)

                data_identification = mc_afficher.fetchall()

                print("data_identification ", data_identification, " Type : ", type(data_identification))

                # Différencier les messages si la table est vide.
                if not data_identification and id_role_identification_sel == 0:
                    flash("""La table "t_identification" est vide. !!""", "warning")
                elif not data_identification and id_role_identification_sel > 0:
                    # Si l'utilisateur change l'id_collaborateur dans l'URL et que le genre n'existe pas,
                    flash(f"Le collaborateur demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données d'identifiactions affichés !!", "primary")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # Envoie la page "HTML" au serveur.
    return render_template("role_identification/role_identification_afficher.html", data=data_identification)

@obj_mon_application.route("/role_identifiaction_ajouter_wtf", methods=['GET', 'POST'])
@si_user_login
@is_admin
def role_identification_ajouter_wtf():
    form = FormWTFAjouterCollaborateur()
    if request.method == "POST":
        try:
            try:
                # Renvoie une erreur si la connexion est perdue.
                MaBaseDeDonnee().connexion_bd.ping(False)
            except Exception as erreur:
                flash(f"Dans Gestion des identification ...terrible erreur, il faut connecter une base de donnée", "danger")
                print(f"Exception grave Classe constructeur GestionGenres {erreur.args[0]}")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                nom_utilisateur_identification_wtf = form.nom_utilisateur_wtf.data
                mot_de_passe_identification_wtf = form.mot_de_passe_wtf.data
                courriel_identificaiton_wtf = form.courriel_wtf.data
                role_identificaiton_wtf = form.role_wtf.data

                nom_utilisateur_identification = nom_utilisateur_identification_wtf.lower()
                mot_de_passe_identification = generate_password_hash(mot_de_passe_identification_wtf)
                courriel_identificaiton = courriel_identificaiton_wtf.lower()
                role_identification = role_identificaiton_wtf.lower()

                valeurs_insertion_dictionnaire = {"value_nom_utilisateur": nom_utilisateur_identification,
                                                  "value_courriel": courriel_identificaiton,
                                                  "value_mot_de_passe": mot_de_passe_identification,
                                                  "value_role": role_identification}

                # ligne pour hasher le mdp
                # hs = hashlib.sha256(password.encode("utf-8")).hexdigest()

                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_identification (id_identification,nom_utilisateur,mot_de_passe,courriel, fk_role) VALUES (NULL,%(value_nom_utilisateur)s,%(value_mot_de_passe)s,%(value_courriel)s, %(value_role)s)"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "info")
                print(f"Données insérées !!")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('role_identification_afficher', order_by='DESC', id_role_identification_sel=0))

        # ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
        except pymysql.err.IntegrityError as erreur_genre_doublon:
            # Dérive "pymysql.err.IntegrityError" dans "MaBdErreurDoublon" fichier "erreurs/exceptions.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            code, msg = erreur_genre_doublon.args

            flash(f"{error_codes.get(code, msg)} ", "warning")

        # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
        except (pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                TypeError) as erreur_gest_genr_crud:
            code, msg = erreur_gest_genr_crud.args

            flash(f"{error_codes.get(code, msg)} ", "danger")
            flash(f"Erreur dans Gestion genres CRUD : {sys.exc_info()[0]} "
                  f"{erreur_gest_genr_crud.args[0]} , "
                  f"{erreur_gest_genr_crud}", "danger")

    return render_template("role_identification/role_identifiaction_ajouter_wtf.html", form=form)

@obj_mon_application.route("/role_identification_update", methods=['GET', 'POST'])
@si_user_login
@is_admin
def role_identification_update_wtf():

    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_identification_update = request.values['id_identification_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateIdentification()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_utilisateur_identification_update = form_update.nom_utilisateur_identification_update_wtf.data
            nom_utilisateur_identification_update = nom_utilisateur_identification_update.capitalize()

            courriel_identification_update = form_update. courriel_identification_update_wtf.data
            courriel_identification_update = courriel_identification_update.lower()

            mdp_identification_update = form_update.mdp_identification_update_wtf.data
            mdp_identification_update = generate_password_hash(mdp_identification_update)

            role_identification_update = form_update.role_identification_update_wtf.data
            role_identification_update = role_identification_update.lower()

            valeur_update_dictionnaire = {"value_id_identification": id_identification_update, "value_nom_utilisateur_identification": nom_utilisateur_identification_update, "value_courriel_identification": courriel_identification_update, "value_mdp_identification": mdp_identification_update, "value_role_identification": role_identification_update}
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_utilisateur = """UPDATE t_identification SET nom_utilisateur = %(value_nom_utilisateur_identification)s, courriel = %(value_courriel_identification)s, mot_de_passe = %(value_mdp_identification)s, fk_role = %(value_role_identification)s WHERE id_identification = %(value_id_identification)s"""

            with MaBaseDeDonnee() as mconn_bd:
                mconn_bd.mabd_execute(str_sql_update_nom_utilisateur, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "info")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_collaborateur_update"
            return redirect(url_for('role_identification_afficher', order_by="ASC", id_role_identification_sel=id_identification_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "nom_famille" de la "t_genre"
            str_sql_id_identification = "SELECT id_identification, nom_utilisateur, courriel, mot_de_passe, fk_role FROM t_identification WHERE id_identification = %(value_id_identification)s"
            valeur_select_dictionnaire = {"value_id_identification": id_identification_update}
            mybd_curseur = MaBaseDeDonnee().connexion_bd.cursor()
            mybd_curseur.execute(str_sql_id_identification, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_utilisateur_identification_collaborateur = mybd_curseur.fetchone()
            print(" ", data_nom_utilisateur_identification_collaborateur, " type ", type(data_nom_utilisateur_identification_collaborateur), " nom_utilisateur ",
                  data_nom_utilisateur_identification_collaborateur["courriel"], data_nom_utilisateur_identification_collaborateur["mot_de_passe"], data_nom_utilisateur_identification_collaborateur["fk_role"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "genre_update_wtf.html"
            form_update.nom_utilisateur_identification_update_wtf.data = data_nom_utilisateur_identification_collaborateur["nom_utilisateur"]
            form_update.courriel_identification_update_wtf.data = data_nom_utilisateur_identification_collaborateur["courriel"]
            form_update.mdp_identification_update_wtf.data = data_nom_utilisateur_identification_collaborateur[
                "mot_de_passe"]
            form_update.role_identification_update_wtf.data = data_nom_utilisateur_identification_collaborateur[
                "fk_role"]

    # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
    except KeyError:
        flash(f"__KeyError dans genre_update_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")
    except ValueError:
        flash(f"Erreur dans genre_update_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]}", "danger")
    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.err.IntegrityError,
            TypeError) as erreur_gest_genr_crud:
        code, msg = erreur_gest_genr_crud.args
        flash(f"attention : {error_codes.get(code, msg)} {erreur_gest_genr_crud} ", "danger")
        flash(f"Erreur dans genre_update_wtf : {sys.exc_info()[0]} "
              f"{erreur_gest_genr_crud.args[0]} , "
              f"{erreur_gest_genr_crud}", "danger")
        flash(f"__KeyError dans genre_update_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")

    return render_template("role_identification/role_identification_update_wtf.html", form_update=form_update)