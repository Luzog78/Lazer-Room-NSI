import sys
import time
import tkinter as tk
from threading import Thread
from Simu_laser_room import GPIO


class Theme:
    def __init__(self, bg, fg, win_color, loose_color, better_color, worse_color, buttons_color, title_font,
                 chrono_title_font, chrono_font, ending_font, board_title_font, board_key_font, board_val_font,
                 normal_font, normal_bold_font, normal_mono_font):
        self.bg = bg
        self.fg = fg

        self.win_color = win_color
        self.loose_color = loose_color
        self.better_color = better_color
        self.worse_color = worse_color
        self.buttons_color = buttons_color

        self.title_font = title_font
        self.chrono_title_font = chrono_title_font
        self.chrono_font = chrono_font
        self.ending_font = ending_font
        self.board_title_font = board_title_font
        self.board_key_font = board_key_font
        self.board_val_font = board_val_font
        self.normal_font = normal_font
        self.normal_bold_font = normal_bold_font
        self.normal_mono_font = normal_mono_font

    @staticmethod
    def LIGHT():
        return Theme("white", "black", "green", "red", "green", "navy", "black", ("Arial", 60, "bold underline"),
                     ("Consolas", 20, "bold"), ("Consolas", 72), ("MS Serif", 72), ("Arial", 20, "bold underline"),
                     ("Arial", 15, "bold"), ("Arial", 15), ("Roboto", 12), ("Roboto", 12, "bold"), ("Consolas", 12))

    @staticmethod
    def DARK():
        return Theme("black", "white", "green", "red", "green", "navy", "white", ("Arial", 60, "bold underline"),
                     ("Consolas", 20, "bold"), ("Consolas", 72), ("MS Serif", 72), ("Arial", 20, "bold underline"),
                     ("Arial", 15, "bold"), ("Arial", 15), ("Roboto", 12), ("Roboto", 12, "bold"), ("Consolas", 12))

    @staticmethod
    def CHEM():
        return Theme("yellow", "green", "black", "magenta", "gray", "blue", "white", ("Comic sans ms", 11, ""),
                     ("MS Serif", 100, "italic"), ("Impact", 5, "bold underline italic"), ("Impact", 5, "bold underline italic"),
                     ("MV Boli", 20, "underline"), ("Segoe Print", 7, "italic"), ("Trebuchet MS", 30, "bold underline"), ("Arial", 7),
                     ("Roboto", 12, "bold"), ("Roboto", 12, "bold"))


