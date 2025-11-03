elevi = ["Ana", "Bogdan", "Carmen", "Darius", "Elena"]
note  = [9,       7,        10,       4,        8]

elev_nou        = "Felix"
nota_elev_nou   = 6
elev_de_sters   = "Darius"

interogari_nume = ["Ana", "Mara", "Elena", "stop"]

absente = [1, 0, 2, 3, 0]
#a1,a2
nota_max = max(note)
nota_min = min(note)
for i in range(len(elevi)):
    print(elevi[i], "are", note[i])
    if note[i] == nota_max:
        print("Elevul cu nota maximă este" ,{elevi[i]}, "are nota", {nota_max})
    if note[i] == nota_min:
        print("Elevul cu nota maximă este" ,{elevi[i]}, "are nota", {nota_min})

#a3
print(sum(note)/len(note))

#a4
for i in range(len(elevi)):
    if note[i] > 5:
        print(elevi[i])
#b5
for i in range(len(elevi)):
    note[i]
    print(note[i]+1)

#b6

note.append(nota_elev_nou)
elevi.append(elev_nou)
print(elevi)
print(note)

#b7
if elev_nou in elevi:
    poz = elevi.index(elev_de_sters)
    elevi.pop(poz)
    note.pop(poz)
    print("Elevul", elev_de_sters,"a fost sters" )
else:
    print("Elevul", elev_de_sters,"nu exista" )

#b8
for i in range(len(elevi)):
    print(elevi[i], note[i])

#c9
i = 0
"""while interogari_nume[i] != "stop":
    nume = interogari_nume[i]
    if nume in elevi:
        poz = elevi.index(nume)
        print("elevul", nume, "are nota",note[poz])
    else:
        print("elevul", nume, "nu exista" )"""

#c10
promovati = 0
respinsi = 0

for n in note:
    if n >= n:
        promovati += 1
    else:
        respinsi += 1
print("elevi promovati",promovati,"elevi respinsi" , respinsi)

#c11

note_elevi_promovati = []

for n in note:
    if n >=5:
        note_elevi_promovati.append(n)
if len(note_elevi_promovati) > 0:
    media_promovatilor = sum(note_elevi_promovati)/len(note_elevi_promovati)
    print("media promovatilor", media_promovatilor)
else:
    print("nu exista elevi promovati")
