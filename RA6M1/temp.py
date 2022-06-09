while 1:
    choice = int(input('Enter the operation detail: \n'
                       '1: Header_function:\n'
                       '2: maximize_voltage:\n'
                       '3: Exit\n'
                       'Option: \n'))
    import time
    from fpdf import FPDF
    from selenium.webdriver.common.by import By
    import CN299_const as CN

    # import Common_function as CF
    # import constants as CS
    def header_function():
        print('hhhh')

    if choice == 1:
        header_function()
        exit()

    if choice == 2:
        def maximize_voltage():
            print('ssss')

        header_function()
        maximize_voltage()
        exit()

    if choice == 3:
        print('Thanks for executing me!!!!')
        exit()

    if __name__ == '__main__':
        pdf = FPDF()
        pdf.add_page()

        pdf.output('result.pdf')
        # CF.click_button(CS.old_connect_button)

# time.sleep(5)
# CF.click_button(CS.Connect_Button)
#
# from fpdf import FPDF
#
# # PDF = FPDF()
# # PDF.add_page()
# # PDF.set_font("Arial", size=12)
# # text_data = ["Live-Video : ", "Live-Video : ", "live-Video : "]
# # # for i in text_data:
# # #     # PDF.ln(1)
# # PDF.cell(0, 15, txt="Live-Video : ", ln=1, align='L')
# # img = r"./screenshot/live_video.png"
# # PDF.image(img, x=50, w=100)
# # PDF.ln(5)
# #
# # PDF.cell(0, 15, txt="Live-Video : ", ln=1, align='L')
# # img = r"./screenshot/LCD_video.png"
# # PDF.image(img, x=50, w=100)
# # PDF.ln(5)
# #
# # PDF.cell(0, 15, txt="Live-Video : ", ln=1, align='L')
# # img = r"./screenshot/live_video.png"
# # PDF.image(img, x=50, w=100)
# # PDF.ln(5)
# # PDF.output("temp.pdf")
