from flask import Flask, request, render_template, url_for, flash, redirect


app = Flask(__name__)



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

















