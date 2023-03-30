import calendar
import datetime
from fpdf import FPDF

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


monthList = [
"January", "Febrary", "Match", "April", "May", "June",
"July", "Augest",  "September", "October", "November", "December"
]
now_time = datetime.datetime.now()
nowtime_str = datetime.datetime.strftime(now_time,'%Y-%m-%d!%H%M%S')
today = datetime.date.today()
monthRange = calendar.monthrange(today.year, today.month)
monthStr = monthList[today.month-1]
print(nowtime_str)
print(int(monthRange[1]))
print(today.year)
print(today.month)
print(monthStr)


path = str(today.year)+monthStr
mkdir(path)

'''
cal = calendar.month(2020,12).strip()
#print(cal)
#print(cal[-3:])
#print(cal[1:9])

month = cal.split(' ')[0]
year = cal.split(' ')[1]
#month = monthlist[0].split(' ')[0].strip()
#print(month+", "+ year)

#for d in monthRange:
#    print(month+" "+ d + ", "+ year)

'''
def release_pdf(path, day):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 38)
    for n in range(0,10):
        pdf.cell(200,10,'', ln=1, align='C')
        
    pdf.cell(200,10,'OFFICIALLY RELEASED', ln=1, align='C')

    pdf.set_font('Arial', '', 20)
    pdf.cell(200,10,'DOCUMENT CONTROL', ln=1, align='C')

    pdf.set_font('Arial', '', 36)
    pdf.cell(200,10,monthStr+' '+day+', '+str(today.year), ln=1, align='C')

    pdf.output(path+'/'+"RELEASED"+str(today.year)+'-'+monthStr+ day +'.pdf', 'F')

def quote_pdf(path, day):
    pdf = FPDF()
    #pdf = FPDF(format='letter', unit='in')
    #pdf.add_font('Times New Roman', '', fname=r'C:\Windows\Fonts\Times New Roman.ttf', uni=True)

    pdf.add_page()
    #pdf.set_font(family='Times New Roman', style="", size=36)
    #pdf.set_font('Times New Roman', '', 36)
    #pdf.set_font('helvetica', '', 36)
    pdf.set_font('Arial', '', 36)
    for n in range(0,10):
        pdf.cell(200,10,'', ln=1, align='C')
    
    #pdf.text(50, 50, "Hello!")    
    pdf.cell(200,15,'UNAPPROVED PRINT', ln=1, align='C')
    pdf.cell(200,15,'FOR QUOTE ONLY', ln=1, align='C')

    pdf.set_font('Arial', '', 20)
    pdf.cell(200,10,'Do Not Use to Manufacture Parts', ln=1, align='C')

    pdf.set_font('Arial', '', 36)
    pdf.cell(200,30,monthStr+' '+day+', '+str(today.year), ln=1, align='C')

    pdf.output(path+'/'+"QUOTE"+str(today.year)+'-'+monthStr+ day +'.pdf', 'F')



for d in range(1,int(monthRange[1]+1)):
    release_pdf(path, str(d))
    quote_pdf(path, str(d))
    pass









