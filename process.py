log_file = open("um-server-01.txt")
#opens the um-server-01.txt file

def sales_reports(log_file):    # defines a fuction taking in a file
    for line in log_file:       # for each line in the file it strips it of whitespace
        line = line.rstrip()    #  then pulls the day of the line and if the day
        day = line[0:3]         # and if the day is tuesday it will print the line
        if day == "Mon":
            print(line)


# sales_reports(log_file)

def melon_orders_greaterthan(file, num):
    for line in file:
        line = line.rstrip()
        line = line.split(':')
        msg = line[1].split(' ')
        qty = int(msg[1])
        if qty > num:
            print(" ".join(msg))
        

melon_orders_greaterthan(log_file, 10)