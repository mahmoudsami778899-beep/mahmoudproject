import matplotlib.pyplot as plt

dasy = [ "friday" , "saturday" , "sunday" , "monday" , "tuesday" , "wednesday" , "thursday" ]

temperatures = [18, 24, 21, 26, 28, 24, 27]

plt.plot( dasy , temperatures , marker='o', linestyle='-' , color='RED' )

plt.title("temperature week")
plt.xlabel("days of week")
plt.ylabel("temperature")

plt.show()