import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import constants as JP
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import os
import image

screenshot_path = r"./screenshot"
if not os.path.isdir(screenshot_path):
    os.makedirs(screenshot_path)


def click_button(UI_button):
    live = wait.until(EC.element_to_be_clickable((By.XPATH, UI_button)))
    live.click()


def Convert_ProgressLog_text(ProgressLog_txt):
    handler = open(screenshot_path + "/" + ProgressLog_txt, "+a")
    handler.write(e.strftime("Time %I:%M %p\n"))
    handler.write(driver.find_element(By.XPATH, '//*[@id="console_status"]').text)
    handler.close()


def Take_Image(Image_Path, Image_pdf):
    Image = driver.find_element(By.XPATH, Image_Path)
    Image.screenshot(screenshot_path + '/image.png')
    image.image_to_pdf(screenshot_path + '/image.png', Image_pdf)


def Text_To_Pdf(txt_File, Pdf_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    file = open(screenshot_path + "/" + txt_File, "r")

    for xy in file:
        pdf.cell(200, 10, txt=xy, ln=1, align='l')

    pdf.output(Pdf_file)
    pdf.close()
    file.close()


def Merger_Pdf(First_pdf, Second_pdf, Result_pdf):
    File_path = "D:\\TenXer\\gmail_login\\"
    merger = PdfFileMerger()
    merger.append(File_path + First_pdf)
    merger.append(File_path + Second_pdf)
    merger.write(File_path + Result_pdf)
    merger.close()


def Remove_File(First_file):
    os.remove(First_file)


options = webdriver.ChromeOptions()
# options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
# options.add_argument('--profile-directory=session')
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)
url = JP.JP128_url
e = datetime.datetime.now()

driver.maximize_window()

# -------------------------------------------- TURN_ON_LIGHT START------------------------------------------------------

driver.get(url)
click_button(JP.login_url)
time.sleep(3)
click_button(JP.login_url_1)
time.sleep(3)
username = "pritam@tenxertech.com"
passwrd = "pritam1928"

email_1 = '//*[@id="username"]'
email = driver.find_element(By.XPATH, email_1)
email.send_keys(username)
time.sleep(5)

passwrd_1 = '//*[@id="password"]'
password = driver.find_element(By.XPATH, passwrd_1)
password.send_keys(passwrd)
click_button(JP.submit)
time.sleep(10)


pro = 'JP128'
inputElement = driver.find_element_by_xpath('//*[@id="formSerachBar"]')
inputElement.send_keys(pro)

# # Scroll the window step by step
# SCROLL_PAUSE_TIME = 1
# for i in range(1, 12):
#     x_path = f'//*[@id="helpCarousel"]/div[{i}]'
#     actions.move_to_element(driver.find_element(By.XPATH, x_path)).perform()
#     time.sleep(SCROLL_PAUSE_TIME)
# time.sleep(5)

# clicks the live button for saw the live part
# click_button(JP.Live_Button)
# time.sleep(5)

# Clicked the refresh button
# driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="77a46be1-2b26-51c7-f423-cd51ae5350e2"]/div/tx-elements'
#                                                      '/div[2]/div/div/div[3]/iframe'))
# print('Click for refresh')
# click_button(JP.Video_refresh_jp128)
# driver.switch_to.parent_frame()
# time.sleep(8)

# clicked turn on the light
# click_button(JP.Turn_on_light_jp128)
# time.sleep(5)

# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video_jp128.pdf')
# time.sleep(5)
#
# Convert_ProgressLog_text('light_on.txt')
# Text_To_Pdf('light_on.txt', 'light_on_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)

# maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)

