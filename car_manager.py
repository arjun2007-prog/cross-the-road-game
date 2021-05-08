from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
move_distance = 5
MOVE_INCREMENT = 2

class CarManager():
    def __init__(self):
        #This is a array where all the car elements are stored
        self.cars = []

    def make_cars(self):
        #in this function all the car elements are made.
        #here a random number is generated between 1 and 6 (1,2,3,4,5)
        num = randint(1,6)
        #and if and only if the random number generated is 1 then only a new car is generated and appended into
        # the array. This makes the generation of cars random and prevents a new car being generated on every run
        # of the loop
        if num == 1:
          new_car = Turtle()
          new_car.penup()
          new_car.shape("square")
          y = randint(-250, 250)
          new_car.goto(300, y)
          new_car.color(choice(COLORS))
          new_car.shapesize(1, 2)
          new_car.setheading(180)
          self.cars.append(new_car)

    def move_car(self):
        global move_distance
        for car in self.cars:
            car.forward(move_distance)

    def improve(self):
        #here whenever the turtle levels up. the amount of steps the car takes everytime it moves forward is
        # increased by 2. This make the cars go faster
        global move_distance
        global MOVE_INCREMENT
        move_distance += MOVE_INCREMENT
