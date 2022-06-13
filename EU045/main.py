while 1:
    choice = int(input('This is EU045: \n'
                       '1: Header_function:\n'
                       '2: Alcohol_gas_shot_function:\n'
                       '3: Humidity_shot_function:\n'
                       '4: Temperature_function:\n'
                       '5: Clear_air_function:\n'
                       '6: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import EU045_const as EU
    import Common_function as CF
    import constants as CS

    pdf = FPDF()
    date_time = (CF.e.strftime("Time : %b %d %Y %H:%M:%S"))

    def header_function():
        CF.login_and_connect(EU.board_name)
        time.sleep(10)
        connectText = CF.driver.find_element(By.XPATH, CS.connection_path)
        if "Ready" in connectText.text:
            CF.click_button(CS.live_button)
            CF.write_header(pdf, 'EU045')
            CF.wait_until_progress("SYSTEM READY")
            CF.write_result(pdf, 'Connection : ', 'START EVALUATING')
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\appli_video'
                                                          '.png', 'appli_video.png')
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, EU.live_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\live_video.png',
                          'live_video.png')
            CF.click_button(EU.maximize_live_video)
            CF.update_progress_log(pdf)
            time.sleep(5)

    if choice == 1:
        pdf.add_page()
        header_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 2:
        def alcohol_gas_function():
            pdf.add_page()
            header_function()
            CF.click_button(EU.alcohol_gas_shot)
            CF.wait_until_progress('Inducing of gas turned OFF')
            CF.write_result(pdf, 'Alcohol_gas_testing : ', 'Inducing of gas turned OFF')
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, EU.live_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\alcohol_live_video.png',
                          'alcohol_live_video.png')
            CF.click_button(EU.maximize_live_video)
            CF.wait_until_progress('Inducing of gas turned OFF')
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\alcohol_apply'
                                                          '.png', 'alcohol_apply.png')
            # CLICKING Device GAS SHOT
            CF.click_button(EU.device_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\device_gas'
                                                          '.png', 'device_gas.png')
            time.sleep(5)

            # CLICKING Sensors GAS SHOT
            CF.click_button(EU.sensor_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\sensors_gas'
                                                          '.png', 'sensors_gas.png')
            time.sleep(5)

            CF.write_result(pdf, 'Image : ', 'SYSTEM READY')
            # CLICKING Graphs GAS SHOT
            CF.click_button(EU.graph_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\graph_gas'
                                                          '.png', 'graph_gas.png')
            time.sleep(5)

            # CLICKING Tables GAS SHOT
            CF.click_button(EU.tables_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\table_gas'
                                                          '.png', 'table_gas.png')
            time.sleep(5)

            # CLICKING Settings GAS SHOT
            CF.click_button(EU.setting_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\settings_gas'
                                                          '.png', 'settings_gas.png')
            time.sleep(5)
            CF.update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        alcohol_gas_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 3:
        def humidity_shot_function():
            pdf.add_page()
            header_function()
            CF.click_button(EU.humidity_button)
            CF.wait_until_progress('Humidifier turned OFF')
            CF.write_result(pdf, 'Humidity_shot_function : ', 'Humidifier turned OFF')
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, EU.live_video_path,
                          'D:\\TenXer\\gmail_login\\EU045\\screenshot\\humidity_live_video.png',
                          'humidity_live_video.png')
            CF.click_button(EU.maximize_live_video)
            CF.wait_until_progress('Humidifier turned OFF')
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\humidity_apply'
                                                          '.png', 'humidity_apply.png')
            # CLICKING Device GAS SHOT
            CF.click_button(EU.device_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\device_humidity'
                                                          '.png', 'device_humidity.png')
            time.sleep(5)

            # CLICKING Sensors GAS SHOT
            CF.click_button(EU.sensor_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\sensors_humidity'
                                                          '.png', 'sensors_humidity.png')
            time.sleep(5)

            # CLICKING Graphs GAS SHOT
            CF.click_button(EU.graph_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\graph_humidity'
                                                          '.png', 'graph_humidity.png')
            time.sleep(5)

            # CLICKING Tables GAS SHOT
            CF.click_button(EU.tables_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\table_humidity'
                                                          '.png', 'table_humidity.png')
            time.sleep(5)

            # CLICKING Settings GAS SHOT
            CF.click_button(EU.setting_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot'
                                                          '\\settings_humidity.png', 'settings_humidity.png')
            time.sleep(5)
            CF.update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        humidity_shot_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 4:
        def temperature_function():
            pdf.add_page()
            header_function()
            CF.click_button(EU.temperature_button)
            CF.wait_until_progress('Temperature Increased')
            CF.write_result(pdf, 'Temperature_function : ', 'Temperature Increased')
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, EU.live_video_path,
                          'D:\\TenXer\\gmail_login\\EU045\\screenshot\\temperature_live_video.png',
                          'temperature_live_video.png')
            CF.click_button(EU.maximize_live_video)
            CF.wait_until_progress('Temperature Increased')
            CF.take_image(pdf, EU.application_video_path,
                          'D:\\TenXer\\gmail_login\\EU045\\screenshot\\temperature_apply'
                          '.png', 'temperature_apply.png')
            # CLICKING Device GAS SHOT
            CF.click_button(EU.device_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\device_temp'
                                                          '.png', 'device_temp.png')
            time.sleep(5)

            # CLICKING Sensors GAS SHOT
            CF.click_button(EU.sensor_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\sensors_temp'
                                                          '.png', 'sensors_temp.png')
            time.sleep(5)

            # CLICKING Graphs GAS SHOT
            CF.click_button(EU.graph_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\graph_temp'
                                                          '.png', 'graph_temp.png')
            time.sleep(5)

            # CLICKING Tables GAS SHOT
            CF.click_button(EU.tables_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\table_temp'
                                                          '.png', 'table_temp.png')
            time.sleep(5)

            # CLICKING Settings GAS SHOT
            CF.click_button(EU.setting_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot'
                                                          '\\settings_temp.png', 'settings_temp.png')
            time.sleep(5)
            CF.update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        temperature_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 5:
        def clear_air_function():
            pdf.add_page()
            header_function()
            CF.click_button(EU.clear_air_button)
            CF.wait_until_progress('Blower turned ON...Clearing Air')
            CF.write_result(pdf, 'Clear_air_function : ', 'Blower turned ON...Clearing Air')
            CF.click_button(EU.maximize_live_video)
            time.sleep(5)
            CF.take_image(pdf, EU.live_video_path,
                          'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_live_video.png',
                          'air_live_video.png')
            CF.click_button(EU.maximize_live_video)
            CF.wait_until_progress('Blower turned ON...Clearing Air')
            CF.take_image(pdf, EU.application_video_path,
                          'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_apply'
                          '.png', 'air_apply.png')
            # CLICKING Device GAS SHOT
            CF.click_button(EU.device_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_temp'
                                                          '.png', 'air_temp.png')
            time.sleep(5)

            # CLICKING Sensors GAS SHOT
            CF.click_button(EU.sensor_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_temp'
                                                          '.png', 'air_temp.png')
            time.sleep(5)

            # CLICKING Graphs GAS SHOT
            CF.click_button(EU.graph_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_temp'
                                                          '.png', 'air_temp.png')
            time.sleep(5)

            # CLICKING Tables GAS SHOT
            CF.click_button(EU.tables_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot\\air_temp'
                                                          '.png', 'air_temp.png')
            time.sleep(5)

            # CLICKING Settings GAS SHOT
            CF.click_button(EU.setting_button)
            time.sleep(5)
            CF.wait.until(CF.EC.text_to_be_present_in_element((By.XPATH, CS.connection_path), "Ready"))
            CF.take_image(pdf, EU.application_video_path, 'D:\\TenXer\\gmail_login\\EU045\\screenshot'
                                                          '\\air_temp.png', 'air_temp.png')
            time.sleep(5)
            CF.update_progress_log(pdf)
            pdf.cell(0, 7, txt=date_time, align='L')


        clear_air_function()
        pdf.output('result.pdf')
        CF.click_button(CS.Connect_Button)
        exit()

    if choice == 6:
        print('Thanks for executing me!!!!')
        exit()

