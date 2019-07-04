from bs4 import BeautifulSoup
import requests
import re
import unicodecsv as csv
def FormatString(s:str):
    return s.strip(": \r\n")
def FormatInt(s:str):
    s=FormatString(s)
    s=re.search(r"\d*",s)
    if (s==None): return 0
    s=s[0]
    if (len(s)==0): return 0
    return int(s)
def FormatFloat(s:str):
    s=FormatString(s.replace(',','.'))
    s=re.search(r"\d*\.*\d*",s)
    if (s==None): return float(0)
    s=s[0]
    if (len(s)==0): return float(0)
    return float(s)
class Studen:
    def __init__(this,data):
        this.name=FormatString(data[0].th.span.string)
        this.SBD=FormatInt(data[1].td.string)
        this.birthday=FormatString(data[2].td.string)
        this.sex=FormatString(data[3].td.string)
        this.BornIn=FormatString(data[4].td.string)
        this.SecSchool=FormatString(data[5].td.string)
        this.nv1=FormatInt(data[6].td.string)
        this.nv2=FormatInt(data[7].td.string)
        this.nvC1=FormatString(data[8].td.string)
        this.nvC2=FormatString(data[9].td.string)
        this.PriorityPoints=FormatFloat(data[10].td.string)
        data=data[11].find_all('th')
        this.SVan=FormatFloat(data[7].string)
        this.SAnh=FormatFloat(data[8].string)
        this.SToan=FormatFloat(data[9].string)
        this.SC1=FormatFloat(data[10].string)
        this.SC2=FormatFloat(data[11].string)
        tmp=re.findall(r": [\w0-9\.]*\r",data[12].text.replace(',','.'))
        this.SumTVA=FormatFloat(tmp[0])
        this.SumC1=FormatFloat(tmp[1])
        this.SumC2=FormatFloat(tmp[2])


Prefix="http://sgd.binhduong.gov.vn/Tracuudiem/Tuyensinh10/tabid/294/NamThi/2019/DotThiId/28/ThiSinhId/"
Suffix="/Default.aspx"
Line=[u'Tên',u'SBD',u'Ngày sinh',u'Giới Tính',u'Nơi sinh',u'Trường',u'Nguyện vọng 1',u'Nguyện vọng 2',u'Chuyên 1',u'Chuyên 2',u'Điểm ưu tiên',u'Văn',u'Anh',u'Toán',u'Chuyên 1',u'Chuyên 2',u'Tổng',u'Tổng chuyên 1',u'Tổng chuyên 2']
with open('Tuyensinh10.csv','ab') as writeFile:
    writer = csv.writer(writeFile,encoding='utf-8')
    writer.writerow(Line)
    L=124294
    R=138890
    for i in range(L,R+1):
        print("Geting",i)
        x=requests.get(Prefix+str(i)+Suffix).text
        soup=BeautifulSoup(x,'html.parser')
        Test = Studen(soup.tbody.find_all('tr'))
        writer.writerow([Test.name,Test.SBD,Test.birthday,Test.sex,Test.BornIn,Test.SecSchool,Test.nv1,Test.nv2,Test.nvC1,Test.nvC2,Test.PriorityPoints,Test.SVan,Test.SAnh,Test.SToan,Test.SC1,Test.SC2,Test.SumTVA,Test.SumC1,Test.SumC2])
        #print("Tên {}\nSBD {}\nNgày sinh {}\nGiới Tính {}\nNơi sinh {}\nTrường {}\nNguyện vọng 1 {}\nNguyện vọng 2 {}\nChuyên 1 {}\nChuyên 2 {}\nĐiểm ưu tiên {}\nVăn {}\nAnh {}\nToán {}\nChuyên 1 {}\nChuyên 2 {}\nTổng {}\nTổng chuyên 1 {}\nTổng chuyên 2 {}\n".format(Test.name,Test.SBD,Test.birthday,Test.sex,Test.BornIn,Test.SecSchool,Test.nv1,Test.nv2,Test.nvC1,Test.nvC2,Test.PriorityPoints,Test.SVan,Test.SAnh,Test.SToan,Test.SC1,Test.SC2,Test.SumTVA,Test.SumC1,Test.SumC2))
writeFile.close()