# Take_Image(JP.Graph_image_jp128, 'graph_jp128.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./light_on_jp128.pdf', './video_jp128.pdf', './video.pdf')
# Merger_Pdf('./video.pdf', 'graph_jp128.pdf', './main.pdf')
#
# Remove_File('./light_on_jp128.pdf')
# Remove_File('./video_jp128.pdf')
# Remove_File('./graph_jp128.pdf')
# Remove_File('./video.pdf')
#
# # ---------------------------------------- TURN_ON_TV START---------------------------------------------------------
#
# # click turn of light
# click_button(JP.Turn_on_tv_jp128)
# time.sleep(3)
# click_button(JP.Turn_on_tv_jp128)
# time.sleep(10)
#
# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video.pdf')
#
# time.sleep(5)
#
# Convert_ProgressLog_text('tv_on.txt')
# Text_To_Pdf('tv_on.txt', 'tv_on_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)
#
# # maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Take_Image(JP.Graph_image_jp128, 'graph.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./tv_on_jp128.pdf', './video.pdf', './main1.pdf')
# Merger_Pdf('./main1.pdf', 'graph.pdf', './main2.pdf')
# Merger_Pdf('./main.pdf', './main2.pdf', './main3.pdf')
#
# Remove_File('./tv_on_jp128.pdf')
# Remove_File('./video.pdf')
# Remove_File('./main.pdf')
# Remove_File('./graph.pdf')
# Remove_File('./main1.pdf')
# Remove_File('./main2.pdf')
#
# # -------------------------------------------- CHANNEL_UP START---------------------------------------------------------
#
# # click turn of light
# click_button(JP.Channel_up_jp128)
# time.sleep(3)
# click_button(JP.Channel_up_jp128)
# time.sleep(10)
#
# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video.pdf')
#
# time.sleep(5)
#
# Convert_ProgressLog_text('channel_up.txt')
# Text_To_Pdf('channel_up.txt', 'channel_up_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)
#
# # maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Take_Image(JP.Graph_image_jp128, 'graph.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./channel_up_jp128.pdf', './video.pdf', './main1.pdf')
# Merger_Pdf('./main1.pdf', 'graph.pdf', './main2.pdf')
# Merger_Pdf('./main3.pdf', './main2.pdf', './main4.pdf')
#
# Remove_File('./channel_up_jp128.pdf')
# Remove_File('./video.pdf')
# Remove_File('./main3.pdf')
# Remove_File('./graph.pdf')
# Remove_File('./main1.pdf')
# Remove_File('./main2.pdf')
#
# # -------------------------------------------- CHANNEL_DOWN START-------------------------------------------------------
#
# # click turn of light
# click_button(JP.Channel_down_jp128)
# time.sleep(3)
# click_button(JP.Channel_down_jp128)
# time.sleep(10)
#
# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video.pdf')
#
# time.sleep(5)
#
# Convert_ProgressLog_text('channel_down.txt')
# Text_To_Pdf('channel_down.txt', 'channel_down_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)
#
# # maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Take_Image(JP.Graph_image_jp128, 'graph.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./channel_down_jp128.pdf', './video.pdf', './main1.pdf')
# Merger_Pdf('./main1.pdf', 'graph.pdf', './main2.pdf')
# Merger_Pdf('./main4.pdf', './main2.pdf', './main5.pdf')
#
# Remove_File('./channel_down_jp128.pdf')
# Remove_File('./video.pdf')
# Remove_File('./main4.pdf')
# Remove_File('./graph.pdf')
# Remove_File('./main1.pdf')
# Remove_File('./main2.pdf')
#
# # -------------------------------------------- TURN_OFF_TV START-------------------------------------------------------
#
# # click turn of light
# click_button(JP.Turn_off_tv_jp128)
# time.sleep(10)
#
# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video.pdf')
#
# time.sleep(5)
#
# Convert_ProgressLog_text('Turn_off.txt')
# Text_To_Pdf('Turn_off.txt', 'Turn_off_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)
#
# # maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Take_Image(JP.Graph_image_jp128, 'graph.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./Turn_off_jp128.pdf', './video.pdf', './main1.pdf')
# Merger_Pdf('./main1.pdf', 'graph.pdf', './main2.pdf')
# Merger_Pdf('./main5.pdf', './main2.pdf', './main6.pdf')
#
# Remove_File('./Turn_off_jp128.pdf')
# Remove_File('./video.pdf')
# Remove_File('./main5.pdf')
# Remove_File('./graph.pdf')
# Remove_File('./main1.pdf')
# Remove_File('./main2.pdf')
#
# # -------------------------------------------- TURN_OFF_LIGHT START-----------------------------------------------------
#
# # click turn of light
# click_button(JP.Turn_off_light_jp128)
# time.sleep(10)
#
# # maximize video
# click_button(JP.Maximize_video_jp128)
# time.sleep(2)
#
# # take image
# Take_Image(JP.Video_container_jp128, 'video.pdf')
#
# time.sleep(5)
#
# Convert_ProgressLog_text('Turn_off_light.txt')
# Text_To_Pdf('Turn_off_light.txt', 'Turn_off_light_jp128.pdf')
#
# click_button(JP.Maximize_video_jp128)
# time.sleep(5)
#
# # maximize graph image and take image
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Take_Image(JP.Graph_image_jp128, 'graph.pdf')
#
# click_button(JP.Maximize_graph_jp128)
# time.sleep(5)
#
# Merger_Pdf('./Turn_off_light_jp128.pdf', './video.pdf', './main1.pdf')
# Merger_Pdf('./main1.pdf', 'graph.pdf', './main2.pdf')
# Merger_Pdf('./main6.pdf', './main2.pdf', './main7.pdf')
#
# Remove_File('./Turn_off_light_jp128.pdf')
# Remove_File('./video.pdf')
# Remove_File('./main6.pdf')
# Remove_File('./graph.pdf')
# Remove_File('./main1.pdf')
# Remove_File('./main2.pdf')
#
# # -------------------------------------------- LIVE_VIDEO START-----------------------------------------------------
#
# click_button(JP.Maximize_live_video)
# time.sleep(5)
#
# Take_Image(JP.Live_video_jp128, 'live.pdf')
#
# click_button(JP.Maximize_live_video)
#
# Merger_Pdf('./main7.pdf', './live.pdf', './Result_JP128.pdf')
#
# Remove_File('./main7.pdf')
# Remove_File('./live.pdf')
#
# # Off the radio button
# click_button(JP.Connect_Button)
#
#
