import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
from CN268 import CN268_const as CN
from Common_function import common
import constants as CS

pdf = FPDF()
CF = common()


class CN268:
    def __init__(self):
        self.date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))

    def header_function(self):
        pdf.add_page()
        CF.login_and_connect(CN.board_name)
        time.sleep(10)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN268-1')
            CF.wait_until_progress("SYSTEM READY")
            CF.update_progress_log(pdf)
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\graph2.png',
                          'graph2.png')
            time.sleep(3)
            CF.click_button(CN.start_button)
            time.sleep(8)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.click_button(CN.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, CN.live_video_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\live_video.png',
                          'live_video.png')
            CF.click_button(CN.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\graph.png',
                          'graph.png')
            time.sleep(3)
            CF.update_progress_log(pdf)
            time.sleep(3)
            CF.write_result(pdf, 'Slave--Log : ', 'START EVALUATING')
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\Run_all_BOARDS\\screenshot\\graph1.png',
                          'graph1.png')
            CF.slave_log_path(pdf)
            pdf.cell(0, 7, txt=self.date_time, align='L')

            pdf.output('CN268_result.pdf')
            CF.click_button(CS.Connect_Button)
            CF.driver.close()


if __name__ == "__main__":
    stu = CN268()
    stu.header_function()
