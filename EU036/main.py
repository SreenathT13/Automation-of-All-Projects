import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from EU036 import EU036_const as EU
from Common_function import common
import constants as CS

pdf = FPDF()
CF = common()


def main_function():
    CF.login_and_connect(EU.board_name)
    time.sleep(10)
    CF.write_header(pdf, 'EU036')
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        CF.wait_until_progress("SYSTEM READY")
        CF.write_result(pdf, 'Connection : ', 'connected')
        time.sleep(10)
        CF.update_progress_log(pdf)
        print("Connection secure....")
        CF.take_image(pdf, EU.live_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\live_video.png',
                      'live_video.png')


class EU036:
    def __init__(self):
        self.date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))

    def slider_function(self):
        pdf.add_page()
        main_function()
        time.sleep(5)
        # Scroll slider
        Scroll = CF.driver.find_element(By.XPATH, EU.slider_path)
        CF.actions.drag_and_drop_by_offset(Scroll, 40, 0).perform()
        CF.wait_until_progress('Moving Reflector')
        CF.write_result(pdf, 'Slider-connection : ', 'Moving Reflector')
        time.sleep(5)

        # Maximize main video
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)

        CF.take_image(pdf, EU.main_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\main_video.png',
                      'main_video.png')
        time.sleep(3)
        CF.click_button(EU.maximize_live_video)
        CF.update_progress_log(pdf)
        time.sleep(3)
        pdf.cell(0, 7, txt=self.date_time, align='L')

        pdf.output('EU036_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()

    def temperature_control_function(self):
        pdf.add_page()
        main_function()
        CF.click_button(EU.temperature_control_button)
        CF.wait_until_progress("Blowing Hot-air")

        CF.write_result(pdf, 'Temperature-control-test : ', 'Blowing Hot-air')
        CF.click_button(EU.maximize_live_video)
        time.sleep(5)
        CF.take_image(pdf, EU.main_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\main_video_2.png',
                      'main_video_2.png')
        CF.click_button(EU.maximize_live_video)

        time.sleep(3)
        CF.click_button(EU.temperature_control_button)
        CF.update_progress_log(pdf)
        time.sleep(3)
        pdf.cell(0, 7, txt=self.date_time, align='L')

        pdf.output('EU036_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = EU036()
    stu.slider_function()
    stu.temperature_control_function()
