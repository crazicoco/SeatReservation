# -*- coding: utf-8 -*-
"""
#intent      :
#Author      :Fang Haisheng
#start date  : 2020./9/7
#Software    : PyCharm

"""
# !E:\Anaconda\conda1\envs\SeatReservat python
import time
from datetime import datetime
import os
from selenium import webdriver
from pymouse import PyMouse
from twilio.rest import Client
# 先安装pywin32，才能导入下面两个包
import win32api
from ctypes import *
import win32con


# 环境配置
def config():
    chromedriver = r"C:\Users\Hp\AppData\Local\Google\Chrome\Application"
    os.environ["webdriver.ie.driver"] = chromedriver
    driver = webdriver.Chrome()  # 选择Chrome浏览器
    driver.get('http://lib-room.chu.edu.cn/ClientWeb/xcus/ic2/Default.aspx')  # 打开网站
    driver.maximize_window()  # 最大化谷歌浏览器
    time1 = {"x_start": 777, "x_end": 873, "y_start": 825, "y_end": 873}
    time2 = {"x_start": 972, "x_end": 873, "y_start": 1020, "y_end": 873}
    time3 = {"x_start": 1022, "x_end": 873, "y_start": 1071, "y_end": 873}
    # time1 = {"x_start": 828, "x_end": 870, "y_start": 1020, "y_end": 870}  # 8~12
    # time2 = {"x_start": 1116, "x_end": 870, "y_start": 1308, "y_end": 870} # 14~18
    # time3 = {"x_start": 1356, "x_end": 870, "y_start": 1500, "y_end": 870} # 19~22
    phone_number = '+8618852066732'
    text = 'Successful'
    return driver, time1, time2, time3, phone_number, text

def login(driver):
    """登陆
        点击登录按钮
        输入id和密码
        点击提交按钮
    """
    driver.find_element_by_class_name('login').click()  # 点击“账户登录”
    time.sleep(1)
    username = "17027058"  # 请替换成你的用户名
    password = "022420"  # 请替换成你的密码
    driver.find_element_by_xpath(
        '//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input').click()  # 点击用户名输入框
    driver.find_element_by_xpath(
        '//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input').clear()  # 清空输入框
    driver.find_element_by_xpath('//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[1]/td[2]/input').send_keys(
        username)
    driver.find_element_by_xpath(
        '//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input').click()  # 点击密码输入框
    driver.find_element_by_xpath(
        '//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input').clear()  # 清空输入框
    driver.find_element_by_xpath('//*[@id="dlg_login"]/form/div[1]/div[2]/table/tbody/tr[2]/td[2]/input').send_keys(
        password)
    driver.find_element_by_class_name('default').click()  # 点击“登录”按钮


def drag(x1, y1, x2, y2):
    time.sleep(0.05)
    windll.user32.SetCursorPos(x1, y1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(1)
    windll.user32.SetCursorPos(x2, y2)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def mouse_click(x=None, y=None):
    if not x is None and not y is None:
        windll.user32.SetCursorPos(x, y)
        time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


# 选择时间
# 点开房间
#     循环三次
#       触发1一次时间
#       点击预定
def selectroom(driver):
    """ 点开# 609个人研修间"""
    driver.find_element_by_xpath('//*[@id="item_list"]/ul/li/ul/li[1]/a/span').click()


def selecttomorrow():
    """第二天"""
    x_d = 832
    y_d = 700
    mouse_click(x_d, y_d)


def submittime(times):
    """拖动时间
        研修间3"""
    drag(times["x_start"], times["x_end"], times["y_start"], times["y_end"])
    # 提交的位置
    x_submit = 920
    y_submit = 844
    mouse_click(x_submit, y_submit)

    x_sure = 974
    y_sure = 627
    time.sleep(0.5)
    time.sleep(0.5)
    mouse_click(x_sure, y_sure)

def SendMessage(phone_number, text):
    """
    预定发送
    发送消息给妹妹
    """
    auth_token = '83e6598eb046abfeeee24791e775bec3'
    account_sid = 'ACb1819bc852ff6dc82933e04862754270'
    trial_number = '12029317929'
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=trial_number,
        body=text,
        to=phone_number
    )
    return message


# 代码调用：
# python.exe JDSignup.py
# 可以将这行命令添加到Windows计划任务，每天运行，从而实现每日自动签到领取京豆。


def main():
    """
        登录
        点开房间
        选择时间，确定，完成提交
        同时开三个进程，选择三个不同时间
        发送消息
    """

    # date = datetime.now()
    # week = datetime.strftime("date.year").weekday()
    driver, time1, time2, time3, phone_number, text = config()
    login(driver)
    time.sleep(0.5)
    selectroom(driver)
    time.sleep(0.5)
    selecttomorrow()
    time.sleep(0.5)
    submittime(time1)
    time.sleep(0.5)
    selecttomorrow()
    time.sleep(0.5)
    submittime(time2)
    time.sleep(0.5)
    selecttomorrow()
    time.sleep(0.5)
    submittime(time3)
    # 使用报文来判断是否成功


if __name__ == '__main__':
    main()
