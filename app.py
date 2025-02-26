import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
import bcrypt
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@127.0.0.1:3306/{os.getenv('MYSQL_DATABASE')}"
)


login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username and password:
            hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
            user = User(username=username, password=hashed_password.decode('utf-8'), role='user')
            db.session.add(user)
            db.session.commit()
            flash("Usuário cadastrado com sucesso!")
            return redirect(url_for('login'))
        else:
            flash("Dados inválidos! Preencha todos os campos.")
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username and password:
            user = User.query.filter_by(username=username).first()
            if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
                login_user(user)
                flash("Autenticação realizada com sucesso!")
                return redirect(url_for('profile'))
            else:
                flash("Credenciais inválidas!")
        else:
            flash("Por favor, preencha todos os campos!")
    
    return render_template('login.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout realizado com sucesso!")
    return redirect(url_for('login'))

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
