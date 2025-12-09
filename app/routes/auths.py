from flask import Blueprint, session, flash, render_template, redirect, url_for, request

auth_bp = Blueprint("auth", __name__)

user_credantial = {
    'username':'admit',
    'password':'pass'
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == user_credantial["username"] and password == user_credantial["password"]:
            session['user'] = username
            flash('Login successful', 'success')
        else:
            flash('Invalide username, password', 'danger')
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.pop('user', None)
    flash('Logged out', 'info')
    return redirect(url_for("auth.login"))



#blueprint -> all routes will be in a group