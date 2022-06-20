import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from RZ_A2M import RZ_A2M_const as RZ
from Common_function import common
import constants as CS

pdf = FPDF()
CF = common()


def header_function():
    CF.login_and_connect(RZ.board_name)
    time.sleep(5)
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        CF.write_header(pdf, 'RZ_A2M')
        CF.wait_until_progress("SYSTEM READY")
        time.sleep(15)
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        CF.update_progress_log(pdf)
        CF.take_image(pdf, RZ.setup_stream_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\setup_stream1.png',
                      'setup_stream1.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\monitor_stream1.png',
                      'monitor_stream1.png')
        print("Connection secure....")


class RZ_A2M:
    def __init__(self):
        self.date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))

    def face_detection_function(self):
        pdf.add_page()
        header_function()
        CF.write_result(pdf, 'Face_Detection_Function : ', 'START EVALUATING')
        time.sleep(5)
        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\setup_stream.png',
                      'setup_stream.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path,
                      'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\monitor_stream.png',
                      'monitor_stream.png')
        print("Connection secure....")

        CF.click_button(RZ.start_button_path)
        CF.wait_until_progress("Showing fast demo video")
        CF.write_result(pdf, 'Control_parameter_function(After clicking stop button) : ', 'START EVALUATING')
        CF.update_progress_log(pdf)

        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\setup_stream_1'
                                                 '.png',
                      'setup_stream_1.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                   '\\monitor_stream_1.png', 'monitor_stream_1.png')
        time.sleep(5)
        CF.click_button(RZ.stop_button_path)
        CF.update_progress_log(pdf)
        pdf.cell(0, 7, txt=self.date_time, align='L')

        pdf.output('RZA2M_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()

    def barcode_scanner_function(self):
        pdf.add_page()
        header_function()
        CF.click_button(RZ.barcode_scanner_path)
        time.sleep(5)
        CF.click_button(RZ.demo_video_path)
        time.sleep(5)
        CF.click_button(RZ.start_button_path)
        print('click start')
        CF.wait_until_connection_path()
        time.sleep(5)
        CF.write_result(pdf, 'Barcode_scanner_function : ', 'START EVALUATING')
        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\setup_stream_2'
                                                 '.png', 'setup_stream_2.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot'
                                                   '\\monitor_stream_2.png', 'monitor_stream_2.png')
        CF.click_button(RZ.stop_button_path)
        time.sleep(5)
        print('click stop')
        CF.update_progress_log(pdf)
        pdf.cell(0, 7, txt=self.date_time, align='L')

        pdf.output('RZA2M_result.pdf')
        CF.click_button(CS.Connect_Button)
        CF.driver.close()


if __name__ == "__main__":
    stu = RZ_A2M()
    stu.face_detection_function()
    stu.barcode_scanner_function()
