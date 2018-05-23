import turtle as t

t.setup(600, 400, 100, 100)
t.penup()
t.right(90)
t.fd(100)
t.pendown()
t.left(90)
for i in range(4):
	t.circle(60 + 20 * i)
t.done()