class GameHandler(tk.Tk):
    GAME_CHRONO = 5.0

    def __init__(self, buttons: list[int] = [7, 11, 13, 15],
                 sensors: list[int] = [29, 31, 33, 35],
                 indicators: list[int] = [32, 36, 38, 40],
                 theme: Theme = Theme.DARK()):
        super().__init__("GameHandler")

        self.theme = theme

        self.buttons = buttons
        self.sensors = sensors
        self.indicators = indicators
        self.thread_handler = Thread(target=self.target_handler)
        self.thread_chrono = Thread(target=self.target_chrono)

        self.running, self.playing = False, False
        self.play_state = -1
        self.chrono = 0
        self.chronos = []

        self.title("Lazer Game Handler !")
        self.geometry("1080x720")
        self.config(bg=self.theme.bg)

        self.label = tk.Label(self, bg=self.theme.bg, fg=self.theme.fg, font=self.theme.title_font, text="Lazer Game")
        self.label.pack()

        self.left_frame = tk.Frame(self, bg=self.theme.bg)
        self.left_frame.place(relx=0.6, x=-60, y=self.theme.title_font[1] * 1.6 + 30, anchor="ne")

        self.chrono__lbl = tk.Label(self.left_frame, bg=self.theme.bg, fg=self.theme.fg,
                                    font=self.theme.chrono_title_font, text="CHRONO :")
        self.chrono__lbl.pack(anchor="e")
        self.chrono_lbl = tk.Label(self.left_frame, bg=self.theme.bg, fg=self.theme.fg, font=self.theme.chrono_font)
        self.chrono_lbl.pack(anchor="e")
        tk.Frame(self.left_frame, bg=self.theme.bg).pack(pady=20)

        self.best_scores_lbl = tk.Label(self.left_frame, bg=self.theme.bg, fg=self.theme.fg,
                                         font=self.theme.chrono_title_font, text="MEILLEURS SCORES :")
        self.best_scores_lbl.pack(anchor="e")
        self.best_scores_frame = tk.Frame(self.left_frame, bg=self.theme.bg)
        self.best_scores_frame.pack(anchor="e", ipady=10)
        params = {"bg": self.theme.bg, "fg": self.theme.fg, "font": self.theme.normal_bold_font}
        self.top_1__lbl = tk.Label(self.best_scores_frame, **params, text="1.")
        self.top_1__lbl.grid(row=0, column=0)
        self.top_2__lbl = tk.Label(self.best_scores_frame, **params, text="2.")
        self.top_2__lbl.grid(row=1, column=0)
        self.top_3__lbl = tk.Label(self.best_scores_frame, **params, text="3.")
        self.top_3__lbl.grid(row=1, column=2)
        self.top_4__lbl = tk.Label(self.best_scores_frame, **params, text="4.")
        self.top_4__lbl.grid(row=2, column=0)
        self.top_5__lbl = tk.Label(self.best_scores_frame, **params, text="5.")
        self.top_5__lbl.grid(row=2, column=2)
        params = {"bg": self.theme.bg, "fg": self.theme.fg, "font": self.theme.normal_mono_font, "width": 10,
                  "anchor": "w", "padx": 10}
        self.top_1_lbl = tk.Label(self.best_scores_frame, **(params | {"anchor": "center"}), text="Marc")
        self.top_1_lbl.grid(row=0, column=1, columnspan=3, pady=10)
        self.top_2_lbl = tk.Label(self.best_scores_frame, **params, text="Jean")
        self.top_2_lbl.grid(row=1, column=1, pady=3)
        self.top_3_lbl = tk.Label(self.best_scores_frame, **params, text="Paul")
        self.top_3_lbl.grid(row=1, column=3, pady=3)
        self.top_4_lbl = tk.Label(self.best_scores_frame, **params, text="Jacques")
        self.top_4_lbl.grid(row=2, column=1, pady=3)
        self.top_5_lbl = tk.Label(self.best_scores_frame, **params, text="Hadrien")
        self.top_5_lbl.grid(row=2, column=3, pady=3)

        tk.Frame(self, bg=self.theme.bg).pack(side="bottom", pady=10)
        self.opt_frame = tk.Frame(self, bg=self.theme.bg)
        self.opt_frame.pack(side="bottom", ipady=10)
        self.opt_lbl = tk.Label(self, bg=self.theme.bg, fg=self.theme.fg,
                                font=self.theme.chrono_title_font, text="OPTIONS :")
        self.opt_lbl.pack(side="bottom", )
        params = {"bg": self.theme.bg, "fg": self.theme.fg, "font": self.theme.normal_font, "activebackground": self.theme.bg,
                  "activeforeground": self.theme.fg, "bd": 2, "relief": "groove", "width": 8, "padx": 2, "pady": 8}
        self.opt_pause = tk.Button(self.opt_frame, **params, text="Play",
                                   command=self.switch)
        self.opt_pause.pack(side="left")
        tk.Frame(self.opt_frame, bg=self.theme.bg).pack(side="left", padx=5)
        self.opt_play_again = tk.Button(self.opt_frame, **params, text="Rejouer", command=self.start)
        self.opt_play_again.pack(side="left")
        tk.Frame(self.opt_frame, bg=self.theme.bg).pack(side="left", padx=5)
        self.opt_quit = tk.Button(self.opt_frame, **params, text="Quitter", command=self.exit)
        self.opt_quit.pack(side="left")

        self.right_frame = tk.Frame(self, bg=self.theme.bg)
        self.right_frame.place(relx=0.6, y=self.theme.title_font[1] * 1.6 + 30, anchor="nw")
        self.chrono_board_frame = tk.Frame(self.right_frame, bg=self.theme.bg)
        self.chrono_board_frame.pack()
        t = tk.Label(self.chrono_board_frame, bg=self.theme.bg, fg=self.theme.fg, text="Actions :",
                     font=self.theme.board_title_font)
        t.grid(row=0, column=0, columnspan=2, sticky="w")
        self.chrono_board = [(tk.Label(self.chrono_board_frame, bg=self.theme.bg, fg=self.theme.fg,
                                       text=f"Bouton {i + 1}", font=self.theme.board_key_font),
                              tk.Label(self.chrono_board_frame, bg=self.theme.bg, fg=self.theme.fg,
                                       font=self.theme.board_val_font))
                             for i, b in enumerate(buttons)]
        for i, (k, v) in enumerate(self.chrono_board):
            k.grid(row=2 * i + 2, column=0, padx=15, pady=5, sticky="w")
            v.grid(row=2 * i + 2, column=1, padx=15, pady=5, sticky="w")

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def start(self):
        self.running, self.playing = True, True
        self.chrono = self.GAME_CHRONO
        self.chronos = [None for _ in self.buttons]
        if not self.thread_handler.is_alive():
            self.thread_handler.start()
        if not self.thread_chrono.is_alive():
            self.thread_chrono.start()
        self.GPIO_setup()
        self.init()
        self.mainloop()

    def pause(self):
        self.playing = False

    def resume(self):
        self.playing = True

    def switch(self):
        if self.playing:
            self.pause()
            self.opt_pause.config(text="Play")
        else:
            self.resume()
            self.opt_pause.config(text="Pause")
        self.update()

    def exit(self):
        self.quit()
        self.running, self.playing = False, False

    def GPIO_setup(self):
        GPIO.setmode(GPIO.BOARD())

        for c in self.buttons + self.sensors:
            GPIO.setup(c, GPIO.IN())

        for c in self.indicators:
            GPIO.setup(c, GPIO.OUT())

    def get(self, composant):
        return GPIO.input(composant)

    def set(self, composants: int | list[int] | set[int] | tuple[int], activation: bool):
        try:
            for c in composants:
                GPIO.output(c, activation)
        except TypeError:
            GPIO.output(composants, activation)

    def init(self):
        self.set(self.indicators, False)
        self.set(self.indicators[0], True)
        self.play_state = 0

        self.chrono_lbl.config(text="", fg=self.theme.fg)
        for k, v in self.chrono_board[:len(self.buttons)]:
            v.config(text="", fg=self.theme.fg)
        for k, v in self.chrono_board[len(self.buttons):]:
            k.destroy()
            v.destroy()
            self.chrono_board.remove((k, v))

        self.update()

    def end(self, win: bool = False):
        self.pause()
        self.set(self.indicators, False)
        self.chrono_lbl.config(text="Gagné !" if win else "Perdu...", fg=self.theme.win_color if win
                               else self.theme.loose_color, font=self.theme.ending_font)
        self.chrono_board.append((tk.Label(self.chrono_board_frame, bg=self.theme.bg, fg=self.theme.fg, text="Total",
                                           font=self.theme.board_title_font),
                                  tk.Label(self.chrono_board_frame, bg=self.theme.bg, fg=self.theme.fg,
                                           font=self.theme.board_key_font,
                                           text=f"{float(round(sum(c for c in self.chronos if c is not None), 1))}")))
        self.chrono_board[-1][0].grid(row=2 * len(self.buttons) + 3, column=0, padx=15, pady=10, sticky="w")
        self.chrono_board[-1][1].grid(row=2 * len(self.buttons) + 3, column=1, padx=15, pady=10, sticky="w")
        self.update()

    def target_handler(self):
        while self.running:
            if not self.playing:
                continue
            for i, b in enumerate(self.buttons):
                if self.get(b):
                    print(i)
                    if i == self.play_state:
                        print("YESS !!")
                        try:
                            t = float(round(self.GAME_CHRONO - self.chrono, 1))
                            chrs = [c for c in self.chronos if c is not None]
                            comparator = (1 if t < sum(chrs) / len(chrs) else ((-1) if t > sum(chrs) / len(chrs)
                                                                               else 0)) if self.play_state != 0 else 0
                            self.chronos[self.play_state] = t
                            self.chrono_board[self.play_state][1].config(
                                text=f"{'(+) ' if comparator == 1 else '(-) ' if comparator == -1 else ''}{t}",
                                fg=self.theme.better_color if comparator == 1 else self.theme.worse_color
                                if comparator == -1 else self.theme.fg)
                            self.chrono = self.GAME_CHRONO
                            self.play_state += 1
                            self.set(self.indicators[self.play_state - 1], False)
                            self.set(self.indicators[self.play_state], True)
                            self.update()
                        except IndexError:
                            self.end(True)
                    else:
                        print("NOO...")

            for i, s in enumerate(self.sensors):
                if self.get(s):
                    t = float(round(self.GAME_CHRONO - self.chrono, 1))
                    self.chronos[self.play_state] = t
                    self.chrono_board.append((tk.Label(self.chrono_board_frame, bg=self.theme.bg, text=f"Laser {i + 1}",
                                                       fg=self.theme.loose_color, font=self.theme.board_key_font),
                                              tk.Label(self.chrono_board_frame, bg=self.theme.bg, text=f"{t}",
                                                       fg=self.theme.loose_color, font=self.theme.board_val_font)))
                    self.chrono_board[-1][0].grid(row=2 * self.play_state + 1, column=0, padx=15, pady=5, sticky="w")
                    self.chrono_board[-1][1].grid(row=2 * self.play_state + 1, column=1, padx=15, pady=5, sticky="w")
                    self.end(False)

    def target_chrono(self):
        while self.running:
            if not self.playing:
                continue
            self.chrono = round(self.chrono - 0.1, 1)
            try:
                self.chrono_lbl.config(text=f"{float(self.chrono)}")
                self.update()
                if self.chrono == 0:
                    self.end(False)
                    continue
            except RuntimeError:
                continue
            time.sleep(0.1)


g = GameHandler()
g.start()
