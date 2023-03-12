# Main input: Bekéri, hogy melyik része fusson le a fájlnak
main = input('Mi fusson le? ')

# 😉
if main == 'easter egg':
    with open('easteregg.txt', 'w', encoding='utf-8') as file:
        szoveg = 'Gratulálok megtaláltad az easter egg-et!'
        file.write(szoveg)

#########################################################################   JELSZÓ PROGRAM   #########################################################################

# Megnézi, ha a main inputba az van beírva, hogy jelszo program akkor ráfut erre
if main == 'jelszo program':

        
        # Regisztráció
        user = input('Mi legyen a felhasználónév? ') # bekéri a felhasználónevet
        passw = input('Mi legyen a jelszó? ') # Bekéri a jelszavat

        # Bejelentkezés
        
        user_bemenet = input('Mi a felhasználónév? ') # Bekéri a megadott felhasználónevet


        # Folymat
        
        # A 3 próbálkozás megvalósítása
        proba = 0 # Van egy változó a először nulla

        while user_bemenet != user: # ha nem jó a felhasználónév ráfut erre
            proba += 1 # mindegyik ciklusnál hozzáad 1-et
            user_bemenet = input('Hibás felhasználónév!\nMi a felhasználónév? ') # kiad egy bemenetet



            if proba == 2: # Ha a próbaszám eléri a 3-at (az 1 a 0, a 2 az 1 stb.) akkor ez fog lefutni
                print('Sikertelen bejelentkezés!') # kiír a konzolra
                break # megtöri a ciklust és leáll a futás

        if user_bemenet == user: # ha jó a fehlhasználónév akkor ráfut erre
            passw_bemenet = input('Mi a jelszó? ') # bekéri a megadott jelszót

            while passw_bemenet != passw: # ha nem jó a jelszó akkor ráfut erre
                passw_bemenet = input('Hibás jelszó!\nMi a jelszó? ') # kiad egy bemenetet
                proba += 1 # szintén minden ciklusnál növeli a próbák számát

                if proba == 2: # ugyan az a folyamat
                    print('Sikertelen bejelentkezés!') 
                    break

            if passw_bemenet == passw: # ha jó akkor ráfut erre 
                print('Sikeres bejelentkezés!') # kiír a konzolra



#########################################################################   FÁLJ RENDSZER   #########################################################################
if main == 'fajl rendszer': # ha a main input ez akkor ráfut erre
    
        whatdo = input('Mit csináljunk? ') # kiad egy inputot
        
        if whatdo == 'új': # ha azt kapja meg, hogy új akkor ez fut le
            filename = input('Mi legyen fájl neve? ') # kiad egy inputot

            with open(filename, 'w', encoding='utf-8') as file: # létrehoz egy fájlt azon a néven amit megadtunk neki. A 'w' azt jelenti write tehát írás. Utána a karakterkódolást állítja be, hogy megjeleníthessen ékezetes betűket
                    filecon = input('Mi legyen a fájlban? ') # input
                    file.write(filecon) # beleírja a fileba amit megadtunk az inputban
                    print('Sikeresen végrehajtva!') # print


        if whatdo == 'hozzáfűz': # ha hozzáfűzet kap az inputban
            filename = input('Melyik fájlal? ') # input
            with open(filename, 'a', encoding='utf-8') as file: # ahhoz a fájlhoz amit megadtunk neki hozzáfűz egy szöveget. Az 'a' azt jelenti append tehát itt hozzáfűz valamit. Utána pedig a karakterkódolás
                filecon = input('Mit fűzzünk hozzá? ') # input
                newline = input('Új sorba? ') # input
                if newline == 'igen': # Ha azt kapta meg, hogy igen akkor ráfut erre
                    file.write('\n' + filecon) # \n azt jelenti, hogy új sorba kezdi el írni azt amit megadtunk neki szöveget
                elif newline == 'nem': # ha nem akkor ide fut rá
                    file.write(filecon) # csak beleírja a szöveget sortörés nélkül
                print('Sikeresen végrehajtva!') # print

        if whatdo == 'olvas': # Ha azt kapta meg, hogy olvas
            filename = input('Melyik fájlal? ') # input
            with open(filename, 'r', encoding='utf-8') as file: # beolvassa azt a fájlt amit megadtunk neki 
                sor = file.read() # beolvassa az egész file-t egyszerre 
                print(sor) # ki printeli 
