#
#2023-3-1 "March fixed by Jude F."
#
#
#
#######################################################

import calendar
import datetime
import os,sys
from fpdf import FPDF
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIcon, QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import QApplication, QCompleter, QWidget

monthList = [
"January", "Febrary", "March", "April", "May", "June",
"July", "Augest",  "September", "October", "November", "December"
]

yearSelect = 0
monthSelect = 0
monthString = ''
class Ui_cipconsolelog(object):

    def __init__(self):
        super().__init__()
        print('__init__')

    
    # 需要导入模块: from PyQt5 import QtWidgets [as 别名]
    # 或者: from PyQt5.QtWidgets import QDateEdit [as 别名]
    def setupUi2(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 250)
        self.calendarWidget = QtWidgets.QCalendarWidget(Dialog)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 0, 312, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.selectionChanged.connect(self.getDate)
        
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onButtonClick)
        self.pushButton.setText('Create PDF')
        
        #self.dateEdit = QtWidgets.QDateEdit(Dialog)
        #self.dateEdit.setGeometry(QtCore.QRect(120, 260, 110, 22))
        #self.dateEdit.setObjectName("dateEdit")

        #self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)     

    def getDate(self):
        self.date = str(self.calendarWidget.selectedDate())
        self.date = self.date.split('(')[1]
        self.date = self.date.split(')')[0]
        self.date = self.date.split(',')
        self.year  = self.date[0]
        self.month = self.date[1].strip()
        #self.day   = int(self.date[2])
        #monthRange = calendar.monthrange(self.date[0], self.date[1])
        self.path = (self.year)+ '-' + (self.month)
        print(self.path)
        
    def create_pdf(self, year, month):
        monthRange = calendar.monthrange(int(year), int(month))[1]
        #monthRange = int(self.monthRange[1])
        print(monthRange)
        for d in range(int(monthRange)):
            release_pdf(str(d+1), year, month)
            quote_pdf(str(d+1), year, month)
            pass
 
    def onButtonClick(self):
        mkdir(self.path)
        self.create_pdf(self.year, self.month)
        print("Click")
       
            

def release_pdf(day, year, month):
    monthString = monthList[int(month)-1]
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 38)
    for n in range(0,10):
        pdf.cell(200,10,'', ln=1, align='C')
        
    pdf.cell(200,10,'OFFICIALLY RELEASED', ln=1, align='C')

    pdf.set_font('Arial', '', 20)
    pdf.cell(200,10,'DOCUMENT CONTROL', ln=1, align='C')

    pdf.set_font('Arial', '', 36)
    pdf.cell(200,10, monthString+' '+day+', '+str(year), align='C')

    pdf.output(year+'-'+month+'/'+"RELEASED"+'-'+str(year)+'-'+monthString+ '-'+day +'.pdf')
    #print(year+'-'+month+'/'+"RELEASED"+'-'+str(year)+'-'+monthString+ '-'+day +'.pdf')

def quote_pdf(day, year, month):
    monthString = monthList[int(month)-1]
    pdf = FPDF()
    pdf.add_page()
    #pdf.set_font(family='Times New Roman', style="", size=36)
    #pdf.set_font('Times New Roman', '', 36)
    pdf.set_font('helvetica', '', 36)
    #pdf.set_font('Arial', '', 36)
    for n in range(0,10):
        pdf.cell(200,10,'', ln=1, align='C')
    
    #pdf.text(50, 50, "Hello!")    
    pdf.cell(200,15,'UNAPPROVED PRINT', border=0, ln=1, align='C')
    pdf.cell(200,15,'FOR QUOTE ONLY', ln=1, align='C')

    pdf.set_font('', '', 20)
    pdf.cell(200,10,'Do Not Use to Manufacture Parts', ln=1, align='C')

    pdf.set_font('', '', 36)
    pdf.cell(200,30, monthString+' '+day+', '+str(year), ln=1, align='C')

    pdf.output(year+'-'+month+'/'+"QUOTE"+'-'+str(year)+'-'+monthString+ '-'+day +'.pdf')

        
        
def mkdir(path):
    '''
    创建指定的文件夹
    :param path: 文件夹路径，字符串格式
    :return: True(新建成功) or False(文件夹已存在，新建失败)
    '''
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
         # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

def getCurrentTime():
    now_time = datetime.datetime.now()
    nowtime_str = datetime.datetime.strftime(now_time,'%Y-%m-%d!%H%M%S')
    today = datetime.date.today()
    monthRange = calendar.monthrange(today.year, today.month)
    monthStr = monthList[today.month-1]
    print(nowtime_str)
    print(int(monthRange[1]))
    print(today.year)
    print(today.month)


#os.system('pause')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = QWidget()
    form.setWindowTitle('WatermarkPDF')
    w = Ui_cipconsolelog()
    w.setupUi2(form)
    #w.createForm()
    form.show()
    sys.exit(app.exec_())
 





