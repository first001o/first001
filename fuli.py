#encoding: utf-8
from flask import Flask,session,redirect,request,url_for,render_template
from exts import db
from models import *
import config
import os
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

maindir = '/root/myflask/fuli/static/images'
@app.route('/')
def index():
    def get_dirs(maindir):
        for root, dirs, files in os.walk(maindir):
            return dirs
    dirlist = get_dirs(maindir)
    imglist = []
    for dir in dirlist:
        path = os.path.join(maindir, dir)
        dict1 = {}
        dict1['dirname'] = dir.decode("utf-8")
        dict1['filelist'] = os.listdir(path)
        imglist.append(dict1)

    return render_template('index.html',imglist=imglist)


@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone==telephone,
                User.password==password).first()
        if user:
            session['user_id'] = user.id
            return  redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    return redirect(url_for('login'))
@app.route('/regist/',methods=['GET','POST'])
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        print telephone,username,password2,password1
        if not username :
            return u'不能为空'
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return u'该手机已经注册！！'
        if password1 == password2:
            user = User(telephone=telephone,username=username,password=password1)
            db.session.add(user)
            db.session.commit()
            return  redirect(url_for('login'))
        else:
            return u'两次输入密码不一致！！！'


@app.route('/detail/<picture_name>',methods=['GET','POST'])
def detail(picture_name):
    picture_dir = os.path.join(maindir,picture_name)
    picture_list = os.listdir(picture_dir)
    return render_template('detail.html',picture_name=picture_name,picture_list=picture_list)

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    user = User.query.filter(User.id == user_id).first()
    if user:
        return {'user':user}
    else:
        return {}


if __name__ == '__main__':
    app.run()
