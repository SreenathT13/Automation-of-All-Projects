while 1:
    choice = int(input('This is CN157: \n'
                       '1: Header_function:\n'
                       '2: Manual_testing:\n'
                       '3: Auto_testing:\n'
                       '4: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import CN157_const as CN
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.old_login_connect(CN.board_name)
        CF.wait_until_progress("START EVALUATING")
        connectText = CF.driver.find_element(By.XPATH, CS.old_connection_path)
        if "Ready" in connectText.text:
            CF.write_header(pdf, 'CN157')
            CF.wait_until_old_progress("START EVALUATING")
            CF.driver.switch_to.frame(CF.driver.find_element(By.XPATH, CN.iframe))
            time.sleep(5)
            CF.wait_until_clickable(CN.continue_button)
            print('vvvvv')

            CF.driver.switch_to.parent_frame()
            time.sleep(10)
            CF.write_result(pdf, 'Connection : ', 'SYSTEM READY')
            CF.old_update_progress_log(pdf)
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\live_image.png',
                          'live_image.png')
            time.sleep(5)


    if choice == 1:
        pdf.add_page()
        header_function()
        pdf.output('result.pdf')
        CF.click_button(CS.old_connect_button)
        exit()

    if choice == 2:
        def manual_testing():
            pdf.add_page()
            header_function()
            time.sleep(5)
            CF.click_button(CN.manual_apply_button)
            CF.wait_until_old_progress('Light Intensity set to 0%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\manual_0%.png',
                          'manual_0%.png')
            time.sleep(5)
            slider = CF.driver.find_element(By.XPATH,
                                            '/html/body/div[1]/div/ng-content/div/div[2]/div/div/div/div['
                                            '2]/div/div/div/div/div/ul/li[1]/div/div/tx-elements/div['
                                            '2]/div/div/form/tx-elements[1]/div[2]/div/div/div[3]/span[5]')
            CF.ActionChains(CF.driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(100, 0). \
                release().perform()
            time.sleep(5)
            CF.click_button(CN.manual_apply_button)
            CF.wait_until_old_progress('Light Intensity set to 53%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\manual_53%.png',
                          'manual_53%.png')
            time.sleep(5)
            CF.ActionChains(CF.driver).move_to_element(slider).pause(1).click_and_hold(slider).move_by_offset(180, 0). \
                release().perform()
            time.sleep(5)
            CF.click_button(CN.manual_apply_button)
            CF.wait_until_old_progress('Light Intensity set to 95%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\manual_95%.png',
                          'manual_95%.png')
            time.sleep(5)
            pdf.cell(0, 7, txt=date_time, align='L')


        manual_testing()
        pdf.output('result.pdf')
        CF.click_button(CS.old_connect_button)
        exit()

    if choice == 3:
        def auto_testing():
            pdf.add_page()
            header_function()
            time.sleep(5)
            CF.old_write_result(pdf, 'Auto_testing : ', 'SYSTEM READY')
            time.sleep(5)
            CF.click_button(CN.auto_apply_button)
            CF.wait_until_old_progress('Light Intensity set to 10%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\auto_10%.png',
                          'auto_10%.png')
            CF.wait_until_old_progress('Light Intensity set to 20%')
            CF.old_write_result(pdf, 'Image : ', 'Auto Mode')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\auto_20%.png',
                          'auto_20%.png')
            CF.wait_until_old_progress('Light Intensity set to 30%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\auto_30%.png',
                          'auto_30%.png')
            CF.wait_until_old_progress('Light Intensity set to 40%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\auto_40%.png',
                          'auto_40%.png')
            CF.wait_until_old_progress('Light Intensity set to 50%')
            CF.take_image(pdf, CN.iframe,
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\auto_50%.png',
                          'auto_50%.png')
            CF.old_update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        auto_testing()
        pdf.output('result.pdf')
        CF.click_button(CS.old_connect_button)
        exit()

    if choice == 4:
        print('Thanks for executing me!!!!')
        exit()
