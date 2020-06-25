from utils.colors.colors import Foreground, Background
from utils.colors.effects import Effects


class TerminalColor:
    def __init__(self):
        self._base = '\033[$SETTINGS$m'
        self.effect = Effects()
        self.foreground = Foreground()
        self.background = Background()

    def set_colors(self, effect: Effects = None, fg: Foreground = None, bg: Background = None):
        print(self._base.replace('$SETTINGS$', effect + ';' + fg + ';' + bg), end='')

    def reset_terminal_color(self):
        self.set_colors()
