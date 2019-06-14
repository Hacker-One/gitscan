#!/usr/bin/python
# _*_ coding: utf-8 _*_

import requests
											#
headers = {
	"Authorization": "token 716267814956960e00cf0cc63d684b5d9015e771",
	"User-Agent": "Awesome-Octocat-App"
}


proxies = {
    "http": "http://127.0.0.1:6666",
    "https": "https://127.0.0.1:6666",
}

'''
Api_interfaces:{
	"Get_Token_AccessNumber":"https://api.github.com/rate_limit?access_token={token}"				#获取token还有多少次数
	"Get_All_Users":"https://api.github.com/users",													#获取所有用户
	"Get_User_Info":"https://api.github.com/users/{username}",										#获取用户基本信息
	_"Get_User_Followers":"https://api.github.com/users/{username}/followers",						#获取跟踪该用户的用户列表
	_"Get_User_Following":"https://api.github.com/users/{username}/following",						#获取该用户跟踪的其他用户列表
	_"Get_User_Gists":"https://api.github.com/users/{username}/gists",
	_"Get_User_Organizations":"https://api.github.com/users/{username}/orgs",						#获取用户的组织信息
	_"Get_User_Events":"https://api.github.com/users/{username}/events",							#获取该用户操作事件信息
	_"Get_User_Received_Events":"https://api.github.com/users/{username}/events",					#获取该用户接受到的事件信息
	_"Get_User_Starred":"https://api.github.com/users/{username}/starred",							#获取用户喜欢的项目列表
	_"Get_User_Subscriptions":"https://api.github.com/users/{username}/subscriptions",				#获取用户订阅的仓库列表
	"Get_User_All_Repos":"https://api.github.com/users/{username}/repos",							#获取用户所有仓库
	"Get_User_Repo_Info":"https://api.github.com/repos/{username}}/{repo}",							#获取用户仓库信息
	"Get_User_Repo_Commits":"https://api.github.com/repos/{username}/{repo}/commits",				#获取用户仓库的提交记录
	"":"",
	"":"",
	"":"",
}

Api_parameter:{
	"page":"获取第几页",
	"per_page":"每页查询条数",
	"sha":"查询分支",
}
'''
# rsp = requests.get('https://api.github.com/users',headers=headers,proxies=proxies,verify=False)
# for i in xrange(100):
rsp = requests.get('https://api.github.com/users',headers=headers)
print rsp.content