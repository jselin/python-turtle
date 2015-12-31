#!/usr/bin/env python
#
# A tool to create Lindemayer drawings with Turtle
#
# Coryright Jari Selin 2015
#
#

import turtle 

class lindemayer:
    def __init__(self, start, replacement_rules, iterations = 5, size = 4,  angle = 25, ):
        self.position_stack = []
        self.heading_stack = []

        self.angle = 25
        self.size = 4

        self.rules = {"-":self.turn_left, "+":self.turn_right, "F":self.go_forward, "G":self.go_forward, "[": self.store, "]":self.retrieve, "X":self.nop }

        self.commands = self.replace(start, replacement_rules, iterations)

    def replace(self, commands, replacement_rules, n ):
        for i in range(n):
            new_commands = ""
            for element in commands:
                new_commands = new_commands + replacement_rules.get(element,element)
            commands = new_commands
        return commands

    def draw(self):
        for b in self.commands:
            self.rules[b]()

    def turn_left(self):
        turtle.left(self.angle)

    def turn_right(self):
        turtle.right(self.angle)

    def go_forward(self):
        turtle.forward(self.size)

    def store(self):
        self.position_stack.append(turtle.pos())
        self.heading_stack.append(turtle.heading())

    def retrieve(self):
        turtle.up()
        turtle.goto(self.position_stack.pop())
        turtle.setheading(self.heading_stack.pop())
        turtle.down()

    def nop(self):
        pass

    def __del__(self):
        pass

if __name__ == "__main__":
    lindemayer = lindemayer(start = "X",
                            replacement_rules = {"F": "FF", "X": "F-[[X]+X]+F[+FX]-X"},
                            iterations = 6,
                            size = 4,
                            angle = 25)

    print lindemayer.commands

    turtle.color("#4ddd4b")
    turtle.speed(0)
    turtle.hideturtle()
    turtle.up()
    turtle.goto(-200,-200)
    turtle.left(80)
    turtle.down()

    lindemayer.draw()
    input()    






