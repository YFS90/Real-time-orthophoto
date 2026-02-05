import matplotlib as mpl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import font_manager

# Figure自动调整格式
plt.rcParams['figure.constrained_layout.use']=True

plt.rcParams['axes.unicode_minus'] = False

# 将图表以矢量图格式显示，提高清晰度
plt.rcParams['savefig.dpi'] = 300
mpl.rcParams['figure.dpi'] = 100

mpl.rcParams['legend.fontsize'] = 20
fig = plt.figure(figsize=(16, 14))
# ax = fig.gca(projection='3d')
ax = fig.add_axes(Axes3D(fig))

# read data
data1 = pd.read_csv("./009.csv", delimiter=",", header=None, na_values=[''])
# 将DataFrame转换为numpy数组，空值填充为NaN
data1 = data1.to_numpy()

# 坐标轴范围和坐标字体大小
ax.set_xlim([np.min(data1[:, 3]) - 50, np.max(data1[:, 3]) + 150])
ax.set_ylim([np.min(data1[:, 4]) - 50, np.max(data1[:, 4]) + 200])
ax.set_zlim([np.min(data1[:, 5]) - 100, np.max(data1[:, 5]) + 100])
ax.tick_params(labelsize=14)
# 坐标不科学计数法
plt.ticklabel_format(useOffset=False, style='plain')

# 三维坐标轴比例伸缩,前3个参数用来调整各坐标轴的缩放比例
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 1, 1]))

# 灰色的底想把它换成白色的
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# 分别上下旋转和左右旋转，可以自己设置成一个比较好的参数
ax.view_init(45, -45)

true_valid_rows = np.sum(~np.isnan(data1[:, 3]))
true_x = data1[:true_valid_rows, 3]
true_y = data1[:true_valid_rows, 4]
true_z = data1[:true_valid_rows, 5]

optimize_valid_rows = np.sum(~np.isnan(data1[:, 0]))
optimize_x = data1[:optimize_valid_rows, 0]
optimize_y = data1[:optimize_valid_rows, 1]
optimize_z = data1[:optimize_valid_rows, 2]

n_opt = len(optimize_x)
n_true = len(true_x)

if n_opt != n_true:
    print("error, check data!!!")
    min_len = min(n_opt, n_true)
    optimize_x = optimize_x[:min_len]
    optimize_y = optimize_y[:min_len]
    optimize_z = optimize_z[:min_len]
    true_x = true_x[:min_len]
    true_y = true_y[:min_len]
    true_z = true_z[:min_len]
else:
    min_len = n_opt

err_x = optimize_x - true_x
err_y = optimize_y - true_y
err_z = optimize_z - true_z

# 1. Mean Absolute Error (MAE)
MAE_x = np.mean(np.abs(err_x))
MAE_y = np.mean(np.abs(err_y))
MAE_z = np.mean(np.abs(err_z))
MAE_all = np.mean(np.abs([err_x, err_y, err_z]))

# 2. Root Mean Square Error (RMSE)
RMSE_x = np.sqrt(np.mean(err_x**2))
RMSE_y = np.sqrt(np.mean(err_y**2))
RMSE_z = np.sqrt(np.mean(err_z**2))
RMSE_all = np.sqrt(np.mean([err_x**2, err_y**2, err_z**2]))   

print(f"  MAE_X: {MAE_x:.4f} m")
print(f"  MAE_Y: {MAE_y:.4f} m")
print(f"  MAE_Z: {MAE_z:.4f} m")
print(f"AVERAGE MAE: {MAE_all:.4f} m\n")

print(f"  RMSE_X: {RMSE_x:.4f} m")
print(f"  RMSE_Y: {RMSE_y:.4f} m")
print(f"  RMSE_Z: {RMSE_z:.4f} m")
print(f"AVERAGE RMSE : {RMSE_all:.4f} mm")

# 3. plot Trajectory
ax.set_xlabel('X(m)', labelpad=25, fontdict={'family': 'Times New Roman', 'color': 'Black', 'size': 22})
ax.set_ylabel('Y(m)', labelpad=25, fontdict={'family': 'Times New Roman', 'color': 'Black', 'size': 22})
ax.set_zlabel('Z(m)', labelpad=25, fontdict={'family': 'Times New Roman', 'color': 'Black', 'size': 22})

ticks_font = font_manager.FontProperties(family='Times New Roman')
for tick in ax.get_xticklabels():
    tick.set_fontproperties(ticks_font)
for tick in ax.get_yticklabels():
    tick.set_fontproperties(ticks_font)
for tick in ax.get_zticklabels():
    tick.set_fontproperties(ticks_font)
ax.tick_params(labelsize=18) # font size for all axis

figure_true = ax.plot(true_x, true_y, true_z, label='True Trajectory', c='r')
figure_optimize = ax.plot(optimize_x, optimize_y, optimize_z, label='Ours', c='b')

legend = ax.legend(loc=(16.0/20, 6.0/10), fontsize=18)

plt.savefig('./output.png', dpi=300, bbox_inches = 'tight', pad_inches=0.0)
plt.show()
