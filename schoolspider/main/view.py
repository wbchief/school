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
        if login.password == password and login.flag == '1':
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

            flash('正在评估')
            spider = SchoolSpider(student_number, password)
            flag = spider.login_assess()
            flag = True
            if flag:
                flash('评估完成')
                username = session.get('username')

                result = Login.query.filter_by(username=username).update({'flag': '0'})
                print(result)
                db.session.commit()
                return redirect(url_for('login'))
            else:
                flash('评估失败，请重新评估')
                return render_template('index.html')

        return render_template('index.html')
    else:
        return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9999')