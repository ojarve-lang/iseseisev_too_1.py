# Iseseisev töö 1
# Autor: (Olavi Järve)
# Kuupäev: (25.10.2025)
# -----------------------------

# 1.1. Tervitus
print("Tere, maailm!")

# -----------------------------

# 1.2. Aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

# -----------------------------

# 1.3. Pilved
korgus = float(input("Sisesta pilvede aluse kõrgus kilomeetrites: "))

if korgus > 6.0:
    print("Need on ülemised pilved.")
else:
    print("Need ei ole ülemised pilved.")

# -----------------------------

# 1.4. Bussid
inimesed = int(input("Sisesta inimeste arv: "))
kohad = int(input("Sisesta ühe bussi kohtade arv: "))

# Arvutame vajaliku busside arvu
busside_arv = (inimesed + kohad - 1) // kohad

# Mitu inimest on viimases bussis
viimases_bussis = inimesed % kohad
if viimases_bussis == 0:
    viimases_bussis = kohad

print("Vaja läheb", busside_arv, "bussi.")
print("Viimases bussis on", viimases_bussis, "inimest.")
