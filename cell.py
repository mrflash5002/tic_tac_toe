from tkinter import Button, DISABLED
from settings import CELL_HEIGHT, CELL_WIDTH, GRID_SIZE, game_on, IDYES
import random
import ctypes
import sys

class Cell :
    all_buttons = []

    def __init__(self, x, y) :
        self.is_clicked = False
        self.button_obj = None
        self.sign = None
        self.x = x
        self.y = y

        Cell.all_buttons.append(self)


    def __repr__(self) :
        return f'Cell(x :{self.x}, y :{self.y})'


    def create_button_obj(self, location) :
        btn = Button(location, height = CELL_HEIGHT, width=CELL_WIDTH)   

        btn.bind('<Button-1>', self.left_click_actions)

        self.button_obj = btn
        


    @staticmethod
    def cpu_move() :
        if game_on :
            while True :
                cpu_choise = random.choice(Cell.all_buttons)

                if not cpu_choise.is_clicked :
                    cpu_choise.button_obj.configure(text = 'O')
                    cpu_choise.sign = 'O'

                    cpu_choise.button_obj.unbind('<Button-1>')
                    cpu_choise.is_clicked = True

                    break
            
            Cell.win_check()


    def left_click_actions(self, event) :
        self.button_obj.configure(text='X')
        self.sign = 'X'

        self.button_obj.unbind('<Button-1>')
        self.is_clicked = True

        Cell.win_check()
        Cell.cpu_move()



    @staticmethod
    def clicked_cells() :
        clicked_cells_list = []

        for button in Cell.all_buttons :
            if button.is_clicked :
                clicked_cells_list.append(button)

        return clicked_cells_list

    @staticmethod
    def win_options() :
        # make dynamical version not ard codeed
        win_positions = [
            [[0,0], [1,0],[2,0]],
            [[0,1], [1,1],[2,1]],
            [[0,2], [1,2],[2,2]],
            [[0,0], [0,1],[0,2]],
            [[1,0], [1,1],[1,2]],
            [[2,0], [2,1],[2,2]],
            [[0,0], [1,1],[2,2]],
            [[2,0], [1,1],[0,2]],
        ]

        return win_positions 


    @staticmethod
    def get_btn_instance(list_of_btn) :
        instance_of_btn = []

        for position in list_of_btn :
            for cell in Cell.clicked_cells() :
                if cell.x == position[0] and cell.y == position[1] :
                    instance_of_btn.append(cell)
                
        return instance_of_btn


    @staticmethod
    def possible_win_positions() :
        possible_wins = []
        clicked_cells_positions = [[btn.x, btn.y] for btn in Cell.clicked_cells()]

        for win_list in Cell.win_options() :
            for position in win_list :
                if position not in clicked_cells_positions :
                    break

                elif position == win_list[-1] :
                    possible_wins.append(Cell.get_btn_instance(win_list))          

                else :
                    continue

        return possible_wins



    @staticmethod
    def win_check():
        global game_on

        for win_pos in Cell.possible_win_positions() : # change this so that you can color winner with green on board
            sign = set([])

            for cell in win_pos :
                sign.add(cell.button_obj.cget('text'))
            
            if len(sign) == 1 :
                winner = list(sign)[0]
                game_on = False
                Cell.win(winner, win_pos)
                break

            elif len(Cell.clicked_cells()) == len(Cell.all_buttons) and win_pos == Cell.possible_win_positions()[-1]:
                close = ctypes.windll.user32.MessageBoxW(0, 'Well played! \nDo you want to close the game?', 'Draw', 4)
                            
                for btn in Cell.all_buttons :
                    btn.button_obj.configure(bg = 'yellow')

                game_on = False

                if close == IDYES :
                    sys.exit()
                else :
                    break

            else :
                continue

        
    @staticmethod
    def win(winner, win_pos) :
        for btn in Cell.all_buttons :
            btn.button_obj.unbind('<Button-1>')

        if winner == 'X' :
            for btn in win_pos :
                btn.button_obj.configure(bg = 'green')

            close = ctypes.windll.user32.MessageBoxW(0, 'Congratualtions !!! \nDo you want to close the game?', 'You Won', 4)

                    
        else :
            for btn in win_pos :
                btn.button_obj.configure(bg = 'red')

            close = ctypes.windll.user32.MessageBoxW(0, 'Maybe next time :( \nDo you want to close the game ?', 'You Lost', 4)


        if close == IDYES :
            sys.exit()

