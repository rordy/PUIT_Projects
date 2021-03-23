import tkinter as tk

FPS = int(1000 / 30)


# Simple global container until you learn classes
class Game:
    pass


def move_ball(obj, x, y):
    Game.canvas.move(obj, x, y)
    # Game.canvas.xview_scroll(3, tk.UNITS)


def update_keypressed():
    if Game.keys['d']:
        move_ball(Game.ball, Game.xmove, 0)
    elif Game.keys['a']:
        move_ball(Game.ball, -Game.xmove, 0)

    Game.master.after(FPS, update_keypressed)


def key_pressed(event):
    # print('KeyPress', event.keysym)
    Game.keys[event.keysym] = True


def key_release(event):
    # print('KeyRelease', event.keysym)
    Game.keys[event.keysym] = False


def main():
    Game.master = tk.Tk()

    # Set Globals
    Game.xmove = 3

    canvas_width = 1000
    canvas_height = 600
    canvas_scroll_width = 3000
    canvas_scroll_height = 3000

    Game.canvas = tk.Canvas(Game.master,
                            width=canvas_width,
                            height=canvas_scroll_height,
                            bg='black')

    Game.canvas.configure(scrollregion=(0, 0,
                                        canvas_scroll_width, canvas_scroll_height),
                          yscrollincrement='1',
                          xscrollincrement='1')

    x = (Game.master.winfo_screenwidth() / 2) - (canvas_width / 2)
    y = (Game.master.winfo_screenheight() / 2) - (canvas_height / 2)

    Game.master.geometry('%dx%d+%d+%d' % (canvas_width + 4, canvas_height + 4, x, y))
    Game.canvas.pack()

    x1, y1 = canvas_scroll_width / 2, canvas_scroll_height / 2
    Game.ball = Game.canvas.create_oval(x1, y1, x1 + 50, y1 + 50, fill="red")
    Game.canvas.xview_moveto((x1 - canvas_width / 2) / canvas_scroll_width)
    Game.canvas.yview_moveto((y1 - canvas_height / 2) / canvas_scroll_height)

    Game.keys = {'d': False, 'a': False}
    Game.master.bind("a<KeyPress>", key_pressed)
    Game.master.bind("a<KeyRelease>", key_release)
    Game.master.bind("d<KeyPress>", key_pressed)
    Game.master.bind("d<KeyRelease>", key_release)

    # Start the update key loop
    update_keypressed()
    Game.master.mainloop()


main()