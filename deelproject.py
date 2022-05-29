# Tutorial met spelregels.
print('Hallo beste deelnemer! In dit spel gaan we een code raden. Hieronder de spelregels:')
print('1. Je moet een code raden van 4 getallen')
print('2. De code bestaat alleen uit cijfers tussen de 1 en de 7.')
print('3. Elk cijfer mag maar één keer voorkomen.')
print('4. Je krijgt 10 beurten om het getal te raden.')
print('5. Ben je het beu? gebruik code 9999 om te stoppen')
print('6. Probeer je een ander getal of symbool te gebruiken dan tussen 1 en 7, kost dit alsnog een beurt.')

# Genereren van een random 4-cijferig getal met getallen tussen de 1-7 en geen dubbele cijfers.
import random
a = random.randint(1, 7)
b = random.randint(1, 7)
c = random.randint(1, 7)
d = random.randint(1, 7)

while a == b or a == c or a == d or b == c or b == d or c == d:
    a = random.randint(1, 7)
    b = random.randint(1, 7)
    c = random.randint(1, 7)
    d = random.randint(1, 7)

x = 1 #teller van het aantal beurten
goed = 0 #teller van het aantal getallen op de juiste plek
aanwezig = 0 #teller van het aantal getallen dat juist is maar op de verkeerde plek

# Beurt 1
print('beurt', x)
k = int(input('geef getal 1:'))
l = int(input('geef getal 2:'))
m = int(input('geef getal 3:'))
n = int(input('geef getal 4:'))

# Regelt het aantal beurten
for x in range (1, 10):
# Dit deel hanteert de getallen die binnen 1-7 vallen.
    if k >= 1 and k <= 7 and l >= 1 and l <= 7 and m >= 1 and m <= 7 and n >= 1 and n <= 7:
# Bij de juiste code hoort een felicitatie
        if k == a and l == b and m == c and n == d:
            print('Gefeliciteerd! Je hebt de code geraden!')
            break

# Dubbele getallen worden niet gewaardeerd. Dit deel corrigeert de invoer van dubbele getallen.
        elif k == l or k == m or k == n or l == m or l == n or m == n:
            x += 1
            print('Je hebt dubbele getallen gebruikt! foei! opnieuw.')
            print('beurt', x)
            k = int(input('geef getal 1:'))
            l = int(input('geef getal 2:'))
            m = int(input('geef getal 3:'))
            n = int(input('geef getal 4:'))

# De lijnen 56 t/m 98 regelen de puntenverdeling voor hoeveel cijfers correct zijn en
# welke op de verkeerde plek staan.
        while k == a:
            goed += 1
            break
        
        while l == b:
            goed += 1
            break
        
        while m == c:
            goed += 1
            break
        
        while n == d:
            goed += 1
            break
        
        while k != a:
            if k == b or k == c or k == d:
                aanwezig += 1
                break
            else:
                break
          
        while l != b:
            if l == a or l == c or l == d:
                aanwezig += 1
                break
            else:
                break
            
        while m != c:
            if m == a or m == b or m == d:
                aanwezig += 1
                break
            else:
                break
            
        while n != d:
            if n == a or n == b or n == c:
                aanwezig += 1
                break
            else:
                break
# Dit deel geeft feedback over de ingevoerde nummers en reset de waarden, zodat bij de volgende beurt
# het aantal goede e naanwezige cijfers niet doorgeteld worden
        x += 1
        print('Je hebt', goed,  'getallen op de juiste plek')
        print('je hebt', aanwezig, 'getallen juist, maar niet op de juiste plek')
        goed -= goed
        aanwezig -= aanwezig
        print('beurt', x)
        k = int(input('geef getal 1:'))
        l = int(input('geef getal 2:'))
        m = int(input('geef getal 3:'))
        n = int(input('geef getal 4:'))
            
# dit deel hanteert de getallen die buiten 1-7 vallen.
    elif k > 7 or k < 1 or l > 7 or l < 1 or m > 7 or m < 1 or n > 7 or n < 1:
# Dit deel regelt de quitters en mensen die van gedachten veranderen
        if k == 9 and l == 9 and m == 9 and n == 9:
            e=str(input('weet je het zeker? ja/nee'))
            if e == 'ja':
                print('Game over')
                break
            
            else:
                x += 1
                print('opgeven is voor watjes! Raad nog een keer!')
                print('beurt', x)
                k = int(input('geef getal 1:'))
                l = int(input('geef getal 2:'))
                m = int(input('geef getal 3:'))
                n = int(input('geef getal 4:'))


# Bij verkeerde invoer voert die je terug naar het begin
        else: 
            x += 1
            print('verkeerde invoer, probeer opnieuw.')
            print('beurt', x)
            k = int(input('geef getal 1:'))
            l = int(input('geef getal 2:'))
            m = int(input('geef getal 3:'))
            n = int(input('geef getal 4:'))

# Laat weten dat je beurt voorbij is
else:
    print('je beurten zijn op. game over! De code was', a, b, c, d)

