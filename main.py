from tkinter import *
from cell import Cell
from settings import GRID_SIZE, win_height, win_width
from utils import get_percent

root = Tk()
root.title('TIC TAC TOE')
root.geometry(f'{str(win_width)}x{str(win_height)}')
root.resizable(height = False, width = False)

# frames of the game
top_frame = Frame(root, bg = 'black', width=get_percent(win_width, 100), height= get_percent(win_height, 10))
top_frame.place(x = 0, y = 0)

game_frame = Frame(root, bg = 'black', width=get_percent(win_width, 75), height=get_percent(win_height, 80))
game_frame.place(x = get_percent(win_width, 12.5), y = get_percent(win_height, 10))


# side frames for color
left_frame = Frame(root, bg = 'DeepSkyBlue', width=get_percent(win_width, 12.5), height = get_percent(win_height, 90))
left_frame.place(x = 0, y = get_percent(win_height, 10))

right_frame = Frame(root, bg = 'DeepSkyBlue', width=get_percent(win_width, 14.7), height = get_percent(win_height, 90))
right_frame.place(x = get_percent(win_height, 85.5), y = get_percent(win_height, 10))

bottom_frame = Frame(root, bg = 'black', width=get_percent(win_width, 100), height = get_percent(win_height, 15))
bottom_frame.place(x = get_percent(win_height, 0), y = get_percent(win_height, 85.5))



title = Label(top_frame, bg = 'black', fg = 'orange', text='TIC TAC TOE', font = ('', 48))
title.place(x = get_percent(win_width, 20), y = get_percent(win_height, 0.1))



for x in range(GRID_SIZE) :
    for y in range(GRID_SIZE) :
        button = Cell(x, y)
        button.create_button_obj(game_frame)
        button.button_obj.grid(column = x, row= y)




root.mainloop()