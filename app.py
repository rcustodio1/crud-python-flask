from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Página inicial: lista todos os usuários
@app.route('/')
def index():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

# Rota para criar novo usuário
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn = get_db_connection()
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('add.html')

# Rota para editar
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        conn.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, id))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('edit.html', user=user)

# Rota para deletar
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
