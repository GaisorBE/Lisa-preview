from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uren')
def uren():
    uren_data = [
        {'naam': 'Pieter', 'project': 'IMEC 1', 'uren': 8},
        {'naam': 'Evelyne', 'project': 'PV installatie', 'uren': 7.5}
    ]
    return render_template('uren.html', uren=uren_data)

@app.route('/materiaal')
def materiaal():
    materialen = [
        {'item': 'XGB 3G2.5mm²', 'aantal': 10, 'eenheid': 'm'},
        {'item': 'HVK kabel', 'aantal': 5, 'eenheid': 'm'}
    ]
    return render_template('materiaal.html', materiaal=materialen)

@app.route('/projecten')
def projecten():
    projecten_data = [
        {'project': 'IMEC 1', 'status': 'Actief'},
        {'project': 'PV installatie', 'status': 'Afgewerkt'}
    ]
    return render_template('projecten.html', projecten=projecten_data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port)
