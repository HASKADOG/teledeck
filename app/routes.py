from app import app, db
from flask import request, jsonify, render_template, redirect, url_for, flash
from app.api import api
from app.models import Users, Variables, Ads, Ads_updates, Time, Payment_history, Restore_tokens
from app.forms import LoginForm, RegistrationForm, ProcessPayment, RestorePassword, PasswordRestoration
from flask_login import current_user, login_user, logout_user
from yandex_checkout import Configuration, Payment
from notifier import send_email
from werkzeug.security import generate_password_hash
from config import Config
from datetime import timedelta
import datetime
from secrets import token_hex
import uuid
import base64
import json
import uuid



def convert_status(status):
    if status == 1:
        return 'Ожидает модерации'
    if status == 2:
        return 'Досылка документов'
    if status == 3:
        return 'Ожидает оплаты'
    if status == 4:
        return 'Транслируется'
    if status == 5:
        return 'Завершено'
    if status == 6:
        return 'Отклонено'
    if status == 7:
        return 'Отменено'
    if status == 8:
        return 'Отменено с возвратом'
    if status == 31:
        return 'Оплачено'
    if status == 71:
        return 'Ожидает отмены'


@app.route('/api', methods=['POST'])
def hello():
    return api(request)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('main.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    incorrect = ''
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            print('Invalid username or password')
            incorrect = '<script>alert("Неверный email или пароль");</script>'

            return render_template('login.html', title='Sign In', form=form, incorrect=incorrect)
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, incorrect=incorrect)


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    try:
        if request.args['ref_code']:
            ref_code = request.args['ref_code']
        else:
            ref_code = ''
    except:
        ref_code = ''
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    print('bbbb')
    if form.validate_on_submit() and form.submit.data:
        print('aaaaa')
        collected = 0
        if form.ref_code.data != '':
            ref_master = Users.query.filter_by(ref_code=form.ref_code.data).first()
            if ref_master:
                ref_master_id = ref_master.id
                collected = int(Variables.query.filter_by(name = 'REF_REG_BONUS').first().value)
            else:
                ref_master_id = None
                collected = 0

        else:
            ref_master_id = None

        user = Users(username=form.login.data, second_name=form.second_name.data, third_name=form.third_name.data,
                     password_hash=form.password.data, email=form.email.data, phone_number=form.phone_number.data,
                     is_entity=form.is_entity.data, entity_name=form.entity_name.data, iin=form.iin.data,
                     ogrn=form.ogrn.data, ref_master_code=form.ref_code.data, ref_master=ref_master_id, register_date=datetime.datetime.now(),
                     status='user', ref_code=token_hex(3), collected_m=collected)

        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        print('done')
        print(form.email.data)
        send_email(form.email.data, 'Ваш аккаунт на теледоска.рф успешно зарегистрирован!')

    return render_template('registration.html', title='Registration', form=form, ref_code=ref_code)


