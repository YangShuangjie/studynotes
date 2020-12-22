<p style='text-align:center;font-family:LiSu;font-size:40px'>pyecharts绘图笔记</p>
<p style="text-align:center;font-family:XingSu;font-size:20px;">
    ——杨双杰 2018年5月3日
</p>
[TOC]


```python
# coding: utf-8
from pyecharts import configure,online
from pyecharts import online,Page
from pyecharts_snapshot.main import make_a_snapshot
# configure(output_image='png')
# chart.render(path='chart')
# make_a_snapshot('chart','chart.pdf')
online()
# page=Page()
```

# -----2D绘图-----

## 一、柱状图/条形图
### (一)数据堆叠柱状图
```python
# #-----2D绘图-----
# 一、柱状图/条形图
#     Bar（）#add可接受xyAxis,dataZoom,markLine&markPoint等通用配置
#     add(name, x_axis, y_axis,is_stack=False,
#         bar_category_gap='20%', **kwargs)
# (一)数据堆叠柱状图(最简单的是通过设置参数is_more_utils=True后点击图形按钮)
from pyecharts import Bar
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图数据堆叠示例")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True,is_more_utils=True)
# page.add(bar)
bar
```
![](plots/1.png)


### (二)带标记线、标记点的柱状图
```python
#(二)带标记线、标记点的柱状图
from pyecharts import Bar
bar = Bar("标记线和标记点示例")
bar.add("商家A", attr, v1, mark_point=["average"])
bar.add("商家B", attr, v2, mark_line=["min", "max"])
page.add(bar)
bar
```
![](2.png)

### (三)xy轴交换柱状图
```python
# (三)xy轴交换柱状图
from pyecharts import Bar
bar = Bar("x 轴和 y 轴交换")
bar.add("商家A", attr, v1)
bar.add("商家B", attr, v2, is_convert=True)
page.add(bar)
bar
```
![](3.png)


### （四）数据缩放柱状图
1. datazoom-slider

```python
# （四）数据缩放柱状图
# 1.datazoom-slider
import random
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - slider 示例")
bar.add("", attr, v1, is_label_show=True, is_datazoom_show=True)
page.add(bar)
bar
```
![](4.png)


2. datazoom-inside
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add("", attr, v1, is_datazoom_show=True, 
        datazoom_type='inside',datazoom_range=[10, 25])
page.add(bar)
bar
```
![](5.png)


3. datazoom-both
```python
attr = ["{}天".format(i) for i in range(30)]
v1 = [random.randint(1, 30) for _ in range(30)]
bar = Bar("Bar - datazoom - inside 示例")
bar.add("", attr, v1, is_datazoom_show=True, 
        datazoom_type='both',datazoom_range=[10, 25])
page.add(bar)
bar
```
![](6.png)


### (五)坐标轴标签旋转柱状图
```python
attr = ["{}天".format(i) for i in range(20)]
v1 = [random.randint(1, 20) for _ in range(20)]
bar = Bar("坐标轴标签旋转示例")
bar.add("", attr, v1, xaxis_interval=0, xaxis_rotate=30, 
        yaxis_rotate=30,label_color=['orange'])
page.add(bar)
bar
```
![](7.png)


### (六)瀑布图
```python
from pyecharts import Bar
attr = ["{}月".format(i) for i in range(1, 8)]
v1 = [0, 100, 200, 250, 275, 300, 350]
v2 = [1000, 800, 600, 500, 450, 400, 300]
bar = Bar("瀑布图示例")
# 利用第一个 add() 图例的颜色为透明,并且设置 is_stack 标志为 True.
bar.add("", attr, v1, label_color=['rgba(0,0,0,0)'], is_stack=True)
bar.add("月份", attr, v2, is_label_show=True, 
        is_stack=True, label_pos='inside')
page.add(bar)
bar
```
![](8.png)


### (七)直方图
```python
from pyecharts import Bar
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 21, 15, 9]
bar = Bar("直方图示例")
bar.add("", attr, v1 , bar_category_gap=0)
page.add(bar)
bar
```
![](9.png)

### -----pandas&numpy示例-----

```python
import numpy as np
import pandas as pd
from pyecharts import Bar
title = 'pd&np bar'
index = pd.date_range('2018-1-3',periods=6,freq='M')
df = pd.DataFrame(np.random.randint(-10,10,12).reshape(-1,2),index=index)
bar = Bar(title,'a and b distribution')
bar.add('a',index,df[0],mark_line=['average'],
        mark_point=['max','min'],is_more_utils=True,is_stack=True)
bar.add('b',index,df[1],mark_line=["average"],
        mark_point=["max","min"],is_stack=True)
page.add(bar)
bar
```
![](10.png)


## 二、折线/面积图
```python
#     Line（）#可接受xyAxis,dataZoom,lineStyle,markLine&markPoint通用配置
#     add(name, x_axis, y_axis,
#         is_symbol_show=True,
#         is_smooth=False,
#         is_stack=False,
#         is_step=False,
#         is_fill=False, **kwargs)
# name -> str
#     图例名称
# x_axis -> list
#     x 坐标轴数据
# y_axis -> list
#     y 坐标轴数据
# is_symbol_show -> bool
#     是否显示标记图形，默认为 True
# is_smooth -> bool
#     是否平滑曲线显示，默认为 False
# is_stack -> bool
#     数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置。默认为 False
# is_step -> bool/str
#     是否是阶梯线图。可以设置为 True 显示成阶梯线图。默认为 False
#     也支持设置成'start','middle','end'分别配置在当前点,中间,下个点拐弯。
# is_fill -> bool
#     是否填充曲线所绘制面积，默认为 False
```
### （一）标记点、线折线图
```python
from pyecharts import Line
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
v2 = [55, 60, 16, 20, 15, 80]
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average"])
line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
page.add(line)
line
```
![](11.png)



### （二）不同标记点形状折线图
```python
line = Line("折线图示例")
line.add("商家A", attr, v1, mark_point=["average", "max", "min"],
         mark_point_symbol='diamond', mark_point_textcolor='#40ff27')
line.add("商家B", attr, v2, mark_point=["average", "max", "min"],
         mark_point_symbol='arrow', mark_point_symbolsize=40)
page.add(line)
line
```
![](12.png)


### （三）指定标记点
```python
line = Line("折线图示例")
line.add("商家A", attr, v1,
            mark_point=["average", {
                "coord": ["裤子", 10], "name": "这是第一个标记点"}])
line.add("商家B", attr, v2, is_smooth=True,
            mark_point=[{
                "coord": ["袜子", 80], "name": "这是第二个标记点"}])
page.add(line)
line
```
![](13.png)


### (四)数据堆叠折线图
```python
line = Line("折线图-数据堆叠示例")
line.add("商家A", attr, v1, is_stack=True, is_label_show=True)
line.add("商家B", attr, v2, is_stack=True, is_label_show=True)
page.add(line)
line
```
![](14.png)


### (五)阶梯折线图
```python
line = Line("折线图-阶梯图示例")
line.add("商家A", attr, v1, is_step=True, is_label_show=True)
page.add(line)
line
```
![](15.png)


### （六）面积折线图
```python
line = Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2,
         area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000',
         area_opacity=0.3, is_smooth=True)
page.add(line)
line
```
![](16.png)



### (七)对数y轴折线图
```python
import math, random
line = Line("折线图示例")
line.add("商家A", attr, [
        math.log10(random.randint(1, 99999)) for _ in range(6)])
line.add("商家B", attr, [
        math.log10(random.randint(1, 99999999)) for _ in range(6)],
         yaxis_type="log")
page.add(line)
line
```
![](17.png)



### （八）自定义轴标签折线图
```python
from pyecharts import Line
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
line = Line("折线图示例")
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
         mark_point=["max", "min"],  mark_line=["average"],
         yaxis_formatter="°C")
# line.show_config()
page.add(line)
line
```
![](18.png)



## 三、箱形图
```python
#     Boxplot（）#可接受datazoom通用配置项
#     add(name, x_axis, y_axis, **kwargs)
#      y_axis -> [list], 嵌套列表
#         y_axis为二维数组,一个列表渲染一个box,含有五个量值，依次是：
#         [min, Q1, median (or Q2), Q3, max]
#         可自行计算出所需五个数值，也可通过内置 prepare_data()转换
from pyecharts import Boxplot
boxplot = Boxplot("箱形图")
x_axis = ['expr1', 'expr2']
y_axis1 = [[850, 740, 900, 1070, 930, 850, 950, 980, 980, 880,
            1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
            [960, 940, 960, 940, 880, 800, 850, 880, 900, 840,
            830, 790, 810, 880, 880, 830, 800, 790, 760, 800]]
y_axis2 = [[890, 810, 810, 820, 800, 770, 760, 740, 750, 760,
            910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
            [890, 840, 780, 810, 760, 810, 790, 810, 820, 850,
            870, 870, 810, 740, 810, 940, 950, 800, 810, 870]]
boxplot.add("category1", x_axis, boxplot.prepare_data(y_axis1))
boxplot.add("category2", x_axis, boxplot.prepare_data(y_axis2))
page.add(boxplot)
boxplot
```
![](19.png)



## 四、散点图
```python
#     Scatter（xyAxis,dataZoom）
#     add(name, x_axis, y_axis,extra_data=None,
#         symbol_size=10, **kwargs)
# name -> str
#     图例名称
# x_axis -> list
#     x 坐标轴数据
# y_axis -> list
#     y 坐标轴数据
# extra_data -> int
#     第三维度数据，x 轴为第一个维度，y 轴为第二个维度。
#     （可在 visualmap 中将视图元素映射到第三维度）
# symbol_size -> int
#     标记图形大小，默认为 10
```
### (一)数值轴散点图
```python
from pyecharts import Scatter
v1 = [10, 20, 30, 40, 50, 60]
v2 = [10, 20, 30, 40, 50, 60]
scatter = Scatter("散点图示例")
scatter.add("A", v1, v2)
scatter.add("B", v1[::-1], v2, is_visualmap=True,
           visual_type='size', visual_range_size=[20, 80])
page.add(scatter)
scatter
```
![](20.png)


#### 利用 Visualmap 组件映射到第三维度数据
```python
data = [
        [28604, 77, 17096869],
        [31163, 77.4, 27662440],
        [1516, 68, 1154605773],
        [13670, 74.7, 10582082],
        [28599, 75, 4986705],
        [29476, 77.1, 56943299],
        [31476, 75.4, 78958237],
        [28666, 78.1, 254830],
        [1777, 57.7, 870601776],
        [29550, 79.1, 122249285],
        [2076, 67.9, 20194354],
        [12087, 72, 42972254],
        [24021, 75.4, 3397534],
        [43296, 76.8, 4240375],
        [10088, 70.8, 38195258],
        [19349, 69.6, 147568552],
        [10670, 67.3, 53994605],
        [26424, 75.7, 57110117],
        [37062, 75.4, 252847810]
    ]

x_lst = [v[0] for v in data]
y_lst = [v[1] for v in data]
extra_data = [v[2] for v in data]
sc = Scatter()
sc.add("scatter", x_lst, y_lst, extra_data=extra_data,
        is_visualmap=True,visual_dimension=2,
        visual_orient='horizontal',visual_type='size', 
        visual_range=[254830, 1154605773],
        visual_text_color='#000')
page.add(sc)
sc
```
![](21.png)


### （二）类目轴散点图
```python
# 散点图默认的横坐标轴为数值轴,如想实现类目轴，可通过xaxis_type修改
scatter = Scatter("散点图示例")
scatter.add("A", ["a", "b", "c", "d", "e", "f"], v2)
scatter.add("B", ["a", "b", "c", "d", "e", "f"], v1[::-1], 
            xaxis_type="category")
page.add(scatter)
scatter
```
![](22.png)



### （三）散点图画画
```python
# Scatter 内置了画画方法
#     draw(path, color=None)
#     ''' 
#     将图片上的像素点转换为数组，如 color 为（255,255,255）
#     只保留非白色像素点的坐标信息，返回两个 k_lst, v_lst 
#     两个列表刚好作为散点图的数据项。
#     '''
#     path -> str
#         转换图片的地址
#     color -> str
#         所要排除的颜色

from pyecharts import Scatter
scatter = Scatter("散点图画画示例")
v1, v2 = scatter.draw("C:\\Users\\win10\\Pictures\\Camera Roll\\pika.png")
scatter.add("pika qiu~", v1, v2, is_random=True)
page.add(scatter)
scatter
```
![](23.png)

## 五、饼图
```python
#     Pie（）
#     add(name, attr, 
#         value,radius=None,
#         center=None,rosetype=None, **kwargs)
# name -> str
#     图例名称
# attr -> list
#     属性名称
# value -> list
#     属性所对应的值
# radius -> list
#     饼图的半径,数组的第一项是内半径,第二项是外半径,默认为[0,75]
#     默认设置成百分比，相对于容器高宽中较小的一项的一半
# center -> list
#     饼图的中心坐标,数组的第一项是横坐标,第二项是纵坐标,默认[50,50].
#     默认设置成百分比,设置成百分比时第一项是相对于容器宽度,
#     第二项是相对于容器高度
# rosetype -> str
#     是否展示成南丁格尔图，通过半径区分数据大小，
#     有'radius'和'area'两种模式。默认为'radius'
#     radius：扇区圆心角展现数据的百分比，半径展现数据的大小
#     area：所有扇区圆心角相同，仅通过半径展现数据大小
```
### (一)一般饼图
```python
from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")
pie.add("", attr, v1, is_label_show=True)
page.add(pie)
pie
```
![](24.png)


### （二）圆环图
```python
from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图-圆环图示例", title_pos='center')
pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
        is_label_show=True, legend_orient='vertical',
        legend_pos='left')
page.add(pie)
pie
```
![](25.png)


### （三）玫瑰图
```python
from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=700)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True,
        radius=[30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True,
        radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
page.add(pie)
pie
```
![](26.png)


### （四）饼中饼图
```python
import random
from pyecharts import Pie

attr = ['A', 'B', 'C', 'D', 'E', 'F']
pie = Pie("饼图示例", width=700, height=400)
pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
        radius=[50, 55], center=[25, 50], is_random=True)
pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
        radius=[0, 45], center=[25, 50], rosetype='area')

pie.add("", attr, [random.randint(0, 100) for _ in range(6)],
        radius=[50, 55], center=[65, 50], is_random=True)
pie.add("", attr, [random.randint(20, 100) for _ in range(6)],
        radius=[0, 45], center=[65, 50], rosetype='radius')
page.add(pie)
pie
```
![](27.png)


### (五)多个圆环
```python
from pyecharts import Pie,Style
pie = Pie('各类电影"好片"所占比例',"数据来自豆瓣",title_pos='center')
style = Style()
pie_style = style.add(
    label_pos="center",
    is_label_show=True,
    label_text_color=None,
#     legend_oreint = 'vertical',
#     legend_pos = 'left'
)
pie.add("", ["剧情", ""], [25, 75], center=[10, 30],
        radius=[18, 24], **pie_style)
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30],
        radius=[18, 24], **pie_style)
pie.add("", ["爱情", ""], [14, 86], center=[50, 30],
        radius=[18, 24], **pie_style)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30],
        radius=[18, 24], **pie_style)
pie.add("", ["冒险", ""], [27, 73], center=[90, 30],
        radius=[18, 24], **pie_style)
pie.add("", ["动作", ""], [15, 85], center=[10, 70],
        radius=[18, 24], **pie_style)
pie.add("", ["喜剧", ""], [54, 46], center=[30, 70],
        radius=[18, 24], **pie_style)
pie.add("", ["科幻", ""], [26, 74], center=[50, 70],
        radius=[18, 24], **pie_style)
pie.add("", ["悬疑", ""], [25, 75], center=[70, 70],
        radius=[18, 24], **pie_style)
pie.add("", ["犯罪", ""], [28, 72], center=[90, 70],
        radius=[18, 24], legend_top="center", **pie_style)
