from flask import Flask, request, render_template
from vsearch import search4letters
import mysql.connector

app = Flask(__name__)

# Configuración de tu base de datos
dbconfig = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'AkimiPichu26',
    'database': 'vsearchlogdb',
}

def log_request(req: 'flask_request', res: str) -> None:
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log
              (phrase, letters, ip, browser, results)
              values
              (%s, %s, %s, %s, %s)"""
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          str(req.user_agent.browser), # <--- ¡El cambio está aquí!
                          res, ))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def hello() -> str:
    return render_template('entry.html', 
                           the_title='¡Bienvenido a Search4Letters en la Web!')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    la_frase = request.form['phrase']
    las_letras = request.form['letters']
    if las_letras == "":
        el_resultado = str(search4letters(la_frase))
        las_letras = "Vocales (Por defecto)"
    else:
        el_resultado = str(search4letters(la_frase, las_letras))
    
    log_request(request, el_resultado) # Guarda en la BD

    return render_template('results.html',
                           the_title='Aquí están tus resultados:',
                           frase_recibida = la_frase,
                           letras_buscadas = las_letras,
                           resultado_final = el_resultado)

@app.route('/viewlog')
def view_the_log() -> 'html':
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """select phrase, letters, ip, browser, results from log"""
    cursor.execute(_SQL)
    contents = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('viewlog.html',
                           the_title='Registros en MySQL',
                           the_row_titles=['Frase', 'Letras', 'IP', 'Navegador', 'Resultado'],
                           the_data=contents,)

if __name__ == '__main__':
    app.run(debug=True)