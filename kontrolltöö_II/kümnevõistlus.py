def loe_tulemused(fail):
    with open(fail, 'r', encoding="UTF-8") as f:
        result = {}
        for rida in f:
            rida_list = rida.strip().split(";")
            key = rida_list[0]
            rida_list.pop(0)
            new_list = []

            for arv in rida_list:
                new_list.append(int(arv))

            result[key] = new_list

        return result
    
def punktisummad(tulemused):
    hulk = set()
    
    # summa arvutamine
    for nimi, punktid in tulemused.items():
        summa = 0
        for arv in punktid:
            summa += arv
        uus_tuple = (nimi, summa)
        hulk.add(uus_tuple)

    return hulk

def main():
    tulemused = loe_tulemused("tulemused.txt")
    summad = punktisummad(tulemused)
    punktisumma = int(input("Sisesta punktisumma: "))

    paremad = False
    for nimi, summa in summad:
        if summa > punktisumma:
            print(f"{nimi} - punktisumma {summa}, punktid 100 meetri distantsilt {tulemused[nimi][0]}")
            paremad = True

    if not paremad:
        print("Sellest punktisummast paremat tulemust ei ole")

if __name__=="__main__":
    main()
    

