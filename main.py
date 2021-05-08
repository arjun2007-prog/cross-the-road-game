import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()#here we are importing a a calss of turtle that helps us to control screen sizes and do other stuff
# with the screen
screen.setup(width=600, height=600)#we setup the screen width and height
screen.tracer(0)#this helps us to stop updating the screen constantly and the screen updates only when we use the
# update() method

game_is_on = True

#we are importing the class we created in diffrent files and making new objects with them
player = Player()
car = CarManager()
score = Scoreboard()

#this enables the screen to listen to players keyboard inputs and react to it
screen.listen()
#this tells the screen that wheever the w key is pressed by the player move method should be a called that is present in
# player object
screen.onkey(player.move, "w")

#this is loop that keeps runing until the user is playing the game
while game_is_on:
    #this makes all the processes of the program stop or puause for the given seconds
    time.sleep(0.1)

    #this updates the screen and shows all the new objects created
    screen.update()

    score.write_level()

    car.make_cars()

    #this runs a loop on all the cars spawned in the game
    for vehicle in car.cars:
        #and while looping through each car it check if the car is close to the turtle or has collided with the
        # turtle. The distance method from turtle class helps us to know the distance between 2 elements
        if vehicle.distance(player) < 25:
            game_is_on = False
            score.game_over()
            break

    #this checks if the turtle has reached the top and has finished the level
    if player.ycor() > 270:
        player.level_up()
        car.improve()
        score.level_up()

    car.move_car()



screen.exitonclick()