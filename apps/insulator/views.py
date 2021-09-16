from flask import Blueprint, render_template, request

insulator_bp = Blueprint('insulator', __name__)

@insulator_bp.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return ''

    return render_template('login.html')