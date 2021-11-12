log_file = open("um-server-01.txt")
#opens the um-server-01.txt file

def sales_reports(log_file):    # defines a fuction taking in a file
    for line in log_file:       # for each line in the file it strips it of whitespace
        line = line.rstrip()    #  then pulls the day of the line and if the day
        day = line[0:3]         # and if the day is tuesday it will print the line
        if day == "Mon":
            print(line)


sales_reports(log_file)
