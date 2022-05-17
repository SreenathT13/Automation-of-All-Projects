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
options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
options.add_argument('--profile-directory=session')
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)
url = JP.EU036_url
e = datetime.datetime.now()

driver.maximize_window()

# -------------------------------------------- STAGE-1 START---------------------------------------------------------


# Clicks the radio button for start the live program
driver.get(url)
click_button(JP.Connect_Button)
time.sleep(10)

path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
connectText = driver.find_element(By.XPATH, path)

if "Ready" in connectText.text:
    # Scroll the window step by step
    SCROLL_PAUSE_TIME = 1
    for i in range(1, 10):
        x_path = f'//*[@id="helpCarousel"]/div[{i}]'
        actions.move_to_element(driver.find_element(By.XPATH, x_path)).perform()
        time.sleep(SCROLL_PAUSE_TIME)
    time.sleep(5)

    # clicks the live button for saw the live part
    click_button(JP.Live_Button)
    time.sleep(5)

    # Maximize and take screen shoot
    click_button(JP.Maximize_live_EU036)
    time.sleep(5)

    Take_Image(JP.Live_video_path_EU036, 'video_path_1.pdf')

    click_button(JP.Maximize_live_EU036)
    time.sleep(5)

    Convert_ProgressLog_text('progressLog_1.txt')
    Text_To_Pdf('progressLog_1.txt', 'progressLog_1.pdf')

    Merger_Pdf('./progressLog_1.pdf', './video_path_1.pdf', './EU036_1.pdf')

    Remove_File('./progressLog_1.pdf')
    Remove_File('./video_path_1.pdf')

    # Scroll slider
    Scroll = driver.find_element(By.XPATH, '//*[@id="f70d3edd-8b07-3e62-87d8-21f7f90b8feb"]/span[3]')
    ActionChains(driver).drag_and_drop_by_offset(Scroll, 40, 0).perform()
    time.sleep(10)

    # Maximize and take screen shoot
    click_button(JP.Maximize_live_EU036)
    time.sleep(5)

    Take_Image(JP.Live_video_path_EU036, 'video_path_2.pdf')

    click_button(JP.Maximize_live_EU036)
    time.sleep(5)

    driver.save_screenshot(screenshot_path + '/US069.png')
    image.image_to_pdf(screenshot_path + '/US069.png', "full_screen_EU036.pdf")

    Convert_ProgressLog_text('progressLog_2.txt')
    Text_To_Pdf('progressLog_2.txt', 'progressLog_2.pdf')

    Merger_Pdf('./progressLog_2.pdf', './video_path_2.pdf', './EU036_2.pdf')
    Merger_Pdf('./EU036_1.pdf', './EU036_2.pdf', './EU036_3.pdf')
    Merger_Pdf('./EU036_3.pdf', './full_screen_EU036.pdf', './EU036_4.pdf')

    Remove_File('./progressLog_2.pdf')
    Remove_File('./video_path_2.pdf')
    Remove_File('./EU036_1.pdf')
    Remove_File('./EU036_2.pdf')
    Remove_File('./EU036_3.pdf')
    Remove_File('./full_screen_EU036.pdf')


# --------------------------------------- TEMPERATURE CONTROL---------------------------------------------------------

    click_button(JP.Temp_Button_EU036)
    time.sleep(5)

    click_button(JP.Live_video_display_EU036)
    time.sleep(5)

    Take_Image(JP.Display_live_video_path, 'video_path_3.pdf')

    click_button(JP.Live_video_display_EU036)
    time.sleep(5)

    Convert_ProgressLog_text('progressLog_3.txt')
    Text_To_Pdf('progressLog_3.txt', 'progressLog_3.pdf')

    Merger_Pdf('./progressLog_3.pdf', './video_path_3.pdf', './EU036_5.pdf')
    Merger_Pdf('./EU036_4.pdf', './EU036_5.pdf', './EU036_6.pdf')

    Remove_File('./progressLog_3.pdf')
    Remove_File('./video_path_3.pdf')
    Remove_File('./EU036_4.pdf')
    Remove_File('./EU036_5.pdf')

    click_button(JP.Temp_Button_EU036)
    time.sleep(5)

    # Off the radio button
    click_button(JP.Connect_Button)
else:
    print('Some one use this board')
