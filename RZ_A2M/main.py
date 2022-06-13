while 1:
    choice = int(input('This is RZ_A2M: \n'
                       '1: Face_detection_function:\n'
                       '2: Barcode_scanner_function:\n'
                       '3: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import RZ_A2M_const as RZ
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.login_and_connect(RZ.board_name)
        time.sleep(5)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'RZ_A2M')
            CF.wait_until_progress("SYSTEM READY")


    if choice == 1:
        def face_detection_function():
            pdf.add_page()
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

            CF.click_button(RZ.start_button_path)
            CF.wait_until_progress("Showing fast demo video")
            CF.write_result(pdf, 'Control_parameter_function(After clicking stop button) : ', 'START EVALUATING')
            CF.update_progress_log(pdf)

            CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\setup_stream_1.png',
                          'setup_stream_1.png')
            time.sleep(5)
            CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\monitor_stream_1'
                                                       '.png', 'monitor_stream_1.png')
            time.sleep(5)
            CF.click_button(RZ.stop_button_path)
            pdf.cell(0, 7, txt=date_time, align='L')


        face_detection_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 2:
        def barcode_scanner_function():
            pdf.add_page()
            header_function()
            CF.click_button(RZ.barcode_scanner_path)
            time.sleep(5)
            CF.click_button(RZ.demo_video_path)
            time.sleep(5)
            CF.click_button(RZ.start_button_path)
            print('click start')
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            time.sleep(5)
            CF.write_result(pdf, 'Barcode_scanner_function : ', 'START EVALUATING')
            CF.update_progress_log(pdf)
            CF.take_image(pdf, RZ.setup_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\setup_stream_2.png',
                          'setup_stream_2.png')
            time.sleep(5)
            CF.take_image(pdf, RZ.monitor_stream_path, 'D:\\TenXer\\gmail_login\\RZ_A2M\\screenshot\\monitor_stream_2'
                                                       '.png', 'monitor_stream_2.png')
            CF.click_button(RZ.stop_button_path)
            time.sleep(5)
            print('click stop')
            pdf.cell(0, 7, txt=date_time, align='L')


        barcode_scanner_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 3:
        print('Thanks for executing me!!!!')
        exit()