page.add(pie)
pie
```
![](28.png)


## 六、K线图
```python
#     Kline/Candlestick（）
#      可接受xyAxis,dataZoom,markLine&markPoint通用配置
#     add(name, x_axis, y_axis, **kwargs)
#       y_axis -> [list]
#         y坐标轴数据。数据中每一行是一个『数据项』,每一列属于一个『维度。 
#         数据项具体为 [open, close, lowest, highest]。
```

### (一)Kline
```python
from pyecharts import Kline
v1 = [[2320.26, 2320.26, 2287.3, 2362.94], [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92], [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76], [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15], [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42], [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89], [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8], [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94], [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88], [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71], [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16], [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54], [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44], [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67], [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29], [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
page.add(kline)
kline
```
![](29.png)


###（二）Kline + dataZoom
```python
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], 
          v1,mark_point=["max"], is_datazoom_show=True)
page.add(kline)
kline
```
![](30.png)


###（三）dataZoom 效果加在纵坐标轴上
```python
kline = Kline("K 线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)],
          v1,mark_point=["max"], is_datazoom_show=True,
          datazoom_orient='vertical')
page.add(kline)
kline
```
![](31.png)

### （四）指定 markLine 位于开盘或者收盘上

```python
kline = Kline("K线图示例")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)],
          v1,mark_line=["max"], mark_line_symbolsize=0.2,
          datazoom_orient='vertical', mark_line_valuedim=['close'])
page.add(kline)
kline
```
![](32.png)


## 七、热力图
```python
#     HeatMap（）
#     add(*args, **kwargs)
# 如果指定了 is_calendar_heatmap（使用日历热力图）为 True，则参数为：
#     name -> str
#         图例名称
#     data -> [list]
#         数据项每一行是一个『数据项』，每一列属于一个『维度』
#     calendar_date_range -> str/list
#         日历热力图的日期, "2016" 表示2016年, 
#         ["2016-5-5", "2017-5-5"] 表示2016年5月5日至2017年5月5日
#     calendar_cell_size -> list
#         日历每格框的大小,可设置单值或数组——第一个元素是宽,第二个元素是高，
#         支持设置自适应 "auto"。默认为 ["auto", 20]
# 默认为不指定，参数为：
#     name -> str
#         图例名称
#     x_axis -> str
#         x 坐标轴数据。需为类目轴，也就是不能是数值。
#     y_axis -> str
#         y 坐标轴数据。需为类目轴，也就是不能是数值。
#     data -> [list], 包含列表的列表
#         数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
```

### （一）非日历热力图（默认）

```python
import random
from pyecharts import HeatMap
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", 
    "6a", "7a", "8a", "9a", "10a", "11a",
    "12p", "1p", "2p", "3p", "4p", "5p", 
    "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = ["Saturday", "Friday", "Thursday",
          "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] 
        for i in range(24) for j in range(7)]
heatmap = HeatMap()
heatmap.add("热力图直角坐标系", x_axis, y_axis,
            data, is_visualmap=True,visual_text_color="#000",
            visual_orient='horizontal')
page.add(heatmap)
heatmap
```
![](33.png)


###（二）日历热力图
```python
import datetime
import random
from pyecharts import HeatMap
begin = datetime.date(2017, 1, 1)
end = datetime.date(2017, 12, 31)
data = [[str(begin + datetime.timedelta(days=i)),
        random.randint(1000, 25000)] 
        for i in range((end - begin).days + 1)]
heatmap = HeatMap("日历热力图示例", "某人2017年微信步数情况", width=1000)
heatmap.add("", data, is_calendar_heatmap=True,
            visual_text_color='#000', visual_range_text=['', ''],
            visual_range=[1000, 25000], calendar_cell_size=['auto', 30],
            is_visualmap=True, calendar_date_range="2017",
            visual_orient="horizontal", visual_pos="center",
            visual_top="80%", is_piecewise=True)
page.add(heatmap)
heatmap
```
![](34.png)


## 八、树图
```python
#     TreeMap（）
#     TreeMap()
#     add(name, attr, value,
#         shape="circle",
#         word_gap=20,
#         word_size_range=None,
#         rotate_step=45)
# name -> str
#     图例名称
# data -> list
#     树图的数据项是一棵树,每个节点包括value,name(可选),children(也是树,可选)
# treemap_left_depth -> int
#     leafDepth 表示『展示几层』，层次更深的节点则被隐藏起来。
#     设置了leafDepth后,下钻（drill down）功能开启。
#     drill down 功能即点击后才展示子层级。例如,leafDepth设置为1,表示展示一层节点。
# treemap_drilldown_icon -> str
#     当节点可以下钻时的提示符。只能是字符。默认为 '▶'
# treemap_visible_min -> int
#     如果某个节点的矩形的面积，小于这个数值（单位：px平方），这个节点就不显示。
```

### (一)默认TreeMap

```python
from pyecharts import TreeMap
data = [
    {
        "value": 40,
        "name": "我是A",
    },
    {
        "value": 180,
        "name": "我是B",
        "children": [
            {
                "value": 76,
                "name": "我是B.children",
                "children": [
                    {
                        "value": 12,
                        "name": "我是B.children.a",
                    },
                    {
                        "value": 28,
                        "name": "我是B.children.b",
                    },
                    {
                        "value": 20,
                        "name": "我是B.children.c",
                    },
                    {
                        "value": 16,
                        "name": "我是B.children.d",
                    }]
            }]}
]

treemap = TreeMap("树图-默认示例", width=700, height=400)
treemap.add("treemap", data, is_label_show=True, label_pos='inside')
page.add(treemap)
treemap
```
![](35.png)


### （二）下钻TreeMap
```python
from pyecharts import TreeMap
treemap = TreeMap("树图-下钻示例", width=700, height=400)
treemap.add("演示数据", data, is_label_show=True, label_pos='inside',
            treemap_left_depth=1)
page.add(treemap)
treemap
```
![](36.png)


```python
from pyecharts import TreeMap

treemap = TreeMap("树图示例", width=700, height=400)
import json
with open("E:\\Sublime Text 3\\Files\\Nbfiles\\cities.json", 
          "r", encoding="utf-8") as f:
    data = json.load(f)
treemap.add("cities", data, is_label_show=True, 
            label_pos='inside',treemap_left_depth=1)
page.add(treemap)
treemap
​```<!-- <if![]" w.png)


## 九、关系图
​```python
#     Graph（）#可接受lineStyle通用配置
#      add(name, nodes, links,
#         categories=None,
#         is_focusnode=True,
#         is_roam=True,
#         is_rotatelabel=False,
#         layout="force",
#         graph_edge_length=50,
#         graph_gravity=0.2,
#         graph_repulsion=50, **kwargs)
# name -> str
#     图例名称
# nodes -> dict
#     关系图结点，包含的数据项有
#     name：结点名称（必须有！）
#     x：节点的初始 x 值
#     y：节点的初始 y 值
#     value：结点数值
#     category：结点类目
#     symbol：标记图形
#     symbolSize：标记图形大小
# links -> dict
#     结点间的关系数据，包含的数据项有
#     source：边的源节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
#     target：边的目标节点名称的字符串，也支持使用数字表示源节点的索引（必须有！）
#     value：边的数值，可以在力引导布局中用于映射到边的长度
# categories -> list
#     结点分类的类目，结点可以指定分类，也可以不指定。
#     如果节点有分类的话可以通过 nodes[i].category 指定每个节点的类目，
#     类目的样式会被应用到节点样式上。
# is_focusnode -> bool
#     是否在鼠标移到节点上的时候突出显示节点以及节点的边和邻接节点。默认为 True
# is_roam -> bool/str
#     是否开启鼠标缩放和平移漫游。默认为 True
#     如果只想要开启缩放或平移，可以设置成'scale'或者'move'.设置成True为都开启
# is_rotatelabel -> bool
#     是否旋转标签，默认为 False
# graph_layout -> str
#     关系图布局，默认为 'force'
#     none：不采用任何布局，使用节点中必须提供的 x， y 作为节点的位置。
#     circular：采用环形布局
#     force：采用力引导布局
# graph_edge_length -> int
#     力布局下边的两个节点之间的距离，这个距离也会受 repulsion 影响。默认为 50
#     支持设置成数组表达边长范围,不同大小的值会线性映射到不同长度。值越小长度越长
# graph_gravity -> int
#     节点受到的向中心的引力因子。该值越大节点越往中心点靠拢。默认为 0.2
# graph_repulsion -> int
#     节点之间的斥力因子。默认为 50
#     支持设置成数组表达斥力范围,不同大小的值会线性映射到不同的斥力。值越大斥力越大
# graph_edge_symbol -> str/list
#     边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
#     默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol:['circle','arrow']
# graph_edge_symbolsize -> int/list
#     边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
```
### (一)关系图-力引导布局
```python
from pyecharts import Graph
nodes = [{"name": "结点1", "symbolSize": 10},
         {"name": "结点2", "symbolSize": 20},
         {"name": "结点3", "symbolSize": 30},
         {"name": "结点4", "symbolSize": 35},
         {"name": "结点5", "symbolSize": 40},
         {"name": "结点6", "symbolSize": 35},
         {"name": "结点7", "symbolSize": 30},
         {"name": "结点8", "symbolSize": 20}]
links = []
for i in nodes:
    for j in nodes:
        links.append({"source": i.get('name'), "target": j.get('name')})
graph = Graph("关系图-力引导布局示例")
graph.add("", nodes, links,graph_repulsion=500)
page.add(graph)
graph
```
![](38.png)


### (二)关系图-环形布局
```python
graph = Graph("关系图-环形布局示例")
graph.add("", nodes, links, is_label_show=True,
          graph_repulsion=8000, graph_layout='circular',
          label_text_color=None)
page.add(graph)
graph
```
![](39.png)

### （三）微博转发关系图

```python
# from pyecharts import Graph
# import json
# with open("data\weibo.json", "r", encoding="utf-8") as f:
#     j = json.load(f)
#     nodes, links, categories, cont, mid, userl = j
# graph = Graph("微博转发关系图", width=1200, height=600)
# graph.add("", nodes, links, categories, label_pos="right",
#           graph_repulsion=50, is_legend_show=False,
#           line_curve=0.2, label_text_color=None)
# graph
```

## 十、带有涟漪特效动画的散点图
```python
#     EffectScatter（）#可接受xyAxis,dataZoom通用配置
#     add(name, x_axis, y_axis,symbol,symbol_size=10, **kwargs)
#      symbol_size -> int 标记图形大小，默认为 10
#        symbol -> str
#          标记图形，有'rect', 'roundRect', 'triangle', 
#          'diamond', 'pin', 'arrow'可选
#        effect_brushtype -> str
#          波纹绘制方式，有'stroke', 'fill'可选。默认为'stroke'
#        effect_scale -> float
#          动画中波纹的最大缩放比例。默认为 2.5
#        effect_period -> float
#          动画持续的时间。默认为 4（s）
```
### (一) 一般动态散点图
```python
from pyecharts import EffectScatter
v1 = [10, 20, 30, 40, 50, 60]
v2 = [25, 20, 15, 10, 60, 33]
efsc = EffectScatter("动态散点图示例")
efsc.add("effectScatter", v1, v2)
page.add(efsc)
efsc
```
![](40.png)


### (二)各种样式动态散点图
```python
efsc = EffectScatter("动态散点图各种图形示例")
efsc.add("", [10], [10], symbol_size=20, effect_scale=3.5,
       effect_period=3, symbol="pin")
efsc.add("", [20], [20], symbol_size=12, effect_scale=4.5,
       effect_period=4,symbol="rect")
efsc.add("", [30], [30], symbol_size=30, effect_scale=5.5,
       effect_period=5,symbol="roundRect")
efsc.add("", [40], [40], symbol_size=10, effect_scale=6.5,
       effect_brushtype='fill',symbol="diamond")
efsc.add("", [50], [50], symbol_size=16, effect_scale=5.5,
       effect_period=3,symbol="arrow")
efsc.add("", [60], [60], symbol_size=6, effect_scale=2.5,
       effect_period=3,symbol="triangle")
page.add(efsc)
efsc
```
![](41.png)


## 十一、仪表盘
```python
#     Gauge（）
#     add(name,attr,value,scale_range=None,angle_range=None,**kwargs)
#      scale_range -> list 仪表盘数据范围。默认为 [0, 100]
#      angle_range -> list 仪表盘角度范围。默认为 [225, -45]
from pyecharts import Gauge
gauge = Gauge("仪表盘示例")
gauge.add("汽车仪表盘", "时速km/h", 130, angle_range=[180, 0],
          scale_range=[0, 200], is_legend_show=False)
#如何去掉百分号？或者不显示vlaue
page.add(gauge)
gauge
```
![](42.png)


## 十二、漏斗图
```python
#     Funnel（）
#      add(name, attr, value, **kwargs)
from pyecharts import Funnel
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
value = [20, 40, 60, 80, 100, 120]
funnel = Funnel("漏斗图示例", width=600, height=400, title_pos='center')
funnel.add("商品", attr, value, is_label_show=True, label_pos="outside",
           legend_orient='vertical', legend_pos='left')
page.add(funnel)
funnel
```
![](43.png)


## 十三、水球图
```python
#     Liquid（） 
#     add(name, data,
#         shape='circle',
#         liquid_color=None,
#         is_liquid_animation=True,
#         is_liquid_outline_show=True, **kwargs)
# name -> str
#     图例名称
# data -> list
#     数据项
# shape -> str
#     水球外形，有'circle', 'rect', 'roundRect', 'triangle',
#     'diamond','pin', 'arrow'可选。默认'circle'。可自定义SVG路径。
# liquid_color -> list
#     波浪颜色,默认颜色列表为['#294D99','#156ACF','#1598ED','#45BDFF']。
# is_liquid_animation -> bool
#     是否显示波浪动画，默认为 True。
# is_liquid_outline_show -> bool
#     是否显示边框，默认为 True。
```


### （一）圆形水球图
```python
from pyecharts import Liquid
liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6])
page.add(liquid)
liquid
```
![](44.png)

```python
from pyecharts import Liquid
liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], 
           is_liquid_outline_show=False)
page.add(liquid)
liquid
```
![](45.png)


### （二）钻石水球图
```python
from pyecharts import Liquid
liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
           is_liquid_animation=False, shape='diamond')
page.add(liquid)
liquid
```
![](46.png)


### （三）自定义SVG路径
```python
from pyecharts import Liquid
shape = ("path://M367.855,428.202c-3.674-1.385-7.452-1.966-11.146-1"
         ".794c0.659-2.922,0.844-5.85,0.58-8.719 c-0.937-10.407-7."
         "663-19.864-18.063-23.834c-10.697-4.043-22.298-1.168-29.9"
         "02,6.403c3.015,0.026,6.074,0.594,9.035,1.728 c13.626,5."
         "151,20.465,20.379,15.32,34.004c-1.905,5.02-5.177,9.115-9"
         ".22,12.05c-6.951,4.992-16.19,6.536-24.777,3.271 c-13.625"
         "-5.137-20.471-20.371-15.32-34.004c0.673-1.768,1.523-3.423"
         ",2.526-4.992h-0.014c0,0,0,0,0,0.014 c4.386-6.853,8.145-14"
         ".279,11.146-22.187c23.294-61.505-7.689-130.278-69.215-153"
         ".579c-61.532-23.293-130.279,7.69-153.579,69.202 c-6.371,"
         "16.785-8.679,34.097-7.426,50.901c0.026,0.554,0.079,1.121,"
         "0.132,1.688c4.973,57.107,41.767,109.148,98.945,130.793 c58."
         "162,22.008,121.303,6.529,162.839-34.465c7.103-6.893,17.826"
         "-9.444,27.679-5.719c11.858,4.491,18.565,16.6,16.719,28.643 "
         "c4.438-3.126,8.033-7.564,10.117-13.045C389.751,449.992,"
         "382.411,433.709,367.855,428.202z")
