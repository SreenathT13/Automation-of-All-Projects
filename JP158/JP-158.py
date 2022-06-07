import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import Common_function as CF
import constants as CS
import Jp158_const as JP

url = CS.evm_url

CF.login(JP.board_name)

pdf = FPDF()
pdf.add_page()


def main_function():
    CF.write_header(pdf, 'JP158')
    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    if "Ready" in connectText.text:
        CF.click_button(CS.live_button)
        time.sleep(5)
        CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
        CF.update_progress_log(pdf)
        time.sleep(10)
        print("Connection secure....")

        def button_clicking_function(same_pdf, button_name, test_case, right_txt, img_path, img_name):
            CF.click_button(button_name)
            time.sleep(7)
            CF.write_result(same_pdf, test_case, right_txt)
            CF.update_progress_log(same_pdf)
            pdf.ln(15)
            CF.take_image(same_pdf, JP.battery_path, img_path, img_name)
            time.sleep(3)

        # 3W button clicked
        button_clicking_function(pdf, JP.three_watt_button, '3W button clicked : ', 'LED Lamp Configuration is 3W',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\3watt_battery.png', '3watt_battery.png')

        # 8W button clicked
        button_clicking_function(pdf, JP.eight_watt_button, '8W button clicked : ', 'LED Lamp Configuration is 8W',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\8watt_battery.png', '8watt_battery.png')

        # 11W button clicked
        button_clicking_function(pdf, JP.eleven_watt_button, '11W button clicked : ', 'LED Lamp Configuration is 11W',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\11watt_battery.png', '11watt_battery.png')

        # Next button clicked
        button_clicking_function(pdf, JP.next_button, 'Next button clicked : ', 'Pressed Next (SW19) on JP158 ('
                                                                                'Remote Function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\next_button.png', 'next_button.png')

        # Prev button clicked
        button_clicking_function(pdf, JP.prev_button, 'Prev button clicked : ', 'Pressed Prev (SW18) on JP158 ('
                                                                                'Remote Function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\prev_button.png', 'prev_button.png')

        # Pause button clicked
        button_clicking_function(pdf, JP.pause_button, 'Pause button clicked : ', 'Pressed Play/Pause (SW15) on '
                                                                                  'JP158 (Remote Function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\pause_button.png', 'pause_button.png')

        # Humidity button clicked
        button_clicking_function(pdf, JP.humidity_button, 'Humidity button clicked : ', 'Pressed Humidity (SW17) on '
                                                                                        'JP158 (Sensing & Display '
                                                                                        'function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\humidity_button.png',
                                 'humidity_button.png')

        # Temperature button clicked
        button_clicking_function(pdf, JP.temperature_button, 'Temperature button clicked : ',
                                 'Pressed Temperature (SW13) on JP158 (Sensing & Display function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\temperature_button.png',
                                 'temperature_button.png')

        # Lcd button clicked
        button_clicking_function(pdf, JP.lcd_button, 'Lcd button clicked : ',
                                 'Pressed Demo (SW20) on JP158 (Sensing & Display function)',
                                 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\pause_button.png', 'pause_button.png')

        def video_screenshot():
            CF.click_button(JP.maximize_video_button)
            time.sleep(5)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 20, txt="Live-Video : ", ln=1, align='L')
            print('ssss')
            CF.take_image(pdf, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\live_video.png',
                          'live_video.png')
            time.sleep(5)
            print('dddd')
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 20, txt="LCD-Video : ", ln=1, align='L')
            CF.take_image(pdf, JP.lcd_video_path, 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\LCD_video.png',
                          'LCD_video.png')
            time.sleep(5)
            CF.click_button(JP.maximize_video_button)
            time.sleep(5)

        def taking_graph_image():
            CF.click_button(JP.maximize_graph_button)
            time.sleep(5)
            pdf.set_text_color(0, 0, 0)
            pdf.cell(0, 20, txt="Graph-image : ", ln=1, align='L')
            pdf.cell(40)
            CF.take_image(pdf, JP.graph_image_path, 'D:\\TenXer\\gmail_login\\JP158\\screenshot\\graph_image.png',
                          'graph_image.png')
            time.sleep(5)

        video_screenshot()
        taking_graph_image()
    else:
        print("FAIL")


main_function()
pdf.output('result.pdf')

CF.click_button(CS.Connect_Button)
