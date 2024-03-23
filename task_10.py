import turtle
import ru_local as ru

x_l1 = float(input('xl1 = '))
y_l1 = float(input('yl1 = '))
x_r1 = float(input('xr1 = '))
y_r1 = float(input('yr1 = '))
x_l2 = float(input('xl2 = '))
y_l2 = float(input('yl2 = '))
x_r2 = float(input('xr2 = '))
y_r2 = float(input('yr2 = '))

turtle.up()
turtle.setposition(x_l1, y_l1)
turtle.down()
turtle.forward(x_r1 - x_l1)
turtle.right(90)
turtle.forward(y_l1 - y_r1)
turtle.right(90)
turtle.forward(x_r1 - x_l1)
turtle.right(90)
turtle.forward(y_l1 - y_r1)
turtle.right(90)

turtle.up()
turtle.setposition(x_l2, y_l2)
turtle.down()
turtle.forward(x_r2 - x_l2)
turtle.right(90)
turtle.forward(y_l2 - y_r2)
turtle.right(90)
turtle.forward(x_r2 - x_l2)
turtle.right(90)
turtle.forward(y_l2 - y_r2)
turtle.right(90)

turtle.up()
turtle.setposition(-200, -200)
turtle.down()
if x_l1 > x_r2 or x_r1 < x_l2 or y_l1 < y_r2 or y_r1 > y_l2:
    turtle.write(ru.RECTANGLE_NO_TOUCH, False, 'left', ('Arial', 15, 'normal'))
elif x_l1 < x_l2 and x_r1 > x_r2 and y_l1 > y_l2 and y_r1 < y_r2:
    turtle.write(ru.RECTANGLE_INSIDE, False, 'left', ('Arial', 15, 'normal'))
elif (x_l1 == x_r2 or x_r1 == x_l2 or y_l1 == y_r2 or y_r1 == y_l2 or
      (x_l1 == x_l2 and y_l2 <= y_l1 and y_r2 >= y_r1 and x_r2 <= x_r1) or
      (x_r1 == x_r2 and y_l2 <= y_l1 and y_r2 >= y_r1 and x_l2 >= x_l1) or
      (y_l1 == y_l2 and x_l2 >= x_l1 and y_r2 >= y_r1 and x_r2 <= x_r1) or
      (y_r1 == y_r2 and y_l2 <= y_l1 and x_r2 <= x_r1 and x_l2 >= x_l1)):
    turtle.write(ru.RECTANGLE_TOUCH, False, 'left', ('Arial', 15, 'normal'))
else:
    turtle.write(ru.RECTANGLE_INTERSECTION, False, 'left', ('Arial', 15, 'normal'))

turtle.done()
