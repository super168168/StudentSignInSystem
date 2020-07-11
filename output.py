# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     output
   Description :  输出结果到外部文件，传进格式为dict对象
   Author :       joryzhu
   date：          2020/6/17
-------------------------------------------------
   Change Activity:
                   2020/6/17:
-------------------------------------------------
"""
__author__ = 'joryzhu'
# 传进识别结果，对识别结果进行格式处理
'''
格式模板:
recognition_result = [{'Name':'XXX','Recognition_status':'Success/Faild'},{'Name':'XXX','Recognition_status':'Success/Faild'}]
函数调用:
PushResult(recognition_result)
'''
import time
import xlwt
import xlrd
import sys
import importlib
import os
from xlutils.copy import copy;

# 设置xls中的字体
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


class output(object):
    importlib.reload(sys)
    # sys.setdefaultencoding('utf-8')

    # 传进格式为dict的识别结果
    def PushResult(self, recognition_result):
        if recognition_result != None:
            self.current_time = time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
            self.college = "北京理工大学珠海学院"
            self.profession = "计算机科学与技术"
            self.grade = "2017级"
            self.recognition_type = "程序识别"
            self.output_result = []
            for v in recognition_result:
                self.recognition_status = v['Recognition_status']
                self.Name = v['Name']

                self.output_result.append([self.Name, self.college, self.profession, self.grade,
                                           self.recognition_type, self.recognition_status,
                                           self.current_time])
            self.OutputResult(self.output_result)


    # 输出指定格式的识别结果到test,xls文件
    def OutputResult(self, output_result):
        if self.output_result != None:
            if (os.path.isfile("test.xls")):

                # f = xlwt.Workbook()
                rb = xlrd.open_workbook('test.xls')
                f = copy(rb)
                # sheet1 = f.add_sheet('学生签到信息', cell_overwrite_ok=True)
                sheet1 = f.get_sheet(0)
                row0 = ["姓名", "学校", "专业", "年级", "识别方式", "签到状态", "签到时间"]
                # 写入excel数据
                # for i in range(0, len(row0)):
                #     sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, False))
                k = len(sheet1.rows)
                for index in range(0, len(output_result)):
                    for index_1 in range(0, len(output_result[index])):
                        print(output_result[index][index_1])
                        sheet1.write(k, index_1, output_result[index][index_1],
                                     set_style('Times New Roman', 220, False))
                f.save('test.xls')

            else:
                f = xlwt.Workbook()
                sheet1 = f.add_sheet('学生签到信息', cell_overwrite_ok=True)
                row0 = ["姓名", "学校", "专业", "年级", "识别方式", "签到状态", "签到时间"]
                # 写入excel数据
                for i in range(0, len(row0)):
                    sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, False))
                # k = len(sheet1.rows)
                for index in range(0, len(output_result)):
                    for index_1 in range(0, len(output_result[index])):
                        print(output_result[index][index_1])
                        sheet1.write(index + 1, index_1, output_result[index][index_1],
                                     set_style('Times New Roman', 220, False))
                f.save('test.xls')



if __name__ == '__main__':
    recognition_result = [{'Name': 'AXB', 'Recognition_status': 'Success/Faild'}]
    output().PushResult(recognition_result)
