"""
    Fichier : gestion_genres_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import DateTimeField
from wtforms.validators import Length
from wtforms.validators import Regexp
from flask import url_for


class FormWTFAjouterDetails(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    origine_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    origine_wtf = StringField("Taper le prénom du collaborateur ",
                             validators=[Length(min=2, max=40, message="min 2 max 20"),
                                         Regexp(origine_regexp,
                                                message="Pas de chiffres, de caractères "
                                                        "spéciaux, "
                                                        "d'espace à double, de double "
                                                        "apostrophe, de double trait union")
                                         ])

    submit = SubmitField("Enregistrer details")