liquid = Liquid("水球图示例")
liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3],
           shape=shape, is_liquid_outline_show=False)
page.add(liquid)
liquid
```
![](47.png)


## 十四、地理坐标系
```python
#     Geo（）
#     add(name, attr, value,
#         type="scatter",
#         maptype='china',
#         symbol_size=12,
#         border_color="#111",
#         geo_normal_color="#323c48",
#         geo_emphasis_color="#2a333d",
#         geo_cities_coords=None,
#         is_roam=True, **kwargs)
#     type -> str
#         图例类型,有'scatter','effectScatter','heatmap'可选。
#     maptype -> str
#         地图类型。 支持 china、world、各城市地图。
#         提醒：在画市级地图的时候，城市名字后面的‘市’须省去.
#     symbol_size -> int
#         标记图形大小。默认为 12
#     border_color -> str
#         地图边界颜色。默认为 '#111'
#     geo_normal_color -> str
#         正常状态下地图区域的颜色。默认为 '#323c48'
#     geo_emphasis_color -> str
#         高亮状态下地图区域的颜色。默认为 '#2a333d'
#     geo_cities_coords -> dict
#         用户自定义地区经纬度，类似如 {'阿城':[126.58, 45.32],}这样的字典，
#         当用于提供了该参数时，将会覆盖原有预存的区域坐标信息。
#     is_roam -> bool
#         是否开启鼠标缩放和平移漫游。默认为 True
#         如果只想要开启缩放或者平移,可以设置成'scale'或者'move'。True为都开启。

```
### （一）Scatter 类型（连续型）
```python
from pyecharts import Geo
data = [
    ("海门", 9),("鄂尔多斯", 12),("招远", 12),("舟山", 12),
    ("齐齐哈尔", 14),("盐城", 15),("赤峰", 16),("青岛", 18),
    ("乳山", 18),("金昌", 19),("泉州", 21),("莱西", 21),
    ("日照", 21),("胶南", 22),("南通", 23),("拉萨", 24),
    ("云浮", 24),("梅州", 25),("文登", 25),("上海", 25),
    ("攀枝花", 25),("威海", 25),("承德", 25),("厦门", 26),
    ("汕尾", 26),("潮州", 26),("丹东", 27),("太仓", 27),
    ("曲靖", 27),("烟台", 28),("福州", 29),("瓦房店", 30),
    ("即墨", 30),("抚顺", 31),("玉溪", 31),("张家口", 31),
    ("阳泉", 31),("莱州", 32),("湖州", 32),("汕头", 32),
    ("昆山", 33),("宁波", 33),("湛江", 33),("揭阳", 34),
    ("荣成", 34),("连云港", 35),("葫芦岛", 35),("常熟", 36),
    ("东莞", 36),("河源", 36),("淮安", 36),("泰州", 36),
    ("南宁", 37),("营口", 37),("惠州", 37),("江阴", 37),
    ("蓬莱", 37),("韶关", 38),("嘉峪关", 38),("广州", 38),
    ("延安", 38),("太原", 39),("清远", 39),("中山", 39),
    ("昆明", 39),("寿光", 40),("盘锦", 40),("长治", 41),
    ("深圳", 41),("珠海", 42),("宿迁", 43),("咸阳", 43),
    ("铜川", 44),("平度", 44),("佛山", 44),("海口", 44),
    ("江门", 45),("章丘", 45),("肇庆", 46),("大连", 47),
    ("临汾", 47),("吴江", 47),("石嘴山", 49),("沈阳", 50),
    ("苏州", 50),("茂名", 50),("嘉兴", 51),("长春", 51),
    ("胶州", 52),("银川", 52),("张家港", 52),("三门峡", 53),
    ("锦州", 54),("南昌", 54),("柳州", 54),("三亚", 54),
    ("自贡", 56),("吉林", 56),("阳江", 57),("泸州", 57),
    ("西宁", 57),("宜宾", 58),("呼和浩特", 58),("成都", 58),
    ("大同", 58),("镇江", 59),("桂林", 59),("张家界", 59),
    ("宜兴", 59),("北海", 60),("西安", 61),("金坛", 62),
    ("东营", 62),("牡丹江", 63),("遵义", 63),("绍兴", 63),
    ("扬州", 64),("常州", 64),("潍坊", 65),("重庆", 66),
    ("台州", 67),("南京", 67),("滨州", 70),("贵阳", 71),
    ("无锡", 71),("本溪", 71),("克拉玛依", 72),("渭南", 72),
    ("马鞍山", 72),("宝鸡", 72),("焦作", 75),("句容", 75),
    ("北京", 79),("徐州", 79),("衡水", 80),("包头", 80),
    ("绵阳", 80),("乌鲁木齐", 84),("枣庄", 84),("杭州", 84),
    ("淄博", 85),("鞍山", 86),("溧阳", 86),("库尔勒", 86),
    ("安阳", 90),("开封", 90),("济南", 92),("德阳", 93),
    ("温州", 95),("九江", 96),("邯郸", 98),("临安", 99),
    ("兰州", 99),("沧州", 100),("临沂", 103),("南充", 104),
    ("天津", 105),("富阳", 106),("泰安", 112),("诸暨", 112),
    ("郑州", 113),("哈尔滨", 114),("聊城", 116),("芜湖", 117),
    ("唐山", 119),("平顶山", 119),("邢台", 119),("德州", 120),
    ("济宁", 120),("荆州", 127),("宜昌", 130),("义乌", 132),
    ("丽水", 133),("洛阳", 134),("秦皇岛", 136),("株洲", 143),
    ("石家庄", 147),("莱芜", 148),("常德", 152),("保定", 153),
    ("湘潭", 154),("金华", 157),("岳阳", 169),("长沙", 175),
    ("衢州", 177),("廊坊", 193),("菏泽", 194),("合肥", 229),
    ("武汉", 273),("大庆", 279)]

geo = Geo("全国主要城市空气质量", "data from pm2.5",
          title_color="#fff",
          title_pos="center", width=700,
          height=400, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], 
        visual_text_color="#fff",symbol_size=15,
        is_visualmap=True,border_color='orange',
        geo_emphasis_color='black')
page.add(geo)
geo
```
![](48.png)


### (二)Scatter 类型（分段型）
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", 
          title_color="#fff",
          title_pos="center", width=700,
          height=400, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200],
        visual_text_color="#fff",
        symbol_size=15, is_visualmap=True,
        is_piecewise=True, visual_split_number=6)
page.add(geo)
geo
```
![](49.png)


### （三）HeatMap 类型
```python
geo = Geo("全国主要城市空气质量", "data from pm2.5", 
          title_color="#fff",
          title_pos="center", width=700,
          height=400, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="heatmap", 
        is_visualmap=True, visual_range=[0, 300],
        visual_text_color='#fff')
page.add(geo)
geo
```
![](50.png)


### （四）EffectScatter 类型（全国）
```python
from pyecharts import Geo
data = [("海门", 9), ("鄂尔多斯", 12), ("招远", 12),
    ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
geo = Geo("全国主要城市空气质量", "data from pm2.5", 
          title_color="#fff",
          title_pos="center", width=700,
          height=400, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, type="effectScatter", 
        is_random=True, effect_scale=5)
page.add(geo)
geo
```
![](51.png)


### （五）EffectScatter 类型（四川）
```python
from pyecharts import Geo
data =[('成都市', 50), ('眉山市', 60), ('宜宾市', 35),
    ('乐山市', 44), ('广元市', 72)]
geo = Geo("四川城市空气质量", "data from pm2.5",
          title_color="#fff",
          title_pos="center", width=700,
          height=400, background_color='#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, maptype='四川', type="effectScatter",
        is_random=True, effect_scale=5, is_legend_show=False)
page.add(geo)
geo
```
![](52.png)


## 十五、地理坐标系线图
```python
#     GeoLines（）
#         add(name, data,
#         maptype='china',
#         symbol=None,
#         symbol_size=12,
#         border_color="#111",
#         geo_normal_color="#323c48",
#         geo_emphasis_color="#2a333d",
#         geo_cities_coords=None,
#         geo_effect_period=6,
#         geo_effect_traillength=0,
#         geo_effect_color='#fff',
#         geo_effect_symbol='circle',
#         geo_effect_symbolsize=5,
#         is_geo_effect_show=True,
#         is_roam=True, **kwargs)
# name -> str
#     图例名称
# data -> [list]
#     数据项，数据中每一行是一个『数据项』，每一列属于一个『维度』。
#     每一行包含两个数据, 如 ["广州", "北京"]，则指定从广州到北京。
# maptype -> str
#     地图类型。 支持 china、world、各城市地图。
#     城市名字后面的‘市’须省去,如眉山市直接写作眉山。
# symbol -> str
#     线两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。
# symbol_size -> int
#     线两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
# geo_effect_period -> int/float
#     特效动画的时间，单位为 s，默认为 6s
# geo_effect_traillength -> float
#     特效尾迹的长度。取从 0 到 1 的值，数值越大尾迹越长。默认为 0
# geo_effect_color -> str
#     特效标记的颜色。默认为 '#fff'
# geo_effect_symbol -> str
#     特效图形的标记。有 'circle', 'rect', 'roundRect', 'triangle',
#     'diamond', 'pin', 'arrow', 'plane' 可选。
# geo_effect_symbolsize -> int/list
#     特效标记的大小，可设置成诸如10这样单一的数字，也可用数组分开表示高和宽，
#     例如 [20, 10] 表示标记宽为 20，高为 10。
# is_geo_effect_show -> bool
#     是否显示特效。
# border_color -> str
#     地图边界颜色。默认为 '#111'
# geo_normal_color -> str
#     正常状态下地图区域的颜色。默认为 '#323c48'
# geo_emphasis_color -> str
#     高亮状态下地图区域的颜色。默认为 '#2a333d'
# geo_cities_coords -> dict
#     用户自定义地区经纬度，类似如 {'阿城': [126.58, 45.32],} 这样的字典，
#     当用于提供了该参数时，将会覆盖原有预存的区域坐标信息。
# is_roam -> bool
#     是否开启鼠标缩放和平移漫游。默认为 True。如果只想要开启缩放或者平移，
#     可以设置成'scale'或者'move'。设置成 True 为都开启
```

### （一）默认效果
```python
from pyecharts import GeoLines, Style
style = Style(
    title_top="#fff",
    width=700,
    height=400,
    background_color="#404a59"
)

data_chengdu = [["成都", "上海"],
                ["成都", "北京"],
                ["成都", "南京"],
                ["成都", "重庆"],
                ["成都", "兰州"],
                ["成都", "杭州"]]
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从成都出发", data_chengdu)
page.add(geolines)
geolines
```
![](53.png)


### (二)配置效果
```python
from pyecharts import GeoLines, Style
style_geo = style.add(
    is_label_show=True,
    line_curve=0.2,
    line_opacity=0.6,
    legend_text_color="#eee",
    legend_pos="right",
    geo_effect_symbol="plane",
    geo_effect_symbolsize=15,
    label_color=['#a6c84c', '#ffa022', '#46bee9'],
    label_pos="right",
    label_formatter="{b}",
    label_text_color="#eee",
#     legend_selectedmode="single", #指定单例模式
)
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从成都出发", data_chengdu, **style_geo)
page.add(geolines)
geolines
```
![](54.png)


### (三)多例模式
```python
#单例模式，在style_geo中指定 legend_selectedmode="single"
from pyecharts import GeoLines, Style
data_beijing = [
    ["北京", "上海"],
    ["北京", "成都"],
    ["北京", "南京"],
    ["北京", "重庆"],
    ["北京", "兰州"],
    ["北京", "杭州"]
]
geolines = GeoLines("GeoLines 示例", **style.init_style)
geolines.add("从成都出发", data_chengdu, **style_geo)
geolines.add("从北京出发", data_beijing, **style_geo)
page.add(geolines)
geolines
```
![](55.png)


## 十六、地图
```python
#     Map（）
#     add(name, attr, value,
#         maptype='china',
#         is_roam=True,
#         is_map_symbol_show=True, **kwargs)
# name -> str
#     图例名称
# attr -> list
#     属性名称
# value -> list
#     属性所对应的值
# maptype -> str
#     地图类型。 支持 china、world及各省市。
# is_roam -> bool/str
#     是否开启鼠标缩放和平移漫游。默认为 True。如果只想要开启缩放
#     或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
# is_map_symbol_show -> bool
#     是否显示地图标记红点，默认为 True。
# name_map -> dict
#     用自定义的地图名称. 有些地图提供行政区号，
#     name_map 可以帮助把它们转换成用户满意的地名。
#     比如英国选区地图，伦敦选区的行政区号是 E14000639 ，
#     把它转换成可读地名就需要这么一个字典：
#       name_map = {"E14000639": "Cities of London and Westminster"}
```
### (一)中国地图
```python
from pyecharts import Map
value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
_map = Map("全国地图示例", width=700, height=400)
_map.add("", attr, value, maptype='china',is_label_show=True)
page.add(_map)
_map
```
![](56.png)


### (二)VisualMap中国地图 
```python
from pyecharts import Map
value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = ["福建","山东","北京","上海","甘肃","新疆","河南","广西","西藏"]
_map = Map("Map 结合 VisualMap 示例", width=700, height=400)
_map.add("", attr, value, maptype='china', is_visualmap=True,
        visual_text_color='#000')
page.add(_map)
_map
```
![](57.png)


### (三)visualmap省市地图
```python
from pyecharts import Map
value = [20, 190, 253, 77, 65,435]
attr = ['汕头市', '汕尾市', '揭阳市', '阳江市', '肇庆市','深圳市']
_map = Map("广东地图示例", width=700, height=400)
_map.add("", attr, value, maptype='广东', is_isualmap=True,
        visual_text_color='#000')
page.add(_map)
_map
```
![](58.png)


### (四)世界地图
```python
from pyecharts import Map
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]
_map = Map("世界地图示例", width=700, height=400)
_map.add("", attr, value, maptype="world", is_visualmap=True,
        visual_text_color='#000')
# 设置 is_map_symbol_show=False 取消显示标记红点
_map
```
![](59.png)



### (五)自定义地图
```python
# from pyecharts import Map
# from echarts_united_kingdom_pypkg import NM_WESTMINSTER_2016_UK
# value = []
# attr = []
# _map = Map('United Kingdom', width=700, height=400)
# _map.add('', attr, value, maptype='英国选区2016', is_visualmap=True,
#         visual_text_color="#000", name_map=NM_WESTMINSTER_2016_UK)
# _map
```

### (六)视觉颜色分段地图
```python
from pyecharts import Map
value = [155, 10, 66, 78]
attr = ["福建", "山东", "北京", "上海"]
_map = Map("全国地图示例", width=700, height=400)
_map.add("", attr, value, maptype='china',
        is_visualmap=True, is_piecewise=True,
        visual_text_color="#000",
        visual_range_text=["", ""],
        pieces=[
            {"max": 160, "min": 70, "label": "高数值"},
            {"max": 69, "min": 0, "label": "低数值"},
        ])
page.add(_map)
_map
```
![](60.png)


## 十七、平行坐标系
```python
#     Parallel（）#可接受lineStyle通用配置
#   1.add(name, data, **kwargs)
#     name -> str
#         图例名称
#     data -> [list], 包含列表的列表
#         数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』
#   2.config(schema=None, c_schema=None)
#     schema
#     默认平行坐标系的坐标轴信息，如["dim_name1","dim_name2","dim_name3"]。
#     c_schema
#     用户自定义平行坐标系的坐标轴信息。
#         dim -> int
#             维度索引
#         name -> str
#             维度名称
#         type -> str
#             维度类型，有'value', 'category'可选
#             value：数值轴，适用于连续数据。
#             category： 类目轴，适用于离散的类目数据。
#         min -> int
#             坐标轴刻度最小值。
#         max -> int
#             坐标轴刻度最大值。
#         inverse - bool
#             是否是反向坐标轴。默认为 False
#         nameLocation -> str
#             坐标轴名称显示位置。有'start', 'middle', 'end'可选
```

