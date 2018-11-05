import random
import time

from flask import current_app
from flask import flash
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask_login import current_user
from werkzeug.utils import redirect

from schoolspider import create_app, db
from schoolspider.models import Login
from schoolspider.sspider.spider import SchoolSpider

app = create_app('testing')



@app.route('/login/', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        form = request.form.to_dict()
        username = form.get('username')
        password = form.get('password')
        login = Login.query.filter_by(username=username).first()
        if login.password == password and login.flag != '0':
            session['logined_in'] = True
            session['username'] = username
            print('--------------')
            return redirect(url_for('assess'))

    return render_template('hello.html')


@app.route('/assess/', methods=['GET', 'POST'])
def assess():
    '''
    评估输入
    :return:
    '''
    print(session.get('logined_in'))
    if session.get('logined_in'):
        print('++++')
        if request.method == 'POST':
            form = request.form.to_dict()
            student_number = form.get('username')
            password = form.get('password')
            print(form)
            username = session.get('username')

            flash('正在评估')

            user = Login.query.filter_by(username=username).first()
            # print(user)
            # print(user.flag)
            # if user.flag == '2':
            #     result = Login.query.filter_by(username=username).update({'counts': user.counts + 1})
            # else:
            #     result = Login.query.filter_by(username=username).update({'flag': '0'})
            # print(result)
            # flash('评估完成')
            # db.session.commit()
            spider = SchoolSpider(student_number, password)
            classes = spider.login_assess()
            print(classes)
            data = ""
            if classes:
                for value in classes[1:]:
                    print(value)
                    if spider.assess(value):
                        data += value.get('name') + ', '
                    else:
                        flash(value.get('name'), '评估失败')
                    time.sleep(1)
                user = Login.query.filter_by(username=username).first()
                if user.flag == '2':
                    result = Login.query.filter_by(username=username).update({'counts': user.counts + 1})
                else:
                    result = Login.query.filter_by(username=username).update({'flag': '0'})
                flash(data + '  已完成评估，请核对一下哦')
                flash('评估完成')
                db.session.commit()
            else:
                flash('对不起哦，本次评估失败，请一会尔重试一下呗')
            spider.driver.close()

        flash('评估会需要一小会时间哦')
        return render_template('index.html')
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')