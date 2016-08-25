#!/usr/bin/python 
#coding:utf-8
from flask import Flask ,render_template,request 
from db import *

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
	#	print request.method
	#	print request.form	#结果为===>ImmutableMultiDict([('password', u'123'), ('name', u'123')])
		login_info = dict((k,v[0]) for k,v in dict(request.form).items())
	#	print login_info	#结果为==>{'password': u'123', 'name': u'123'}
	#	print login_info.keys()
		fields = ['name','id','password','role','status']
		re = check_user({'name':login_info['name']},fields)	#传字典时只将name值传到后端查询下.需要查询的结果可以通过列表key传到后端进行查询后操作.
	#	print re
		if not re:
			return render_template("login.html",mes={"code":1,"errmsg":"用户名不存在"})
		if re['password'] == login_info['password'] :
			 reTmp = getall(fields)
			 return render_template("userlist.html",result=reTmp ,mes={"code":0,"errmsg":"登陆成功"})
		else :
			return render_template("login.html",mes={"code":1,"errmsg":"用户名或者密码错误"})



@app.route("/userlist")
def userlist():
	fields = ['name','password','role','status']
	reTmp = getall(fields)
	return render_template("userlist.html",result=reTmp,mes={"code":0,"errmsg":"userlist"})


@app.route("/update" , methods=['GET','POST'])
def update():
	fields = ['name','id','mobile','email','role','status']
	if request.method == 'GET':
		id =  request.args.get("id") 
		re = check_user({'id':id},fields)
		print request.method
		print re
		return render_template("update.html",users=re ,mes = {"code":1,"errmsg":"update"})
	if request.method == 'POST':
		fields = ['name','mobile','email','role','status']
		update_info = dict((k,v[0]) for k,v in dict(request.form).items())
		print request.method
		print update_info 
		result =update_user(update_info)
		return render_template("update.html",users={} ,mes = result)



@app.route("/delete")
def delete():
	fields = ['name','id','mobile','email','role','status']
	id =  request.args.get("id") 
	print id
	re = remove(id)
	return render_template("delete.html",mes = re)

@app.route("/useradd",methods=['GET','POST'])
def useradd():
	if request.method == 'GET':
		return render_template("useradd.html",users={},mes = {"code":0,"errmsg":" get page useradd"})
	if request.method == 'POST':
		add_info = dict((k,v[0]) for k,v in dict(request.form).items())
		print add_info  #====>{'mobile': u'zzzzz', 'status': u'zzzz', 'role': u'zzz', 'name': u'zzzz', 'email': u'zzz'}
		respon = add_user(add_info)
		return render_template("userlist.html",users=respon,mes = {"code":0,"errmsg":"useradd"})
	


if __name__=='__main__':
	app.run(host='0.0.0.0',port=2021,debug=True)