### (一)默认平行坐标系
```python
from pyecharts import Parallel
schema = ["data", "AQI", "PM2.5", "PM10", "CO", "NO2"]
data = [
        [1, 91, 45, 125, 0.82, 34],
        [2, 65, 27, 78, 0.86, 45,],
        [3, 83, 60, 84, 1.09, 73],
        [4, 109, 81, 121, 1.28, 68],
        [5, 106, 77, 114, 1.07, 55],
        [6, 109, 81, 121, 1.28, 68],
        [7, 106, 77, 114, 1.07, 55],
        [8, 89, 65, 78, 0.86, 51, 26],
        [9, 53, 33, 47, 0.64, 50, 17],
        [10, 80, 55, 80, 1.01, 75, 24],
        [11, 117, 81, 124, 1.03, 45]
]
parallel = Parallel("平行坐标系-默认指示器")
parallel.config(schema=schema) 
parallel.add("parallel", data, is_random=True)
page.add(parallel)
parallel
```
![](61.png)


### (二)用户自定义平行坐标系
```python
from pyecharts import Parallel
c_schema = [
    {"dim": 0, "name": "data"},
    {"dim": 1, "name": "AQI"},
    {"dim": 2, "name": "PM2.5"},
    {"dim": 3, "name": "PM10"},
    {"dim": 4, "name": "CO"},
    {"dim": 5, "name": "NO2"},
    {"dim": 6, "name": "CO2"},
    {"dim": 7, "name": "等级",
    "type": "category",
    "data": ['优','良','轻度污染','中度污染','重度污染','严重污染']}
]
data = [
    [1, 91, 45, 125, 0.82, 34, 23, "良"],
    [2, 65, 27, 78, 0.86, 45, 29, "良"],
    [3, 83, 60, 84, 1.09, 73, 27, "良"],
    [4, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [5, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [6, 109, 81, 121, 1.28, 68, 51, "轻度污染"],
    [7, 106, 77, 114, 1.07, 55, 51, "轻度污染"],
    [8, 89, 65, 78, 0.86, 51, 26, "良"],
    [9, 53, 33, 47, 0.64, 50, 17, "良"],
    [10, 80, 55, 80, 1.01, 75, 24, "良"],
    [11, 117, 81, 124, 1.03, 45, 24, "轻度污染"],
    [12, 99, 71, 142, 1.1, 62, 42, "良"],
    [13, 95, 69, 130, 1.28, 74, 50, "良"],
    [14, 116, 87, 131, 1.47, 84, 40, "轻度污染"]
]
parallel = Parallel("平行坐标系-用户自定义指示器")
parallel.config(c_schema=c_schema)
parallel.add("parallel", data)
page.add(parallel)
parallel
```
![](62.png)


## 十八、极坐标系
```python
#     Polar（lineStyle）
#     add(name, data,
#         angle_data=None,
#         radius_data=None,
#         type='line',
#         symbol_size=4,
#         start_angle=90,
#         rotate_step=0,
#         boundary_gap=True,
#         clockwise=True, **kwargs)
# name -> str
#     图例名称
# data -> [list], 包含列表的列表
#     数据项 [极径，极角 [数据值]]
# angle_data -> list
#     角度类目数据
# radius_data -> list
#     半径类目数据
# type -> str
#     图例类型，有'line', 'scatter', 'effectScatter', 
#     'barAngle', 'barRadius'可选。默认为 'line'
# symbol_size -> int
#     标记图形大小，默认为 4。
# start_angle -> int
#     起始刻度的角度，默认为 90 度，即圆心的正上方。0 度为圆心的正右方
# rotate_step -> int
#     刻度标签旋转的角度，在类目轴的类目标签显示不下的时候
#     可以通过旋转防止标签之间重叠旋转的角度从-90到90度。默认0
# boundary_gap -> bool
#     坐标轴两边留白策略
#     默认为 True，这时候刻度只是作为分隔线，
#     标签和数据点都会在两个刻度之间的带(band)中间
# clockwise -> bool
#     刻度增长是否按顺时针，默认 True
# is_stack -> bool
#     数据堆叠，同个类目轴上系列配置相同的 stack 值可以堆叠放置
# axis_range -> list
#     坐标轴刻度范围。默认值为 [None, None]。
# is_angleaxis_show -> bool
#     是否显示极坐标系的角度轴，默认为 True
# radiusaxis_z_index -> int 
#     radius 轴的 z 指数，默认为 50
# angleaxis_z_index -> int 
#     angel 轴的 z 指数，默认为 50
# is_radiusaxis_show -> bool
#     是否显示极坐标系的径向轴，默认为 True
# is_splitline_show -> bool
#     是否显示分割线，默认为 True
# is_axisline_show -> bool
#     是否显示坐标轴线，默认为 True
# area_opacity -> float
#     填充区域透明度
# area_color -> str
#     填充区域颜色
# param render_item -> function 
#     开发者自己提供图形渲染的逻辑,这个渲染逻辑一般命名为 render_item
# def render_item(params, api):
#     values = [api.value(0), api.value(1)]
#     coord = api.coord(values)
#     size = api.size([1, 1], values)
#     return {
#         "type": 'sector',
#         "shape": {
#             "cx": params.coordSys.cx,
#             "cy": params.coordSys.cy,
#             "r0": coord[2] - size[0] / 2,
#             "r": coord[2] + size[0] / 2,
#             "startAngle": coord[3] - size[1] / 2,
#             "endAngle": coord[3] + size[1] / 2,
#         },
#         "style": api.style({"fill": api.visual('color')}),
#     }

```
### (一)极坐标散点图
```python
from pyecharts import Polar
import random
data_1 = [(10, random.randint(1, 100)) for i in range(300)]
data_2 = [(11, random.randint(1, 100)) for i in range(300)]
data_3 = [(9, random.randint(1, 100)) for _ in range(300)]
data_4 = [(12,random.randint(1, 100)) for _ in range(300)]
polar = Polar("极坐标系-散点图示例", width=700, height=400)
polar.add("", data_1, type='scatter')
polar.add("", data_2, type='scatter')
polar.add("", data_3, type='scatter')
polar.add("", data_4, type='scatter')
page.add(polar)
polar
```
![](63.png)


### (二)极坐标动态散点图
```python
from pyecharts import Polar
import random
data_1 = [(10, random.randint(1, 30)) for i in range(70)]
data_2 = [(11, random.randint(1, 30)) for i in range(80)]
data_3 = [(12,random.randint(1, 30)) for _ in range(110)]
polar = Polar("极坐标系-散点图示例", width=700, height=400)
polar.add("", data_1, type='effectScatter', 
          effect_scale=3, effect_period=5)
polar.add("", data_2, type='effectScatter',
          effect_scale=4, effect_period=5)
polar.add("", data_3, type='effectScatter',
          effect_scale=5, effect_period=5)
page.add(polar)
polar
```
![](64.png)


### （三）极坐标堆叠柱状图-barRadius
```python
from pyecharts import Polar
radius = ['周一','周二','周三','周四','周五','周六','周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=700, height=400)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius,
          type='barRadius', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius,
          type='barRadius', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius,
          type='barRadius', is_stack=True)
page.add(polar)
polar
```
![](65.png)


### （四）极坐标堆叠柱状图-barAngle
```python
from pyecharts import Polar
radius = ['周一','周二','周三','周四','周五','周六','周日']
polar = Polar("极坐标系-堆叠柱状图示例", width=700, height=400)
polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius,
          type='barAngle', is_stack=True)
polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius,
          type='barAngle', is_stack=True)
polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius,
          type='barAngle', is_stack=True)
page.add(polar)
polar
```
![](66.png)


## 十九、雷达图
```python
#     Radar（lineStyle）
#     1.add(name, value,item_color=None, **kwargs)
# name -> list
#     图例名称
# value -> [list], 包含列表的列表
#     数据项。数据中，每一行是一个『数据项』，每一列属于一个『维度』
# item_color -> str
#     指定单图例颜色

#     2.config(schema=None,c_schema=None, shape="",
#             rader_text_color="#000", **kwargs)
# schema -> list
#     默认雷达图的指示器，用来指定雷达图中的多个维度，
#     会对数据处理成 {name:xx, value:xx} 的字典
# c_schema -> dict
#     用户自定义雷达图的指示器，用来指定雷达图中的多个维度
#     name: 指示器名称
#     min: 指示器最小值
#     max: 指示器最大值
# shape -> str
#     雷达图绘制类型，有'polygon'（多边形）和'circle'可选
# rader_text_color -> str
#     雷达图数据项字体颜色，默认为'#000'
# radar_text_size -> int
#     雷达图m数据项字体大小，默认为 12
# is_area_show -> bool
#     是否显示填充区域
# area_opacity -> float
#     填充区域透明度
# area_color -> str
#     填充区域颜色
# is_splitline_show -> bool
#     是否显示分割线，默认为 True
# is_axisline_show -> bool
#     是否显示坐标轴线，默认为 True
# symblo=None 
#     可隐藏标记图形（小圆圈）
```
### (一)polygon雷达图
```python
from pyecharts import Radar
schema = [ 
    ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
    ("客服", 38000), ("研发", 52000), ("市场", 25000)
]
v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
radar = Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, 
          is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], 
          is_area_show=False,
          legend_selectedmode='single')
page.add(radar)
radar
```
![](67.png)


### （二）circle雷达图
```python
value_bj = [
    [55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2],
    [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4],
    [42, 24, 44, 0.76, 40, 16, 5], [82, 58, 90, 1.77, 68, 33, 6],
    [74, 49, 77, 1.46, 48, 27, 7], [78, 55, 80, 1.29, 59, 29, 8],
    [267, 216, 280, 4.8, 108, 64, 9], [185, 127, 216, 2.52, 61, 27, 10],
    [39, 19, 38, 0.57, 31, 15, 11], [41, 11, 40, 0.43, 21, 7, 12],
    [64, 38, 74, 1.04, 46, 22, 13], [108, 79, 120, 1.7, 75, 41, 14],
    [108, 63, 116, 1.48, 44, 26, 15], [33, 6, 29, 0.34, 13, 5, 16],
    [94, 66, 110, 1.54, 62, 31, 17], [186, 142, 192, 3.88, 93, 79, 18],
    [57, 31, 54, 0.96, 32, 14, 19], [22, 8, 17, 0.48, 23, 10, 20],
    [39, 15, 36, 0.61, 29, 13, 21], [94, 69, 114, 2.08, 73, 39, 22],
    [99, 73, 110, 2.43, 76, 48, 23], [31, 12, 30, 0.5, 32, 16, 24],
    [42, 27, 43, 1, 53, 22, 25], [154, 117, 157, 3.05, 92, 58, 26],
    [234, 185, 230, 4.09, 123, 69, 27],[160, 120, 186, 2.77, 91, 50, 28],
    [134, 96, 165, 2.76, 83, 41, 29], [52, 24, 60, 1.03, 50, 21, 30],
]
value_sh = [
    [91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2],
    [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4],
    [106, 77, 114, 1.07, 55, 51, 5], [109, 81, 121, 1.28, 68, 51, 6],
    [106, 77, 114, 1.07, 55, 51, 7], [89, 65, 78, 0.86, 51, 26, 8],
    [53, 33, 47, 0.64, 50, 17, 9], [80, 55, 80, 1.01, 75, 24, 10],
    [117, 81, 124, 1.03, 45, 24, 11], [99, 71, 142, 1.1, 62, 42, 12],
    [95, 69, 130, 1.28, 74, 50, 13], [116, 87, 131, 1.47, 84, 40, 14],
    [108, 80, 121, 1.3, 85, 37, 15], [134, 83, 167, 1.16, 57, 43, 16],
    [79, 43, 107, 1.05, 59, 37, 17], [71, 46, 89, 0.86, 64, 25, 18],
    [97, 71, 113, 1.17, 88, 31, 19], [84, 57, 91, 0.85, 55, 31, 20],
    [87, 63, 101, 0.9, 56, 41, 21], [104, 77, 119, 1.09, 73, 48, 22],
    [87, 62, 100, 1, 72, 28, 23], [168, 128, 172, 1.49, 97, 56, 24],
    [65, 45, 51, 0.74, 39, 17, 25], [39, 24, 38, 0.61, 47, 17, 26],
    [39, 24, 39, 0.59, 50, 19, 27], [93, 68, 96, 1.05, 79, 29, 28],
    [188, 143, 197, 1.66, 99, 51, 29], [174, 131, 174, 1.55, 108, 50, 30],
]
c_schema= [{"name": "AQI", "max": 300, "min": 5},
           {"name": "PM2.5", "max": 250, "min": 20},
           {"name": "PM10", "max": 300, "min": 5},
           {"name": "CO", "max": 5},
           {"name": "NO2", "max": 200},
           {"name": "SO2", "max": 100}]
radar = Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None,
          legend_selectedmode='single')
page.add(radar)
radar
```
![](68.png)


## 二十、桑基图
```python
#     Sankey（）
#     add(name, nodes, links,
#         sankey_node_width=20,
#         sankey_node_gap=8, **kwargs)
# name -> str
#     图例名称
# nodes -> list
#     桑基图结点，必须包含的数据项有：
#     name：数据项名称
#     value：数据项数值
# links -> list
#     桑基图结点关系
#     source：边的源节点名称（必须有！）
#     target：边的目标节点名称（必须有！）
#     value：边的数值，决定边的宽度。
# sankey_node_width -> int
#     图中每个矩形节点的宽度。默认为 20
# sankey_node_gap -> int
#     图中每一列任意两个矩形节点之间的间隔。默认为 8

from pyecharts import Sankey
nodes = [
    {'name': 'category1'}, {'name': 'category2'}, 
    {'name': 'category3'},{'name': 'category4'}, 
    {'name': 'category5'}, {'name': 'category6'},
]

links = [
    {'source':'category1','target':'category2','value':10},
    {'source':'category2','target':'category3','value':15},
    {'source':'category3','target':'category4','value':20},
    {'source':'category5','target':'category6','value':25}
]
sankey = Sankey("桑基图示例", width=900, height=600)
sankey.add("sankey", nodes, links, line_opacity=0.2,
           line_curve=0.5, line_color='source',
           is_label_show=True, label_pos='right')
page.add(sankey)
sankey
```
![](69.png)


