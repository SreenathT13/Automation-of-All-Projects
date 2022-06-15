while 1:
    choice = int(input('This is CN300: \n'
                       '1: Full_function:\n'
                       '2: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import CN300_const as CN
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.old_login_connect(CN.board_name)
        CF.wait_until_progress("START EVALUATING")
        connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        if "Ready" in connectText.text:
            CF.write_header(pdf, 'CN300')
            CF.wait_until_progress("START EVALUATING")
            # GOING LIVE VIDEO
            hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
            CF.actions.move_to_element(hover).perform()

            CF.driver.implicitly_wait(0.5)
            CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))
            CF.wait_until_clickable(CS.old_refresh_button)
            print('Clicked REFRESH button')

            CF.driver.switch_to.parent_frame()
            time.sleep(8)
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.old_update_progress_log(pdf)
            CF.take_image(pdf, CS.old_live_video_xpath,
                          'D:\\TenXer\\gmail_login\\CN300\\screenshot\\live_image.png',
                          'live_image.png')


    if choice == 1:
        def full_function():
            pdf.add_page()
            header_function()
            time.sleep(5)
            CF.write_result(pdf, 'Full-function : ', 'SYSTEM READY')
            hover = CF.driver.find_element(By.XPATH, CS.old_connection_path)
            CF.actions.move_to_element(hover).perform()
            print('click outside')
            CF.click_button(CN.load_current_path)
            CF.click_button(CN.set_load_current)
            time.sleep(3)
            CF.click_button(CN.start_button)
            CF.wait_until_old_connection_path()
            hover = CF.driver.find_element(By.XPATH, CS.old_live_video_xpath)
            CF.actions.move_to_element(hover).perform()
            CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CS.old_switch_to_frame))

            CF.driver.switch_to.parent_frame()

            CF.take_image(pdf, CS.old_live_video_xpath,
                          'D:\\TenXer\\gmail_login\\CN300\\screenshot\\Full_live_image.png',
                          'Full_live_image.png')
            time.sleep(5)
            CF.click_button(CN.maximize_graph)
            time.sleep(5)
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\CN300\\screenshot\\graph.png',
                          'graph.png')
            CF.click_button(CN.maximize_graph)
            CF.old_update_progress_log(pdf)
            CF.wait_until_old_progress('Discharge is Complete')
            CF.write_result(pdf, 'Information--Data : ', 'Discharge is Complete')
            CF.old_take_information(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        full_function()
        pdf.output('result.pdf')
        CF.click_button(CS.off_old_connect_button)
        exit()

    if choice == 2:
        print('Thanks for executing me!!!!')
        exit()
