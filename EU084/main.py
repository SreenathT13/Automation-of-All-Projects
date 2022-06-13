while 1:
    choice = int(input('This is CN299-1: \n'
                       '1: Header_function:\n'
                       '2: Manual_testing:\n'
                       '3: Auto_testing:\n'
                       '4: Exit\n'
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
                          'D:\\TenXer\\gmail_login\\CN157\\screenshot\\live_image.png',
                          'live_image.png')
            time.sleep(5)
















