while 1:
    choice = int(input('This is CN299-1: \n'
                       '1: Header_function:\n'
                       '2: Maximize_voltage:\n'
                       '3: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import CN299_const as CN
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.old_login_connect(CN.board_name)
        CF.wait_until_progress("START EVALUATING")
        connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        if "Ready" in connectText.text:
            CF.write_header(pdf, 'CN299-1')
            CF.wait_until_progress("START EVALUATING")
            # GOING LIVE VIDEO
            hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
            CF.actions.move_to_element(hover).perform()

            CF.driver.implicitly_wait(0.5)
            CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
            CF.wait_until_clickable(CS.old_refresh_button)
            print('vvvvv')

            CF.driver.switch_to.parent_frame()
            time.sleep(8)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.old_update_progress_log(pdf)
            CF.take_image(pdf, CS.old_live_video_xpath,
                          'D:\\TenXer\\gmail_login\\CN299-1\\screenshot\\live_image.png',
                          'live_image.png')

    if choice == 1:
        pdf.add_page()
        header_function()
        pdf.cell(0, 7, txt=date_time, align='L')
        pdf.output('result.pdf')
        CF.click_button(CS.old_connect_button)
        exit()

    if choice == 2:
        def maximize_voltage():
            pdf.add_page()
            header_function()
            time.sleep(5)
            hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
            CF.actions.move_to_element(hover).perform()
            print('hover')
            CF.click_button(CN.old_output_voltage)
            CF.click_button(CN.old_5V_voltage)
            time.sleep(5)
            CF.click_button(CN.old_set_button)
            CF.wait_until_progress('Input Voltage, Output Voltage and VLDO read from board is successful')
            time.sleep(5)
            CF.click_button(CN.maximize_graph_path)
            time.sleep(5)
            CF.write_result(pdf, '5V value coming : ', 'Input Voltage, Output Voltage and VLDO read from board is '
                                                       'successful')
            CF.old_update_progress_log(pdf)
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\CN299-1\\screenshot\\graph.png',
                          'graph.png')
            pdf.cell(0, 7, txt=date_time, align='L')
            CF.click_button(CN.maximize_graph_path)


        maximize_voltage()
        pdf.output('result.pdf')
        CF.click_button(CS.old_connect_button)
        exit()

    if choice == 3:
        print('Thanks for executing me!!!!')
        exit()

