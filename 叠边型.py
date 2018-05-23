import turtle as t 
t.setup(600, 400, 100, 100)
t.penup()
t.fd(-150)
t.right(90)
t.fd(100)
t.left(90)
t.pendown()
t.fd(180)
for i in range(8):
	t.left(80)
	t.fd(180)
t.done()