## 二十一、主题河流图
```python
#     ThemeRiver（）
#     add(name, data)
# name -> list
#     图例名称，必须为 list 类型，list 中每个值为数据项中的种类。
# data -> [list], 包含列表的列表
#     数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』。
#     每个数据项至少需要三个维度，如 
#     ['2015/11/08', 10, 'DQ']，分别为 [时间，数值，种类（图例名）]
```
```python
from pyecharts import ThemeRiver

data = [
    ['2015/11/08', 10, 'DQ'], ['2015/11/09', 15, 'DQ'], ['2015/11/10', 35, 'DQ'],
    ['2015/11/14', 7, 'DQ'], ['2015/11/15', 2, 'DQ'], ['2015/11/16', 17, 'DQ'],
    ['2015/11/17', 33, 'DQ'], ['2015/11/18', 40, 'DQ'], ['2015/11/19', 32, 'DQ'],
    ['2015/11/20', 26, 'DQ'], ['2015/11/21', 35, 'DQ'], ['2015/11/22', 40, 'DQ'],
    ['2015/11/23', 32, 'DQ'], ['2015/11/24', 26, 'DQ'], ['2015/11/25', 22, 'DQ'],
    ['2015/11/08', 35, 'TY'], ['2015/11/09', 36, 'TY'], ['2015/11/10', 37, 'TY'],
    ['2015/11/11', 22, 'TY'], ['2015/11/12', 24, 'TY'], ['2015/11/13', 26, 'TY'],
    ['2015/11/14', 34, 'TY'], ['2015/11/15', 21, 'TY'], ['2015/11/16', 18, 'TY'],
    ['2015/11/17', 45, 'TY'], ['2015/11/18', 32, 'TY'], ['2015/11/19', 35, 'TY'],
    ['2015/11/20', 30, 'TY'], ['2015/11/21', 28, 'TY'], ['2015/11/22', 27, 'TY'],
    ['2015/11/23', 26, 'TY'], ['2015/11/24', 15, 'TY'], ['2015/11/25', 30, 'TY'],
    ['2015/11/26', 35, 'TY'], ['2015/11/27', 42, 'TY'], ['2015/11/28', 42, 'TY'],
    ['2015/11/08', 21, 'SS'], ['2015/11/09', 25, 'SS'], ['2015/11/10', 27, 'SS'],
    ['2015/11/11', 23, 'SS'], ['2015/11/12', 24, 'SS'], ['2015/11/13', 21, 'SS'],
    ['2015/11/14', 35, 'SS'], ['2015/11/15', 39, 'SS'], ['2015/11/16', 40, 'SS'],
    ['2015/11/17', 36, 'SS'], ['2015/11/18', 33, 'SS'], ['2015/11/19', 43, 'SS'],
    ['2015/11/20', 40, 'SS'], ['2015/11/21', 34, 'SS'], ['2015/11/22', 28, 'SS'],
    ['2015/11/14', 7, 'QG'], ['2015/11/15', 2, 'QG'], ['2015/11/16', 17, 'QG'],
    ['2015/11/17', 33, 'QG'], ['2015/11/18', 40, 'QG'], ['2015/11/19', 32, 'QG'],
    ['2015/11/20', 26, 'QG'], ['2015/11/21', 35, 'QG'], ['2015/11/22', 40, 'QG'],
    ['2015/11/23', 32, 'QG'], ['2015/11/24', 26, 'QG'], ['2015/11/25', 22, 'QG'],
    ['2015/11/26', 16, 'QG'], ['2015/11/27', 22, 'QG'], ['2015/11/28', 10, 'QG'],
    ['2015/11/08', 10, 'SY'], ['2015/11/09', 15, 'SY'], ['2015/11/10', 35, 'SY'],
    ['2015/11/11', 38, 'SY'], ['2015/11/12', 22, 'SY'], ['2015/11/13', 16, 'SY'],
    ['2015/11/14', 7, 'SY'], ['2015/11/15', 2, 'SY'], ['2015/11/16', 17, 'SY'],
    ['2015/11/17', 33, 'SY'], ['2015/11/18', 40, 'SY'], ['2015/11/19', 32, 'SY'],
    ['2015/11/20', 26, 'SY'], ['2015/11/21', 35, 'SY'], ['2015/11/22', 4, 'SY'],
    ['2015/11/23', 32, 'SY'], ['2015/11/24', 26, 'SY'], ['2015/11/25', 22, 'SY'],
    ['2015/11/26', 16, 'SY'], ['2015/11/27', 22, 'SY'], ['2015/11/28', 10, 'SY'],
    ['2015/11/08', 10, 'DD'], ['2015/11/09', 15, 'DD'], ['2015/11/10', 35, 'DD'],
    ['2015/11/11', 38, 'DD'], ['2015/11/12', 22, 'DD'], ['2015/11/13', 16, 'DD'],
    ['2015/11/14', 7, 'DD'], ['2015/11/15', 2, 'DD'], ['2015/11/16', 17, 'DD'],
    ['2015/11/17', 33, 'DD'], ['2015/11/18', 4, 'DD'], ['2015/11/19', 32, 'DD'],
    ['2015/11/20', 26, 'DD'], ['2015/11/21', 35, 'DD'], ['2015/11/22', 40, 'DD'],
    ['2015/11/23', 32, 'DD'], ['2015/11/24', 26, 'DD'], ['2015/11/25', 22, 'DD']
]
tr = ThemeRiver("主题河流图示例图")
tr.add(['DQ', 'TY', 'SS', 'QG', 'SY', 'DD'], 
        data, is_label_show=True)
page.add(tr)
tr
```
![](70.png)


## 二十二、词云图
```python
#     WordCloud（）
#     add(name, attr, value,
#         shape="circle",
#         word_gap=20,
#         word_size_range=None,
#         rotate_step=45)
# name -> str
#     图例名称
# attr -> list
#     属性名称
# value -> list
#     属性所对应的值
# shape -> list
#     词云图轮廓，有'circle', 'cardioid', 'diamond', 
#     'triangle-forward', 'triangle', 'pentagon', 'star'可选
# word_gap -> int
#     单词间隔，默认为 20。
# word_size_range -> list
#     单词字体大小范围，默认为 [12, 60]。
# rotate_step -> int
#     旋转单词角度，默认为 45。 
#     当且仅当 shape 为默认的'circle'时 rotate_step 参数才生效

```
```python
from pyecharts import WordCloud
name = [
    'Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 
    'Charter Communications','Chick Fil A', 'Planet Fitness', 
    'Pitch Perfect', 'Express', 'Home', 'Johnny Depp',
    'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark',
    'Farrah Abraham','Rita Ora', 'Serena Williams', 
    'NCAA baseball tournament', 'Point Break']
value = [
    10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112,
    965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
wordcloud = WordCloud(width=900, height=500)
wordcloud.add("", name, value, 
              word_size_range=[20, 100],shape='diamond')
page.add(wordcloud)
wordcloud
```
![](71.png)

# -----3D绘图-----

## 二十三、3D柱状图
```python
#     Bar3D（）#可接受grid3D,axis3D通用配置
#     add(name, x_axis, y_axis, data,
#         grid3d_opacity=1,grid3d_shading='color', **kwargs)
#     grid3d_shading -> str
#         三维柱状图中三维图形的着色效果。
#         color：只显示颜色，不受光照等其它因素的影响。
#         lambert：通过经典的 lambert 着色表现光照带来的明暗。
#         realistic：真实感渲染，配合light.ambientCubemap和postEffect
#                    可以让展示的画面效果和质感有质的提升。
```
```python
from pyecharts import Bar3D

bar3d = Bar3D("3D 柱状图示例", width=900, height=600)
x_axis = ["12a", "1a", "2a", "3a", "4a", "5a",
          "6a", "7a", "8a", "9a", "10a", "11a",
        "12p", "1p", "2p", "3p", "4p", "5p",
          "6p", "7p", "8p", "9p", "10p", "11p"]
y_axis = ["Saturday", "Friday", "Thursday", 
          "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [
    [0, 0, 5], [0, 1, 1], [0, 2, 0], [0, 3, 0], [0, 4, 0], [0, 5, 0],
    [0, 6, 0], [0, 7, 0], [0, 8, 0], [0, 9, 0], [0, 10, 0], [0, 11, 2],
    [0, 12, 4], [0, 13, 1], [0, 14, 1], [0, 15, 3], [0, 16, 4], [0, 17, 6],
    [0, 18, 4], [0, 19, 4], [0, 20, 3], [0, 21, 3], [0, 22, 2], [0, 23, 5],
    [1, 0, 7], [1, 1, 0], [1, 2, 0], [1, 3, 0], [1, 4, 0], [1, 5, 0],
    [1, 6, 0], [1, 7, 0], [1, 8, 0], [1, 9, 0], [1, 10, 5], [1, 11, 2],
    [1, 12, 2], [1, 13, 6], [1, 14, 9], [1, 15, 11], [1, 16, 6], [1, 17, 7],
    [1, 18, 8], [1, 19, 12], [1, 20, 5], [1, 21, 5], [1, 22, 7], [1, 23, 2],
    [2, 0, 1], [2, 1, 1], [2, 2, 0], [2, 3, 0], [2, 4, 0], [2, 5, 0],
    [2, 6, 0], [2, 7, 0], [2, 8, 0], [2, 9, 0], [2, 10, 3], [2, 11, 2],
    [2, 12, 1], [2, 13, 9], [2, 14, 8], [2, 15, 10], [2, 16, 6], [2, 17, 5],
    [2, 18, 5], [2, 19, 5], [2, 20, 7], [2, 21, 4], [2, 22, 2], [2, 23, 4],
    [3, 0, 7], [3, 1, 3], [3, 2, 0], [3, 3, 0], [3, 4, 0], [3, 5, 0],
    [3, 6, 0], [3, 7, 0], [3, 8, 1], [3, 9, 0], [3, 10, 5], [3, 11, 4],
    [3, 12, 7], [3, 13, 14], [3, 14, 13], [3, 15, 12], [3, 16, 9], [3, 17, 5],
    [3, 18, 5], [3, 19, 10], [3, 20, 6], [3, 21, 4], [3, 22, 4], [3, 23, 1],
    [4, 0, 1], [4, 1, 3], [4, 2, 0], [4, 3, 0], [4, 4, 0], [4, 5, 1],
    [4, 6, 0], [4, 7, 0], [4, 8, 0], [4, 9, 2], [4, 10, 4], [4, 11, 4],
    [4, 12, 2], [4, 13, 4], [4, 14, 4], [4, 15, 14], [4, 16, 12], [4, 17, 1],
    [4, 18, 8], [4, 19, 5], [4, 20, 3], [4, 21, 7], [4, 22, 3], [4, 23, 0],
    [5, 0, 2], [5, 1, 1], [5, 2, 0], [5, 3, 3], [5, 4, 0], [5, 5, 0],
    [5, 6, 0], [5, 7, 0], [5, 8, 2], [5, 9, 0], [5, 10, 4], [5, 11, 1],
    [5, 12, 5], [5, 13, 10], [5, 14, 5], [5, 15, 7], [5, 16, 11], [5, 17, 6],
    [5, 18, 0], [5, 19, 5], [5, 20, 3], [5, 21, 4], [5, 22, 2], [5, 23, 0],
    [6, 0, 1], [6, 1, 0], [6, 2, 0], [6, 3, 0], [6, 4, 0], [6, 5, 0],
    [6, 6, 0], [6, 7, 0], [6, 8, 0], [6, 9, 0], [6, 10, 1], [6, 11, 0],
    [6, 12, 2], [6, 13, 1], [6, 14, 3], [6, 15, 4], [6, 16, 0], [6, 17, 0],
    [6, 18, 0], [6, 19, 0], [6, 20, 1], [6, 21, 2], [6, 22, 2], [6, 23, 6]
    ]
range_color = ['#313695', '#4575b4', '#74add1',
               '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43',
               '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
           is_visualmap=True,visual_range=[0, 15],
          visual_range_color=range_color, 
          grid3d_width=150, grid3d_depth=100,
          grid3d_shading='lambert',is_grid3d_rotate=True) 
#visual_range范围越小,呈现颜色越多
# data中,如[1, 2, 3]表示 x轴的索引为 1，
#     即 "1a"；y轴的索引为 2，即 "Thursday"；z轴的数值为3
# 设置 grid3d_shading 可以让柱状更真实
# 设置 is_grid3d_rotate 启动自动旋转功能;
# 设置 grid3d_rotate_speed 调节旋转速度；如grid3d_rotate_speed=180。
page.add(bar3d)
bar3d
```
![](72.png)


## 二十四、3D折线图
```python
#     Line3D（） #可接受grid3D,axis3D通用配置
#     add(name, data,grid3d_opacity=1, **kwargs)
#      name -> str
#         图例名称
#      data -> [list], 包含列表的列表
#         数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
#      grid3d_opacity -> int
#         3D笛卡尔坐标系组的透明度（线的透明度），默认为 1，完全不透明。
```
### （一）3D弹簧图
```python
from pyecharts import Line3D
import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', 
    '#e0f3f8', '#ffffbf','#fee090', '#fdae61',
    '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=900, height=600)
line3d.add("", _data, is_visualmap=True, 
           visual_range_color=range_color,
           visual_range=[0, 30], grid3d_rotate_sensitivity=3)
page.add(line3d)
line3d
```
![](73.png)


### （二）旋转3D弹簧图
```python
from pyecharts import Line3D
import math
_data = []
for t in range(0, 25000):
    _t = t / 1000
    x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
    y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
    z = _t + 2.0 * math.sin(75 * _t)
    _data.append([x, y, z])
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9',
    '#e0f3f8', '#ffffbf','#fee090', '#fdae61', 
    '#f46d43', '#d73027', '#a50026']
line3d = Line3D("3D 折线图示例", width=900, height=600)
line3d.add("", _data, is_visualmap=True, 
           visual_range_color=range_color,
           visual_range=[0, 30], is_grid3d_rotate=True,
           grid3d_rotate_speed=180)
page.add(line3d)
line3d
```
![](74.png)


## 二十五、3D 散点图
```python
#     Scatter3D（）#可接受grid3D,axis3D通用配置
#     add(name, data,grid3d_opacity=1, **kwargs)
# name -> str
#     图例名称
# data -> [list], 包含列表的列表
#     数据项，数据中，每一行是一个『数据项』，每一列属于一个『维度』
# grid3d_opacity -> int
#     3D 笛卡尔坐标系组的透明度（点的透明度），默认为 1，完全不透明。
```
```python
from pyecharts import Scatter3D
import random
data = [
    [random.randint(0, 100),
    random.randint(0, 100),
    random.randint(0, 100)] for _ in range(80)
]
range_color = [
    '#313695', '#4575b4', '#74add1', '#abd9e9', 
    '#e0f3f8', '#ffffbf','#fee090', '#fdae61',
    '#f46d43', '#d73027', '#a50026']
scatter3D = Scatter3D("3D 散点图示例", width=900, height=600)
scatter3D.add("", data, is_visualmap=True,
              visual_range_color=range_color)
page.add(scatter3D)
scatter3D
```
![](75.png)


#-----自定义类-----
```python
# 一、Grid:并行显示多张图表
#     第一个图需为 有 x/y 轴的图，即不能为 Pie，其他位置顺序任意。
#     Overlap可类放入Grid类中,但不可为多x或多y轴,会出现坐标轴索引混乱
#     Grid()
#      add(chart,
#          grid_width=None,
#          grid_height=None,
#          grid_top=None,
#          grid_bottom=None,
#          grid_left=None,
#          grid_right=None)
# chart -> chart instance
#     图表实例
# grid_width -> str/int
#     grid 组件的宽度。默认自适应。
# grid_height -> str/int
#     grid 组件的高度。默认自适应。
# grid_top -> str/int
#     grid 组件离容器顶部的距离。默认为 None, 
#     有'top', 'center', 'middle'可选，也可以为百分数或者整数
# grid_bottom -> str/int
#     grid 组件离容器底部的距离。默认为 None, 
#     有'top', 'center', 'middle'可选，也可以为百分数或者整数
# grid_left -> str/int
#     grid 组件离容器左侧的距离。默认为 None, 
#     有'left', 'center', 'right'可选，也可以为百分数或者整数
# grid_right -> str/int
#     grid 组件离容器右侧的距离。默认为 None, 
#     有'left', 'center', 'right'可选，也可以为百分数或者整数
```
### (一)Bar+Line
```python
from pyecharts import Bar, Line, Grid
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720)
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True)
line = Line("折线图示例", title_top="50%")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
         mark_point=["max", "min"], mark_line=["average"],
         legend_top="50%")

grid = Grid()
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
page.add(grid)
grid
```
![](76.png)


### （二）Bar + Line + Scatter + EffectScatter
```python
from pyecharts import Bar, Line, Scatter, EffectScatter, Grid  
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", height=720, width=1200, title_pos="65%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_pos="80%")
line = Line("折线图示例")
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
         mark_point=["max", "min"], mark_line=["average"],
         legend_pos="20%")
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
scatter = Scatter("散点图示例", title_top="50%", title_pos="65%")
scatter.add("scatter", v1, v2, legend_top="50%", legend_pos="80%")
es = EffectScatter("动态散点图示例", title_top="50%")
es.add("es", [11, 11, 15, 13, 12, 13, 10], [1, -2, 2, 5, 3, 2, 0],
       effect_scale=6, legend_top="50%", legend_pos="20%")

grid = Grid()
grid.add(bar, grid_bottom="60%", grid_left="60%")
grid.add(line, grid_bottom="60%", grid_right="60%")
grid.add(scatter, grid_top="60%", grid_left="60%")
grid.add(es, grid_top="60%", grid_right="60%")
page.add(grid)
grid
```
![](77.png)


