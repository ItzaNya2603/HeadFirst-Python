from flask import Flask, render_template, request
from vsearch import search4letters
from DBcm import UseDatabase  # Biblioteca imporetada del cap 8

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Configuración de la base de datos
dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': 'AkimiPichu26',
    'database': 'vsearchlogDB',
}

def log_request(req: 'flask_request', res: str) -> None:
    # ...
    with UseDatabase(dbconfig) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser, results)  # Aquí decía browser_string
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                             req.form['letters'],
                             req.remote_addr,
                             req.user_agent.browser,
                             res, ))

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    
    # Se guarda el log, es decir, el dato que se ingreso en la base de datos antes de que se cierre
    try:
        log_request(request, results)
    except Exception as err:
        print('***** El logueo falló con este error:', str(err))
    
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)

@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(dbconfig) as cursor:
        # Agregamos ORDER BY id DESC al final
        _SQL = """select phrase, letters, ip, browser, results
                  from log
                  order by id desc""" 
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    
    titles = ('Frase', 'Letras', 'Dirección IP', 'Navegador', 'Resultado')
    return render_template('viewlog.html',
                           the_title='Historial de Búsquedas',
                           the_row_titles=titles,
                           the_data=contents,)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to vsearch on the web!')

if __name__ == '__main__':
    app.run(debug=True)