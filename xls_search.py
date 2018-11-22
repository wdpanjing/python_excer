#coding=utf-8
import os,re,xlrd,xlwt
os.chdir("C:\\Users\\quiet_wang\\Desktop\\python")
p = re.compile('.*本科.*')
f = xlrd.open_workbook('20181021105223_34042.xls')
sheet1 = f.sheet_by_index(1)
ncols = sheet1.ncols
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = "Times New Roman"
font.height = 220
font.bold = False
style.font = font
aln = xlwt.Alignment()
aln.horz = 0
aln.shri = 0
aln.vert = 0
style.alignment = aln
bd = xlwt.Borders()
bd
i=0
row_num=[]
for r in sheet1.col_values(13):
    if p.search(r) is not None:
        #print(r)
        row_num.append(i)
    i=i+1
fw=xlwt.Workbook(encoding='utf-8')
sheet2=fw.add_sheet('sheet2', cell_overwrite_ok=True)
for m in range(0,2):
    print(m)
    for n in range(0,ncols):
        sheet2.write(m, n, label=sheet1.cell_value(m, n), style=style)
for m in range(2, len(row_num)+2):
    k=row_num[m-2]
    for n in range(0, ncols):
        sheet2.write(m, n, label=sheet1.cell_value(k, n), style=style)
fw.save("t2.xls")
