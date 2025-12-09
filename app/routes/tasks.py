from flask import Blueprint, render_template, session, redirect, url_for, flash, request
from app import db 
# from app.routes import auths
# importing database object to save task and remove tasks

from app.models import Task
 # task is a model class where we will store the tasks

tasks_bp = Blueprint("task", __name__) #ceating blueprint, "task"-> name of bluepring

@tasks_bp.route("/") #to view the tasks
def view_task():
    if 'user' not in session: #if user is not login
        return redirect(url_for("auth.login")) 
    
    tasks = Task.query.all() #patching all the tasks 
    return render_template('tasks.html', task_list=tasks) #sending tasks to tasks.html

@tasks_bp.route("/add", methods=["POST"]) # To add task, post -> becouse user will send something
def add():
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    title = request.form.get("title") #title of the task ,that user wants to add
    if title:
        new_task = Task(title=title, status='Pending') #title(variable of title)=title(new task)
        db.session.add(new_task) #added
        db.session.commit() #saving
        flash('Task added successfully', 'success')

    return redirect(url_for('task.view_task'))

@tasks_bp.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == 'Pending':
            task.status = 'Working'
        elif task.status == 'Working':
            task.status = 'Done'
        else:
            task.status = 'Pending'
        db.session.commit()
    return redirect(url_for('task.view_task'))

@tasks_bp.route('/clear', methods=["POST"])
def clear_tasks():
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'info')
    return redirect(url_for('task.view_task'))
