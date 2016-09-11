#coding:utf-8
from flask import Flask,request,render_template,redirect
import json 
from db import modpasswd,checkuser,delete,adduser,modfiy,userlist,getone

app = Flask(__name__)

app.secret_key = "123.com"

'''登录页面login'''
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        login_info = dict((k,v[0]) for k,v in dict(request.form).items())
        if not checkuser({"name":login_info["name"]},"name"):
            return json.dumps({"code":1,"errmsg":"user is not exist"})
        if login_info["password"] != checkuser({'name':login_info["name"]})[0]:
            return json.dumps({"code":1,"errmsg":"password error"})
	u_role = checkuser({"name":login_info["name"]},"role")	
    	session["username"] = login_info["name"]
    	session["role"] = u_role
    	return json.dumps({"code":0,"result":"login success"})



if __name__=="__main__":
	app.run(host='0.0.0.0',port=1010,debug=True)
