"""
Name: {Marisa Inkaew}
SID: {363411760002}
Group: {MIT431}
"""

myList = [10,20,30,40,50]
myList
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
print(type(myList))
# แสดงผลข้อมูล 20 จาก myList
print(myList[1])
thislist = ["10","20","30","40","50"]
print(thislist[1])
# แสดงผลข้อมูล 50 จาก myList
thislist = ["10","20","30","40","50"]
print(myList[4])
# แสดงผลข้อมูล {20,30,40} โดยใช้ range index
print(myList[1:4])
# แสดงผลข้อมูล {40,50} โดยใช้ range index
print(myList[3:5])
# แสดงผลข้อมูล {10,20} โดยใช้ range negative index
print(myList[-5:-3])
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ while loop
x = 0
while x < (len(myList)):
    print(myList[x])
    x +=1
# แสดงผลข้อมูลใน myList ทั้งหมด โดยการใช้ for loop
for x in myList:
    print(x)
# เพิ่มข้อมูล 100,200,300 ใน myList
myList.append(100)
myList.append(200)
myList.append(300)
print(myList)
# เพิ่มข้อมูล 400 ใน myList ในตำแหน่งที่ 0
myList.insert(0,400)
print(myList)
# เพิ่มข้อมูล 500 ใน myList ในตำแหน่งที่ 3
myList.insert(3,500)
print(myList)
print(len(myList))
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# myList.insert(5,400)
print(myList)
# ลบข้อมูล 10
myList.remove(10)
print(myList)
# ลบข้อมูล 100
myList.pop(-3)
# แสดงผลข้อมูลใน myList ทั้งหมด
print(myList)
# ลบข้อมูล50
del myList[-3]
print(myList)
# ลบข้อมูลตำแหน่งสุดท้ายใน myList
myList.pop
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)
# เรียงข้อมูล myList จาก น้อย-มาก
(myList.sort())
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)
# เรียงข้อมูล myList จาก มาก-น้อย
myList.sort(reverse=True)
# แสดงผลข้อมูลใน myList ทั้งหมด 
print(myList)
# comprehension
# คัดลอกข้อมูลใน myList ที่มีค่ามากกว่า 50 มาเก็บไว้ใน newList
mylist = ["100","200","300","400","500"]
newlist = [x for x in myList if x >=(100)if x >=50]
for x in mylist:
  if ">50" in x:
    newlist.append(x)
# แสดงผลข้อมูลใน newList ทั้งหมด 
print(newlist)
# นำข้อมูลใน mylist และ newList มารวมกัน และเก็บไว้ในตัวแปร myFinalList
myFinalList = myList+newlist
# แสดงผลข้อมูลใน myFinalList ทั้งหมด 
print(myFinalList)