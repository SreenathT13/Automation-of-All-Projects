

screenshot_path = r"./screenshot"

first = 'D:\\TenXer\\gmail_login\\screenshot\\first.txt'
second = 'D:\\TenXer\\gmail_login\\screenshot\\second.txt'

# reading files
f1 = open("D:\\TenXer\\gmail_login\\screenshot\\first.txt", "r")
f2 = open("D:\\TenXer\\gmail_login\\screenshot\\second.txt", "r")

i = 0

for line1 in f1:
    i += 1

    for line2 in f2:

        # matching line1 from both files
        if line1 == line2:
            # print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL")
        else:
            print("Line ", i, ":")
            # else print that line from both files
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break

# closing files
f1.close()
f2.close()

# handler = open(screenshot_path + "/third.text", "a")
# handler.write('some_output_file.txt')
# handler.close()
#
# pdf = FPDF()
# pdf.add_page()
# pdf.set_font("Arial", size=12)
# f = open(screenshot_path + "//third.text", "r")
#
# for x in f:
#     pdf.cell(200, 10, txt=x, ln=1, align='L')
#
# pdf.output("Stage-2.pdf")
# pdf.close()
