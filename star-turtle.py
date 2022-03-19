import turtle
tao = turtle.Pen()   #ใช้ปากกา
tao.shape ('turtle') #แปลงเป็นเต่า
def star ():
    '''ฟังชั้นนี้เอาไว้วนรูปดาว'''
    for i in range(20):
        tao.forward(i * 10)
        tao.right(144)


star()   #คำสั่งเริ่มการทำงาน
