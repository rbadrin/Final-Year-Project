import os,time
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import threading

#initialising the variables
image_id = '8a754758ca52'
port_number_server = '3000'
port_number_client = '49521'
port_number_client_1 = '49525'
speed= '1'
speed1= '2'

#setting up docker containers
os.system('docker run -d -p '+ port_number_client +':'+port_number_server +' '+'-e speed='+speed+' -e time=0 '+image_id )
os.system('docker run -d -p '+ port_number_client_1 +':'+port_number_server+' '+'-e speed='+speed1+' -e time=0 '+image_id )

#creating threads and making calls based on selenium automation
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
cnt = 0
start_time = time.time()
str11 = "http://localhost:49521?speed=1&time="
str12 = "http://localhost:49521?speed=5&time="
str21 = "http://localhost:49525?speed=1&time="
str22 = "http://localhost:49525?speed=5&time="
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

driver.get("http://localhost:49521?speed=1&time=0")
driver.execute_script("window.open('http://localhost:49525?speed=5&time=0', 'secondtab')")
driver.switch_to.window(driver.window_handles[0])

# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# driver.get("http://localhost:49521")
# driver.execute_script("window.open('http://localhost:49525' , 'secondtab')")
#
# for i in range(5):
#     driver.switch_to.window(driver.window_handles[0])
#     driver.fullscreen_window()
#     time.sleep(10)
#
# # time set and speed set into container
#
#     driver.switch_to.window(driver.window_handles[1])
#     driver.fullscreen_window()
#     time.sleep(10)
# os.system('open --new -a "Firefox" --args "localhost:' + port_number_client + '"')
# os.system('open --new -a "Firefox" --args "localhost:' + port_number_client_1 + '"')
