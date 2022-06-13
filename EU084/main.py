while 1:
    choice = int(input('This is EU084: \n'
                       '1: Auto_Mode:\n'
                       '2: Manual_Mode:\n'
                       '3: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import EU084_const as EU
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.old_login_connect(EU.board_name)
        CF.wait_until_progress("START EVALUATING")
        connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        if "Ready" in connectText.text:
            CF.write_header(pdf, 'EU084')
            CF.wait_until_old_progress("START EVALUATING")
            CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, EU.iframe))
            time.sleep(5)
            CF.wait_until_clickable(EU.continue_button)
            print('Click CONTINUE button')

            CF.driver.switch_to.parent_frame()
            time.sleep(10)
            CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
            CF.old_update_progress_log(pdf)
            CF.take_image(pdf, EU.iframe,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\live_image.png',
                          'live_image.png')
            time.sleep(5)


    if choice == 1:
        def auto_mode():
            pdf.add_page()
            header_function()
            CF.click_button(EU.LCD_backlight_button)
            time.sleep(5)
            CF.take_image(pdf, EU.iframe,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\live_video.png',
                          'live_video.png')
            time.sleep(3)
            CF.click_button(EU.temp_limit_path)
            CF.click_button(EU.set_temp_limit)
            time.sleep(3)
            CF.click_button(EU.auto_mode_path)
            CF.old_write_result(pdf, 'Auto_Mode_testing : ', 'SYSTEM READY')
            CF.click_button(EU.set_auto_mode)
            time.sleep(3)
            CF.click_button(EU.start_temp_mode_path)
            CF.click_button(EU.set_start_temp)
            time.sleep(3)
            CF.click_button(EU.end_temp_mode_path)
            CF.click_button(EU.set_end_temp)
            CF.click_button(EU.start_button)
            CF.wait_until_old_connection_path()
            CF.take_image(pdf, EU.iframe,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\auto_video.png',
                          'auto_video.png')
            time.sleep(3)
            CF.click_button(EU.maximize_graph)
            time.sleep(5)
            CF.take_image(pdf, EU.graph_path,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\auto_graph.png',
                          'auto_graph.png')
            CF.click_button(EU.maximize_graph)
            CF.old_update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        auto_mode()
        pdf.output('result.pdf')
        CF.click_button(CS.off_old_connect_button)
        exit()

    if choice == 2:
        def manual_mode():
            pdf.add_page()
            header_function()
            CF.click_button(EU.LCD_backlight_button)
            time.sleep(5)
            CF.take_image(pdf, EU.iframe,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\manual_live_video.png',
                          'manual_live_video.png')
            time.sleep(3)
            CF.click_button(EU.temp_limit_path)
            CF.click_button(EU.set_temp_limit)
            time.sleep(3)
            CF.click_button(EU.auto_mode_path)
            CF.old_write_result(pdf, 'Manual_Mode_testing : ', 'SYSTEM READY')
            CF.click_button(EU.set_manual_mode)
            slider = CF.driver.find_element(By.XPATH, EU.slider_button_path)
            CF.ActionChains(CF.driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(170, 0). \
                release().perform()
            time.sleep(3)
            CF.click_button(EU.set_button)
            CF.wait_until_old_connection_path()
            CF.take_image(pdf, EU.iframe,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\auto_video.png',
                          'auto_video.png')
            time.sleep(5)
            CF.click_button(EU.maximize_graph)
            time.sleep(10)
            CF.take_image(pdf, EU.graph_path,
                          'D:\\TenXer\\gmail_login\\EU084\\screenshot\\auto_graph.png',
                          'auto_graph.png')
            CF.click_button(EU.maximize_graph)
            CF.old_update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        manual_mode()
        pdf.output('result.pdf')
        CF.click_button(CS.off_old_connect_button)
        exit()

    if choice == 3:
        print('Thanks for executing me!!!!')
        exit()
