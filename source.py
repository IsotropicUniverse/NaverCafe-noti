#-*- encoding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, telegram, time, webbrowser, os, re, sys, configparser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

config = configparser.ConfigParser()
config.read('./config.ini')

boardURL = config['TEL_SETTINGS']['boardURL'] 
cafeName = config['TEL_SETTINGS']['cafeName']

dirct = os.path.dirname(os.path.abspath(__file__))
baseURL = 'http://search.naver.com/search.naver?url=https://cafe.naver.com/'

options = webdriver.FirefoxOptions()
browser = webdriver.Firefox(firefox_options=options)

def sendMessage(userMessage):
    usrToken = config['TEL_SETTINGS']['token'] #bot token
    bot = telegram.Bot(token = usrToken)
    id = config['TEL_SETTINGS']['userID'] #receiver user id (not @username)
    bot.sendMessage(chat_id = id, text = userMessage)

def postCheck():
    print("Selenium 실행 중...")
    #options.add_argument('-headless')
    #options.add_argument('-disable-gpu')
    browser.get(boardURL)
    time.sleep(1)
    attempt = 0
    while attempt < int(config['TEL_SETTINGS']['maxAttempt']):
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find("strong", class_="tit")
        uploadDate = soup.find("span", class_="time")
        postURL = soup.find("a", class_="txt_area").get("href")
        postID = re.search('articleid=(.*)&b', postURL).group(1)
        latest = title.text
        with open(os.path.join(dirct, 'database.txt'), 'r+', encoding='euc-kr') as read:
            previous = read.readline()
            if previous != latest:
                print("새 글: %s" % latest)
                browser.get(baseURL + cafeName + "/" + postID)
                browser.switch_to.frame('cafe_main')
                iframesource = browser.page_source
                soup2 = BeautifulSoup(iframesource, 'html.parser')
                if "tbody m-tcol-c" in iframesource:
                    body = soup2.find("div", class_="tbody m-tcol-c")
                    sendMessage(latest+"\n"+body.text)
                    if 'http' in body.text:
                        urls = body.find_all("a")
                        lim = len(urls)
                        nr = 0
                        while nr < lim:
                            webbrowser.open(urls[nr].get("href"))
                            nr = nr + 1
                    else:
                        pass
                else:
                    print("게시글 열람 권한 없음.")
                    pass
            else:
                print("새 글 없음. 마지막 업로드: %s" % uploadDate.text)
            read.close()
        with open(os.path.join(dirct, 'database.txt'), 'w+', encoding='euc-kr') as write:
            write.write(latest)
            write.close()
        time.sleep(int(config['TEL_SETTINGS']['refresh']))
        attempt = attempt + 1
        print("새로 고침(%d)" % attempt)
        browser.get(boardURL)
        time.sleep(1)

postCheck()
