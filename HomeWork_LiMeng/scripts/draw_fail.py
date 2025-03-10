import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置中文字体
font_path = '/Library/Fonts/Arial Unicode.ttf'  # 根据你的系统字体路径选择合适的字体
font_prop = font_manager.FontProperties(fname=font_path)

# 从失败总结中提取失败原因
fail_reasons = {
    "语法错误": 5,
    "逻辑错误": 6,
    "误判": 2,
}

# 生成饼图
labels = fail_reasons.keys()
sizes = fail_reasons.values()
colors = ['gold', 'lightcoral', 'lightyellow']
explode = (0.1, 0, 0)  # 仅突出显示第一个部分

plt.figure(figsize=(10, 7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontproperties': font_prop})
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.


# 调整图表的边距
plt.subplots_adjust(top=0.95)  # 调整顶部边距，增大标题与饼图之间的距离


# 显示图表
plt.title('失败原因统计', fontproperties=font_prop, fontsize=16, color='blue')  # 设置标题字体大小
# 保存图表
plt.savefig('fail_reasons_pie_chart.png', bbox_inches='tight', dpi=300)  # 保存为 PNG 文件，调整边距和分辨率

plt.show()