### （三）HeatMap + Bar
```python
import random
from pyecharts import HeatMap
x_axis = [
    "12a", "1a", "2a", "3a", "4a", "5a", "6a",
    "7a", "8a", "9a", "10a", "11a","12p", "1p", 
    "2p", "3p", "4p", "5p", "6p","7p", "8p", 
    "9p", "10p", "11p"]
y_axis = [
    "Saturday", "Friday", "Thursday",
    "Wednesday", "Tuesday", "Monday", "Sunday"]
data = [[i, j, random.randint(0, 50)] 
        for i in range(24) for j in range(7)]
heatmap = HeatMap("热力图示例", height=700)
heatmap.add("热力图直角坐标系", x_axis, y_axis, 
            data, is_visualmap=True,visual_top="45%",
            visual_text_color="#000",
            visual_orient='horizontal')
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar = Bar("柱状图示例", title_top="52%")
bar.add("商家A", attr, v1, is_stack=True)
bar.add("商家B", attr, v2, is_stack=True, legend_top="50%")

grid = Grid()
grid.add(heatmap, grid_bottom="60%")
grid.add(bar, grid_top="60%")
page.add(grid)
grid
```
![](78.png)


### (四)datazoom 组件同时控制多个图
```python
from pyecharts import Kline,Line
line = Line("折线图示例", width=1200, height=700)
attr = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
         mark_point=["max", "min"], mark_line=["average"])
line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
         mark_point=["max", "min"], 
         legend_top="50%", mark_line=["average"],
         # 设置 dataZoom 控制索引为 0,1 的 x 轴，即第一个和第二个
         is_datazoom_show=True, datazoom_xaxis_index=[0, 1])   

v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
      [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92],
      [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76],
      [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15],
      [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42],
      [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89],
      [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8],
      [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94],
      [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88],
      [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71],
      [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16],
      [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54],
      [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44],
      [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67],
      [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29],
      [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
kline = Kline("K 线图示例", title_top="50%")
kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)],
          v1, is_datazoom_show=True)

grid = Grid()
grid.add(line, grid_top="60%")
grid.add(kline, grid_bottom="60%")
page.add(grid)
grid
```
![](79.png)


### (五)倒映直角坐标系
```python
from pyecharts import Line
import random

attr = ['{}天'.format(i) for i in range(1, 31)]
line_top = Line("折线图示例", width=1200, height=700)
line_top.add("最高气温", attr, 
             [random.randint(20, 100) for i in range(30)],
             mark_point=["max", "min"], mark_line=["average"],
             legend_pos='38%')
line_bottom = Line()
line_bottom.add("最低气温", attr, 
                [random.randint(20, 100) for i in range(30)],
                mark_point=["max", "min"], mark_line=["average"],
                is_yaxis_inverse=True, xaxis_pos='top')

grid = Grid()
grid.add(line_top, grid_bottom='60%')
grid.add(line_bottom, grid_top='50%')
page.add(grid)
grid
```
![](80.png)


## 二、Overlap：结合不同类型图表叠加画在同张图上
```python
#     Overlap()
#     add(chart,
#         xaxis_index=0,
#         yaxis_index=0,
#         is_add_xaxis=False,
#         is_add_yaxis=False)
# chart -> chart instance
#     图表示例
# xaxis_index -> int
#     x 坐标轴索引，默认为 0
# yaxis_index -> int
#     y 坐标轴索引，默认为 0
# is_add_xaxis -> bool
#     是否新增一个 x 坐标轴，默认为 False
# is_add_yaxis -> bool
#     是否新增一个 y 坐标轴，默认为 False
```
### (一)Kline + Line
```python
import random
from pyecharts import Line, Kline, Overlap

v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
      [2300, 2291.3, 2288.26, 2308.38],
      [2295.35, 2346.5, 2295.35, 2345.92],
      [2347.22, 2358.98, 2337.35, 2363.8],
      [2360.75, 2382.48, 2347.89, 2383.76],
      [2383.43, 2385.42, 2371.23, 2391.82],
      [2377.41, 2419.02, 2369.57, 2421.15],
      [2425.92, 2428.15, 2417.58, 2440.38],
      [2411, 2433.13, 2403.3, 2437.42],
      [2432.68, 2334.48, 2427.7, 2441.73],
      [2430.69, 2418.53, 2394.22, 2433.89],
      [2416.62, 2432.4, 2414.4, 2443.03],
      [2441.91, 2421.56, 2418.43, 2444.8],
      [2420.26, 2382.91, 2373.53, 2427.07],
      [2383.49, 2397.18, 2370.61, 2397.94],
      [2378.82, 2325.95, 2309.17, 2378.82],
      [2322.94, 2314.16, 2308.76, 2330.88],
      [2320.62, 2325.82, 2315.01, 2338.78],
      [2313.74, 2293.34, 2289.89, 2340.71],
      [2297.77, 2313.22, 2292.03, 2324.63],
      [2322.32, 2365.59, 2308.92, 2366.16],
      [2364.54, 2359.51, 2330.86, 2369.65],
      [2332.08, 2273.4, 2259.25, 2333.54],
      [2274.81, 2326.31, 2270.1, 2328.14],
      [2333.61, 2347.18, 2321.6, 2351.44],
      [2340.44, 2324.29, 2304.27, 2352.02],
      [2326.42, 2318.61, 2314.59, 2333.67],
      [2314.68, 2310.59, 2296.58, 2320.96],
      [2309.16, 2286.6, 2264.83, 2333.29],
      [2282.17, 2263.97, 2253.25, 2286.33],
      [2255.77, 2270.28, 2253.31, 2276.22]]
attr = ["2017/7/{}".format(i + 1) for i in range(31)]
kline = Kline("Kline - Line 示例")
kline.add("日K", attr, v1)
line_1 = Line()
line_1.add("line-1", attr, 
           [random.randint(2400, 2500) for _ in range(31)])
line_2 = Line()
line_2.add("line-2", attr,
           [random.randint(2400, 2500) for _ in range(31)])

overlap = Overlap()
overlap.add(kline)
overlap.add(line_1)
overlap.add(line_2)
page.add(overlap)
overlap
```
![](81.png)


### （二）Line + EffectScatter
```python
from pyecharts import Line, EffectScatter, Overlap
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 10, 100]
line = Line("line - es 示例")
line.add("", attr, v1, is_random=True)
es = EffectScatter()
es.add("", attr, v1, effect_scale=8)

overlap = Overlap()
overlap.add(line)
overlap.add(es)
page.add(overlap)
overlap
```
![](82.png)


### （三）多 X 轴或者多 Y 轴
```python
from pyecharts import Line, Bar, Overlap

attr = ["{}月".format(i) for i in range(1, 13)]
v1 = [2.0, 4.9, 7.0, 23.2, 25.6, 
      76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
v2 = [2.6, 5.9, 9.0, 26.4, 28.7, 
      70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
v3 = [2.0, 2.2, 3.3, 4.5, 6.3, 
      10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]

bar = Bar(width=1200, height=600)
bar.add("蒸发量", attr, v1)
bar.add("降水量", attr, v2, yaxis_formatter=" ml",
        yaxis_interval=50, yaxis_max=250)

line = Line()
line.add("平均温度", attr, v3,
         yaxis_formatter=" °C", yaxis_interval=5)

overlap = Overlap()
# 默认不新增 x y 轴，并且 x y 轴的索引都为 0
overlap.add(bar)
# 新增一个 y 轴，此时 y 轴的数量为 2，第二个y轴的索引
#     为 1（索引从 0 开始），所以设置 yaxis_index = 1
# 由于使用的是同一个 x 轴，所以 x 轴部分不用做出改变
overlap.add(line, yaxis_index=1, is_add_yaxis=True)
page.add(overlap)
overlap
```
![](83.png)


## 三、Page：同一网页按顺序展示多图
```python
# #     Page()
# #     page = Page() ，可指定 page_title, jhost 参数
# #     show_config()：打印输出所有配置项
# from pyecharts import Line, Pie, Kline, Radar
# from pyecharts import Page

# page = Page()

# # line
# attr = ['周一','周二','周三','周四','周五','周六','周日']
# line = Line("折线图示例")
# line.add("最高气温", attr, [11, 11, 15, 13, 12, 13, 10],
#          mark_point=["max", "min"], mark_line=["average"])
# line.add("最低气温", attr, [1, -2, 2, 5, 3, 2, 0],
#          mark_point=["max", "min"], mark_line=["average"])
# page.add(line)

# # pie
# attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 = [11, 12, 13, 10, 10, 10]
# pie = Pie("饼图-圆环图示例", title_pos='center')
# pie.add("", attr, v1, radius=[40, 75], label_text_color=None,
#         is_label_show=True, legend_orient='vertical', 
#        legend_pos='left')
# page.add(pie)

# # kline
# v1 = [[2320.26, 2320.26, 2287.3, 2362.94],
#       [2300, 2291.3, 2288.26, 2308.38],
#       [2295.35, 2346.5, 2295.35, 2345.92],
#       [2347.22, 2358.98, 2337.35, 2363.8],
#       [2360.75, 2382.48, 2347.89, 2383.76],
#       [2383.43, 2385.42, 2371.23, 2391.82],
#       [2377.41, 2419.02, 2369.57, 2421.15],
#       [2425.92, 2428.15, 2417.58, 2440.38],
#       [2411, 2433.13, 2403.3, 2437.42],
#       [2432.68, 2334.48, 2427.7, 2441.73],
#       [2430.69, 2418.53, 2394.22, 2433.89],
#       [2416.62, 2432.4, 2414.4, 2443.03],
#       [2441.91, 2421.56, 2418.43, 2444.8],
#       [2420.26, 2382.91, 2373.53, 2427.07],
#       [2383.49, 2397.18, 2370.61, 2397.94],
#       [2378.82, 2325.95, 2309.17, 2378.82],
#       [2322.94, 2314.16, 2308.76, 2330.88],
#       [2320.62, 2325.82, 2315.01, 2338.78],
#       [2313.74, 2293.34, 2289.89, 2340.71],
#       [2297.77, 2313.22, 2292.03, 2324.63],
#       [2322.32, 2365.59, 2308.92, 2366.16],
#       [2364.54, 2359.51, 2330.86, 2369.65],
#       [2332.08, 2273.4, 2259.25, 2333.54],
#       [2274.81, 2326.31, 2270.1, 2328.14],
#       [2333.61, 2347.18, 2321.6, 2351.44],
#       [2340.44, 2324.29, 2304.27, 2352.02],
#       [2326.42, 2318.61, 2314.59, 2333.67],
#       [2314.68, 2310.59, 2296.58, 2320.96],
#       [2309.16, 2286.6, 2264.83, 2333.29],
#       [2282.17, 2263.97, 2253.25, 2286.33],
#       [2255.77, 2270.28, 2253.31, 2276.22]]
# kline = Kline("K 线图示例")
# kline.add("日K", ["2017/7/{}".format(i + 1) for i in range(31)], v1)
# page.add(kline)

# # radar
# schema = [
#     ("销售", 6500), ("管理", 16000), ("信息技术", 30000),
#     ("客服", 38000), ("研发", 52000), ("市场", 25000)
# ]
# v1 = [[4300, 10000, 28000, 35000, 50000, 19000]]
# v2 = [[5000, 14000, 28000, 31000, 42000, 21000]]
# radar = Radar("雷达图示例")
# radar.config(schema)
# radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
# radar.add("实际开销", v2, label_color=["#4e79a7"], 
#     is_area_show=False,legend_selectedmode='single')
# page.add(radar)

# page
```
## 四、Timeline：提供时间线轮播多张图
```python
#     TimeLine()
# page_title -> str
#     生成 文件的 <title> 标签的值，默认为'Echarts'
# width -> int
#     画布宽度，默认为 800
# height -> int
#     画布高度，默认为 400
# jhost -> str
#     自定义每个实例的 JavaScript host
# is_auto_play -> bool
#     是否自动播放，默认为 Flase
# is_loop_play -> bool
#     是否循环播放，默认为 True
# is_rewind_play -> bool
#     是否方向播放，默认为 Flase
# is_timeline_show -> bool
#     是否显示 timeline 组件。默认为 True
# timeline_play_interval -> int
#     播放的速度（跳动的间隔），单位毫秒（ms）。
# timeline_symbol -> str
#     标记的图形。ECharts提供的标记类型包括'circle','rect', 
#     'roundRect','triangle','diamond','pin','arrow'
# timeline_symbol_size -> int/list
#     标记的图形大小，可以设置成如10这样单一的数字,
#     也可以用数组分开表示宽和高,
#     例如 [20, 10] 表示标记宽为 20，高为 10。
# timeline_left -> int/str
#     timeline 组件离容器左侧的距离。
#     left 的值可以是像 20 这样的具体像素值，
#     可以是像 '20%' 这样相对于容器高宽的百分比，
#     也可以是 'left', 'center', 'right'。
#     如果 left 的值为'left', 'center', 'right'，
#     组件会根据相应的位置自动对齐。
# timeline_right -> int/str
#     timeline 组件离容器右侧的距离。同 left
# timeline_top -> int/str
#     timeline 组件离容器顶侧的距离。同 left
# timeline_bottom -> int/str
#     timeline 组件离容器底侧的距离。同 left
#   add()
#     接受两个参数，如add(bar,'2013') 
#     第一个为图实例，第二个为时间线的 ”时间点“。
```
### (一)轮播Bar图
```python
from pyecharts import Bar, Timeline
from random import randint
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar_1 = Bar("2012 年销量", "数据纯属虚构")
bar_1.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_1.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_2 = Bar("2013 年销量", "数据纯属虚构")
bar_2.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_2.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_3 = Bar("2014 年销量", "数据纯属虚构")
bar_3.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_3.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_4 = Bar("2015 年销量", "数据纯属虚构")
bar_4.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_4.add("冬季", attr, [randint(10, 100) for _ in range(6)])

bar_5 = Bar("2016 年销量", "数据纯属虚构")
bar_5.add("春季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("夏季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("秋季", attr, [randint(10, 100) for _ in range(6)])
bar_5.add("冬季", attr, [randint(10, 100) for _ in range(6)],
          is_legend_show=True)

timeline = Timeline(is_auto_play=True, timeline_bottom=0)
timeline.add(bar_1, '2012 年')
timeline.add(bar_2, '2013 年')
timeline.add(bar_3, '2014 年')
timeline.add(bar_4, '2015 年')
timeline.add(bar_5, '2016 年')
page.add(timeline)
timeline
```
![](84.png)


### （二）轮播Pie图
```python
from pyecharts import Pie, Timeline

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
pie_1 = Pie("2012 年销量比例", "数据纯属虚构")
pie_1.add("秋季", attr, [randint(10, 100) for _ in range(6)],
          is_label_show=True, radius=[30, 55], rosetype='radius')

pie_2 = Pie("2013 年销量比例", "数据纯属虚构")
pie_2.add("秋季", attr, [randint(10, 100) for _ in range(6)],
          is_label_show=True, radius=[30, 55], rosetype='radius')

pie_3 = Pie("2014 年销量比例", "数据纯属虚构")
pie_3.add("秋季", attr, [randint(10, 100) for _ in range(6)],
          is_label_show=True, radius=[30, 55], rosetype='radius')

pie_4 = Pie("2015 年销量比例", "数据纯属虚构")
pie_4.add("秋季", attr, [randint(10, 100) for _ in range(6)],
          is_label_show=True, radius=[30, 55], rosetype='radius')

pie_5 = Pie("2016 年销量比例", "数据纯属虚构")
pie_5.add("秋季", attr, [randint(10, 100) for _ in range(6)],
          is_label_show=True, radius=[30, 55], rosetype='radius')

timeline = Timeline(is_auto_play=True, timeline_bottom=0)
timeline.add(pie_1, '2012 年')
timeline.add(pie_2, '2013 年')
timeline.add(pie_3, '2014 年')
timeline.add(pie_4, '2015 年')
timeline.add(pie_5, '2016 年')
page.add(timeline)
timeline
```
![](85.png)


