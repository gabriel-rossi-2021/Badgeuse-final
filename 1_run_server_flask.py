import sys

from flask import flash
from flask import render_template

from APP_Timbrage import obj_mon_application
from APP_Timbrage import DEBUG_FLASK
from APP_Timbrage import ADRESSE_SRV_FLASK
from APP_Timbrage import PORT_FLASK

@obj_mon_application.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@obj_mon_application.errorhandler(Exception)
def om_104_exception_handler(error):
    flash(f"Erreur : {error} {error.args[0]} {sys.exc_info()[0]}", "danger")
    a, b, c = sys.exc_info()
    flash(f"Erreur générale : {a} {b} {c}", "danger")
    return render_template("home.html")


if __name__ == "__main__":

    print("obj_mon_application.url_map ____> ", obj_mon_application.url_map)
    obj_mon_application.run(debug=DEBUG_FLASK,
                            host=ADRESSE_SRV_FLASK,
                            port=PORT_FLASK)
