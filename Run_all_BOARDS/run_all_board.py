
while 1:
    choice = int(input('Run All Boards : \n'
                       '1: Run_1st_function_allBoards:\n'
                       '2: Run_2nd_function_allBoards:\n'
                       '3: Exit\n'
                       'Option: \n'))

    if choice == 1:
        from EU065.main import EU065
        EU = EU065()
        EU.light_control_function()

        from CN157.main import CN157
        CN_157 = CN157()
        CN_157.manual_testing()

        from CN268.main import CN268
        CN_268 = CN268()
        CN_268.header_function()

        exit()

    if choice == 2:
        from EU065.main import EU065
        EU = EU065()
        EU.RGB_control_function()

        from CN157.main import CN157
        CN_157 = CN157()
        CN_157.auto_testing()
        exit()

    if choice == 3:
        print('Thanks for executing me!!!!')
        exit()
