import pyodbc
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'Python_Authenticate'


server = 'LAPTOP-SH2LV5E6\SQLEXPRESS'
database = 'Odbc'
username = 'sa'
password = 'YourAutenticationBank'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)


@app.route('/')
def index():
    return render_template('cadastro.html')

@app.route('/cadastrar', methods=['POST'])

def cadastrar():
        nome = request.form['username']
        email = request.form['email']
        pwd = request.form['password']

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cadastro (Usuario, Email, Password) VALUES (?, ?, ?)", nome, email, pwd)
        cursor.commit()

        cursor.close()
        return redirect(url_for('home'))

@app.route('/home')
def home():
    if 'usuario' in session:
        return f'Bem-vindo, {session["usuario"]}! <a href="/logout">Logout</a>'
    return 'Página inicial - <a href="/Login">Login</a>'
@app.route('/Login')
def Login():
    return render_template('Login.html')
@app.route('/logar', methods=['POST'])
def logar():

        email = request.form['email']
        password = request.form['password']
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Cadastro WHERE Email = ? AND Password = ?",
                       (email, password))
        usuario = cursor.fetchone()

        conn.close()
        if usuario:
            session['usuario'] = usuario.Email
            return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