@app.route('/add_add', methods=['GET', 'POST'])
def add_add():
    print('1')

    if current_user.is_authenticated:
        user = Users.query.get(current_user.id)
        if user.ref_master:
            master = Users.query.get(user.ref_master)
            discount = Variables.query.get(2).value #REFFERAL_D
            reffered = True
        else:
            reffered = False
    else:
        reffered = False
        user = False


    # times = Time.query.filter_by(taken=False).all()
    if request.method == 'POST' and request.form['moderate'] == 'true':
        print('ad_add')
        data = request.form
        track_code = token_hex(3)
        username = None if data['username'] == 'None' else data['username']
        second_name = None if data['second_name'] == 'None' else data['second_name']
        third_name = None if data['third_name'] == 'None' else data['third_name']
        phone_number = data['phone_number']
        notify_email = data['notify_email']
        is_entity = False if data['is_entity'] == '0' else True
        time = data['time']
        entity_name = data['entity_name']
        iin = None if data['iin'] == '' else data['iin']
        ogrn = None if data['ogrn'] == '' else data['ogrn']
        promo = data['promo']
        price = int(data['price'])
        if reffered:
            masters_s = int(price * (1 - (100-int(discount))/100))
            print(masters_s)


        template_data = {
            "head": data['head'],
            "body": data['body'],
            "legs": data['legs']
        }

        img = data['image'].split(',')[1]
        with open('/home/haska/Work/teledeck/app/static/users_ads/{}.png'.format(track_code), "wb") as fh:
            fh.write(base64.decodebytes(bytes(img, 'utf-8')))
        print(img)
        a = 2
        if user:
            new_ads = Ads(track=track_code, new=True, price=price, time=time, entity_name=entity_name,
                          username=username,
                          second_name=second_name, third_name=third_name, individual_phone_number=phone_number,
                          notify_email=notify_email, is_entity=is_entity, iin=iin, ogrn=ogrn, promocode=promo, apply_date=datetime.datetime.now(),
                          template_data=json.dumps(template_data), status=1, user=user, masters_money= masters_s if reffered else None, ref_master_id=master.id if reffered else None)
        else:
            new_ads = Ads(track=track_code, new=True, price=price, time=time, entity_name=entity_name,
                          username=username,
                          second_name=second_name, third_name=third_name, individual_phone_number=phone_number,
                          notify_email=notify_email, is_entity=is_entity, iin=iin, ogrn=ogrn, promocode=promo, apply_date=datetime.datetime.now(),
                          template_data=json.dumps(template_data), status=1,  masters_money= masters_s if reffered else None, ref_master_id=master.id if reffered else None)


        db.session.add(new_ads)
        db.session.commit()
        # db.session.add(time_to)
        db.session.commit()
        send_email(notify_email, 'Объявление {} успешно создано! После модерации Вам поступит уведомление'.format(track_code))
        return jsonify({'response': 'Отправлено на модерацию. Трек-код: {}'.format(track_code)})

    curr = current_user
    if current_user.is_authenticated:
        if curr.iin is None:
            curr.iin = ''
        else:
            curr.iin = current_user.iin

        if curr.ogrn is None:
            curr.ogrn = ''
        else:
            curr.ogrn = current_user.ogrn

    a = 1

    return render_template('test.html', current_user=curr)


@app.route('/lk', methods=['GET', 'POST'])
def lk():
    if current_user.is_anonymous:
        return redirect(url_for('login'))

    user = Users.query.get(current_user.id)
    users_ads = user.ads.all()
    to_page = []
    for ad in users_ads:
        if ad.status == 1:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a href="/edit/{}" id="action_one" class="get_add">{}</a> <a id="action_two" href="/cancel/{}" class="get_add">{}</a> </div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление',
                                 ad.track,
                                 'Отменить объявление')
            to_page.append(ad_el)

        if ad.status == 3:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/do_payment/{}" class="get_add">{}</a> <a href="/edit/{}" id="action_two" class="get_add">{}</a> <button id="action_three" class="get_add">{}</button><a id="action_four" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Оплатить объявление', ad.track,
                                 'Изменить объявление', 'Продлить объявление', ad.track, 'Отменить объявление')
            to_page.append(ad_el)

        if ad.status == 2:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a><a id="action_two" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление',
                                 ad.track,
                                 'Отменить объявление')
            to_page.append(ad_el)

        if ad.status == 4:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/cancel/{}" class="get_add">{}</a><a id="action_two" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Отменить объявление',
                                 ad.track,
                                 'Продлить объявление')
            to_page.append(ad_el)

        if ad.status == 5:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Продлить объявление')
            to_page.append(ad_el)

        if ad.status == 6:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            to_page.append(ad_el)

        if ad.status == 7:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            to_page.append(ad_el)

        if ad.status == 8:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            to_page.append(ad_el)

        if ad.status == 31:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Отменить объявление')
            to_page.append(ad_el)

        if ad.status == 71:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/moderate/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Вернуть на модерацию')
            to_page.append(ad_el)

    if request.method == 'POST' and request.form['update_lk'] == 'true':
        data = request.form

        user = Users.query.get(current_user.id)
        user.username = None if data['username'] == 'None' else data['username']
        user.second_name = None if data['second_name'] == 'None' else data['second_name']
        user.third_name = None if data['third_name'] == 'None' else data['third_name']
        user.phone_number = data['phone_number']
        user.email = data['email']
        user.is_entity = False if data['is_entity'] == 'False' else True
        user.entity_name = data['entity_name']
        user.iin = None if data['iin'] == '' else data['iin']
        user.ogrn = None if data['ogrn'] == '' else data['ogrn']

        db.session.add(user)
        db.session.commit()
        send_email(user.email, 'Ваш аккаунт на теледоска.рф успешно обновлен')
        print()
        return jsonify({'response': 'Успешно обновлено!'})

    return render_template('lk.html', user=current_user, users_ads=to_page)


