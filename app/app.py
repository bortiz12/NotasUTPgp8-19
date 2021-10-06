from flask import Flask,render_template,url_for,redirect

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/home")
def home():
    return render_template('home.html')


def pagina_no_encontrada(error):
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True,port=5000)
    