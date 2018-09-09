time= float(input("Input time in seconds: "))
minutes = time // 60
time % = 60
hour= time // 3600
time %= 3600
print("h:m->%d:%d" % (hour,minute))
