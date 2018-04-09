print("find day and minitues" )
t = float(input("Input time in seconds: "))
day = t // (24 * 3600)
t = t % (24 * 3600)
hour = t // 3600
t %= 3600
minutes = t // 60
t %= 60
seconds = t
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
