import re
first_pattern_artist = r"^[A-Z][a-z' ]+$"
second_pattern_song = r'^[A-Z\s]+$'

while True:
    inp = input().split(':')
    if inp[0] == 'end':
        exit()
    artist = inp[0]
    song = inp[1]
    first_reg = re.match(first_pattern_artist, artist)
    if first_reg:
        second_reg = re.match(second_pattern_song, song)
        if second_reg:
            key = len(artist)
            appender = [[], []]
            for i in artist:
                if i == ' ' or i == '\'':
                    appender[0].append(i)
                    continue
                i = ord(i)
                for l in range(key):
                    i += 1
                    if i == 123 or i == 91:
                        i = 97
                appender[0].append(chr(i))
            for l in song:
                if l == ' ' or l == '\'':
                    appender[1].append(l)
                    continue
                l = ord(l)
                for k in range(key):
                    l += 1
                    if l == 123 or l == 91:
                        if l == 123:
                            l = 97
                        else:
                            l = 65
                appender[1].append(chr(l))
            print(f'Successful encryption:'
                  f' {"".join(appender[0])}@{"".join(appender[1])}'
                  )
        else:
            print('Invalid input!')
    else:
        print('Invalid input!')