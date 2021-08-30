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
from APP_Timbrage.details.gestion_details_wtf_forms import FormWTFAjouterDetails
from APP_Timbrage.details.gestion_details_wtf_forms import FormWTFUpdateDetails
from APP_Timbrage.details.gestion_details_wtf_forms import FormWTFDeleteDetails
from APP_Timbrage.utils.utils import si_user_login
from APP_Timbrage.utils.utils import is_admin

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /collaborateur_afficher

    Test : ex : http://127.0.0.1:5005/collaborateur_afficher

    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_collaborateur_sel = 0 >> tous les genres.
                id_collaborateur_sel = "n" affiche le genre dont l'id est "n"
"""


@obj_mon_application.route("/details_afficher/<string:order_by>/<int:id_details_sel>", methods=['GET', 'POST'])
@si_user_login
@is_admin
def details_afficher(order_by, id_details_sel):
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
                if order_by == "ASC" and id_details_sel == 0:
                    strsql_collaborateur_afficher = """SELECT id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise FROM t_details_collaborateur  ORDER BY id_details_collaborateur ASC"""
                    mc_afficher.execute(strsql_collaborateur_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_collaborateur_selected_dictionnaire = {
                        "value_id_collaborateur_selected": id_details_sel}
                    strsql_collaborateur_afficher = """SELECT id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise FROM t_details_collaborateur WHERE id_details_collaborateur= %(value_id_collaborateur_selected)s"""

                    mc_afficher.execute(strsql_collaborateur_afficher, valeur_id_collaborateur_selected_dictionnaire)
                else:
                    strsql_collaborateur_afficher = """SELECT id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise FROM t_details_collaborateur  ORDER BY id_details_collaborateur DESC"""

                    mc_afficher.execute(strsql_collaborateur_afficher)

                data_collaborateur = mc_afficher.fetchall()

                print("data_collaborateur ", data_collaborateur, " Type : ", type(data_collaborateur))

                # Différencier les messages si la table est vide.
                if not data_collaborateur and id_details_sel == 0:
                    flash("""La table "t_collaborateur" est vide. !!""", "warning")
                elif not data_collaborateur and id_details_sel > 0:
                    # Si l'utilisateur change l'id_collaborateur dans l'URL et que le genre n'existe pas,
                    flash(f"Le collaborateur demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données details affichés !!", "primary")

        except Exception as erreur:
            print(f"RGG Erreur générale.")
            # OM 2020.04.09 On dérive "Exception" par le "@obj_mon_application.errorhandler(404)" fichier "run_mon_app.py"
            # Ainsi on peut avoir un message d'erreur personnalisé.
            flash(f"RGG Exception {erreur}")
            raise Exception(f"RGG Erreur générale. {erreur}")
            raise MaBdErreurOperation(f"RGG Exception {msg_erreurs['ErreurNomBD']['message']} {erreur}")

    # Envoie la page "HTML" au serveur.
    return render_template("details/details_afficher.html", data=data_collaborateur)

@obj_mon_application.route("/details_ajouter", methods=['GET', 'POST'])
@si_user_login
@is_admin
def details_ajouter_wtf():
    form = FormWTFAjouterDetails()
    if request.method == "POST":
        try:
            try:
                # Renvoie une erreur si la connexion est perdue.
                MaBaseDeDonnee().connexion_bd.ping(False)
            except Exception as erreur:
                flash(f"Dans Gestion genres ...terrible erreur, il faut connecter une base de donnée", "danger")
                print(f"Exception grave Classe constructeur GestionGenres {erreur.args[0]}")
                raise MaBdErreurConnexion(f"{msg_erreurs['ErreurConnexionBD']['message']} {erreur.args[0]}")

            if form.validate_on_submit():
                sexe_collaborateur_wtf = form.sexe_wtf.data
                sexe_collaborateur = sexe_collaborateur_wtf.capitalize()

                rue_collaborateur_wtf = form.rue_wtf.data
                rue_collaborateur = rue_collaborateur_wtf.capitalize()

                numero_rue_collaborateur_wtf = form.numero_rue_wtf.data
                numero_rue_collaborateur = numero_rue_collaborateur_wtf.lower()

                npa_collaborateur_wtf = form.npa_wtf.data
                npa_collaborateur = npa_collaborateur_wtf.capitalize()

                ville_collaborateur_wtf = form.ville_wtf.data
                ville_collaborateur = ville_collaborateur_wtf.capitalize()

                pays_collaborateur_wtf = form.pays_wtf.data
                pays_collaborateur = pays_collaborateur_wtf.capitalize()

                telephone_collaborateur_wtf = form.telephone_wtf.data
                telephone_collaborateur = telephone_collaborateur_wtf.lower()

                date_entree_entreprise_collaborateur_wtf = form.date_entree_entreprise_wtf.data
                date_entree_entreprise_collaborateur = date_entree_entreprise_collaborateur_wtf

                valeurs_insertion_dictionnaire = {"value_sexe": sexe_collaborateur,
                                                  "value_rue": rue_collaborateur,
                                                  "value_numero_rue": numero_rue_collaborateur,
                                                  "value_npa": npa_collaborateur,
                                                  "value_ville": ville_collaborateur,
                                                  "value_pays": pays_collaborateur,
                                                  "value_telephone": telephone_collaborateur,
                                                  "value_date_entree": date_entree_entreprise_collaborateur}

                print("valeurs_insertion_dictiIonnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_genre = """INSERT INTO t_details_collaborateur (id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise) VALUES (NULL,%(value_sexe)s,%(value_rue)s,%(value_numero_rue)s,%(value_npa)s,%(value_ville)s,%(value_pays)s,%(value_telephone)s,%(value_date_entree)s)"""
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(strsql_insert_genre, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "info")
                print(f"Données insérées !!")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('details_afficher', order_by='DESC', id_details_sel=0))

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

    return render_template("details/details_ajouter_wtf.html", form=form)

"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /genre_update

    Test : ex cliquer sur le menu "genres" puis cliquer sur le bouton "EDIT" d'un "genre"

    Paramètres : sans

    But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

    Remarque :  Dans le champ "nom_genre_update_wtf" du formulaire "genres/genre_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@obj_mon_application.route("/details_update", methods=['GET', 'POST'])
@si_user_login
@is_admin
def details_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_details_update = request.values['id_collaborateur_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateDetails()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            sexe_collaborateur_update = form_update.sexe_update_wtf.data
            sexe_collaborateur_update = sexe_collaborateur_update.capitalize()

            rue_collaborateur_update = form_update.rue_update_wtf.data
            rue_collaborateur_update = rue_collaborateur_update.capitalize()

            numero_rue_collaborateur_update = form_update.numero_update_rue_wtf.data
            numero_rue_collaborateur_update = numero_rue_collaborateur_update.lower()

            npa_collaborateur_update = form_update.npa_update_wtf.data
            npa_collaborateur_update = npa_collaborateur_update.capitalize()

            ville_collaborateur_update = form_update.ville_update_wtf.data
            ville_collaborateur_update = ville_collaborateur_update.capitalize()

            pays_collaborateur_update = form_update.pays_update_wtf.data
            pays_collaborateur_update = pays_collaborateur_update.capitalize()

            telephone_collaborateur_update = form_update.telephone_update_wtf.data
            telephone_collaborateur_update = telephone_collaborateur_update.lower()

            date_entree_entreprise_collaborateur_update = form_update.date_entree_entreprise_update_wtf.data
            date_entree_entreprise_collaborateur_update = date_entree_entreprise_collaborateur_update

            valeur_update_dictionnaire = {"value_id_details": id_details_update,
                                          "value_sexe_update": sexe_collaborateur_update,
                                                  "value_rue_update": rue_collaborateur_update,
                                                  "value_numero_rue_update": numero_rue_collaborateur_update,
                                                  "value_npa_update": npa_collaborateur_update,
                                                  "value_ville_update": ville_collaborateur_update,
                                                  "value_pays_update": pays_collaborateur_update,
                                                  "value_telephone_update": telephone_collaborateur_update,
                                                  "value_date_entree_update": date_entree_entreprise_collaborateur_update}

            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nomcollaborateur = """UPDATE t_details_collaborateur SET sexe = %(value_sexe_update)s, rue = %(value_rue_update)s, numero_rue = %(value_numero_rue_update)s, npa = %(value_npa_update)s, ville = %(value_ville_update)s, pays = %(value_pays_update)s, telephone = %(value_telephone_update)s, date_entree_entreprise = %(value_date_entree_update)s WHERE id_details_collaborateur = %(value_id_details)s"""

            with MaBaseDeDonnee() as mconn_bd:
                mconn_bd.mabd_execute(str_sql_update_nomcollaborateur, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "info")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_details_update"
            return redirect(url_for('details_afficher', order_by="ASC", id_details_sel=id_details_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "nom_famille" de la "t_genre"
            str_sql_id_collaborateur = "SELECT id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise FROM t_details_collaborateur WHERE id_details_collaborateur = %(value_id_details)s"
            valeur_select_dictionnaire = {"value_id_details": id_details_update}
            mybd_curseur = MaBaseDeDonnee().connexion_bd.cursor()
            mybd_curseur.execute(str_sql_id_collaborateur, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_collaborateur = mybd_curseur.fetchone()
            print(" ", data_nom_collaborateur, " type ", type(data_nom_collaborateur), " details ",
                  data_nom_collaborateur["sexe"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "genre_update_wtf.html"
            form_update.sexe_update_wtf.data = data_nom_collaborateur["sexe"]
            form_update.rue_update_wtf.data = data_nom_collaborateur["rue"]
            form_update.numero_update_rue_wtf.data = data_nom_collaborateur["numero_rue"]
            form_update.npa_update_wtf.data = data_nom_collaborateur["npa"]
            form_update.ville_update_wtf.data = data_nom_collaborateur["ville"]
            form_update.pays_update_wtf.data = data_nom_collaborateur["pays"]
            form_update.telephone_update_wtf.data = data_nom_collaborateur["telephone"]
            form_update.date_entree_entreprise_update_wtf.data = data_nom_collaborateur["date_entree_entreprise"]

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

    return render_template("details/details_update_wtf.html", form_update=form_update)

@obj_mon_application.route("/details_delete", methods=['GET', 'POST'])
@si_user_login
@is_admin
def details_delete_wtf():
    data_films_attribue_genre_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_details_delete = request.values['id_collaborateur_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteDetails()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("details_afficher", order_by="ASC", id_details_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_genre_delete = session['data_films_attribue_genre_delete']
                print("data_films_attribue_genre_delete ", data_films_attribue_genre_delete)

                flash(f"Effacer ces details de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_details_collaborateur": id_details_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_genre = """DELETE FROM t_collaborateur_details_collaborateur WHERE FK_details_collaborateur = %(value_id_details_collaborateur)s"""
                str_sql_delete_idgenre = """DELETE FROM t_details_collaborateur WHERE id_details_collaborateur = %(value_id_details_collaborateur)s"""
                # Manière brutale d'effacer d'abord la "FK_collaborateur", même si elle n'existe pas dans la "t_collaborateur_details_collaborateur"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_collaborateur_details_collaborateur"
                with MaBaseDeDonnee() as mconn_bd:
                    mconn_bd.mabd_execute(str_sql_delete_films_genre, valeur_delete_dictionnaire)
                    mconn_bd.mabd_execute(str_sql_delete_idgenre, valeur_delete_dictionnaire)

                flash(f"Genre définitivement effacé !!", "info")
                print(f"Genre définitivement effacé !!")

                # afficher les données
                return redirect(url_for('details_afficher', order_by="ASC", id_details_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_details_collaborateur": id_details_delete}
            print(id_details_delete, type(id_details_delete))

            # Requête qui affiche tous les films qui ont le genre que l'utilisateur veut effacer
            str_sql_genres_films_delete = """SELECT id_collaborateur, nom_famille, prenom FROM t_collaborateur_details_collaborateur
                                            INNER JOIN t_collaborateur ON t_collaborateur_details_collaborateur.FK_collaborateur = t_collaborateur.id_collaborateur
                                            INNER JOIN t_details_collaborateur ON t_collaborateur_details_collaborateur.FK_details_collaborateur = t_details_collaborateur.id_details_collaborateur
                                            WHERE FK_details_collaborateur = %(value_id_details_collaborateur)s"""

            mybd_curseur = MaBaseDeDonnee().connexion_bd.cursor()

            mybd_curseur.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
            data_films_attribue_genre_delete = mybd_curseur.fetchall()
            print("data_films_attribue_genre_delete...", data_films_attribue_genre_delete)

            # Nécessaire pour mémoriser les données afin d'afficher à nouveau
            # le formulaire "genres/genre_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            session['data_films_attribue_genre_delete'] = data_films_attribue_genre_delete

            # Opération sur la BD pour récupérer "id_genre" et "nom_famille" de la "t_genre"
            str_sql_id_collaborateur = "SELECT id_details_collaborateur, sexe, rue, numero_rue, npa, ville, pays, telephone, date_entree_entreprise FROM t_details_collaborateur  WHERE id_details_collaborateur = %(value_id_details_collaborateur)s"

            mybd_curseur.execute(str_sql_id_collaborateur, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()",
            # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
            data_nom_collaborateur = mybd_curseur.fetchone()
            print("data_nom_collaborateur ", data_nom_collaborateur, " type ", type(data_nom_collaborateur), " genre ",
                  data_nom_collaborateur["sexe"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "genre_delete_wtf.html"
            form_delete.sexe_collaborateur_delete_wtf.data = data_nom_collaborateur["sexe"]
            form_delete.rue_collaborateur_delete_wtf.data = data_nom_collaborateur["rue"]
            form_delete.numero_rue_collaborateur_delete_wtf.data = data_nom_collaborateur["numero_rue"]
            form_delete.npa_collaborateur_delete_wtf.data = data_nom_collaborateur["npa"]
            form_delete.ville_collaborateur_delete_wtf.data = data_nom_collaborateur["ville"]
            form_delete.pays_collaborateur_delete_wtf.data = data_nom_collaborateur["pays"]
            form_delete.telephone_collaborateur_delete_wtf.data = data_nom_collaborateur["telephone"]
            form_delete.date_entree_entreprise_collaborateur_delete_wtf.data = data_nom_collaborateur["date_entree_entreprise"]

            # Le bouton pour l'action "DELETE" dans le form. "genre_delete_wtf.html" est caché.
            btn_submit_del = False

    # OM 2020.04.16 ATTENTION à l'ordre des excepts, il est très important de respecter l'ordre.
    except KeyError:
        flash(f"__KeyError dans genre_delete_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")
    except ValueError:
        flash(f"Erreur dans genre_delete_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]}", "danger")
    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.err.IntegrityError,
            TypeError) as erreur_gest_genr_crud:
        code, msg = erreur_gest_genr_crud.args
        flash(f"attention : {error_codes.get(code, msg)} {erreur_gest_genr_crud} ", "danger")

        flash(f"Erreur dans genre_delete_wtf : {sys.exc_info()[0]} "
              f"{erreur_gest_genr_crud.args[0]} , "
              f"{erreur_gest_genr_crud}", "danger")

        flash(f"__KeyError dans genre_delete_wtf : {sys.exc_info()[0]} {sys.exc_info()[1]} {sys.exc_info()[2]}",
              "danger")

    return render_template("details/details_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_collaborateur_associes=data_films_attribue_genre_delete)
