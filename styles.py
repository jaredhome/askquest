import tkinter.font as tkFont

class SolarizedDarkPalette:
    def __init__(self):
        self.base03 = '#002b36'
        self.base02 = '#073642'
        self.base01 = '#586e75'
        self.base00 = '#657b83'
        self.base0 = '#839496'
        self.base1 = '#93a1a1'
        self.base2 = '#eee8d5'
        self.base3 = '#fdf6e3'
        self.yellow = '#b58900'
        self.orange = '#cb4b16'
        self.red = '#dc322f'
        self.magenta = '#d33682'
        self.violet = '#6c71c4'
        self.blue = '#268bd2'
        self.cyan = '#2aa198'
        self.green = '#859900'


class ModernFonts:
    def __init__(self):
        self.default_font = ("Arial", 12)
        self.bold_font = ("Arial", 12, 'bold')
        self.large_font = ("Arial", 24)
        self.small_font = ("Arial", 8)


class StyleProfile:
    def __init__(self, color_palette, fonts):
        self.colors = color_palette
        self.fonts = fonts


# Define style profiles
SolarizedDarkStyle = StyleProfile(SolarizedDarkPalette(), ModernFonts())

