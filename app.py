from flask import Flask, request, render_template
import mysql.connector


app = Flask(__name__)

credenciales = {
  'user': 'root',
  'password': 'root',
  'database': 'test',
  'host': 'localhost'
}

@app.route('/')
def login():
  return(render_template('login.html'))

@app.route('/users', methods=['GET'])
def users():
  conector = mysql.connector.connect(**credenciales)
  cursor = conector.cursor(dictionary=True)
  cursor.execute('SELECT * FROM users')
  users = cursor.fetchall()
  conector.close()
  return (users)

if __name__ == '__main__':
  app.run(debug=True)
