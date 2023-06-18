def dif_name():
    return 'Eryk'

x = dif_name()
print(x)

def a_forest(argument):
    another_tree = argument * 10
    return another_tree

total = a_forest(9)
print(total)

# unusual
'''unvailable
blaekomboebm
bvehvei
'''

def ball_in_box(argument):
    def ball_out_box():
        return 6
    ball = ball_out_box()
    special = argument / ball
    return special

final = ball_in_box(60)
print(final)
