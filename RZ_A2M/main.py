import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import RZ_A2M_const as RZ
import Common_function as CF
import constants as CS

url = CS.evm_url
connectText = CF.driver.find_element(By.XPATH, CS.connection_path)

if "Ready" in connectText.text:
    def header_function():
        CF.login_and_connect(RZ.board_name)
        CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.progress_log_path), "SYSTEM READY"))

        CF.write_header(pdf, 'RZ_A2M')
        CF.click_button(CS.live_button)


    def face_detection_function():
        header_function()
        CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
        time.sleep(10)
        CF.update_progress_log(pdf)

        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\setup_stream.png',
                      'setup_stream.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path,
                      'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\monitor_stream.png',
                      'monitor_stream.png')
        print("Connection secure....")

        CF.click_button(RZ.stop_button_path)
        time.sleep(3)
        CF.write_result(pdf, 'Control_parameter_function(After clicking stop button) : ', 'START EVALUATING')
        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\setup_stream_1.png',
                      'setup_stream_1.png')
        time.sleep(5)
        CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\monitor_stream_1'
                                                   '.png', 'monitor_stream_1.png')
        time.sleep(5)


    def barcode_scanner_function():
        header_function()
        CF.click_button(RZ.barcode_scanner_path)
        time.sleep(5)
        CF.click_button(RZ.demo_video_path)
        time.sleep(5)
        CF.click_button(RZ.start_button_path)
        print('click start')
        CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
        CF.write_result(pdf, 'Barcode_scanner_function : ', 'START EVALUATING')
        CF.update_progress_log(pdf)
        CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\setup_stream_2.png',
                      'setup_stream_2.png')
        time.sleep(5)
        pdf.cell(40)
        CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\monitor_stream_2'
                                                   '.png', 'monitor_stream_2.png')
        CF.click_button(RZ.stop_button_path)
        time.sleep(5)
        print('click stop')
        # CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))


    if __name__ == '__main__':
        pdf = FPDF()
        pdf.add_page()
        face_detection_function()
        barcode_scanner_function()
        pdf.output('result.pdf')

time.sleep(5)
CF.click_button(CS.Connect_Button)
