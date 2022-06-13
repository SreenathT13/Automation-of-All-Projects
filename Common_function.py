import datetime
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import constants as CS

url = CS.evm_url
screenshot_path = r"./screenshot"
PROGRESS_LOG = []
VR_LOG = []
if not os.path.isdir(screenshot_path):
    os.makedirs(screenshot_path)


def click_button(UI_button):
    live = wait.until(EC.element_to_be_clickable((By.XPATH, UI_button)))
    live.click()


def login_and_connect(board_name):
    driver.get(CS.evm_url)
    click_button(CS.login)
    time.sleep(3)

    click_button(CS.login_url_1)
    time.sleep(5)

    email = driver.find_element(By.XPATH, CS.email_1)
    email.send_keys(CS.username)
    time.sleep(5)

    password = driver.find_element(By.XPATH, CS.passwrd_1)
    password.send_keys(CS.passwrd)
    click_button(CS.submit)
    time.sleep(15)

    search_element = '//*[@id="formSerachBar"]'
    inputElement = wait.until(EC.element_to_be_clickable((By.XPATH, search_element)))
    inputElement.send_keys(board_name)
    wait_until_clickable(CS.connect_jp128)
    wait_until_clickable(CS.Connect_Button)


def old_login_connect(board_name):
    driver.get(CS.evm_url)
    click_button(CS.login)
    time.sleep(3)

    click_button(CS.login_url_1)
    time.sleep(5)

    email = driver.find_element(By.XPATH, CS.email_1)
    email.send_keys(CS.username)
    time.sleep(5)

    password = driver.find_element(By.XPATH, CS.passwrd_1)
    password.send_keys(CS.passwrd)
    click_button(CS.submit)
    time.sleep(15)

    search_element = '//*[@id="formSerachBar"]'
    inputElement = wait.until(EC.element_to_be_clickable((By.XPATH, search_element)))
    inputElement.send_keys(board_name)
    time.sleep(10)

    wait_until_clickable(CS.connect_jp128)

    driver.find_element(By.XPATH, CS.old_close_user_guide).click()

    wait_until_clickable(CS.old_connect_button)


def video_testing(pdf, switch_to_frame):
    driver.switch_to.frame(driver.find_element(By.XPATH, switch_to_frame))
    print('Click for refresh')
    click_button(CS.Video_refresh)
    time.sleep(10)

    # PASS IF THERE IS KBps MORE THAN 200 and Fail if 0 KBps
    kbps = driver.find_element(By.XPATH, CS.kbps_path).text
    time.sleep(10)
    slice_txt = kbps[0:3]
    convert_int = int(slice_txt)
    print(convert_int)
    if convert_int > 0:
        driver.switch_to.parent_frame()
        write_result(pdf, 'Video :', 'SYSTEM READY')
        print('PASS')
    else:
        driver.switch_to.parent_frame()
        write_result(pdf, 'No data has come...', 'SYSTEM READY')
        print('FAIL')
    time.sleep(5)


def write_header(pdf1, Board_name):
    pdf1.set_font("Arial", size=15)
    pdf1.cell(0, 7, txt="BOARD NAME", ln=1, align='C')
    pdf1.cell(0, 7, txt=str(Board_name), ln=2, align='C')


def write_result(pdf1, test_case, right_txt):
    pdf1.set_font("Arial", 'B', size=12)
    progress_log = driver.find_element(By.XPATH, '//*[@id="console_status"]').text
    pdf1.set_text_color(0, 0, 0)
    pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
    if right_txt in progress_log:
        pdf1.set_text_color(0, 128, 0)
        pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
    else:
        pdf1.set_text_color(255, 0, 0)
        pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')


def old_write_result(pdf1, test_case, right_txt):
    pdf1.set_font("Arial", 'B', size=12)
    progress_log = driver.find_element(By.XPATH, '//*[@id="console_status"]/div/tx-elements/div[2]/div/ul').text
    pdf1.set_text_color(0, 0, 0)
    pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
    if right_txt in progress_log:
        pdf1.set_text_color(0, 128, 0)
        pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
    else:
        pdf1.set_text_color(255, 0, 0)
        pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')


# def old_write_result(pdf1, test_case, right_txt):
#     pdf1.set_font("Arial", 'B', size=12)
#     progress_log = driver.find_element(By.XPATH, '//*[@id="console_status"]').text
#     pdf1.set_text_color(0, 0, 0)
#     pdf1.cell(0, 30, txt=str(test_case), ln=0, align='L')
#     if right_txt in progress_log:
#         pdf1.set_text_color(0, 128, 0)
#         pdf1.cell(0, 30, txt="PASS", ln=1, align='R')
#     else:
#         pdf1.set_text_color(255, 0, 0)
#         pdf1.cell(0, 25, txt="FAIL", ln=1, align='R')


