from flask import Blueprint, render_template

verifikasipengguna_bp = Blueprint('verifikasipengguna', __name__)

@verifikasipengguna_bp.route('/verifikasipengguna')
def profil():
    return render_template("verifikasipengguna.html")