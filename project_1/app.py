from flask import Flask, request, render_template, session, redirect, url_for
import hashlib
import time
import random
import string
import os
from datetime import datetime, timedelta

# Импортируем необходимые библиотеки
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Хранение пользователей в памяти 
users = {
    'admin': 'password'#generate_password_hash('password'),
}

# Лимиты на попытки входа
MAX_LOGIN_ATTEMPTS = 3
LOGIN_BLOCK_TIME_MINUTES = 10

# Генерация случайного токена
def generate_csrf_token():
    token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    return token

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Генерируем новый токен при каждом запросе
        csrf_token = generate_csrf_token()
        session['csrf_token'] = csrf_token
        return render_template('login.html', csrf_token=csrf_token)
    
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        csrf_token = request.args.get('csrf_token')
        
        # Проверка наличия токена и соответствия токену сессии
        if csrf_token != session.pop('csrf_token', None):
            return 'CSRF Token mismatch!', 400
        
        if username not in users:
            return f'User {username} does not exist.', 401
        
        stored_password_hash = users[username]
        
        # Проверяем, не была ли учетная запись заблокирована
        blocked_until = session.get(f'{username}_blocked_until', None)
        if blocked_until is not None and datetime.utcnow() <= blocked_until:
            remaining_time = (blocked_until - datetime.utcnow()).total_seconds()
            minutes_remaining = int(remaining_time // 60)
            seconds_remaining = int(remaining_time % 60)
            return f'Account locked! Try again in {minutes_remaining} minutes and {seconds_remaining} seconds.', 403
        
        # Проверяем пароль
        if not check_password_hash(stored_password_hash, password):
            # Увеличиваем счетчик неудачных попыток
            attempts = session.get(f'{username}_attempts', 0)
            attempts += 1
            session[f'{username}_attempts'] = attempts
            
            # Блокируем аккаунт, если превышен лимит попыток
            if attempts >= MAX_LOGIN_ATTEMPTS:
                block_until = datetime.utcnow() + timedelta(minutes=LOGIN_BLOCK_TIME_MINUTES)
                session[f'{username}_blocked_until'] = block_until
                return f'Too many failed attempts! Account locked for {LOGIN_BLOCK_TIME_MINUTES} minutes.', 403
            
            # Логируем попытку входа
            print(f'[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] Failed login attempt for user {username}, attempts left: {MAX_LOGIN_ATTEMPTS - attempts}')
            return redirect(url_for('login'))
        
        # Очищаем счетчики неудачных попыток и блокировки
        session.pop(f'{username}_attempts', None)
        session.pop(f'{username}_blocked_until', None)
        
        session['username'] = username
        session.modified = True
        return redirect(url_for('index'))

@app.route('/')
def index():
    username = session.get('username', None)
    if not username:
        return redirect(url_for('login'))
    return render_template('index.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)