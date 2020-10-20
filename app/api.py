import json
from app.models import Users, Ads, Variables, Ads_updates
from app import db
from flask import jsonify
from cal import Calendar
import datetime

def api(request):


    data = request.form
    params = request.args
    secret_key = int(Variables.query.get(1).value)


    try:
        if int(params['SECRET_KEY']) == secret_key:
            try:
                method = params['METHOD']
                # Update status method
                if method == 'update_status':

                    # Data existence check
                    try:
                        a = data['TRACK_CODE']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Track code expected'}), 400
                    try:
                        a = data['STATUS']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Status expected'}), 400
                    try:
                        a = data['COMMENT']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Status expected'}), 400
                    try:
                        a = data['AUTHOR']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Author expected'}), 400

                    # DB query
                    ad = Ads.query.filter_by(track=data['TRACK_CODE']).first()

                    # Check if ad with given tack_code exists
                    if ad:
                        # ad update
                        ad.status, ad.comment, ad.author = data['STATUS'], data['COMMENT'], data['AUTHOR']
                        update = Ads_updates(ad=ad, status=data['STATUS'], comment=data['COMMENT'],author=data['AUTHOR'])
                        db.session.add(update)
                        db.session.commit()
                        return json.dumps({'RESPONSE': 'ad {} updated successfully'.format(data['TRACK_CODE'])}), 200
                    else:
                        return json.dumps({'RESPONSE': 'ad does not exist'}), 200

                # Returns the array of ads
                # Makes all requested ads old
                if method == 'get_new_ads':
                    new = Ads.query.filter_by(new=True)

                    if new.first():
                        response = []
                        for new_add in new:
                            ad = {
                                'id': new_add.id,
                                'track_code': new_add.track_code,
                                'notify_email': new_add.notify_email,
                                'is_entity': new_add.is_entity,
                                'iin': new_add.iin,
                                'ogrn': new_add.ogrn,
                                'username': new_add.username,
                                'individual_phone_number': new_add.individual_phone_number,
                                'promocode': new_add.promocode,
                                'duration': new_add.duration,
                                'ad_type': new_add.ad_type,
                                'is_custom': new_add.is_custom,
                                'template_id': new_add.template_id,
                                'template_data': new_add.template_data,
                                'img_path': new_add.img_path,
                                'status': new_add.status,
                                'comment': new_add.comment,
                                'author': new_add.author,
                                'apply_date': str(new_add.apply_date),
                                'new': new_add.new,
                                'edited': new_add.edited
                            }
                            response.append(ad)
                            new_add.new = False
                            db.session.commit()
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no new ads'}), 200

                # Returns the array of old ads
                if method == 'get_old_ads':
                    new = Ads.query.filter_by(new=False)

                    if new.first():
                        response = []
                        for new_add in new:
                            ad = {
                                'id': new_add.id,
                                'track_code': new_add.track_code,
                                'notify_email': new_add.notify_email,
                                'is_entity': new_add.is_entity,
                                'iin': new_add.iin,
                                'ogrn': new_add.ogrn,
                                'username': new_add.username,
                                'individual_phone_number': new_add.individual_phone_number,
                                'promocode': new_add.promocode,
                                'duration': new_add.duration,
                                'ad_type': new_add.ad_type,
                                'is_custom': new_add.is_custom,
                                'template_id': new_add.template_id,
                                'template_data': new_add.template_data,
                                'img_path': new_add.img_path,
                                'status': new_add.status,
                                'comment': new_add.comment,
                                'author': new_add.author,
                                'apply_date': str(new_add.apply_date),
                                'new': new_add.new
                            }
                            response.append(ad)
                            new_add.new = False
                            db.session.commit()
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no old ads'}), 200

                # Returns the array of all ads
                if method == 'get_all_ads':
                    new = Ads.query.all()

                    if new:
                        response = []
                        for new_add in new:
                            ad = {
                                'id': new_add.id,
                                'track_code': new_add.track_code,
                                'notify_email': new_add.notify_email,
                                'is_entity': new_add.is_entity,
                                'iin': new_add.iin,
                                'ogrn': new_add.ogrn,
                                'username': new_add.username,
                                'individual_phone_number': new_add.individual_phone_number,
                                'promocode': new_add.promocode,
                                'duration': new_add.duration,
                                'ad_type': new_add.ad_type,
                                'is_custom': new_add.is_custom,
                                'template_id': new_add.template_id,
                                'template_data': new_add.template_data,
                                'img_path': new_add.img_path,
                                'status': new_add.status,
                                'comment': new_add.comment,
                                'author': new_add.author,
                                'apply_date': str(new_add.apply_date),
                                'new': new_add.new,
                                'edited': new_add.edited
                            }
                            response.append(ad)
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no ads'}), 200

                # Returns the array of edited ads
                if method == 'get_edited_ads':
                    new = Ads.query.filter_by(edited=True)

                    if new.first():
                        response = []
                        for new_add in new:
                            ad = {
                                'id': new_add.id,
                                'track_code': new_add.track_code,
                                'notify_email': new_add.notify_email,
                                'is_entity': new_add.is_entity,
                                'iin': new_add.iin,
                                'ogrn': new_add.ogrn,
                                'username': new_add.username,
                                'individual_phone_number': new_add.individual_phone_number,
                                'promocode': new_add.promocode,
                                'duration': new_add.duration,
                                'ad_type': new_add.ad_type,
                                'is_custom': new_add.is_custom,
                                'template_id': new_add.template_id,
                                'template_data': new_add.template_data,
                                'img_path': new_add.img_path,
                                'status': new_add.status,
                                'comment': new_add.comment,
                                'author': new_add.author,
                                'apply_date': str(new_add.apply_date),
                                'new': new_add.new,
                                'edited': new_add.edited
                            }
                            response.append(ad)
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no edited ads'}), 200

                # Returns an ad by the track_code
                if method == 'get_ad':

                    try:
                        a = data['TRACK_CODE']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Track code expected'}), 400

                    new = Ads.query.filter_by(track_code=data['TRACK_CODE']).first()

                    if new:
                        response = []
                        ad = {
                            'id': new.id,
                            'track_code': new.track_code,
                            'notify_email': new.notify_email,
                            'is_entity': new.is_entity,
                            'iin': new.iin,
                            'ogrn': new.ogrn,
                            'username': new.username,
                            'individual_phone_number': new.individual_phone_number,
                            'promocode': new.promocode,
                            'duration': new.duration,
                            'ad_type': new.ad_type,
                            'is_custom': new.is_custom,
                            'template_id': new.template_id,
                            'template_data': new.template_data,
                            'img_path': new.img_path,
                            'status': new.status,
                            'comment': new.comment,
                            'author': new.author,
                            'apply_date': str(new.apply_date),
                            'new': new.new,
                            'edited': new.edited
                        }
                        response.append(ad)
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no ad with {} track code'.format(data['TRACK_CODE'])}), 200

                # Returns the payment status of the ad
                if method == 'get_paid_status':

                    try:
                        a = data['TRACK_CODE']
                    except KeyError:
                        return json.dumps({'RESPONSE': 'Wrong data. Track code expected'}), 400

                    new = Ads.query.filter_by(track_code=data['TRACK_CODE']).first()

                    if new:
                        response = []
                        ad = {
                            'paid':new.paid
                        }
                        response.append(ad)
                        return json.dumps(response), 200
                    else:
                        return json.dumps({'RESPONSE': 'There is no ad with {} track code'.format(data['TRACK_CODE'])}), 200

            except KeyError:
                return json.dumps({'RESPONSE': 'Wrong method'}), 406
        else:
            return json.dumps({'RESPONSE': 'Auth error. Wrong secret_key'}), 401

    except KeyError:
        try:
            if data['method'] == 'get_calendar_date':
                print('get_calendar_date')
                try:
                    method = data['button']
                    cal = Calendar(datetime.datetime(2020, 10, 23, 10, 23, 32, 342))
                    resp = cal.get_calendar(datetime.date.today().month, datetime.datetime.today().year)
                    print('sent')
                    return jsonify({'response': resp})
                except KeyError:
                    return json.dumps({'response': 'Wrong method'}), 406

            if data['method'] == 'activate_promo':
                print('activate_promo')

                try:
                    method = data['button']
                    cal = Calendar()
                    resp = cal.get_calendar(data['month_n'], promo=data['promo'], year=data['year'])
                    print(resp['days'])
                    return jsonify({'response': resp})
                except KeyError:
                    return json.dumps({'response': 'Wrong method'}), 406

            if data['method'] == 'get_next_month':
                print('get_next_month')
                try:
                    method = data['button']
                    cal = Calendar()
                    resp = cal.get_calendar(int(data['month_n']) + 1, year=int(data['year']))
                    print(resp)
                    return jsonify({'response': resp})
                except KeyError:
                    return json.dumps({'response': 'Wrong method'}), 406

            if data['method'] == 'get_prev_month':
                print('get_prev_month')
                try:
                    method = data['button']
                    cal = Calendar()
                    resp = cal.get_calendar(int(data['month_n']) - 1, year=int(data['year']))
                    print(resp)
                    return jsonify({'response': resp})
                except KeyError:
                    return json.dumps({'response': 'Wrong method'}), 406

        except KeyError:
            return json.dumps({'RESPONSE': 'Auth error. No secret_key or token'}), 401
