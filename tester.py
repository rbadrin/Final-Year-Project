import os,time
import requests
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import threading
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
cnt = 0
start_time = time.time()
str11 = "http://localhost:3000?speed=1&time="
str12 = "http://localhost:3000?speed=5&time="
str21 = "http://localhost:3001?speed=1&time="
str22 = "http://localhost:3001?speed=5&time="
start_time = time.time()
def f(f_stop):
    global cnt
    timer = time.time() - start_time
    if (cnt % 2 == 0 and cnt != 0):
        driver.get(str22 + str(timer))
        driver.switch_to.window(driver.window_handles[0])
        driver.get(str11 + str( timer ))
    elif (cnt % 2 == 1):
        driver.get(str12 + str(timer ))
        driver.switch_to.window(driver.window_handles[1])
        driver.get(str21 + str(timer ))
    cnt = cnt + 1
    if not f_stop.is_set():
        threading.Timer(10, f, [f_stop]).start()
f_stop = threading.Event()
f(f_stop)

driver.get("http://localhost:3000?speed=1&time=0")
driver.execute_script("window.open('http://localhost:3001?speed=10&time=0', 'secondtab')")
driver.switch_to.window(driver.window_handles[0])
