from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "atm123"

PIN = "fikom12345"
saldo = 1000000000

# LOGIN
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['pin'] == str (PIN)   :
            session['login'] = True
            return redirect('/menu')
        else:
            return render_template("pin_salah.html")

    return render_template('index.html')


# MENU
@app.route('/menu')
def menu():
    if 'login' not in session:
        return redirect('/')
    return render_template('menu.html', saldo=saldo)


# TARIK TUNAI
@app.route('/tarik', methods=['GET', 'POST'])
def tarik():
    global saldo
    if 'login' not in session:
        return redirect('/')

    if request.method == 'POST':
        jumlah = int(request.form['jumlah'])

        if jumlah <= saldo:
            saldo -= jumlah
            return redirect('/menu')
        else:
            return render_template('')

    return render_template('tarik.html')


# SETOR UANG
@app.route('/setor', methods=['GET', 'POST'])
def setor():
    global saldo
    if 'login' not in session:
        return redirect('/')

    if request.method == 'POST':
        jumlah = int(request.form['jumlah'])
        saldo += jumlah
        return redirect('/menu')

    return render_template('setor.html')


if __name__ == '__main__':
    app.run(debug=True)