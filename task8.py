import matplotlib.pyplot as plt

dasy = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

temperatures = [18, 24, 21, 26, 28, 24, 27]

plt.plot( dasy , temperatures , marker='o', linestyle='-' , color='RED' )

plt.title("temperature week")
plt.xlabel("days of week")
plt.ylabel("temperature")

plt.show()