def update_progress_log(pdf1):
    global PROGRESS_LOG
    pdf1.set_font("Arial", size=12)
    path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
    connectText = driver.find_element(By.XPATH, path)
    progress_log = driver.find_element(By.XPATH, '//*[@id="console_status"]').text.split("\n")
    latest_progres_data = progress_log[len(PROGRESS_LOG):]
    PROGRESS_LOG = progress_log
    if "Ready" in connectText.text:
        for line in latest_progres_data:
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 10, txt=line, ln=1, align='L')


def update_VR_log(pdf1):
    global VR_LOG
    pdf1.set_font("Arial", size=12)
    path = '//*[@id="default-dashboard"]/div[1]/nav/div[2]/form'
    connectText = driver.find_element(By.XPATH, path)
    progress_log = driver.find_element(By.XPATH, '//*[@id="11f1e3dc-7e13-2931-ab0c-e3893cab89d3"]').text.split("\n")
    latest_progres_data = progress_log[len(VR_LOG):]
    VR_LOG = progress_log
    if "Ready" in connectText.text:
        for line in latest_progres_data:
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 10, txt=line, ln=1, align='L')


def old_update_progress_log(pdf1):
    global PROGRESS_LOG
    pdf1.set_font("Arial", size=12)
    path = '//*[@id="navbar6"]/ul[3]/li[2]/div'
    connectText = driver.find_element(By.XPATH, path)
    print(connectText.text)
    progress_log = driver.find_element(By.XPATH, CS.old_progress_log_path).text.split("\n")
    latest_progres_data = progress_log[len(PROGRESS_LOG):]
    PROGRESS_LOG = progress_log
    if "Ready" in connectText.text:
        for line in latest_progres_data:
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 10, txt=line, ln=1, align='L')


def take_image(pdf1, Image_Path, img, image):
    Image1 = driver.find_element(By.XPATH, Image_Path)
    Image1.screenshot(screenshot_path + "/" + image)
    pdf1.cell(40)
    pdf1.image(img, x=50, w=100, h=50)
    pdf1.ln(5)


def record_audio(wav):
    import pyaudio
    import wave

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 20
    WAVE_OUTPUT_FILENAME = screenshot_path + "/" + wav

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("* recording")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


def add_audio_link_pdf(pdf1, test_name, LINK):
    pdf1.set_font("Arial", 'B', size=12)
    pdf1.set_text_color(0, 0, 0)
    pdf1.cell(0, 30, txt=str(test_name), ln=0, align='L')
    pdf1.set_font("Arial", size=12)
    pdf1.set_text_color(0, -5, 255)
    pdf1.cell(0, 30, txt=str(LINK), ln=1, align='R', link=LINK)


def wait_until_old_progress(string):
    wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.old_progress_log_path), string))


def wait_until_progress(string):
    wait.until(EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), string))


def wait_until_clickable(xpath):
    secondButton = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    secondButton.click()


# def Text_To_Pdf(txt_File, Pdf_file):
#     pdf = FPDF())
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
#     file = open(screenshot_path + "/" + txt_File, "r")
#
#     for xy in file:
#         pdf.cell(200, 10, txt=xy, ln=1, align='l')
#
#     pdf.output(Pdf_file)
#     pdf.close()
#     file.close()


# def Merger_Pdf(First_pdf, Second_pdf, Result_pdf):
#     File_path = "D:\\TenXer\\gmail_login\\"
#     merger = PdfFileMerger()
#     merger.append(File_path + First_pdf)
#     merger.append(File_path + Second_pdf)
#     merger.write(File_path + Result_pdf)
#     merger.close()
#
#
# def Merger_txt(First_txt, Second_txt, Result_txt):
#     File_path = "D:\\TenXer\\gmail_login\\JP128\\screenshot"
#     filenames = [File_path + First_txt, File_path + Second_txt]
#     with open(File_path + Result_txt, 'w') as outfile:
#         for names in filenames:
#             with open(names) as infile:
#                 outfile.write(infile.read())
#             outfile.write("\n")
#
#
# def Remove_File(First_file):
#     os.remove(First_file)


options = webdriver.ChromeOptions()
options.add_argument(r'--user-data-dir=C:\Users\THIS PC\Desktop\gmail login\session')
options.add_argument('--profile-directory=session')
options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
actions = ActionChains(driver)
wait = WebDriverWait(driver, 60)
e = datetime.datetime.now()

driver.maximize_window()
