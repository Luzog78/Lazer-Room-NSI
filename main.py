import sys
import time
import tkinter as tk
from threading import Thread
from Simu_laser_room import GPIO


class GameHandler(tk.Tk):
    GAME_CHRONO = 5.0

    def __init__(self, buttons: list[int] = [7, 11, 13, 15],
                 sensors: list[int] = [29, 31, 33, 35],
                 indicators: list[int] = [32, 36, 38, 40]):
        super().__init__("GameHandler")

        self.buttons = buttons
        self.sensors = sensors
        self.indicators = indicators
        self.thread_handler = Thread(target=self.target_handler)
        self.thread_chrono = Thread(target=self.target_chrono)

        self.running = False
        self.play_state = -1
        self.chrono = 0
        self.chronos = [None for _ in buttons]

        self.title("Lazer Game Handler !")
        self.geometry("1080x720")

        self.label = tk.Label(self, font=("Arial", 60, "bold underline"), text="Lazer Game")
        self.label.pack()
        tk.Frame(self).pack(pady=30)

        self.chrono__lbl = tk.Label(self, font=("Consolas", 20, "bold"), text="CHRONO :")
        self.chrono__lbl.pack()
        self.chrono_lbl = tk.Label(self, font=("Consolas", 72))
        self.chrono_lbl.pack()
        tk.Frame(self).pack(pady=30)

        self.chrono_board_frame = tk.Frame(self)
        self.chrono_board_frame.pack()
        t = tk.Label(self.chrono_board_frame, text="Actions :", font=("Arial", 20, "bold underline"))
        t.grid(row=0, column=0, columnspan=2, sticky="w", pady=15)
        self.chrono_board = [(tk.Label(self.chrono_board_frame, text=f"Bouton {i + 1}", font=("Arial", 15, "bold")),
                              tk.Label(self.chrono_board_frame, font=("Arial", 15)))
                             for i, b in enumerate(buttons)]
        for i, (k, v) in enumerate(self.chrono_board):
            k.grid(row=2 * i + 2, column=0, padx=15, pady=5, sticky="w")
            v.grid(row=2 * i + 2, column=1, padx=15, pady=5, sticky="w")

        self.protocol("WM_DELETE_WINDOW", self.exit)

    def start(self):
        self.running = True
        self.chrono = self.GAME_CHRONO
        self.thread_handler.start()
        self.thread_chrono.start()
        self.GPIO_setup()
        self.init()
        self.mainloop()

    def stop(self):
        self.running = False

    def exit(self):
        self.quit()
        self.stop()

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

    def target_handler(self):
        while self.running:
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
                                fg="green" if comparator == 1 else "navy" if comparator == -1 else "black")
                            self.chrono = self.GAME_CHRONO
                            self.play_state += 1
                            self.set(self.indicators[self.play_state - 1], False)
                            self.set(self.indicators[self.play_state], True)
                            self.update()
                        except IndexError:
                            print("WIN !!!")
                    else:
                        print("NOO...")

            for i, s in enumerate(self.sensors):
                if self.get(s):
                    t = float(round(self.GAME_CHRONO - self.chrono, 1))
                    self.chronos[self.play_state] = t
                    self.chrono_board.append((tk.Label(self.chrono_board_frame, text=f"Laser {i + 1}", fg="red",
                                                       font=("Arial", 15, "bold")),
                                              tk.Label(self.chrono_board_frame, text=f"{t}", fg="red",
                                                       font=("Arial", 15))))
                    self.chrono_board[-1][0].grid(row=2 * self.play_state + 1, column=0, padx=15, pady=5, sticky="w")
                    self.chrono_board[-1][1].grid(row=2 * self.play_state + 1, column=1, padx=15, pady=5, sticky="w")
                    self.stop()
                    print(f"PERDU. {i}")

            # match self.play_state:
            #     case 0:
            #         pass
            #     case 1:
            #         pass
            #     case 2:
            #         pass
            #     case 3:
            #         pass
            #     case _:
            #         pass

    def target_chrono(self):
        self.chrono += 0.1
        while self.running:
            self.chrono = round(self.chrono - 0.1, 1)
            try:
                self.chrono_lbl.config(text=f"{float(self.chrono)}{'' if self.chrono else '/nPerdu !'}".replace("/n", "\n"))
                self.update()
                if self.chrono == 0:
                    break
            except RuntimeError:
                break
            time.sleep(0.1)


g = GameHandler()
g.start()
