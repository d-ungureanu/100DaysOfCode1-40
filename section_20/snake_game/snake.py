from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):

        self.body_segments = []

        for position in STARTING_POSITIONS:
            self.add_segment(position)

        self.head = self.body_segments[0]

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.body_segments.append(new_segment)

    def extend_body(self):
        self.add_segment(self.body_segments[-1].position())

    def move(self):
        for segment_number in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[segment_number - 1].xcor()
            new_y = self.body_segments[segment_number - 1].ycor()
            self.body_segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

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
