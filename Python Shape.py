import turtle
a = turtle.textinput ("Python Shape", "forward")
# VARIABLE
print(a)
# Print Var
b = turtle.textinput ("Python Shape", "turn")
# VARIABLE
print(b)
# Print Var
c = turtle.textinput ("Python Shape", "color")
# VARIABLE
print(c)
# Print Var
d = turtle.textinput ("Python Shape", "repeat time(s)")
# VARIABLE
print(d)
# Print VAriable
sc = turtle.Screen()
t = turtle
# Make it Easier
sc.setup(1300,900)
# Setup Windows(Turtle)
t.pencolor (c)
# Setup Color
for x in range(int(d)):
# Repeat
 t.forward (int(a))
#Forward
 t.left (int(b))
#Left
t.hideturtle()
t.done()
# End Codes
