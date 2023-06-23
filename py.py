# def statement (this statement don't have argument)
def x_name():
    return 'Alex'

x = x_name()
print(x)

# def statement (this statement has argument)
def a_forest(argument):
    another_tree = argument * 1
    return another_tree

total = a_forest(6)
print(total)

# This is nesting (or nested functions)
#folding sth
def ball_in_box(argument):
    def ball_out_box():
        return 6
    ball = ball_out_box()
    special = argument / ball
    return special

final = ball_in_box(60)
print(final)

# The way we can write comments in Python
'''
unvailable
belief
anyway
This way we can write comments in Python with more than 1 line
'''









