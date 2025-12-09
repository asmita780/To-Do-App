from flask import Flask #to create the app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #global object of sqlalchemy

def create_app(): #function that we create the app(it will return the app)
    app = Flask(__name__) #creating the app

    app.config['SECRET_KEY'] = 'your-secret-key' #use to secure flash, session
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db' #db url to tell where is the db
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app) 
    #linked the db with app

    from app.models import Task
 #what task should created when run bd.create
    
    with app.app_context():
        db.create_all()

    #bluprint -> routes will be inside it, registred it so that flask will know about tham
    from app.routes.auths import auth_bp
    from app.routes.tasks import tasks_bp
    app.register_blueprint(auth_bp) #calling 
    app.register_blueprint(tasks_bp)

    return app #returning the app
