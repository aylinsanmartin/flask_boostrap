from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
db =SQLAlchemy(app)
migrate = Migrate(app, db)
class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    picture = db.Column(db.String(300))
    def __repr__(self):
        return f'<Message {self.title}>'
@app.route('/navegador')
def browser():
    user_agent = request.headers.get('User-Agent')
    return f'Tu navegador es: {user_agent}'
@app.route('/rutas')
def routes():
    print(app.url_map)
    return 'Revisa tu consola para ver las rutas'
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 400

















