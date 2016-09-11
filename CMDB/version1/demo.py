#!/usr/bin/python 
#coding:utf-8
from flask import Flask ,render_template,request 

app = Flask(__name__)

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
		fields = ['name','password','role','status']
		password = check_user({'name':login_info['name']},key='password')	#传字典时只将name值传到后端查询下.需要查询的结果可以通过列表key传到后端进行查询后操作.


if __name__=='__main__':
	app.run(host='0.0.0.0',port=1000,debug=True)
