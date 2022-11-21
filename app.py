from flask import Flask, request, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Escribe cualquier cosa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Aylin93@localhost:5432/flask_bootstrap'
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
@app.route('/')
def index():
    messages = Message.query.all()
    return render_template('index.html', messages = messages)
@app.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        picture = request.form['picture']
        if not title:
            flash('El título es obligatorio')
        elif not content:
            flash('El contenido es obligatorio')
        else:
           message = Message(title = title, content = content, picture = picture)
           db.session.add(message)
           db.session.commit()
           return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/usuario/<name>')
def user(name):
    return render_template('user.html', user = name)
@app.route('/<id>/update', methods =('GET', 'POST'))
def update(id):
    message = Message.query.filter_by(id = id).first()
    if request.method == 'POST':
        if message:
            message.title = request.form['title']
            message.content = request.form['content']
            message.picture = request.form['picture']
            db.session.commit()
            return redirect('/')
    return render_template('update.html', message = message)
@app.route('/delete', methods = ['POST'])
def delete():
    id = request.form['id']
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    flash('Mensaje Eliminado')
    return redirect('/')
def user_incognito():
    return render_template('user.html')
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

