### （三）混合轮播
```python
from pyecharts import Bar, Line, Timeline, Overlap
from random import randint
attr = ["{}月".format(i) for i in range(1, 7)]
bar = Bar("1 月份数据", "数据纯属虚构")
bar.add("bar", attr, [randint(10, 50) for _ in range(6)])
line = Line()
line.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap = Overlap()
overlap.add(bar)
overlap.add(line)

bar_1 = Bar("2 月份数据", "数据纯属虚构")
bar_1.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_1 = Line()
line_1.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_1 = Overlap()
overlap_1.add(bar_1)
overlap_1.add(line_1)

bar_2 = Bar("3 月份数据", "数据纯属虚构")
bar_2.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_2 = Line()
line_2.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_2 = Overlap()
overlap_2.add(bar_2)
overlap_2.add(line_2)

bar_3 = Bar("4 月份数据", "数据纯属虚构")
bar_3.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_3 = Line()
line_3.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_3 = Overlap()
overlap_3.add(bar_3)
overlap_3.add(line_3)

bar_4 = Bar("5 月份数据", "数据纯属虚构")
bar_4.add("bar", attr, [randint(10, 50) for _ in range(6)])
line_4 = Line()
line_4.add("line", attr, [randint(50, 80) for _ in range(6)])
overlap_4 = Overlap()
overlap_4.add(bar_4)
overlap_4.add(line_4)

timeline = Timeline(timeline_bottom=0)
timeline.add(overlap, '1 月')
timeline.add(overlap_1, '2 月')
timeline.add(overlap_2, '3 月')
timeline.add(overlap_3, '4 月')
timeline.add(overlap_4, '5 月')
page.add(timeline)
timeline
```
![](86.png)

```python
page.render('charts.html')
make_a_snapshot('charts.html','charts.pdf')
```
# -----统一风格-----
```python
# 为了简化配置项编写，提供了Style类,可用于一个或多个图保持统一的风格
'''(一）初始化图时'''
from pyecharts import Style,Geo
style = Style(
    title_color="#fff",
    title_pos="center",
    width=1100,
    height=600,
    background_color='#404a59'
)
# style.init_style 会返回类初始化的风格配置字典
geo = Geo("全国主要城市空气质量", "data from pm2.5",
          **style.init_style)
'''(二)增加图例时'''
pie = Pie('各类电影中"好片"所占的比例', "数据来着豆瓣",
          title_pos='center')
# 使用 Style.add() 可配置增加图例的风格配置字典
pie_style = style.add(
    radius=[18, 24],
    label_pos="center",
    is_label_show=True,
    label_text_color=None
)
pie.add("", ["剧情", ""], [25, 75], center=[10, 30], **pie_style)
pie.add("", ["奇幻", ""], [24, 76], center=[30, 30], **pie_style)
pie.add("", ["爱情", ""], [14, 86], center=[50, 30], **pie_style)
pie.add("", ["惊悚", ""], [11, 89], center=[70, 30], **pie_style)
```
# -----高级用法：JavaScript 回调函数-----
## （一）Tooltip 示例
```python
#     举个例子，Geo 图中如何在 tooltip中只显示地图坐标名称和数值，
#     不显示经纬度。现在可以这么操作，先定义一个geo_formatter函数。

def geo_formatter(params):
    return params.name + ' : ' + params.value[2]

def test_geo_shantou_city():
    data = [('澄海区',30),('南澳县',40),('龙湖区',50),('金平区',60)]
    geo = Geo("汕头市地图示例", **style.init_style)
    attr, value = geo.cast(data)
    geo.add(
        "",
        attr,
        value,
        maptype="汕头",
        is_visualmap=True,
        is_legend_show=False,
        tooltip_formatter=geo_formatter,    # 重点在这里，将函数直接传递为参数。
        label_emphasis_textsize=15,
        label_emphasis_pos='right',
    )
    geo
```

## （二）使用 JavaScript 事件处理函数
```python
#     Echarts 本身提供了 api/events 事件处理函数，主要通过 on 方式实现。
# pyecharts根据官方提供的 events 列表，提供了如下全局事件名变量。
# 位于 pyecharts.echarts.events 模块中。

# Mouse Events
MOUSE_CLICK = "click"
MOUSE_DBCLICK = "dbclick"
MOUSE_DOWN = "mousedown"
MOUSE_OVER = "mouseover"
MOUSE_GLOBALOUT = "globalout"

# Other Events
LEGEND_SELECT_CHANGED = "legendselectchanged"
LEGEND_SELECTED = "legendselected"
LEGEND_UNSELECTAED = "legendunselected"
LEGEND_SCROLL = "legendscroll"
DATA_ZOOM = "datazoom"
DATA_RANGE_SELECTED = "datarangeselected"
TIMELINE_CHANGED = "timelinechanged"
TIMELINE_PLAY_CHANGED = "timelineplaychanged"
RESTORE = "restore"
DATA_VIEW_CHANGED = "dataviewchanged"
MAGIC_TYPE_CHANGED = "magictypechanged"
GEO_SELECT_CHANGED = "geoselectchanged"
GEO_SELECTED = "geoselected"
GEO_UNSELECTED = "geounselected"
PIE_SELECT_CHANGED = "pieselectchanged"
PIE_SELECTED = "pieselected"
PIE_UNSELECTED = "pieunselected"
MAP_SELECT_CHANGED = "mapselectchanged"
MAP_SELECTED = "mapselected"
MAP_UNSELECTED = "mapunselected"
AXIS_AREA_SELECTED = "axisareaselected"
FOCUS_NODE_ADJACENCY = "focusnodeadjacency"
UNFOCUS_NODE_ADJACENCY = "unfocusnodeadjacency"
BRUSH = "brush"
BRUSH_SELECTED = "brushselected"

# 使用方式如下：
import pyecharts.echarts.events as events
from pyecharts import Bar
from pyecharts_javascripthon.dom import alert

def on_click():
    alert("点击事件触发")

def test_mouse_click():
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.add(
        "服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        [5, 20, 36, 10, 75, 90])
    bar.on(events.MOUSE_CLICK, on_click)
    bar
```


