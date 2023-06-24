# def statement

# def statement without argumnent
def pyn_name():
    return 'Alex'

x = pyn_name()
print(x)

# def statement with argument
def a_forest(argument):
    another_tree = argument * 1
    return another_tree

z = a_forest(6)
print(z)

# nesting (or nested statement)
# folding sth
def ball_in_box(argument):
    def ball_out_box():
        return 2
    x = ball_out_box()
    alone = argument / x
    return alone

final = ball_in_box(6)
print(final)