@app.route('/payment', methods=['POST', 'GET'])
def payment():
    if request.method == 'POST' and request.form['get_ad'] == 'true':
        print('2')
        ad = Ads.query.filter_by(track=request.form['track_code']).first()
        if ad.status == 1:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a href="/edit/{}" id="action_one" class="get_add">{}</a> <a id="action_two" href="/cancel/{}" class="get_add">{}</a> </div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление', ad.track,
                                 'Отменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 3:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/do_payment/{}" class="get_add">{}</a> <a href="/edit/{}" id="action_two" class="get_add">{}</a> <button id="action_three" class="get_add">{}</button><a id="action_four" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Оплатить объявление',  ad.track,
                                 'Изменить объявление', 'Продлить объявление', ad.track, 'Отменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 2:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a><a id="action_two" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление', ad.track,
                                 'Отменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 4:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/cancel/{}" class="get_add">{}</a><a id="action_two" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Отменить объявление', ad.track,
                                 'Продлить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 5:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Продлить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 6:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 7:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 8:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/edit/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Изменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 31:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/cancel/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Отменить объявление')
            return jsonify({'ad': ad_el})

        if ad.status == 71:
            ad_el = ' <div class="ads"> <div class="ad"> <div class="bread_crumbs"> <span class="track_code"> Трек номер: {} </span> <span class="status"> Статус: {} </span> </div> <hr> <div class="image_body"> <img src="/static/users_ads/{}.png" alt=""> </div> <hr style="margin-top: 10px !important; margin-bottom: 0 !important"> <div class="actions_ads"> <a id="action_one" href="/moderate/{}" class="get_add">{}</a></div> </div> </div>'
            ad_el = ad_el.format(ad.track, convert_status(ad.status), ad.track, ad.track, 'Вернуть на модерацию')
            return jsonify({'ad': ad_el})

    return render_template('payment.html', user=current_user)


@app.route('/do_payment/<track_code>', methods=['POST', 'GET'])
def do_payment(track_code):
    ad = Ads.query.filter_by(track=track_code).first()
    form = ProcessPayment()

    if current_user.is_authenticated:
        user = Users.query.get(current_user.id)

        if ad in user.ads.all():
            is_own = True
        else:
            is_own = False
    else:
        is_own = False

    if form.validate_on_submit() and form.submit.data:

        Configuration.account_id = Variables.query.get(3).value
        Configuration.secret_key = Variables.query.get(4).value

        print(form.waste.data)


        payment = Payment.create({
            "amount": {
                "value": int(ad.price) - int(current_user.collected_m) if form.waste.data else ad.price,
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://vk.com/id608742663"
            },
            "capture": True,
            "description": "Оплата объявления {}".format(ad.track),
            "metadata": {
                "track": ad.track,
                "bonus_used": 1 if form.waste.data else 0,
                "payer": current_user.id if is_own else 'unregistered user'
            }
        }, uuid.uuid4())



        print('передано в оплату')
        return redirect(payment.confirmation.confirmation_url)
    return render_template('do_payment.html', form=form, ad=ad, is_own = is_own, current_user=current_user, price_btn_text='Оплатить {}₽'.format(ad.price))



@app.route('/edit/<track_code>', methods=['POST', 'GET'])
def edit(track_code):
    ad = Ads.query.filter_by(track=track_code).first()

    added_days = []
    for ime in ad.time[:-1].split(','):
        added_days.append([ime.replace('_', '.'), '{}_picked'.format(ime)])
    print(ad.price)
    template_data = json.loads(ad.template_data)
    print(template_data)

    if request.method == 'POST' and request.form['moderate'] == 'true':
        data = request.form
        ad.username = None if data['username'] == 'None' else data['username']
        ad.second_name = None if data['second_name'] == 'None' else data['second_name']
        ad.third_name = None if data['third_name'] == 'None' else data['third_name']
        ad.individual_phone_number = data['phone_number']
        ad.notify_email = data['notify_email']
        ad.is_entity = False if data['is_entity'] == '0' else True
        ad.time = data['time']
        ad.entity_name = data['entity_name']
        ad.iin = None if data['iin'] == '' else data['iin']
        ad.ogrn = None if data['ogrn'] == '' else data['ogrn']
        ad.promoсode = data['promo']
        ad.price = int(data['price'])
        ad.template_data = json.dumps({
            "head": data['head'],
            "body": data['body'],
            "legs": data['legs']
        })
        ad.edited = True
        ad.status = 1

        db.session.add(ad)
        db.session.commit()

        return jsonify({'response': 'Изменено и отправено на модерацию'})

    return render_template('edit.html', ad=ad, days=added_days, template_data=template_data)


