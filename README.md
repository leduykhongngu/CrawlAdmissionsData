# GetEntranceExaminationData
The purpose of this project is get some infomations of all students who had join the Entrace HighSchool Examination in 2019 in Binh Duong. 

The infomations is got by crawling the html of [this website](http://sgd.binhduong.gov.vn/). 

Because the result of every students is store at a url like: prefix+ID+suffix (which "http://sgd.binhduong.gov.vn/Tracuudiem/Tuyensinh10/tabid/294/NamThi/2019/DotThiId/28/ThiSinhId/" is the prefix, "/Default.aspx" is the suffix), so I just brute force all the ID and crawl the html data. 
