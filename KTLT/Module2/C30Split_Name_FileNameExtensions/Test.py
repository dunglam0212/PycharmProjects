from Module2.C30Split_Name_FileNameExtensions.Process import Return_Filename, \
    Return_FileNameExtentions

path = "d:\music\muabui.mp3"
path = "C:\Dung Lam\PycharmProjects\TDLT\LearnPyQtDesign\MainWindow.ui"
rs = Return_FileNameExtentions(path)
print(rs)

rs1 = Return_Filename(path)
print(rs1)