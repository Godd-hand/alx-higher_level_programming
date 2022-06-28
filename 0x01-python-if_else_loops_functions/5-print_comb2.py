able File  6 lines (6 sloc)  162 Bytes
#!/usr/bin/python3
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
