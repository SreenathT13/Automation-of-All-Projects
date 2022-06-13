import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import RA6M1_const as RA
import Common_function as CF
import constants as CS


def header_function():
    CF.login_and_connect(RA.board_name)
    time.sleep(10)
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        CF.write_header(pdf, 'RA6M1')
        CF.wait_until_progress("SYSTEM READY")
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        CF.update_progress_log(pdf)
        CF.wait.until(CF.EC.element_to_be_clickable((By.XPATH, RA.switch_iframe)))
        CF.video_testing(pdf, RA.switch_iframe)
        CF.wait.until(CF.EC.element_to_be_clickable((By.XPATH, RA.live_video_path)))
        CF.take_image(pdf, RA.live_video_path, 'D:\\TenXer\\gmail_login\\RA6M1\\screenshot\\live_video.png',
                      'live_video.png')


pdf = FPDF()
pdf.add_page()
header_function()
pdf.output('result.pdf')
