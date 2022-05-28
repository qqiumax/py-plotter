#-------------------------------------------------------------------------------
# Name:        Automated Graphing machine
# Purpose: An Automated graphics machine that helps you to graph using pyplot
#
# Author:      Max Qiu
#
# Created:     25/05/2022
# Copyright:   (c) Max Qiu 2022
# Licence:     <GNU Public License v3.0>

# SEE IT AT GITHUB: qqiumax/py-plotter
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plot
num = 0
names = []
datas = []
flag_bar_norm = True
def import_name():
    global num
    num = int(input('number of data sets'))
    for i in range(num):
        name = input('name number here: ')
        names.append(name)
def import_data():
    for i in range(num):
        data = input('data number here: ')
        global datas
        datas.append(float(data))
    datas.sort()

def bar(names,datas,flag_bar_norm): #flag_bar_norm is a boolean
    width = float(input('bar width, a suggested one is 0.8: '))
    if flag_bar_norm == 'True':
        plot.bar(names,datas,width)
    else:
        plot.barh(names,datas,width)
def line(names,datas):
    line_type = input("line type, - for solid, : for dotted, -- for dashed, -. for dashdot: ")
    plot.plot(names,datas,line_type)
def pie(names,datas):
    plot.pie(datas,names)
def scatter(names,datas):
    plot.scatter(names,datas)
def header():
    x_label = input('x axis label here, press enter for none: ')
    if x_label != '':
        plot.xlabel(x_label)
    y_label = input('y axis label here, press enter for none: ')
    if y_label != '':
        plot.ylabel(y_label)
    title = input('Title here, press enter for none: ')
    if title != '':
        plot.title(title)
if __name__ == "__main__":
    import_name()
    import_data()
    flag = input("type here, bar,line,pie,or scatter")
    if flag == "bar":
        a = input('do you want to have horizontal, y/n: ')
        if a == 'y':
            flag_bar_norm == False
        bar(names,datas,flag_bar_norm)
    if flag == "line":
        line(names,datas)
    if flag == "pie":
        pie(names,datas)
    if flag == "scatter":
        scatter(names,datas)
    header()
    plot.show()

