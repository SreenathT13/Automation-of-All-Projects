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
url = JP.url
e = datetime.datetime.now()

driver.maximize_window()

# -------------------------------------------- STAGE-1 START---------------------------------------------------------


# Clicks the radio button for start the live program
driver.get(url)
click_button(JP.Connect_Button)
time.sleep(5)

path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
connectText = driver.find_element(By.XPATH, path)

if "Ready" in connectText.text:
    # Scroll the window step by step
    SCROLL_PAUSE_TIME = 1
    for i in range(1, 9):
        x_path = f'//*[@id="helpCarousel"]/div[{i}]'
        actions.move_to_element(driver.find_element(By.XPATH, x_path)).perform()
        time.sleep(SCROLL_PAUSE_TIME)
    time.sleep(5)

    # clicks the live button for saw the live part
    click_button(JP.Live_Button)
    time.sleep(5)

    # Clicks 3w radio button
    click_button(JP.Three_Watt_Button)
    time.sleep(10)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(5)

    Convert_ProgressLog_text('Three_watt_Battery.txt')
    time.sleep(5)

    Text_To_Pdf('Three_watt_Battery.txt', 'Three_watt_Battery.pdf')

    Merger_Pdf('./Three_watt_Battery.pdf', './Battery.pdf', './Result.pdf')

    Remove_File('./Three_watt_Battery.pdf')
    Remove_File('./Battery.pdf')

    # -------------------------------------------- STAGE-2 START--------------------------------------------------------

    # Clicks 8w radio button
    click_button(JP.Eight_Watt_Button)
    time.sleep(10)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(5)

    Convert_ProgressLog_text('Eight_watt_Battery.txt')
    time.sleep(5)

    # uncommon_line_matching('Three_watt_Battery.txt', 'Eight_watt_Battery.txt', 'matching.txt')

    Text_To_Pdf('Eight_watt_Battery.txt', 'Eight_watt_Battery.pdf')

    Merger_Pdf('./Eight_watt_Battery.pdf', './Battery.pdf', './Eight_Result.pdf')
    Merger_Pdf('./Result.pdf', './Eight_Result.pdf', './Result_stage_2.pdf')

    Remove_File('./Eight_Result.pdf')
    Remove_File('./Result.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Eight_watt_Battery.pdf')

    # -------------------------------------------- STAGE-3 START--------------------------------------------------------

    # Clicks 11w radio button
    click_button(JP.Eleven_Watt_Button)
    time.sleep(10)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(5)

    Convert_ProgressLog_text('Eleven_Watt_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Eleven_Watt_Button.txt', 'Eleven_Watt_Button.pdf')

    Merger_Pdf('./Eleven_Watt_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_2.pdf', './Result.pdf', './Result_stage_3.pdf')

    Remove_File('./Eleven_Watt_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_2.pdf')
    Remove_File('./Result.pdf')

    # -------------------------------------------- STAGE-4 START--------------------------------------------------------

    # clicks next button
    click_button(JP.Next_Button)
    time.sleep(1)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Next_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Next_Button.txt', 'Next_Button.pdf')

    Merger_Pdf('./Next_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_3.pdf', './Result.pdf', './Result_stage_4.pdf')

    Remove_File('./Next_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_3.pdf')
    Remove_File('./Result.pdf')

    # -------------------------------------------- STAGE-5 SsTART-------------------------------------------------------
    # clicks previous button
    click_button(JP.Previous_Button)
    time.sleep(1)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Previous_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Previous_Button.txt', 'Previous_Button.pdf')

    Merger_Pdf('./Previous_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_4.pdf', './Result.pdf', './Result_stage_5.pdf')

    Remove_File('./Previous_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_4.pdf')
    Remove_File('./Result.pdf')

    # ------------------------------------------ STAGE-6 START---------------------------------------------------------

    # clicks LCD button
    click_button(JP.Led_Button)
    time.sleep(1)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Led_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Led_Button.txt', 'Led_Button.pdf')

    Merger_Pdf('./Led_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_5.pdf', './Result.pdf', './Result_stage_6.pdf')

    Remove_File('./Led_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_5.pdf')
    Remove_File('./Result.pdf')

    # ------------------------------------------ STAGE-7 START---------------------------------------------------------

    # clicks temperature button
    click_button(JP.Temp_Button)
    time.sleep(1)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Temp_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Temp_Button.txt', 'Temp_Button.pdf')

    Merger_Pdf('./Temp_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_6.pdf', './Result.pdf', './Result_stage_7.pdf')

    Remove_File('./Temp_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_6.pdf')
    Remove_File('./Result.pdf')

    # ------------------------------------------ STAGE-8 START---------------------------------------------------------

    # clicks humidity button
    click_button(JP.Humidity_Button)
    time.sleep(1)

    Take_Image(JP.Three_watt_Battery, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Humidity_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Humidity_Button.txt', 'Humidity_Button.pdf')

    Merger_Pdf('./Humidity_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_7.pdf', './Result.pdf', './Result_stage_8.pdf')

    Remove_File('./Humidity_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_7.pdf')
    Remove_File('./Result.pdf')

    # -------------------------------------------- STAGE-9 START---------------------------------------------------------

    # Maximize the graph button
    click_button(JP.Graph_Open_Button)
    time.sleep(5)

    Take_Image(JP.Graph_Image, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Graph_Open_Button.txt')
    time.sleep(5)

    Text_To_Pdf('Graph_Open_Button.txt', 'Graph_Open_Button.pdf')

    Merger_Pdf('./Graph_Open_Button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_8.pdf', './Result.pdf', './Result_stage_9.pdf')

    click_button(JP.Graph_Close_Button)
    time.sleep(5)

    Remove_File('./Graph_Open_Button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_8.pdf')
    Remove_File('./Result.pdf')

    # ----------------------------------------- STAGE-10 START---------------------------------------------------------

    # Maximize the video button
    click_button(JP.Video_Open_button)
    time.sleep(5)

    Take_Image(JP.Video_Image, 'Battery.pdf')
    time.sleep(2)

    Convert_ProgressLog_text('Video_Open_button.txt')
    time.sleep(5)

    Text_To_Pdf('Video_Open_button.txt', 'Video_Open_button.pdf')

    Merger_Pdf('./Video_Open_button.pdf', './Battery.pdf', './Result.pdf')
    Merger_Pdf('./Result_stage_9.pdf', './Result.pdf', './Result_stage_10.pdf')

    click_button(JP.Video_Close_Button)
    time.sleep(5)

    Remove_File('./Video_Open_button.pdf')
    Remove_File('./Battery.pdf')
    Remove_File('./Result_stage_9.pdf')
    Remove_File('./Result.pdf')

    # -------------------------------------------- STAGE-11 START------------------------------------------------------

    # Pic image and save
    driver.save_screenshot(screenshot_path + '/JP158.png')
    image.image_to_pdf(screenshot_path + '/JP158.png', "Full_Page.pdf")

    Merger_Pdf('./Result_stage_10.pdf', './Full_Page.pdf', './Result_JP158.pdf')

    Remove_File('./Result_stage_10.pdf')
    Remove_File('./Full_Page.pdf')

    # -------------------------------------------- STAGE-11 START------------------------------------------------------

    # Off the radio button
    click_button(JP.Connect_Button)
else:
    print('Some one use this board')
