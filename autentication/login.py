from flask import Blueprint, render_template, redirect, request, url_for
from app import db
from flask_login import login_required, current_user
from models.models import User

login = Blueprint('login', __name__)


@login.route('/')
def index():
    admin = False
    if current_user.is_authenticated:
        admin = current_user.admin
    return render_template('index.html', admin=admin)


def is_admin(id):
    user = User.query.get_or_404(id)
    if user.admin:
        return True
    else:
        return False


@login.route('/usuarios')
@login_required
def usuarios():
    if is_admin(current_user.id):
        users = User.query.order_by(User.id).all()
        return render_template('users.html', users=users, admin=current_user.admin)
    else:
        return redirect(url_for('login.index'))


@login.route('/del/<int:id>')
@login_required
def del_user(id):
    if is_admin(current_user.id):
        user_to_del = User.query.get_or_404(id)
        try:
            db.session.delete(user_to_del)
            db.session.commit()
            return redirect('/registros')
        except:
            return 'Houve um problema ao deletar!'
    else:
        return redirect(url_for('login.index'))


@login.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    if is_admin(current_user.id):
        user = User.query.get_or_404(id)

        if request.method == 'POST':
            user.admin = True if request.form.get('admin') else False
            try:
                db.session.commit()
                return redirect('/usuarios')
            except:
                return 'Ocorreu um erro ao atualizar o usuário'
        else:
            return render_template('update.html', user=user, admin=current_user.admin)
    else:
        return redirect(url_for('login.index'))