# -----参数解释-----
## 图形初始化参数
```python
#     对所有图表均可用如Bar(title,subtile,width,height,background_color)
#  #title相关参数:
# title -> str
#     主标题文本，支持 \n 换行，默认为 ""
# title_pos -> str/int
#     标题距离左侧距离，默认为'left'，有'auto', 'left',
#     'right', 'center'可选，也可为百分比或整数
# title_top -> str/int
#     标题距离顶部距离，默认为'top'，有'top', 
#     'middle', 'bottom'可选，也可为百分比或整数
# title_color -> str
#     主标题文本颜色，默认为 '#000'
# title_text_size -> int
#     主标题文本字体大小，默认为 18
#  #subtitle相关参数 
# subtitle -> str
#     副标题文本，支持 \n 换行，默认为 ""
# subtitle_color -> str
#     副标题文本颜色，默认为 '#aaa'
# subtitle_text_size -> int
#     副标题文本字体大小，默认为 12
#  #其他参数(画布宽高、背景色等)
# width -> int
#     画布宽度，默认为 800（px）
# height -> int
#     画布高度，默认为 400（px）
# background_color -> str
#     画布背景颜色，默认为 '#fff'
# page_title -> str
#     指定生成的 文件中 <title> 标签的值。
#     默认为'Echarts'
# renderer -> str
#     指定使用渲染方式，有'svg'和'canvas'可选，
#     默认为'canvas'。3D图仅能使用'canvas'。
```
## 通用配置项
```python
#     均在add()方法中设置且须在最后一个add()上设置，否侧设置会被冲刷掉
```
### xyAxis：
```python
#     直角坐标系中的x、y轴(Line、Bar、Scatter、EffectScatter、Kline)
```
### x轴配置参数
```python
# x_axis -> list
#     x 轴数据项    
# is_convert -> bool
#     是否交换 x 轴与 y 轴
# is_xaxislabel_align -> bool
#     x 轴刻度线和标签是否对齐，默认为 False
# is_yaxislabel_align -> bool
#     y 轴刻度线和标签是否对齐，默认为 False
# is_xaxis_inverse -> bool
#     是否反向 x 坐标轴，默认为 False
# is_yaxis_inverse -> bool
#     是否反向 y 坐标轴，默认为 False
# is_xaxis_boundarygap -> bool
#     x 轴两边留白策略，适用于类目轴。
#     类目轴中 boundaryGap 可以配置为 True 和 False,默认为 True.
#     这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的
#     带(band)中间，即两边留白。
# is_yaxis_boundarygap -> bool
#     y 轴两边留白策略，适用于类目轴。
#     类目轴中 boundaryGap 可以配置为 True 和 False。
#     默认为 True，这时候刻度只是作为分隔线，
#     标签和数据点都会在两个刻度之间的带(band)中间，即两边留白。
# is_xaxis_show -> bool
#     是否显示 x 轴
# is_yaxis_show -> bool
#     是否显示 y 轴
# is_splitline_show -> bool
#     是否显示 y 轴网格线，默认为 True。
# xaxis_interval -> int
#     x 轴刻度标签的显示间隔，在类目轴中有效。
#     默认会采用标签不重叠的策略间隔显示标签。
#     设置成 0 强制显示所有标签。设置为 1，
#     表示『隔一个标签显示一个标签』，如果值为 2，
#     表示隔两个标签显示一个标签，以此类推
# xaxis_force_interval -> int/str
#     强制设置 x 坐标轴分割间隔。如设置为 50 
#     则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。
#     一般情况下不建议设置这个参数！！因为 splitNumber 是预估的值，
#      实际根据策略计算出来的刻度可能无法达到想要的效果，这时候可以使用
#      interval 配合 min、max 强制设定刻度划分。在类目轴中无效。
# xaxis_margin -> int
#     x 轴刻度标签与轴线之间的距离。默认为 8
# xaxis_name -> str
#     x 轴名称
# xaxis_name_size -> int
#     x 轴名称体大小，默认为 14
# xaxis_name_gap -> int
#     x 轴名称与轴线之间的距离，默认为 25
# xaxis_name_pos -> str
#     x 轴名称位置，有'start'，'middle'，'end'可选
# xaxis_min -> int/float
#     x 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 
#     可自定以数据中最小值为 x 轴最小值。
# xaxis_max -> int/float
#     x 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 
#     可自定以数据中最大值为 x 轴最大值。
# xaxis_pos -> str
#     x 坐标轴位置，有'top','bottom'可选
# xaxis_label_textsize -> int
#     x 坐标轴标签字体大小，默认为 12
# xaxis_label_textcolor -> str
#     x 坐标轴标签字体颜色，默认为 "#000"
# xaxis_type -> str
#     x 坐标轴类型
#     'value'：数值轴，适用于连续数据。
#     'category'：类目轴，适用于离散的类目数据。
#     'log'：对数轴。适用于对数数据。
# xaxis_rotate -> int
#     x 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候
#     可以通过旋转防止标签之间重叠。默认为 0，即不旋转。
#     旋转的角度从 -90 度到 90 度。
# xaxis_formatter -> str | function
#     x轴标签格式器，如'天'，则x轴的标签为数据加'天'(3天,4天),默认为 ""
# ->function：
# from pyecharts_javascripthon.dom import Date
# def xaxis_formatter(value, index):
#     date = Date(value)
#     texts = [(date.getMonth() + 1), date.getDate()]
#     if index == 0:
#         texts.unshift(date.getYear())
#     return '/'.join(texts)
```
### y轴配置参数
```python
# y_axis -> list
#     y 坐标轴数据
# yaxis_interval -> int
#     y 轴刻度标签的显示间隔，在类目轴中有效。
#     默认会采用标签不重叠的策略间隔显示标签。
#     设置成 0 强制显示所有标签。设置为 1，
#     表示『隔一个标签显示一个标签』，如果值为 2，
#     表示隔两个标签显示一个标签，以此类推
# yaxis_force_interval -> int/str
#     强制设置 y 坐标轴分割间隔。如设置为 50 
#     则刻度为 [0, 50, 150, ...]，设置为 "auto" 则只显示两个刻度。
#     一般情况下不建议设置这个参数！！因为 splitNumber 是预估的值，
#     实际根据策略计算出来的刻度可能无法达
#     到想要的效果，这时候可以使用 interval 
#     配合 min、max 强制设定刻度划分。在类目轴中无效。
# yaxis_margin -> int
#     y 轴刻度标签与轴线之间的距离。默认为 8
# yaxis_formatter -> str | function
#     y 轴标签格式器，如'天'，则y轴的标签为数据加'天'(3天，4天),默认为 ""
# -> function
# from pyecharts_javascripthon.dom import Date
# def yaxis_formatter(value, index):
#     date = Date(value)
#     texts = [(date.getMonth() + 1), date.getDate()]
#     if index == 0:
#         texts.unshift(date.getYear())
#     return '/'.join(texts)
# yaxis_name -> str
#     y 轴名称
# yaxis_name_size -> int
#     y 轴名称体大小，默认为 14
# yaxis_name_gap -> int
#     y 轴名称与轴线之间的距离，默认为 25
# yaxis_name_pos -> str
#     y 轴名称位置，有'start', 'middle'，'end'可选
# yaxis_min -> int/float
#     y 坐标轴刻度最小值，默认为自适应。使用特殊值 "dataMin" 
#     可自定以数据中最小值为 y 轴最小值。
# yaxis_max -> int/float
#     y 坐标轴刻度最大值，默认为自适应。使用特殊值 "dataMax" 
#     可自定以数据中最大值为 y 轴最大值。
# yaxis_pos -> str
#     y 坐标轴位置，有'left','right'可选
# yaxis_label_textsize -> int
#     y 坐标轴标签字体大小，默认为 12
# yaxis_label_textcolor -> str
#     y 坐标轴标签字体颜色，默认为 "#000"
# yaxis_type -> str
#     y 坐标轴类型
#     'value'：数值轴，适用于连续数据。
#     'category'：类目轴，适用于离散的类目数据。
#     'log'：对数轴。适用于对数数据。
# yaxis_rotate -> int
#     y 轴刻度标签旋转的角度，在类目轴的类目标签显示不下的时候
#     可以通过旋转防止标签之间重叠。默认为 0，即不旋转。
#     旋转的角度从 -90 度到 90 度。
```
### dataZoom:(Line、Bar、Scatter、EffectScatter、Kline、Boxplot)。
```python 
#     用于区域缩放，从而能自由关注细节的数据信息，
#     或者概览数据整体，或者去除离群点的影响。
# is_datazoom_show -> bool
#     是否使用区域缩放组件，默认为 False
# datazoom_type -> str
#     区域缩放组件类型，默认为'slider'，
#     有'slider','inside','both'可选
# datazoom_range -> list
#     区域缩放的范围，默认为[50, 100]
# datazoom_orient -> str
#     datazoom 组件在直角坐标系中的方向，
#     默认为'horizontal'，效果显示在x轴。
#     如若设置为 'vertical' 的话效果显示在 y 轴。
# datazoom_xaxis_index -> int/list
#     datazoom 组件控制的 x 轴索引。
#     默认控制第一个 x 轴，如没特殊需求无须显示指定。
#     单个为 int 类型而控制多个为 list 类型，
#     如 [0, 1] 表示控制第一个和第二个 x 轴。
# datazoom_yaxis_index -> int/list
#     datazoom 组件控制的 y 轴索引。
#     默认控制第一个 y 轴，如没特殊需求无须显示指定。
#     单个为 int 类型而控制多个为 list 类型，
#     如 [0, 1] 表示控制第一个和第二个 x 轴。
```
### legend：
```python   
#     图例组件。图例组件展现了不同系列的标记(symbol)，
#     颜色和名字。可以通过点击图例控制哪些系列不显示。
# is_legend_show -> bool
#     是否显示顶端图例，默认为 True
# legend_orient -> str
#     图例列表的布局朝向，默认为'horizontal'，
#     有'horizontal', 'vertical'可选
# legend_pos -> str
#     图例组件离容器左侧的距离，默认为'center'，
#     有'left', 'center', 'right'可选，
#     也可以为百分数，如"%60"
# legend_top -> str
#     图例组件离容器上侧的距离，默认为'top'，
#     有'top', 'center', 'bottom'可选，
#     也可以为百分数，如"%60"
# legend_selectedmode -> str/bool
#     图例选择的模式，控制是否可以通过点击图例改变系列的显示状态。
#     默认为'multiple'，
#     可以设成 'single' 或者 'multiple' 使用单选或者多选模式。
#     也可以设置为 False 关闭显示状态。
# legend_text_size -> int
#     图例名称字体大小
# legend_text_color -> str
#     图例名称字体颜色
```
### label：
```python   
#     图形上的文本标签，可用于说明图形的一些数据信息，比如值，名称等。
# is_label_show -> bool
#     是否正常显示标签，默认不显示。标签即各点的数据项信息
# is_label_emphasis -> bool
#     是否高亮显示标签，默认显示。高亮标签即选中数据时显示的信息项。
# label_pos -> str
#     标签的位置，Bar 图默认为'top'。
#     有'top', 'left', 'right', 'bottom', 'inside','outside'可选
# label_emphasis_pos -> str
#     高亮标签的位置，Bar 图默认为'top'。
#     有'top', 'left', 'right', 'bottom', 'inside','outside'可选
# label_text_color -> str
#     标签字体颜色，默认为 "#000"
# label_emphasis_textcolor -> str
#     高亮标签字体颜色，默认为 "#fff"
# label_text_size -> int
#     标签字体大小，默认为 12
# label_emphasis_textsize -> int
#     高亮标签字体大小，默认为 12
# is_random -> bool
#     是否随机排列颜色列表，默认为 False
# label_color -> list
#     自定义标签颜色。全局颜色列表，所有图表的图例颜色均在这里修改。
#     如 Bar 的柱状颜色，Line 的线条颜色等等。
# label_formatter -> str | function 
#     模板变量有{a},{b},{c},{d},{e}，分别表示系列名，数据名，数据值等。
#     使用示例，如 label_formatter='{a}'。在 trigger 为 'axis' 的时候，
#     会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引
#     的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样：
# # 折线（区域）图、柱状（条形）图、K线图 :
# #     {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
# # 散点图（气泡）图 : 
# #     {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
# # 地图 : 
# #     {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
# # 饼图、仪表盘、漏斗图: 
# #     {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）

# label_formatter -> function
# def label_formatter(params):
# 回调函数格式：
# (params: Object|Array) => string

# 参数 params 是 formatter 需要的单个数据集。格式如下：
# {
#     componentType: 'series',
#     // 系列类型
#     seriesType: string,
#     // 系列在传入的 option.series 中的 index
#     seriesIndex: number,
#     // 系列名称
#     seriesName: string,
#     // 数据名，类目名
#     name: string,
#     // 数据在传入的 data 数组中的 index
#     dataIndex: number,
#     // 传入的原始数据项
#     data: Object,
#     // 传入的数据值
#     value: number|Array,
#     // 数据图形的颜色
#     color: string,
# }
```
### lineStyle：
```python
#     带线图形的线的风格选项(Line、Polar、Radar、Graph、Parallel)
# line_width -> int
#     线的宽度，默认为 1
# line_opacity -> float
#     线的透明度，0 为完全透明，1 为完全不透明。默认为 1
# line_curve -> float
#     线的弯曲程度，0 为完全不弯曲，1 为最弯曲。默认为 0
# line_type -> str
#     线的类型，有'solid', 'dashed', 'dotted'可选。默认为'solid'
# line_color -> str
#     线的颜色
```
### grid3D：
```python
#     3D笛卡尔坐标系组配置项，适用于3D图形。(Bar3D, Line3D, Scatter3D)
# grid3d_width -> int
#     三维笛卡尔坐标系组件在三维场景中的宽度。默认为 100
# grid3d_height -> int
#     三维笛卡尔坐标系组件在三维场景中的高度。默认为 100
# grid3d_depth -> int
#     三维笛卡尔坐标系组件在三维场景中的深度。默认为 100
# is_grid3d_rotate -> bool
#     是否开启视角绕物体的自动旋转查看。默认为 False。
# grid3d_rotate_speed -> int
#     物体自传的速度。单位为角度 / 秒，默认为 10 ，也就是 36 秒转一圈。
# grid3d_rotate_sensitivity -> int
#     旋转操作的灵敏度，值越大越灵敏。默认为 1, 设置为 0 后无法旋转。
```
### axis3D：
```python 
#     3D笛卡尔坐标系XYZ轴配置项，适用于3D图形。(Bar3D,Line3D,Scatter3D)
# # 3D X轴
# xaxis3d_name -> str
#     x 轴名称，默认为 ""
# xaxis3d_name_size -> int
#     x 轴名称体大小，默认为 16
# xaxis3d_name_gap -> int
#     x 轴名称与轴线之间的距离，默认为 25
# xaxis3d_min -> int/float
#     x 坐标轴刻度最小值，默认为自适应。
# xaxis3d_max -> int/float
#     x 坐标轴刻度最大值，默认为自适应。
# xaxis3d_interval -> int
#     x 轴刻度标签的显示间隔，在类目轴中有效。
#     默认会采用标签不重叠的策略间隔显示标签。
#     设置成 0 强制显示所有标签。
#     设置为 1，表示『隔一个标签显示一个标签』，
#     如果值为 2，表示隔两个标签显示一个标签，以此类推
# xaxis3d_margin -> int
#     x 轴刻度标签与轴线之间的距离。默认为 8
# # 3D Y轴
# yaxis3d_name -> str
#     y 轴名称，默认为 ""
# yaxis3d_name_size -> int
#     y 轴名称体大小，默认为 16
# yaxis3d_name_gap -> int
#     y 轴名称与轴线之间的距离，默认为 25
# yaxis3d_min -> int/float
#     y 坐标轴刻度最小值，默认为自适应。
# yaxis3d_max -> int/float
#     y 坐标轴刻度最大值，默认为自适应。
# yaxis3d_interval -> int
#     y 轴刻度标签的显示间隔，在类目轴中有效。
#     默认会采用标签不重叠的策略间隔显示标签。
#     设置成 0 强制显示所有标签。
#     设置为 1，表示『隔一个标签显示一个标签』，
#     如果值为 2，表示隔两个标签显示一个标签，以此类推
# yaxis3d_margin -> int
#     y 轴刻度标签与轴线之间的距离。默认为 8
# # 3D Z轴
# zaxis3d_name -> str
#     z 轴名称，默认为 ""
# zaxis3d_name_size -> int
#     z 轴名称体大小，默认为 16
# zaxis3d_name_gap -> int
#     z 轴名称与轴线之间的距离，默认为 25
# zaxis3d_min -> int/float
#     z 坐标轴刻度最小值，默认为自适应。
# zaxis3d_max -> int/float
#     z 坐标轴刻度最大值，默认为自适应。
# zaxis3d_margin -> int
#     z 轴刻度标签与轴线之间的距离。默认为 8
```
### visualMap：
```python
#     视觉映射组件，用于进行『视觉编码』，
#     也就是将数据映射到视觉元素（视觉通道）
# is_visualmap -> bool
#     是否使用视觉映射组件
# visual_type -> str
#     制定组件映射方式，默认为'color'，
#     即通过颜色来映射数值。有'color', 'size'可选。
#     'size'通过数值点的大小，也就是图形点的大小来映射数值。
# visual_range -> list
#     指定组件的允许的最小值与最大值。默认为 [0, 100]
# visual_text_color -> list
#     两端文本颜色。
# visual_range_text -> list
#     两端文本。默认为 ['low', 'hight']
# visual_range_color -> list
#     过渡颜色。默认为 ['#50a3ba', '#eac763', '#d94e5d']
# visual_range_size -> list
#     数值映射的范围，也就是图形点大小的范围。默认为 [20, 50]
# visual_orient -> str
#     visualMap 组件条的方向，默认为'vertical'.
#     有'vertical', 'horizontal'可选。
# visual_pos -> str/int
#     visualmap 组件条距离左侧的位置，默认为'left'.
#     有'right', 'center', 'right'可选，也可为百分数或整数。
# visual_top -> str/int
#     visualmap 组件条距离顶部的位置，默认为'top'。
#     有'top', 'center', 'bottom'可选，也可为百分数或整数。
# visual_split_number -> int
#     分段型中分割的段数，在设置为分段型时生效。默认分为 5 段。
# visual_dimension -> int
#     指定用数据的『哪个维度』，映射到视觉元素上。
#     默认映射到最后一个维度。索引从 0 开始。
#     在直角坐标系中，x 轴为第一个维度（0），y 轴为第二个维度（1）。
# is_calculable -> bool
#     是否显示拖拽用的手柄（手柄能拖拽调整选中范围）。默认为 True
# is_piecewise -> bool
#     是否将组件转换为分段型（默认为连续型），默认为 False
# pieces -> list
#     自定义『分段式视觉映射组件（visualMapPiecewise）』
#     的每一段的范围，以及每一段的文字，以及每一段的特别的样式。
#     （仅在 is_piecewise 为 True 时生效）例如：
#   pieces: [
#       {min: 1500}, // 不指定 max，表示max为无限大（Infinity）。
#       {min: 900, max: 1500},
#       {min: 310, max: 1000},
#       {min: 200, max: 300},
#       {min: 10, max: 200, label: '10 到 200（自定义label）'},
#       // 表示 value 等于 123 的情况。
#       {value: 123, label: '123（自定义特殊颜色）', color: 'grey'}
#       {max: 5}     // 不指定 min，表示 min 为无限大（-Infinity）。
#   ]
```
### markLine&markPoint：
```python
#     图形标记组件,有标记线和标记点两种。(Bar、Line、Kline)
# mark_point -> list
#     标记点，默认有'min', 'max', 'average'可选。
#     支持自定义标记点，具体使用如下
#     [{"coord": [x1, y1], "name": "first markpoint"}, 
#      {"coord": [x2, y2], "name": "second markpoint"}]
#     需自己传入标记点字典，共有两个键值对，
#         'coord' 对应为 xy 轴坐标， 'name' 为标记点名称
# mark_point_symbol -> str
#     标记点图形，，默认为'pin'，有'circle', 'rect',
#     'roundRect', 'triangle', 'diamond', 'pin', 'arrow'可选
# mark_point_symbolsize -> int
#     标记点图形大小，默认为 50
# mark_point_textcolor -> str
#     标记点字体颜色，默认为'#fff'
# mark_point_valuedim -> list
#     标记线指定在哪个维度上指定最大值最小值。
#     这可以是维度的直接名称，Line 时可以是 x、angle 等、
#     Kline 图时可以是 open、close、highest、lowest。
#     可同时制定多个维度，如:
#         mark_point=['min', 'max'],
#         mark_point_valuedim=['lowest', 'highest'] 
#         则表示 min 使用 lowest 维度，max 使用 highest 维度，以此类推
# mark_line -> list
#     标记线，默认有'min', 'max', 'average'可选
# mark_line_symbolsize -> int
#     标记线图形大小，默认为 15
# mark_line_valuedim -> list
#     标记线指定在哪个维度上指定最大值最小值。
#     这可以是维度的直接名称，Line 时可以是 x、angle 等、
#     Kline 图时可以是 open、close、highest、lowest。
#     可同时制定多个维度，如:
#         mark_line=['min', 'max'],
#         mark_line_valuedim=['lowest', 'highest'] 
#         则表示min 使用 lowest 维度，max 使用 highest 维度，以此类推
# mark_line_coords -> [list], 
#     标记线指定起点坐标和终点坐标，
#     如 [[10, 10], [30, 30]]，两个点分别为横纵坐标轴点。
```
### tooltip：
```python
#     提示框组件，用于移动或点击鼠标时弹出数据内容
# tooltip_tragger -> str
#     触发类型。默认为 'item'
#     'item': 数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
#     'axis': 坐标轴触发，主要在柱状图，折线图等会使用类目轴的图表中使用。
#     'none': 什么都不触发。
# tooltip_tragger_on -> str
#     提示框触发的条件。默认为 "mousemove|click"
#     'mousemove': 鼠标移动时触发。
#     'click': 鼠标点击时触发。
#     'mousemove|click': 同时鼠标移动和点击时触发。
#     'none': 不在 'mousemove' 或 'click' 时触发
# tooltip_axispointer_type -> str
#     指示器类型。默认为 "line"
#     'line': 直线指示器
#     'shadow': 阴影指示器
#     'cross': 十字准星指示器。其实是种简写，
#             表示启用两个正交的轴的 axisPointer。
# tooltip_formatter -> str | function
#     模板变量有 {a}, {b}，{c}，{d}，{e}，
#     分别表示系列名，数据名，数据值等。在 trigger 为 'axis'的时候，
#     会有多个系列的数据，此时可以通过 {a0}, {a1}, {a2} 这种后面加索引
#     的方式表示系列的索引。不同图表类型下的 {a}，{b}，{c}，{d} 含义不一样：
# # 折线（区域）图、柱状（条形）图、K线图 :
# #     {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
# # 散点图（气泡）图 :
# #     {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
# # 地图 : 
# #     {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
# # 饼图、仪表盘、漏斗图: 
# #     {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
# tooltip_formatter -> function

# def tooltip_formatter(params):
# (params: Object|Array, 
#  ticket: string, 
#  callback: (ticket: string,: string)) => string
# 第一个参数 params 是 formatter 需要的数据集。格式如下：
# {
#     componentType: 'series',
#     // 系列类型
#     seriesType: string,
#     // 系列在传入的 option.series 中的 index
#     seriesIndex: number,
#     // 系列名称
#     seriesName: string,
#     // 数据名，类目名
#     name: string,
#     // 数据在传入的 data 数组中的 index
#     dataIndex: number,
#     // 传入的原始数据项
#     data: Object,
#     // 传入的数据值
#     value: number|Array,
#     // 数据图形的颜色
#     color: string,
#     // 饼图的百分比
#     percent: number,
# }
```
### toolbox：
```python
#     右侧实用工具箱
# is_toolbox_show -> bool
#     指定是否显示右侧实用工具箱，默认为 True。
# is_more_utils -> bool
#     指定是否提供更多的实用工具按钮。默认只提供『数据视图』和『下载』按钮
# add():
#     1.主要方法，用于添加图表的数据和设置各种通用配置项;
#     2.数据一般为两个长度一致的列表。
#       如果数据是字典或者是带元组的字典，可用cast()方法转换。
#     3.设置'is_more_utils=True'可以提供更多实用工具按钮。
#     4.若数据为Pandas&Numpy 时，整数类型请确保为 int，而不是numpy.int32
#     5.cast(seq)：
#         转换数据序列，将带字典和元组类型的序列转换为[keys],[values]两个列表。
#         (1)元组列表:[(A1, B1), (A2, B2), (A3, B3), (A4, B4)] 
#         (2)字典列表:[{A1: B1}, {A2: B2}, {A3: B3}, {A4: B4}] 
#         (3)字典:{A1: B1, A2: B2, A3: B3, A4: B4}
#             -->[A1,A2,A3,A4],[B1,B2,B3,B4]
# show_config():打印输出图表的所有配置项
# render():默认在根目录下生成render，支持path参数设置文件保存位置,
#         如 render(path="e:\my_first_chart")。 


```

