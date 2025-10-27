#===========================

import matplotlib.pyplot as pit
import numpy as np

# x = np.array(["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10"])
# y = np.array([92, 100, 62, 76, 80, 40, 76, 77, 95, 82])
#
# print(np.mean(y))
# print(np.median(y))
# print(np.std(y))
#
# pit.xlabel("Courses")
# pit.ylabel("Grades")
#
# pit.plot(x, y)
# pit.show()

x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

pit.xlabel("Year")
pit.ylabel("Num of people")

pit.scatter(x,y)
pit.show()




