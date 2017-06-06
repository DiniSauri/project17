import turtle
penna= turtle.Pen()
penna.shape("classic")

penna.pensize(2)
penna.penup()

penna.goto(-300,-270)
penna.pendown()
penna.color("black", "orange") #costruzione casa di fronte
penna.begin_fill()
penna.forward(500)
penna.left(90)
penna.forward(300)
penna.left(90)
penna.forward(500)
penna.left(90)
penna.forward(300)
penna.left(90)
penna.end_fill() #fine costruzione casa di fronte
penna.penup()
penna.goto(200,-270)
penna.pendown()
penna.color("black", "orange") #costruzione casa di lato
penna.begin_fill()
penna.left(45)
penna.forward(150)
penna.left(45)
penna.forward(300)
penna.left(135)
penna.forward(150)
penna.end_fill() #fine costruzione casa di lato
penna.penup()
penna.goto(-300,30)
penna.pendown()
penna.color("black", "dark red") #costruzione tetto di fronte e di lato
penna.begin_fill()
penna.left(135)
penna.left(29)
penna.forward(int((250**2 + 150**2)**(1/2)))
penna.right(59)
penna.forward(int((250**2 + 150**2)**(1/2))-10)
penna.end_fill()
penna.begin_fill()
penna.backward(int((250**2 + 150**2)**(1/2))-10)
penna.goto(306,136)
penna.end_fill() #fine costruzione tetto di fronte e di lato
penna.penup()
penna.goto(-80,-270) #costruzione porta
penna.pendown()
penna.color("black", "saddle brown")
penna.begin_fill()
penna.left(120)
penna.forward(100)
penna.right(90)
penna.forward(60)
penna.right(90)
penna.forward(100)
penna.right(90)
penna.forward(60)
penna.right(90)
penna.forward(100)
penna.right(90)
penna.forward(60)
penna.end_fill()
penna.penup() #fine costruzione porta
penna.forward(60)
penna.pendown() #costruzione finestra bassa destra
penna.color("black", "black")
penna.begin_fill()
penna.right(90)
penna.forward(40)
penna.left(90)
penna.forward(80)
penna.left(90)
penna.forward(80)
penna.left(90)
penna.forward(80)
penna.left(90)
penna.forward(40)
penna.end_fill()
penna.penup() #fine costruzione finestra bassa destra
penna.left(90)
penna.backward(60)
penna.left(180)
penna.forward(60)
penna.penup()
penna.forward(60)
penna.pendown() #costruzione finestra bassa sinistra
penna.color("black", "black")
penna.begin_fill()
penna.left(90)
penna.forward(40)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80) #fine costruzione finestra bassa sinistra
penna.end_fill()
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(135) #inizio credenza finestra bassa sinistra
penna.color("black", "gray")
penna.begin_fill()
penna.forward(10)
penna.left(45)
penna.forward(73)
penna.left(90)
penna.forward(8)
penna.left(90)
penna.forward(80)
penna.end_fill()
penna.backward(80)
penna.right(90)
penna.backward(8)
penna.right(90)

penna.backward(73)
penna.right(90)
penna.forward(73)
penna.begin_fill()
penna.backward(73)
penna.left(45)
penna.backward(10)
penna.right(45)
penna.forward(80)
penna.left(90)
penna.forward(8)
penna.end_fill()
penna.backward(8)
penna.forward(40)
penna.right(90)

penna.penup()
penna.forward(180)

penna.pendown()
penna.right(90)
penna.forward(40)
penna.left(135)
penna.begin_fill()
penna.forward(10)
penna.left(45)
penna.forward(73)
penna.left(90)
penna.forward(8)
penna.end_fill()
penna.backward(8)
penna.right(90)
penna.backward(73)
penna.right(90)
penna.forward(73)
penna.begin_fill()
penna.backward(73)
penna.left(45)
penna.backward(10)
penna.right(45)
penna.forward(80)
penna.left(90)
penna.forward(8)
penna.end_fill()
penna.backward(8)
penna.right(90)
penna.backward(80)
penna.left(90)
penna.forward(80)

