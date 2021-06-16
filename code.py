import re

from bs4 import BeautifulSoup

import requests

import unicodecsv as csv


def format_string(s: str):
    return s.strip(": \r\n")


def format_int(s: str):
    s = format_string(s)
    s = re.search(r"\d*", s)
    if s is None:
        return 0
    s = s[0]
    if len(s) == 0:
        return 0
    return int(s)


def format_float(s: str):
    s = format_string(s.replace(",", "."))
    s = re.search(r"\d*\.*\d*", s)
    if s is None:
        return ""
    s = s[0]
    if len(s) == 0:
        return ""
    return float(s)


class Student:
    def __init__(this, data):
        this.name = format_string(data[0].th.span.string)
        this.id = format_int(data[1].td.string)
        this.birthday = format_string(data[2].td.string)
        this.sex = format_string(data[3].td.string)
        this.born_in = format_string(data[4].td.string)
        this.sec_school = format_string(data[5].td.string)
        this.nv1 = format_int(data[6].td.string)
        this.nv2 = format_int(data[7].td.string)
        this.nvC1 = format_string(data[8].td.string)
        this.nvC2 = format_string(data[9].td.string)
        this.priority_points = format_float(data[10].td.string)
        data = data[11].find_all("th")
        this.p_van = format_float(data[7].string)
        this.p_anh = format_float(data[8].string)
        this.p_toan = format_float(data[9].string)
        this.p_chuyen1 = format_float(data[10].string)
        this.p_chuyen2 = format_float(data[11].string)
        tmp = re.findall(r": [\w0-9\.]*\r", data[12].text.replace(",", "."))
        this.sum_TVA = format_float(tmp[0])
        this.sum_chuyen1 = format_float(tmp[1])
        this.sum_chuyen2 = format_float(tmp[2])


BASE_URL = "http://sgdbinhduong.edu.vn/Tracuudiem/Tuyensinh10/tabid/294/NamThi/2020/DotThiId/34/ThiSinhId/{}/Default.aspx"

heading = [u"Tên", u"SBD", u"Ngày sinh", u"Giới Tính", u"Nơi sinh", u"Trường", u"Nguyện vọng 1",
           u"Nguyện vọng 2", u"Chuyên 1", u"Chuyên 2", u"Điểm ưu tiên", u"Văn", u"Anh", u"Toán",
           u"Chuyên 1", u"Chuyên 2", u"Tổng", u"Tổng chuyên 1", u"Tổng chuyên 2"]

with open("Tuyensinh10.csv", "ab") as writeFile:
    writer = csv.writer(writeFile, encoding="utf-8")
    writer.writerow(heading)
    L = 149774
    # R = 149780
    R = 150486
    for i in range(L, R+1):
        print("Geting", i)
        x = requests.get(BASE_URL.format(i)).text
        soup = BeautifulSoup(x, "html.parser")
        Test = Student(soup.tbody.find_all("tr"))
        writer.writerow([Test.name, Test.id, Test.birthday, Test.sex, Test.born_in, Test.sec_school,
                         Test.nv1, Test.nv2, Test.nvC1, Test.nvC2, Test.priority_points, Test.p_van,
                         Test.p_anh, Test.p_toan, Test.p_chuyen1, Test.p_chuyen2, Test.sum_TVA,
                         Test.sum_chuyen1, Test.sum_chuyen2])

writeFile.close()
