import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


x = np.arange(-10, 11) # x ekseni -10 ile +11 arası olacak şekl. oluşturuldu
# plt.figure(figsize=(12, 6)) # grafik boyutu
# plt.title('My Nice Plot')
# plt.plot(x, x ** 2) # x ekseni oluşturulan x arrayinden, y eksini de x değelerinin karelerinden oluşturuldu
# plt.plot(x, -1 * (x ** 2)) # grafiği -1 ile çarpıp altına ekler



# plt.figure(figsize=(12, 6))
# plt.title('My Nice Plot')
# plt.subplot(1, 2, 1)  # rows, columns, panel selected
# # 1 satır 2 kolundan oluşup 1. grafiği(subplot) çizer
# plt.plot(x, x ** 2) # X**2 olacak şekilde Y ekseni oluşturulur
# plt.plot([0, 0, 0], [-10, 0, 100]) # (0,-10) (0,0) (0-100) noktalarından oluşan ikinci grafiği çizer
# plt.legend(['X^2', 'Vertical Line']) # legend bilgileri
# plt.xlabel('X') # X ve Y eksenine takma adlar verildi
# plt.ylabel('X Squared')

# plt.subplot(1, 2, 2) # 1 satır 2 kolundan oluşup 2. grafiği(subplot) çizer
# plt.plot(x, -1 * (x ** 2)) # birinci grafiği çizer
# plt.plot([-10, 0, 10], [-50, -50, -50]) # (-10,-50) (0,-50) (10-50) noktalarından oluşan ikinci grafiği çizer
# plt.legend(['-X^2', 'Horizontal Line'])
# plt.xlabel('X')
# plt.ylabel('X Squared')



# fig, axes = plt.subplots(figsize=(12, 6))
# axes.plot( #(x,(x**2)) şekl X-Y eksenleri olan, color, linewidth, marker, markersize parametreleri verilen grafik çizildi
#     x, (x ** 2), color='red', linewidth=3,
#     marker='o', markersize=8, label='X^2')
# axes.plot(x, -1 * (x ** 2), 'b--', label='-X^2')
# axes.set_xlabel('X')
# axes.set_ylabel('X Squared')
# axes.set_title("My Nice Plot")
# axes.legend()



# fig, axes = plt.subplots(figsize=(12, 6))
# axes.plot(x, x + 0, linestyle='solid') # marker benzeri işlevi olan linestyle değişkeni kullanılarak 4 tane grafik çizildi
# axes.plot(x, x + 1, linestyle='dashed')
# axes.plot(x, x + 2, linestyle='dashdot')
# axes.plot(x, x + 3, linestyle='dotted')
# axes.set_title("My Nice Plot")



# fig, axes = plt.subplots(figsize=(12, 6))
# axes.plot(x, x + 0, '-og', label="solid green") # (x,x) şeklinde farklı parametrelerle grafikler çizildi
# axes.plot(x, x + 1, '--c', label="dashed cyan") # (x,x+1)
# axes.plot(x, x + 2, '-.b', label="dashdot blue") # (x,x+2)
# axes.plot(x, x + 3, ':r', label="dotted red") # (x,x+3)
# axes.set_title("My Nice Plot")
# axes.legend()



# plot_objects = plt.subplots(nrows=2, ncols=2, figsize=(14, 6)) # 2satır 2kolon, toplamda 4 adet grafik olacağı belirtildi
# fig, ((ax1, ax2), (ax3, ax4)) = plot_objects
# ax4.plot(np.random.randn(50), c='yellow')
# ax1.plot(np.random.randn(50), c='red', linestyle='--')
# ax2.plot(np.random.randn(50), c='green', linestyle=':')
# ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3.0) # (x,y) eksenlerine random değer atanarak, color, marker, linestyle... parametreleriyle grafikler çizdirildi



# plt.figure(figsize=(14, 6))
# ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
# ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
# ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
# ax4 = plt.subplot2grid((3,3), (2,0))
# ax5 = plt.subplot2grid((3,3), (2,1)) # bu şekilde bir subplot konumlandırması da yapılabilir


# SCATTER PLOT
# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = np.pi * (20 * np.random.rand(N))**2  # 0 to 15 point radii
# # plt.figure(figsize=(14, 6))
# # plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral')
# # plt.colorbar()


# fig = plt.figure(figsize=(14, 6))
# ax1 = fig.add_subplot(1,2,1)
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel1')
# plt.colorbar()
# ax2 = fig.add_subplot(1,2,2)
# plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel2')
# plt.colorbar() # iki adet subplotu olan bir grafik çizdirildi



# HISTOGRAMS
# values = np.random.randn(1000)
# plt.subplots(figsize=(12, 6))
# plt.hist(values, bins=100, alpha=0.8, # (x,y) değerleri random olarak oluşturuldu
#           histtype='bar', color='steelblue',
#           edgecolor='green')
# plt.xlim(xmin=-5, xmax=5) # histogram grafiği örneği



# KDE (kernel density estimation)
values = np.random.randn(1000)
density = stats.kde.gaussian_kde(values)
# plt.subplots(figsize=(12, 6))
values2 = np.linspace(min(values)-10, max(values)+10, 100)
# plt.plot(values2, density(values2), color='#FF7F00')
# plt.fill_between(values2, 0, density(values2), alpha=0.5, color='#FF7F00')
# plt.xlim(xmin=-5, xmax=5)



# COMBINE PLOTS 
# plt.subplots(figsize=(12, 6))

# plt.hist(values, bins=100, alpha=0.8, density=1,
#           histtype='bar', color='steelblue',
#           edgecolor='green')

# plt.plot(values2, density(values2), color='#FF7F00', linewidth=3.0)
# plt.xlim(xmin=-5, xmax=5)



# BAR PLOTS
Y = np.random.rand(1, 5)[0]
Y2 = np.random.rand(1, 5)[0]
# plt.figure(figsize=(12, 4))
# barWidth = 0.5
# plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894')


# plt.figure(figsize=(12, 4))
# barWidth = 0.5
# plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894', label='Label Y')
# plt.bar(np.arange(len(Y2)), Y2, width=barWidth, color='#e17055', bottom=Y, label='Label Y2')
# plt.legend()




plt.show()