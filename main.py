from flask import render_template, request, redirect, url_for, Blueprint
from models.models import Register, db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/atendimento', methods=['POST', 'GET'])
def atendimento():
    if request.method == 'POST':
        contact = request.form['contact']
        channel = request.form['channel']
        attendance = request.form['attendance']
        associate = request.form['associate']
        demand = request.form['demand']
        product_offer = request.form['product_offer']
        product = request.form['product'] if product_offer == 'Sim' else ''
        effective = request.form['effective'] if product_offer == 'Sim' else ''
        time_spent = request.form['time_spent']
        time_hour = request.form['time_hour']
        new_register = Register(contact=contact, channel=channel, attendance=attendance, associate=associate,
                                demand=demand, product_offer=product_offer, product=product, effective=effective,
                                time_spent=time_spent, time_hour=time_hour, manager_id=current_user.id)
        try:
            db.session.add(new_register)
            db.session.commit()
            return redirect(url_for('login.index'))
        except:
            return "Houve um problema ao registrar!"
    else:
        return render_template('index.html')


@main.route('/delete/<int:id>')
def delete(id):
    register_to_del = Register.query.get_or_404(id)
    try:
        db.session.delete(register_to_del)
        db.session.commit()
        return redirect('/registros')
    except:
        return 'Houve um problema ao deletar!'


@main.route('/registros')
@login_required
def registro():
    registers = Register.query.order_by(Register.id).all()
    return render_template('registros.html', registers=registers, name=current_user.name, admin=current_user.admin)
