from turtle import Turtle

STARTING_POSTIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSTIONS:
            snake = Turtle("square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.snake_body.append(snake)
        print("Snake has been created!")

    def move(self):
        for s in range(len(self.snake_body)-1, 0, -1):
            new_x = self.snake_body[s-1].xcor()
            new_y = self.snake_body[s-1].ycor()
            self.snake_body[s].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        x = self.snake_body[-1].xcor()
        y = self.snake_body[-1].ycor()
        position = (x, y)
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def reset(self):
        for snake in self.snake_body:
            snake.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    