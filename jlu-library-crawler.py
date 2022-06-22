from urllib import request
from urllib import parse
from time import sleep
from http import cookiejar
from tqdm import tqdm
import requests
import random
import json
from hashlib import md5
import math
import urllib.request
import random
from bs4 import BeautifulSoup
import time
import sys
import os
def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now =  time.localtime()
    now_time = time.strftime("%Y_%m_%d_%H_%M_%S", now)
    # now_time = time.strftime("%Y-%m-%d ", now)
    return now_time
# 拼接URL地址
def get_url(word):
  url = 'https://ss.zhizhen.com/s?{}'
  #此处使用urlencode()进行编码
  params = parse.urlencode({'sw':word})
  url = url.format(params)
  return url
# 发请求,保存本地文件
def request_html(url):
  headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39','Cookie':cookieStr}
  
  # 请求对象 + 响应对象 + 提取内容
  request = urllib.request.Request(url=url,headers=headers)
  return request
def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()
if __name__ == '__main__':
    appid = ''
    appkey = ''
    baiduheaders = {'Content-Type': 'application/x-www-form-urlencoded'}
    # For list of language codes, please refer to `https://api.fanyi.baidu.com/doc/21`
    from_lang = 'en'
    to_lang =  'zh'

    endpoint = 'http://api.fanyi.baidu.com'
    path = '/api/trans/vip/translate'
    baiduurl = endpoint + path
    now_time = get_now_time()
    print("             吉大图书馆爬虫工具v1.1                ")
    print("**************************************************")
    print("*这是一个图书馆爬虫工具,用于爬取标题和对应的摘要 *")
    print("*请尽量减少爬取数量,减少图书馆服务器负载         *")
    print("*             请按照提示输入                     *")
    print("**************************************************")
    print("初始化……")
    #m=0
    url='https://ss.zhizhen.com'
    headers = {
        'User-Agent': 'Mozilla/5.0(Windows NT 10.0; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3427.400 QQBrowser/9.6.12513.400'
    }
    cookie = cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(url)
 
    cookieStr = ''
    for item in cookie:
        cookieStr = cookieStr + item.name + '=' + item.value + ';'
    

    word= input('请输入搜索内容:')
    #print("是否翻译摘要？翻译会严重影响爬取速度（约原速度的7%），翻译输入“1”，不翻译输入“2”")

    numb=1
    j=0
    


    
    boshi= "&strdegree=3"
    qikan= "&strchannel=1%2C2"
    zhuanli="&strchannel=1%2C2%2C10%2C19&strdegree=3"
    year1 = "&stryear=8"
    year2= "&stryear=8%2C9"
    year3 = "&stryear=8%2C9%2C10"
    year4= "&stryear=8%2C9%2C10%2C11"
    year5= "&stryear=8%2C9%2C10%2C11%2C12"

    print("请选择你要查询的文献类别:1:期刊;2:期刊+博士论文;3:期刊+博士论文+专利")
    leibie=input("请输入“1”或“2”或“3”:")
    while leibie not in["1","2","3"]:
        print("输入错误，请重新输入")
        leibie=input("请输入“1”或“2”或“3”:")
    if leibie==str(1):
        url=get_url(word)+qikan
        name="期刊"
    elif leibie==str(2):
        url=get_url(word)+qikan+boshi
        name="期刊+博士"
    elif leibie==str(3):
        url=get_url(word)+zhuanli
        name="期刊+博士+专利"
    else:
        pass
    print("请选择你要查询的年份:5:最近5年;4:最近4年;3:最近3年;2:最近2年;1:最近1年")    
    nianfen= input("请输入“1”或“2”或“3”或4或“5”:")
    while nianfen not in["1","2","3","4","5"]:
        print("输入错误，请重新输入")
        nianfen=input("请输入“1”或“2”或“3”或4或“5”:")
    if nianfen==str(1):
        url=url+year1
        #print(url)
        name=name+"2022"
        print("你输入的是1")
    elif nianfen==str(2):
        url=url+year2
        name=name+"2022+2021"
        #print(url)
        print("你输入的是2")
    elif nianfen==str(3):
        url=url+year3
        name=name+"2022+2021+2020"
        #print(url)
        print("你输入的是3")
    elif nianfen==str(4):
        url=url+year4
        name=name+"2022+2021+2020+2019"
        #print(url)
        print("你输入的是4")
    elif nianfen==str(5):
        url=url+year5
        name=name+"2022+2021+2020+2019+2018"
        #print(url)
        print("你输入的是5")
    else:
        pass
    request=request_html(url)
    html = urllib.request.urlopen(request).read().decode('utf8')
    soup = BeautifulSoup(html,'html.parser')
    shuliang = soup.select('div.searchResultWrapper > div > table > tbody > tr > td:nth-child(3) > div > div.searchResult_wai > div > div.left > span:nth-child(2)')
    shuliang= str(shuliang)[str(shuliang).find(">")+1:str(shuliang).find('</span>')].replace(",","")
    up=math.ceil(int(shuliang)/15)
    print("查询中……请等待")
    print("查询到"+shuliang+"个结果，是否继续？(y/n)")
    
    

    
    
    
    jixu =input("请输入y/n:")
    while jixu not in["y","n"]:
        print("输入错误，请重新输入")
        jixu=input("请输入y/n:")
    if jixu=="y":
        print("请选择是否翻译，翻译输入“y”，不翻译输入“n”:")
        fanyi=input("请输入y/n:")
    
        
        
        while fanyi not in["y","n"]:
            print("输入错误，请重新输入")
            fanyi=input("请输入y/n:")



            
        fpath='d:/'+word+name+"_"+now_time+'.txt'
        #name=word+".txt"
        fp=open(fpath,'a',encoding='utf-8')
        max=int(shuliang)
        m=0
        url= url+"&pages=1"
        with tqdm(total=max,desc="爬取中",ncols=70) as t:
            for i in range(up):
                m=m+1

                for numb in range(m,up+1):
                    
                    
                    url = url[:-1]+str(numb)
                    #print(url)
                    request=request_html(url)
                    html = urllib.request.urlopen(request).read().decode('utf8')
                    soup = BeautifulSoup(html,'html.parser')
                    #shuliang = soup.select('div.searchResultWrapper > div > table > tbody > tr > td:nth-child(3) > div > div.searchResult_wai > div > div.left > span:nth-child(2)')
                    zhaiyao = soup.select('#mainlist > div:nth-child(n) > form > input:nth-of-type(6)')
                    timu = soup.select('#mainlist > div:nth-child(n) > form > input:nth-of-type(4)') 
                    #shuliang= int(str(shuliang)[str(shuliang).find(">")+1:str(shuliang).find('</span>')].replace(",",""))    
                    


            
                
                    for i,k in zip(timu,zhaiyao):
                        j=j+1

                        timu1=str(j)+"、"+"题目"+"《"+i.get('value')+"》"        
                        zhaiyao1="摘要："+k.get('value')
                        if fanyi=="y":
                        
                            #if k.get('value')=="":
                                #pass
                                #u=""
                            #else:
                                query =k.get('value')
                                salt = random.randint(32768, 65536)
                                sign = make_md5(appid + query + str(salt) + appkey)
                                payload = {'appid': appid, 'q': query, 'from': from_lang, 'to': to_lang, 'salt': salt, 'sign': sign}

                                # Send request
                                r = requests.post(baiduurl, params=payload, headers=baiduheaders)
                                result = r.json()
                                #print(result)
                                try:
                                    u=result['trans_result']
                                    l=len(u)
                                except:u={}

                                # Build request
                        
                        
                        else:
                            pass    
                        print(timu1+"\n",file=fp)
                        print(zhaiyao1+"\n",file=fp)

                        if fanyi=="y":

                            sleep(1)
                            if u=={}:
                                print("翻译："+"\n",file=fp)
                            else:
                                for g in range(0,int(l)):
                                    if g==int(l)-1:
                                
                                        print("翻译："+u[g]['dst']+"\n",file=fp)
                                    else:
                                        print("翻译："+u[g]['dst'],file=fp)
                        else:
                            pass
                           
                      
                    if fanyi=="y":
                        pass
                    else:
                        sleep(1)
                    #sleep(2)
                    break
                
                t.update(15)
            #m.update(int(numb*15))
                #print('\r{}'.format("已完成"+str(numb*15)+"/"+str(shuliang)),end='',flush=True)
            
 
            
                
                
            

            

            #sys.stdout.flush()
                
        fp.close()
        
        print("爬取完成，文件保存在"+"“"+fpath+"”"+"，按“d”打开文件\n")
        tuichu=input("请输入：")
          

        
        while tuichu!="d":
            tuichu=input()
        os.startfile(fpath)
        
                 
            
            


                
        #tuichu=input("爬取完成，文件保存在"+"d:/"+word+name+".txt"+"按“q”退出，按“d”打开文件\n")

            

        

        
    else:
        print("程序退出！")
        sleep(2)
        exit()

    
    
          
