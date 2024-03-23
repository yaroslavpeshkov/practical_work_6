import turtle
import ru_local as ru

x_1 = float(input('x1 = '))
y_1 = float(input('y1 = '))
r_1 = float(input('r1 = '))
x_2 = float(input('x2 = '))
y_2 = float(input('y2 = '))
r_2 = float(input('r2 = '))

turtle.up()
turtle.setposition(x_1, y_1 - r_1)
turtle.down()
turtle.circle(r_1)

turtle.up()
turtle.setposition(x_2, y_2 - r_2)
turtle.down()
turtle.circle(r_2)

turtle.up()
turtle.setposition((x_1 + x_2)/2, min(x_1, x_2) - max(r_1, r_2) - 20)
turtle.down()
distance = ((x_2 - x_1)**2 + (y_2 - y_1)**2)**0.5
if distance > r_1 + r_2:
    turtle.write(ru.NO_TOUCH, False, 'left', ('Arial', 15, 'normal'))
elif distance == r_1 + r_2:
    turtle.write(ru.EXTERNAL_TOUCH, False, 'left', ('Arial', 15, 'normal'))
elif abs(r_1 - r_2) < distance < r_1 + r_2:
    turtle.write(ru.INTERSECTION, False, 'left', ('Arial', 15, 'normal'))
elif distance == abs(r_1 - r_2):
    turtle.write(ru.INNER_TOUCH, False, 'left', ('Arial', 15, 'normal'))
else:
    turtle.write(ru.INSIDE, False, 'left', ('Arial', 15, 'normal'))

turtle.done()
