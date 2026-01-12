import random

# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius.
# Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        break
    else:
        print("S")

print("----------------------------------------")
# Tris kartus iškritus herbui; A
count = 0
while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("H")
        count += 1
        if count >= 3:
            break
    else:
        print("S")
print("----------------------------------------")

# Tris kartus iškritus herbui; B
count = 0
while True:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")
    if count >= 3:
        break
print("----------------------------------------")

# Tris kartus iškritus herbui; C
count = 0
while count < 3:
    coin = random.randint(0, 1)
    if coin == 0:
        print("H")
        count += 1
    else:
        print("S")
print("----------------------------------------")

# Tris kartus iš eilės iškritus herbui;
count = 0
count_h = 0
while True:
    coin = random.randint(0, 1)
    count += 1
    if coin == 0:
        print("H")
        count_h += 1
    else:
        print("S")
        count_h = 0
    if count_h >= 3:
        break
print(count,count_h)
print("----------------------------------------")
# Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: ​laimėtojo vardas​”. Taškų kiekį generuokite funkcija ​random.randint(x,x)​. Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.

k_pts_t = 0
p_pts_t = 0
while True:
    k_pts = random.randint(5,25)
    p_pts = random.randint(10,20)
    k_pts_t += k_pts
    p_pts_t += p_pts
    if k_pts > p_pts:
        print(f'Partiją laimėjo Kazys su taškų persvara {k_pts} > {p_pts}. bendras taškų balansas P:{p_pts_t}, K:{k_pts_t}')
    elif p_pts > k_pts:
        print(f'Partiją laimėjo Petras su taškų persvara {p_pts} > {k_pts}. bendras taškų balansas P:{p_pts_t}, K:{k_pts_t}')
    else:
        print(f'Partija baigėsi lygiosiomis abiems žaidėjams surinkus po {p_pts} taškų.')
    if k_pts_t >= 222 or p_pts_t >= 222:
        break
if k_pts_t > p_pts_t:
    print("Žaidimą laimėjo Kazys")
elif p_pts_t > k_pts_t:
    print("Žaidimą laimėjo Petras")
else:
    print("Žaidimas baigėsi lygiosiomis")


# Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).
# “Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.

total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        taukst = random.randint(5,20)
        total_taukst += taukst
        count += 1
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.')
print(f'Iš viso prireikė {total_count} smūgių')


# “Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        count += 1
        if random.randint(0,1) == 0:
             continue
        taukst = random.randint(20,30)
        total_taukst += taukst
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.')
print(f'Iš viso prireikė {total_count} smūgių')
print("----------------------------------------")

total_count = 0
for i in range(5):
    count = 0
    nail_length = 85
    total_taukst = 0
    while total_taukst < nail_length:
        count += 1
        taukst = random.randint(20,30) * random.randint(0,1)
        total_taukst += taukst
        # print(total_taukst)
    total_count += count
    print(f'Vinį įkalėme {count} smūgiais, iš viso sukalta {total_taukst}mm.') # komentaras
print(f'Iš viso prireikė {total_count} smūgių')
print('Dovilės kodas')
print()