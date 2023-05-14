import matplotlib.pyplot as plt
import numpy as np

win_table = [51.61744492737472]
loss_table = [39.5070767859133]
draw_table = [100 - win_table[0] - loss_table[0]]

win_basic = [44.853]
loss_basic = [50]
draw_basic = [100 - loss_basic[0] - win_basic[0]]


print(win_basic[0] + loss_basic[0] + draw_basic[0])
x = ["15 i Terskel", "Tabellmetode"]

win_list = win_basic + win_table
loss_list = loss_basic + loss_table
draw_list = draw_basic + draw_table

alpha = 0.75
bars = np.add(win_list, loss_list).tolist()

print(win_list)


print(loss_list)
print(draw_list)
plt.bar(x, win_list, color="y", alpha=alpha)
plt.bar(x, loss_list, bottom=win_list, color="r", alpha=alpha)
plt.bar(x, draw_list, bottom=bars, color="b", alpha=alpha)
plt.legend(["Vinn", "Tap", "Likt"], loc="upper left")
plt.ylabel("Prosent sjanse %")
plt.suptitle("15 i Terskel vs Tabellmetode")
plt.show()
