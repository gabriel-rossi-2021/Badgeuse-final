"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import DateField
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import Length
from wtforms.validators import Regexp
from flask import url_for


class FormWTFAjouterDetails(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    sexe_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    sexe_wtf = StringField("Clavioter le sexe ", validators=[Length(min=2, max=5, message="min 2 max 5"),
                                                                   Regexp(sexe_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union"
                                                                                    " Femme ou Homme")
                                                                   ])
    rue_regexp = "^[A-Za-z'\.\-\s\,]"
    rue_wtf = StringField("Taper la rue du collaborateur ",
                             validators=[Length(min=2, max=48, message="min 2 max 48"),
                                         Regexp(rue_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])

    numero_rue_regexp = "^[0-9]+$"
    numero_rue_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=1, max=3, message="min 2 max 3"),
                                         Regexp(numero_rue_regexp,
                                                message="Pas de texte,"
                                                        " Pas de caractères spéciaux, "
                                                        " d'espace à double, de double "
                                                        " apostrophe, de double trait union,"
                                                        " Que des chiffre")
                                         ])
    npa_regexp = "^[0-9]+$"
    npa_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=1, max=5, message="min 1 max 5"),
                                         Regexp(npa_regexp,
                                                message="Pas de texte,"
                                                        " Pas de caractères spéciaux, "
                                                        " d'espace à double, de double "
                                                        " apostrophe, de double trait union,"
                                                        " Que des chiffre")
                                         ])
    ville_regexp = "^[A-Za-z'\.\-\s\,]"
    ville_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(ville_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    pays_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(pays_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    telephone_regexp = "^[0-9]+$"
    telephone_wtf = StringField("Taper le prénom du collaborateur ")
                             #validators=[Length(min=2, max=20, message="min 2 max 20"),
                              #           Regexp(telephone_regexp,
                               #                 message="Pas de chiffres, de caractères "
                                #                        "spéciaux, "
                                    #                    "d'espace à double, de double "
                                     #                   "apostrophe, de double trait union")
                                       #  ])

    date_entree_entreprise_regexp = "^((((31\/(0?[13578]|1[02]))|((29|30)\/(0?[1,3-9]|1[0-2])))\/(1[6-9]|[2-9]\d)?\d{2})|(29\/0?2\/(((1[6-9]|[2-9]\d)?(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))|(0?[1-9]|1\d|2[0-8])\/((0?[1-9])|(1[0-2]))\/((1[6-9]|[2-9]\d)?\d{2})) (20|21|22|23|[0-1]?\d):[0-5]?\d:[0-5]?\d+$"
    date_entree_entreprise_wtf = DateField("Date d'entrée")
    """
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(date_entree_entreprise_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    """
    submit = SubmitField("Enregistrer details")


class FormWTFUpdateDetails(FlaskForm):
    """
        Dans le formulaire "genre_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    sexe_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    sexe_update_wtf = StringField("Clavioter le sexe ", validators=[Length(min=2, max=5, message="min 2 max 5"),
                                                                   Regexp(sexe_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union"
                                                                                    " Femme ou Homme")
                                                                   ])
    rue_regexp = "^[A-Za-z'\.\-\s\,]"
    rue_update_wtf = StringField("Taper la rue du collaborateur ",
                             validators=[Length(min=2, max=48, message="min 2 max 48"),
                                         Regexp(rue_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])

    numero_rue_regexp = "^[0-9]+$"
    numero_update_rue_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=1, max=3, message="min 2 max 3"),
                                         Regexp(numero_rue_regexp,
                                                message="Pas de texte,"
                                                        " Pas de caractères spéciaux, "
                                                        " d'espace à double, de double "
                                                        " apostrophe, de double trait union,"
                                                        " Que des chiffre")
                                         ])
    npa_regexp = "^[0-9]+$"
    npa_update_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=1, max=5, message="min 1 max 5"),
                                         Regexp(npa_regexp,
                                                message="Pas de texte,"
                                                        " Pas de caractères spéciaux, "
                                                        " d'espace à double, de double "
                                                        " apostrophe, de double trait union,"
                                                        " Que des chiffre")
                                         ])
    ville_regexp = "^[A-Za-z'\.\-\s\,]"
    ville_update_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(ville_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    pays_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    pays_update_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(pays_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    telephone_regexp = "^[0-9]+$"
    telephone_update_wtf = StringField("Taper le prénom du collaborateur ")
                             #validators=[Length(min=2, max=20, message="min 2 max 20"),
                              #           Regexp(telephone_regexp,
                               #                 message="Pas de chiffres, de caractères "
                                #                        "spéciaux, "
                                 #                       "d'espace à double, de double "
                                  #                      "apostrophe, de double trait union")
                                   #      ])

    date_entree_entreprise_regexp = "^((((31\/(0?[13578]|1[02]))|((29|30)\/(0?[1,3-9]|1[0-2])))\/(1[6-9]|[2-9]\d)?\d{2})|(29\/0?2\/(((1[6-9]|[2-9]\d)?(0[48]|[2468][048]|[13579][26])|((16|[2468][048]|[3579][26])00))))|(0?[1-9]|1\d|2[0-8])\/((0?[1-9])|(1[0-2]))\/((1[6-9]|[2-9]\d)?\d{2})) (20|21|22|23|[0-1]?\d):[0-5]?\d:[0-5]?\d+$"
    date_entree_entreprise_update_wtf = DateField("Taper le prénom du collaborateur ")
    """
    validators=[Length(min=2, max=20, message="min 2 max 20"),
                                         Regexp(date_entree_entreprise_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])
    """

    submit = SubmitField("Enregistrer details")
class FormWTFDeleteDetails(FlaskForm):
    """
        Dans le formulaire "genre_delete_wtf.html"

        nom_collaborateur_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    sexe_collaborateur_delete_wtf = StringField("")
    rue_collaborateur_delete_wtf = StringField("")
    numero_rue_collaborateur_delete_wtf = StringField("")
    npa_collaborateur_delete_wtf = StringField("")
    ville_collaborateur_delete_wtf = StringField("")
    pays_collaborateur_delete_wtf = StringField("")
    telephone_collaborateur_delete_wtf = StringField("")
    date_entree_entreprise_collaborateur_delete_wtf = DateField("")

    submit_btn_del = SubmitField("Effacer ce collaborateur")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")