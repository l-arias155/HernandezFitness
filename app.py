from flask import Flask, render_template, flash, redirect, url_for

from service.form import LoginForm, RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

data = [
    {
        "name": "Luis Antonio Arias Chaves",
        "id": "2-0740-0871",
        "birthdate": "15/Jun/1995",
        "age": "25 años",
        "address": "Sarchí Norte, Sarchí, Alajuela",
        "phone": "85245504",
        "observations": "Su objetivo es generar masa muscular, para participar el el próximo concurso el 22 de agosto del 2021"
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Register complete")
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'luis.arias.chaves@gmail.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('account'))
        elif form.email.data == 'admin@gmail.com' and form.password.data == 'password':
            flash('Admin logging')
            return redirect(url_for('admin'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/account")
def account():
    return render_template('user_account.html', data=data)


@app.route("/admin")
def admin():
    return render_template('admin_account.html', data=data)


@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template('user_account_editable.html', data=data)


if __name__ == '__main__':
    app.run()
