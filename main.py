
try:
    # adatok bekérése


    whatdo = input('Mit csináljunk? ')
    if whatdo == 'új':
        filename = input('Mi legyen fájl neve? ')

        with open(filename + '.txt', 'w', encoding='utf-8') as file:
                filecon = input('Mi legyen a fájlban? ')
                file.write(filecon)
                print('Sikeresen végrehajtva!')


    if whatdo == 'hozzáfűz':
        filename = input('Melyik fájlal? ')
        with open(filename, 'a', encoding='utf-8') as file:
            filecon = input('Mit fűzzünk hozzá? ')
            newline = input('Új sorba? ')
            if newline == 'igen':
                file.write('\n' + filecon)
            elif newline == 'nem':
                file.write(filecon)
            print('Sikeresen végrehajtva!')

    if whatdo == 'olvas':
        filename = input('Melyik fájlal? ')
        with open(filename, 'r', encoding='utf-8') as file:
            # print('Sikeresen végrehajtva!')
            sor = file.read()
            print(sor.strip())

except:
    print('Kaki van a palacsintában!')