liste1 = []
liste2 = []
print("Enter your list elements: ")
zaehler = 0
while True:
    eingabe = input('')
    liste1.append(eingabe)
    zaehler += 1
    if eingabe == "":
        for i in liste1:
            liste2.append(i)
        break
liste1.remove("")
liste2.remove("")
print("............................................ ")
for i in liste1:
    print(i + " ", end="")
print()
print("............................................ ")
for i in range(len(liste2) - 1, -1, -1):
    print(liste2[i] + " ", end="")
print()
print("............................................")
'''
zaehler = zaehler -1
while zaehler >= 0:
    print(liste2[zaehler])
    zaehler -= 1
    '''