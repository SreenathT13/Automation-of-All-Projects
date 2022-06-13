while 1:
    choice = int(input('This is CN268-1: \n'
                       '1: Main_function:\n'
                       '2: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import CN268_const as CN
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))


    def header_function():
        CF.login_and_connect(CN.board_name)
        time.sleep(10)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'CN268-1')
            CF.click_button(CN.start_button)
            time.sleep(3)
            CF.wait_until_progress("SYSTEM READY")
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.click_button(CN.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, CN.live_video_path, 'D:\\TenXer\\gmail_login\\CN268-1\\screenshot\\live_video.png',
                                                   'live_video.png')
            CF.click_button(CN.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, CN.graph_path, 'D:\\TenXer\\gmail_login\\CN268-1\\screenshot\\graph.png',
                          'graph.png')
            CF.update_progress_log(pdf)
            time.sleep(3)
            CF.write_result(pdf, 'Slave--Log : ', 'START EVALUATING')
            CF.slave_log_path(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


    if choice == 1:
        pdf.add_page()
        header_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 2:
        print('Thanks for executing me!!!!')
        exit()


























