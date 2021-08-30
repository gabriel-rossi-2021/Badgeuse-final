import sys

from flask import Flask
import environs
from environs import Env

HOST_MYSQL = None
USER_MYSQL = None
PASS_MYSQL = None
PORT_MYSQL = None
NAME_BD_MYSQL = None
NAME_FILE_DUMP_SQL_BD = None

ADRESSE_SRV_FLASK = None
DEBUG_FLASK = None
PORT_FLASK = None
SECRET_KEY_FLASK = None
WTF_CSRF_ENABLED = True

try:

    obj_env = Env()
    obj_env.read_env()
    HOST_MYSQL = obj_env("HOST_MYSQL")
    USER_MYSQL = obj_env("USER_MYSQL")
    PASS_MYSQL = obj_env("PASS_MYSQL")
    PORT_MYSQL = int(obj_env("PORT_MYSQL"))  # Pour la connection à la BD le port doit être une valeur numérique INT
    NAME_BD_MYSQL = obj_env("NAME_BD_MYSQL")
    NAME_FILE_DUMP_SQL_BD = obj_env("NAME_FILE_DUMP_SQL_BD")

    ADRESSE_SRV_FLASK = obj_env("ADRESSE_SRV_FLASK")
    DEBUG_FLASK = obj_env("DEBUG_FLASK")
    PORT_FLASK = obj_env("PORT_FLASK")
    SECRET_KEY_FLASK = obj_env("SECRET_KEY_FLASK")

except environs.EnvError as NameVariableEnv:
    print(f"environs.EnvError Problème avec les variables d'environnement "
          f"{NameVariableEnv.args[0]} , "
          f"{NameVariableEnv}")
    # Erreur très importante d'initialisation des paramètres de l'application. Donc ARRET immédiat.
    sys.exit()
except NameError as NameVariableErrorEnv:
    print(f"Problème avec les noms des variables d'environnement "
          f"{NameVariableErrorEnv.args[0]} , "
          f"{NameVariableErrorEnv.args[0]} , "
          f"{NameVariableErrorEnv}")

except Exception as ErreurFichierEnvironnement:
    raise (f"Problème avec le fichier .env  ")

try:

    # Objet qui fait "exister" notre application
    print(" __name__ ", __name__)
    obj_mon_application = Flask(__name__, template_folder="templates")

    # Flask va pouvoir crypter les cookies
    obj_mon_application.secret_key = SECRET_KEY_FLASK
except Exception as error_app:
    print(f"Problème d'application "
          f"{error_app.args[0]} , "
          f"{error_app}")
    raise

from APP_Timbrage.database import database_tools

from APP_Timbrage.collaborateur import gestion_collaborateur_CRUD
from APP_Timbrage.collaborateur import gestion_collaborateur_wtf_forms

from APP_Timbrage.identification import gestion_identification_crud
from APP_Timbrage.identification import gestion_identification_wtf_forms

from APP_Timbrage.login import login

from APP_Timbrage.origine_collaborateurs import gestion_origine_collaborateurs_crud

from APP_Timbrage.horaire import gestion_horaire_crud

from APP_Timbrage.details import gestion_details_CRUD
from APP_Timbrage.details import gestion_details_wtf_forms

from APP_Timbrage.role_identification import gestion_role_identification_CRUD
from APP_Timbrage.role_identification import gestion_role_identification_wtf_forms

from APP_Timbrage.setting import routes_demos
from APP_Timbrage.erreurs import msg_avertissements
