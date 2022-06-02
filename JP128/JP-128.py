import time
from fpdf import FPDF
from selenium.webdriver.common.by import By
import JP128_const as JP
import Common_function as CF
import constants as CS

url = CS.evm_url


# -------------------------------------------- TURN_ON_LIGHT START------------------------------------------------------

CF.login(JP.board_name)

pdf1 = FPDF()
pdf1.add_page()


# -------------------------------------------- HEADER FUNCTION---------------------------------------------------------

def header_function():
    CF.write_header(pdf1, 'JP128')

    connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
    # connectText = 'Ready'

    if "Ready" in connectText.text:
        # CONNECTION TESTING
        CF.click_button(CS.live_button)
        time.sleep(5)
        CF.write_result(pdf1, 'Connection :', 'SYSTEM READY')
        CF.update_progress_log(pdf1)
        time.sleep(10)
        print('ggggg')

        # -------------------------------------------- VIDEO TESTING ---------------------------------------------------
        CF.video_testing(pdf1, JP.switch_to_frame)
        # TAKE IMAGE AND ADD THE PDF
        CF.click_button(JP.Maximize_live_video)
        time.sleep(7)

        CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image1.png',
                      'image1.png')

        CF.click_button(JP.Maximize_live_video)
        time.sleep(5)
        print(' complete video testing.....')

        # -------------------------------------------- HMI TESTING -----------------------------------------------

        def HMI_testing():
            # START GIVING COMMANDS
            CF.click_button(JP.turn_on_light_jp128)
            CF.record_audio("voice1.wav")
            time.sleep(5)
            CF.write_result(pdf1, 'HMI Tracking :')
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice1.wav')
            time.sleep(5)
            pdf1.ln(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image2.png',
                          'image2.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)

            # TURN OFF LIGHT
            CF.click_button(JP.Turn_off_light_jp128)
            CF.record_audio("voice2.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice2.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image3.png',
                          'image3.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)

            # TURN ON TV
            CF.click_button(JP.Turn_on_tv_jp128)
            CF.record_audio("voice3.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice3.wav')
            time.sleep(5)
            pdf1.ln(5)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image4.png',
                          'image4.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # CHANNEL UP
            CF.click_button(JP.Channel_up_jp128)
            CF.record_audio("voice4.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice4.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image5.png',
                          'image5.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(75)

            # CHANNEL DOWN
            CF.click_button(JP.Channel_down_jp128)
            CF.record_audio("voice5.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Channel-Down : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice5.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image6.png',
                          'image6.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN OFF TV
            CF.click_button(JP.Turn_off_tv_jp128)
            CF.record_audio("voice6.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Turn-Off-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice6.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image7.png',
                          'image7.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)
            print(' complete HMI testing.....')

            # -------------------------------------------- PERFORMANCE UNDER NOICE ROAD --------------------------------

        def noice_road():
            #     # SCROLL_PAUSE_TIME = 1
            #     # for i in range(1, 2):
            #     #     x_path = f'//*[@id="helpCarousel"]/div[{i}]'
            #     #     CF.actions.move_to_element(CF.driver.find_element(By.XPATH, x_path)).perform()
            #     #     time.sleep(SCROLL_PAUSE_TIME)
            #     # time.sleep(5)
            CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE ROAD)--')
            noice_button = CF.driver.find_element(By.XPATH, JP.induce_noice_button).click()
            print('jjjj')
            time.sleep(5)
            CF.click_button(JP.river_button)
            time.sleep(3)

            # START GIVING COMMANDS
            CF.click_button(JP.turn_on_light_jp128)
            CF.record_audio("voice7.wav")
            time.sleep(5)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice7.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image8.png',
                          'image8.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN OFF LIGHT
            CF.click_button(JP.Turn_off_light_jp128)
            CF.record_audio("voice8.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice8.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image9.png',
                          'image9.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN ON TV
            CF.click_button(JP.Turn_on_tv_jp128)
            CF.record_audio("voice9.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice9.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image10.png',
                          'image10.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # CHANNEL UP
            CF.click_button(JP.Channel_up_jp128)
            CF.record_audio("voice10.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice10.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image11.png',
                          'image11.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)
            print(' complete road testing.....')

            # -------------------------------------------- PERFORMANCE UNDER NOICE TRAFFIC ----------------------------

        def traffic_noice():
            CF.click_button(JP.traffic_button)
            time.sleep(3)
            CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE TRAFFIC)--')
            time.sleep(5)

            # START GIVING COMMANDS
            CF.click_button(JP.turn_on_light_jp128)
            CF.record_audio("voice11.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice11.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image12.png',
                          'image12.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN OFF LIGHT
            CF.click_button(JP.Turn_off_light_jp128)
            CF.record_audio("voice12.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice12.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image13.png',
                          'image13.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN ON TV
            CF.click_button(JP.Turn_on_tv_jp128)
            CF.record_audio("voice13.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice13.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image14.png',
                          'image14.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # CHANNEL UP
            CF.click_button(JP.Channel_up_jp128)
            CF.record_audio("voice14.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice14.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image15.png',
                          'image15.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)
            print(' complete traffic testing.....')

            # # -------------------------------------------- PERFORMANCE UNDER NOICE BABBLE ---------------------------

        def babble_noice():
            CF.click_button(JP.babble_button)
            time.sleep(3)
            CF.write_result(pdf1, 'HMI-Tracking : (PERFORMANCE UNDER NOICE BABBLE Tracking)--')
            time.sleep(5)

            # START GIVING COMMANDS
            CF.click_button(JP.turn_on_light_jp128)
            CF.record_audio("voice15.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice15.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image16.png',
                          'image16.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN OFF LIGHT
            CF.click_button(JP.Turn_off_light_jp128)
            CF.record_audio("voice16.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-Off : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice16.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image17.png',
                          'image17.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # TURN ON TV
            CF.click_button(JP.Turn_on_tv_jp128)
            CF.record_audio("voice17.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Light-On-TV : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice17.wav')
            time.sleep(5)
            pdf1.ln(11)
            pdf1.set_text_color(0, 0, 0)
            pdf1.cell(0, 30, txt="IMAGE", ln=1, align='L')
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image18.png',
                          'image18.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            # CHANNEL UP
            CF.click_button(JP.Channel_up_jp128)
            CF.record_audio("voice18.wav")
            time.sleep(10)
            CF.update_progress_log(pdf1)
            CF.add_audio_link_pdf(pdf1, 'Channel-UP : ', 'file:///D:/TenXer/gmail_login/JP128/screenshot/voice18.wav')
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image19.png',
                          'image19.png')

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)
            print(' complete babble testing.....')

        # -------------------------------------------- 2 D DRAWING ENGINE ----------------------------------------------

        def drawing_engine():
            CF.click_button(JP.display_performance)
            time.sleep(5)
            CF.click_button(JP.d_drawing_button)
            time.sleep(5)
            CF.click_button(JP.click_apply_button)
            time.sleep(5)
            CF.write_result(pdf1, '2 D drawing Engine Tracking : ')
            CF.update_progress_log(pdf1)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            pdf1.cell(0, 30, txt="After on the switch---take screenshots", ln=1, align='L')
            time.sleep(3)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image20.png',
                          'image20.png')
            time.sleep(3)

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)

            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.Maximize_live_video)
            time.sleep(7)

            pdf1.cell(0, 30, txt="After on the switch---take screenshots", ln=1, align='L')
            time.sleep(3)
            CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image21.png',
                          'image21.png')
            time.sleep(3)

            CF.click_button(JP.Maximize_live_video)
            time.sleep(5)
            CF.click_button(JP.d_drawing_button)
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_video_jp128)
            time.sleep(7)

            pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
            time.sleep(3)
            pdf1.ln(2)

            CF.take_image(pdf1, JP.maximize_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image22.png',
                          'image22.png')
            time.sleep(3)

            CF.click_button(JP.maximize_video_jp128)
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.Maximize_live_video)
            time.sleep(7)

            pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
            time.sleep(3)

            CF.take_image(pdf1, JP.live_video_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image23.png',
                          'image23.png')
            time.sleep(3)

            CF.click_button(JP.Maximize_live_video)
            time.sleep(5)
            # TAKE IMAGE AND ADD THE PDF
            CF.click_button(JP.maximize_graph_button)
            time.sleep(7)

            pdf1.cell(0, 30, txt="After off the switch---take screenshots", ln=1, align='L')
            time.sleep(3)

            CF.take_image(pdf1, JP.graph_path, 'D:\\TenXer\\gmail_login\\JP128\\screenshot\\image24.png',
                          'image24.png')
            time.sleep(3)

            CF.click_button(JP.maximize_graph_button)
            time.sleep(5)
            drawing_engine()
        HMI_testing()
        noice_road()
        traffic_noice()
        babble_noice()
    else:
        print('FAIL')


header_function()

pdf1.output('result.pdf')
