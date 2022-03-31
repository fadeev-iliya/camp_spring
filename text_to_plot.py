from text_file_reading import read_with_split
import matplotlib.pyplot as plt

temp = read_with_split('text_2.txt', '\n')
temp_int = []
day = []
i = 1

for element in temp:
    temp_int.append(float(element))
    day.append(i)
    i += 1

plt.plot(day,temp_int)
plt.show()