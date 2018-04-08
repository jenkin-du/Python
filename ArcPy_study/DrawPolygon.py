# -*- coding: utf-8 -*-

import arcpy


arcpy.env.overwriteOutput = True
# 指定输出数据的路径
outputFeatureClass = r"H:\编程\数据\Python\ArcPython\Holepoly.shp"


def drawPolygon(coord_list):
    array = arcpy.Array()
    point = arcpy.Point()

    features = []
    # 读取坐标串
    for part in coord_list:
        for coordPair in part:
            point.X = coordPair[0]
            point.Y = coordPair[1]

            array.add(point)
        null_point = arcpy.Point()
        array.add(null_point)

    # 调用ArcPy绘制多边形
    polygon = arcpy.Polygon(array)
    features.append(polygon)

    # 生成要素类
    arcpy.CopyFeatures_management(features, outputFeatureClass)


if __name__ == '__main__':
    coordList = [[[0, 0], [0, 10], [10, 10], [10, 0], [0, 0]], [[4, 4], [4, 6], [6, 6], [6, 4], [4, 4]]]

    drawPolygon(coordList)