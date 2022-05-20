from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
# actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)
