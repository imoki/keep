import requests
import random
import linecache
import schedule
import time

url = "https://bark服务器地址"	# 自己的bark服务器地址

'''
def randomline():
	count = len(open('./bark.txt','r', encoding='utf-8').readlines())	#获取行数
	num=random.randrange(1,count, 1)	#生成随机行数
	return linecache.getline('./bark.txt',num)	#随机读取某行

def bark(line):
	response = requests.get(url + line)	#用导入的request模块的get方法访问URL
	#print(response.status_code)	#状态码
	#print(response.text)
'''

def job():
	count = len(open('./bark.txt', 'r', encoding='utf-8').readlines())#获取行数
	num = random.randrange(1, count, 1)#生成随机行数
	response = requests.get(url + linecache.getline('./bark.txt', num))#用导入的request模块的get方法访问URL
	#print(response.status_code)#调用response里的status_code方法查看状态码

schedule.every(3).minutes.do(job)	# 每3分钟执行一次job函数

if __name__ == "__main__":
	while True:
		schedule.run_pending()	# 启动服务
		time.sleep(1)