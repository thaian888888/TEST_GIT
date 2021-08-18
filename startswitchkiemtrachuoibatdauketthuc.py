#hàm find tìm vị trí đầu tiên kí tự xuất hiện
#hàm count đếm số lần xuất hiện của kí tự
#kiểm tra chuỗi bắt đầu kết thúc bằng gì
s='*thaian#'
print(s.startswith('*'))
print(s.startswith('#'))
print(s.endswith('*'))
print(s.endswith('#'))

#kiểm tra định dạng bài hát
s1="C:/music/edm/iloveyou.mp3"
print(s1)
if s1.endswith(".mp3"):
  print("Bài hát này có định dạng mp3")
else :
 print("Bài hát này ko có định dạng mp3")
### sau if và else câu lệnh tiếp phải thụt lùi dầu dòng


#bài tập lọc số điện thoai
def LocSoDienThoai(dauso):
    dsArr=['0901234567', '0987654321', '0984562348', 
    '0934561237', '0586523546']
    for phone in dsArr:
        if(phone.startswith(dauso)):
          return phone;
    return '<empty>';
print('Mời bạn nhập đầu số : ')
dauso=input()
phone=LocSoDienThoai(dauso)
print(phone)

#bài tập lọc toàn bộ số điện thoai
def LocToanBoSoDienThoai(dauso):
    dsArr=['0901234567', '0987654321', '0984562348', 
    '0934561237', '0586523546']
    dsFound=[]
    for phone in dsArr :
      if(phone.startswith(dauso)):
        dsFound.append(phone)           #append chèn số tìm được từ found vào print
    return dsFound
dauso=input('Mời bạn nhập vào đầu số : ')
dsFound = LocToanBoSoDienThoai(dauso)
print(dsFound)

#xóa kí tự
s='d:/tailieu/python/lamchupython.pdf'
p=s.rfind('/')
print(s[p+1:])