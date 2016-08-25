#!/usr/bin/python 
#coding:utf-8


import MySQLdb as mysql
conn = mysql.connect(host="localhost",user="root",passwd="123456",db="reboot10",charset="utf8")
conn.autocommit(True)
cur = conn.cursor()

def check_user(user_dict,fields):
	result = {}
	sql = 'select %s from users where %s = "%s"' %(','.join(fields),user_dict.keys()[0],user_dict.values()[0])
	#print sql
	cur.execute(sql)
	res = cur.fetchone() # ===>对应结果为(u'cc', u'123456', u'sa', 1)
	for k,v in enumerate(fields):
		result[v] = res[k]
	return   result
'''
	##测试check_user函数的功能
user_dict = {'password': u'password', 'name': u'cc'}
fields = ['name','password','role','status']
#print user_dict.keys()
#print "*" * 40 
#print user_dict.values()
#print check_user({'id':1},['name','password','role','status'])
'''

def getall(fields):
	result = []
	sql = 'select %s from users ' %(','.join(fields))
	cur.execute(sql)
	res = cur.fetchall()	#===>对应结果为((u'admin', u'sa', 0), (u'cc', u'sa', 0))
	for x in res:
		mid = {}
		for k,v in enumerate(fields):
			mid[v] = x[k]
		result.append(mid)
	return   result


#fields = ['name','role','status']
#getall(fields)


def remove(id):
	sql = 'delete from users where id=%s ' %(id)
#	print sql
	cur.execute(sql)
	result = {'code':0,"errmsg":"delete success"}
	return  result



def add_user(respon):
	sql = "insert into users (%s) values ('%s')" %(','.join(respon.keys()),"','".join(respon.values()))
	sql = sql +';'
	#print sql
	cur.execute(sql)
	result = {'code':0,"errmsg":"added user success"}
	return result
	
#add_user({'mobile': u'zzzzz', 'status': u'zzzz', 'role': u'zzz', 'name': u'zzzz', 'email': u'zzz'})



def update_user(respon):
	data = ["%s='%s'" %(k,v) for k,v in respon.items()]	#==>字典转换为列表,高级用法
	print data
	sql = "update users set %s where id='%s';" %(','.join(data),respon["id"])
	print sql
	cur.execute(sql)
	result = {"code":0,"errmsg":"update success"}
	return result


#update_user({'mobile': u'bbbbbb', 'status': 1, 'role': u'zzzzzz', 'name': u'vv', 'email': u'aaa'},["id",8])

