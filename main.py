from flask import request, make_response,redirect, render_template,session, url_for, flash
from flask_login import login_required, current_user


from app.firestore_service import get_users, get_todos, put_todo, delete_todo, update_todo
from app import create_app
from app.forms import todoForm, DeleteForm, UpdateForm

import unittest


# App init

app = create_app()


lista = ['hola 1','hola 2','hola 3','hola 4','adsada'] 

# Testing

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

# Error Handler

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

# Routes

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    #response.set_cookie('user_id',user_ip)
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET','POST'])
@login_required
def hello(user_ip=0,username='ss'):
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = todoForm()
    delete_form = DeleteForm()
    update_form = UpdateForm()

    context = {
        'user_ip': user_ip,
        'lista': get_todos(username),
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    }

    if todo_form.validate_on_submit():
        description = todo_form.description.data
        put_todo(description=description,user_name=username)

        flash('Tarea creada con exito')

        redirect(url_for('hello'))

    # users = get_users()
    #
    # for user in users:
    #     print(user.id)
    #     print(user.to_dict().get('password'))

    return render_template('hello.html',**context)


@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    update_todo(user_id, todo_id, done)

    return redirect(url_for('hello'))

# Run app


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)