penna.penup()
penna.forward(30)
penna.pendown()
penna.color("black", "black")
penna.begin_fill()
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.end_fill()

penna.right(135)
penna.color("black", "gray")
penna.begin_fill()
penna.forward(10)
penna.left(45)
penna.forward(73)
penna.left(90)
penna.forward(8)
penna.end_fill()
penna.backward(8)
penna.right(90)
penna.backward(73)
penna.right(90)
penna.forward(73)
penna.begin_fill()
penna.backward(73)
penna.left(45)
penna.backward(10)
penna.right(45)
penna.forward(80)
penna.left(90)
penna.forward(8)
penna.end_fill()
penna.backward(8)
penna.right(90)
penna.backward(80)
penna.left(90)
penna.forward(80)
penna.backward(40)
penna.left(90)
penna.penup()
penna.forward(180)
penna.pendown()
penna.left(90)
penna.forward(40)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(90)
penna.forward(80)
penna.right(135)
penna.forward(10)
penna.left(45)
penna.forward(73)
penna.backward(73)
penna.right(90)
penna.forward(73)
penna.backward(73)
penna.left(45)
penna.backward(10)
penna.right(45)
penna.forward(80)
penna.penup()
penna.forward(340)
penna.left(45)
penna.forward(35)
penna.pendown()
penna.forward(80)
penna.left(45)
penna.forward(80)
penna.left(135)
penna.forward(80)
penna.left(45)
penna.forward(80)
penna.left(157)
penna.forward(15)
penna.left(23)
penna.forward(72)
penna.backward(72)
penna.right(45)
penna.forward(72)
penna.backward(72)
penna.left(22)
penna.backward(15)
penna.left(23)
penna.penup()
penna.backward(30)
penna.left(180)
penna.pendown()
penna.forward(80)
penna.left(135)
penna.forward(80)
penna.left(45)
penna.forward(80)
penna.left(135)
penna.forward(80)
penna.left(45)
penna.forward(80)
penna.left(135)
penna.left(22)
penna.forward(15)
penna.left(23)
penna.forward(72)
penna.backward(72)
penna.right(45)
penna.forward(72)
penna.backward(72)
penna.left(23)
penna.backward(15)
penna.left(22)
penna.forward(80)
penna.penup()
penna.goto(-300,30)
penna.pendown()
penna.right(61)
penna.forward(24)
penna.right(29)
penna.forward(458)
penna.left(45)
penna.forward(138)
penna.backward(138)
penna.right(45)
penna.backward(458)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(416)
penna.left(45)
penna.forward(126)
penna.backward(126)
penna.right(45)
penna.backward(416)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(374)
penna.left(45)
penna.forward(114)
penna.backward(114)
penna.right(45)
penna.backward(374)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(332)
penna.left(45)
penna.forward(102)
penna.backward(102)
penna.right(45)
penna.backward(332)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(291)
penna.left(45)
penna.forward(89)
penna.backward(89)
penna.right(45)
penna.backward(291)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(250)
penna.left(45)
penna.forward(76)
penna.backward(76)
penna.right(45)
penna.backward(250)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(209)
penna.left(45)
penna.forward(63)
penna.backward(63)
penna.right(45)
penna.backward(209)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(168)
penna.left(45)
penna.forward(50)
penna.backward(50)
penna.right(45)
penna.backward(168)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(127)
penna.left(45)
penna.forward(37)
penna.backward(37)
penna.right(45)
penna.backward(127)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(88)
penna.left(45)
penna.forward(24)
penna.backward(24)
penna.right(45)
penna.backward(88)
penna.left(29)
penna.forward(24)
penna.right(29)
penna.forward(47)
penna.left(45)
penna.forward(11)
penna.backward(11)
penna.right(45)
penna.backward(47)
penna.left(29)
penna.backward(264)
penna.right(29)