import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import EU036_const as EU
import Common_function as CF
import constants as CS

url = CS.evm_url
CF.login_and_connect(EU.board_name)

pdf = FPDF()
pdf.add_page()


def main_function():
    CF.write_header(pdf, 'EU036')
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), "SYSTEM READY"))
        CF.write_result(pdf, 'Connection : ', 'connected')
        time.sleep(10)
        CF.update_progress_log(pdf)
        print("Connection secure....")
        CF.take_image(pdf, EU.live_video_path, 'D:\\TenXer\\gmail_login\\EU036\\screenshot\\live_video.png',
                      'live_video.png')

        def slider_function():
            # Scroll slider
            Scroll = CF.driver.find_element(By.XPATH, EU.slider_path)
            CF.ActionChains(CF.driver).drag_and_drop_by_offset(Scroll, 40, 0).perform()
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), "Moving Reflector"))

            CF.write_result(pdf, 'Slider-connection : ', 'Moving Reflector')
            time.sleep(5)

            CF.update_progress_log(pdf)
            time.sleep(3)

            # Maximize main video
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)

            pdf.cell(40)
            CF.take_image(pdf, EU.main_video_path, 'D:\\TenXer\\gmail_login\\EU036\\screenshot\\main_video.png',
                          'main_video.png')
            time.sleep(3)
            CF.click_button(EU.maximize_live_video)

        def temperature_control_function():
            CF.click_button(EU.temperature_control_button)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), "Blowing Hot-air"))

            CF.write_result(pdf, 'temperature-control-test : ', 'Blowing Hot-air')
            time.sleep(5)

            CF.update_progress_log(pdf)
            time.sleep(5)
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)

            CF.take_image(pdf, EU.main_video_path, 'D:\\TenXer\\gmail_login\\EU036\\screenshot\\main_video_2.png',
                          'main_video_2.png')
            time.sleep(3)
            CF.click_button(EU.maximize_live_video)

            time.sleep(5)
            CF.click_button(EU.temperature_control_button)

        slider_function()
        temperature_control_function()


main_function()
pdf.output('result.pdf')

time.sleep(5)
CF.click_button(CS.Connect_Button)
