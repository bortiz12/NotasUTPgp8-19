from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/Gestionusu")
def Gestionusu():
    return render_template('Gestionusu.html')

@app.errorhandler(404)
def pagina_no_encontrada(e):
    return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True,port=5000)
    