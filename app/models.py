from app import db 

class Task(db.Model): #db.model -> telling that convert this class with an actual database
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    status = db.Column(db.String(20), default = "Pending")
