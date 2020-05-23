from pyfiglet import figlet_format


def print_art(txt):
    ascii_art = figlet_format(txt)
    return ascii_art


figlet = input()
print(print_art(figlet))