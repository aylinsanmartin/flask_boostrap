from app.auth import bp
from flask import render_template, request, flash, redirect, url_for
from app.models.user import User
from app.extensions import db
@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users = users)
@bp.route('/register', methods =('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        if not username:
            flash('El nombre de usuario esobligatorio')
        elif not email:
            flash('El correo es obligatorio')
        elif not password == password_confirm:
            flash('La contraseña no coinciden')
        else:
            user = User(username = username, email = email, password_hash = password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.index'))
    return render_template('auth/register.html')





