log_file = open("um-server-01.txt")


def generate_sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)

# it explicilty assigns log_file as the file in the qoutes and opens it

# """it generates sales reports by day"""

# for each line in the file it:
#   seperates strings that have a space
#   each day will be on a new line, starting at iterable 0 to 3,inclusive
# `as long as the day is tuesday it prints
# 
# its implemented by passing a file through it


# 1-look at content of files
# 2-verify what mondays abbrev. is
# 3-replace
# 4-run