@app.route('/approve_payment', methods=['POST', 'GET'])
def approve():
    if request.json['type'] == 'notification' and request.json['event'] == 'payment.succeeded':
        paid_ad = Ads.query.filter_by(track=request.json['object']['metadata']['track']).first()
        history = Payment_history(date = datetime.datetime.now(), sum = request.json['object']['amount']['value'].split('.')[0], payment = paid_ad)

        if paid_ad.ref_master_id:
            master = Users.query.get(int(paid_ad.ref_master_id))
        else:
            master = False

        if request.json['object']['metadata']['bonus_used'] == '1':
            user = Users.query.get(request.json['object']['metadata']['payer'])
            user.collected_m = 0
            paid_ad.bonus_used = True
            db.session.add(user)
            db.session.commit()

        if master:
            master.collected_m += paid_ad.masters_money
            db.session.add(master)
            db.session.commit()
        paid_ad.paid = 1
        paid_ad.status = 31
        db.session.add(paid_ad)
        db.session.commit()
        db.session.add(history)
        db.session.commit()
        send_email(paid_ad.notify_email, 'Оплата объявления {} на сумму {}₽ прошла успешно'.format(request.json['object']['metadata']['track'], request.json['object']['amount']['value'].split('.')[0]))
        print()
        print('payment.succeeded')
        a = 1
        b = 2
    return jsonify({'response': 'thanks'}), 200

@app.route('/cancel/<track>', methods=['POST', 'GET'])
def cancel(track):
    ad = Ads.query.filter_by(track=track).first()
    ad.status = 71
    db.session.add(ad)
    db.session.commit()
    send_email(ad.notify_email,'Объявление {} ожидает отмены'.format(ad.track))
    print('{} canceled'.format(ad.track))
    return redirect(url_for('payment'))

@app.route('/moderate/<track>', methods=['POST', 'GET'])
def moderate(track):
    ad = Ads.query.filter_by(track=track).first()
    ad.status = 1
    db.session.add(ad)
    db.session.commit()
    send_email(ad.notify_email, 'Объявление {} возвращено на модерацию'.format(ad.track))
    return redirect(url_for('payment'))

@app.route('/restore_password', methods=['POST', 'GET'])
def restore_password():
    form = RestorePassword()
    incorrect = ''

    try:
        if request.args['msg']:
            incorrect = '<script>alert("{}");</script>'.format(request.args['msg'])
            return render_template('restore_password.html', form=form, incorrect=incorrect)
        else:
            ref_code = ''
    except:
        ref_code = ''

    if form.validate_on_submit() and form.submit.data:
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            now = datetime.datetime.now()
            hex = token_hex(16)
            token = Restore_tokens(date_expires=now + timedelta(days=1), token=hex, account_to_restore=user)
            db.session.add(token)
            db.session.commit()
            send_email(user.email, 'Ссылка для восстановления пароля: https://теледоска.рф/password_restoration/{}'.format(hex))
            incorrect = '<script>alert("Ссылка на восстановление пароля отправлена на Вашу почту");</script>'
            return render_template('restore_password.html', form=form, incorrect=incorrect)
        else:
            incorrect = '<script>alert("Неверный email");</script>'
        return render_template('restore_password.html', form=form, incorrect=incorrect)
    return render_template('restore_password.html', form=form, incorrect=incorrect)

@app.route('/password_restoration/<token>', methods=['POST', 'GET'])
def password_restoration(token):
    form = PasswordRestoration()

    incorrect = ''

    restoration_token = Restore_tokens.query.filter_by(token=token).first()
    if restoration_token:
        if restoration_token.date_expires < datetime.datetime.now():
            return redirect('/restore_password?msg=Запрос на восстановление истек')
    else:
        return redirect('/restore_password?msg=Неверная ссылка')

    if form.validate_on_submit() and form.submit.data:
        user = Users.query.get(restoration_token.acc_to_restore)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template('password_restoration.html', form = form, incorrect = incorrect)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect(url_for('index'))
