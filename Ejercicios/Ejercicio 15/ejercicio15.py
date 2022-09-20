"""Elija cuatro códigos desarrollados previamente e integre dichos
códigos a su página personal, la información debe solicitarse por
medio de formularios al usuario, los resultados de dicho códigos
debe mostrarse en el navegador."""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/visualizar',methods=['POST'])
def visualizar():
    def fahrenheit_a_celsius(data)->float:
        """
        Con la Letra F 
        """
        res = (5/9)*(data-32)
        return res

    def celsius_a_fahrenheit(data)->float:
        """
        Con la Letra C 
        """
        res = (9/5)*data+32
        return res
    if request.method == 'POST':
        print("Entre..")
        farengein = request.form['Farengein']
        celcius = request.form['Celcius']
        faren =float(farengein)
        celc = float(celcius)
        faren_transf = round(celsius_a_fahrenheit(celc),2)
        celcius_transf = round(fahrenheit_a_celsius(faren),2)   
        
        print(farengein)
        print(celcius)
        

    return render_template('index.html', far=farengein,cel=celcius, farT=faren_transf, celT=celcius_transf)

@app.route('/index')
def form():
    return render_template('form.html')



if __name__ == '__main__':
    app.run(debug=True)