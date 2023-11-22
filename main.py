# import another_module
# print(another_module.another_variable)

# import  turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.color('blue')
# timmy.shape('turtle')
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()


table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"]
])
table.align["Pokemon Name"] = "l"

print(table)