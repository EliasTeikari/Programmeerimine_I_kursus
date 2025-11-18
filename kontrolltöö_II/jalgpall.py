def leia_keskmised(fail):

    result_list = []

    with open(fail, 'r', encoding="UTF-8") as f:
        for rida in f:
            summa = 0
            loendur = 0

            rida_list = rida.strip().split(" ")
            for element in rida_list:
                summa += int(element)
                loendur += 1
            
            keskmine = summa / loendur
            result_list.append(round(keskmine, 2))
            
    return result_list

def kas_rohkem_väravaid(löögid, väravad, fail):
    oodatav_väravad = väravad / 38
    kesk_list = leia_keskmised(fail)

    for arv in kesk_list:
        if arv < oodatav_väravad:
            return False

    return True
    
def main():
    fail = input("Sisesta faili nimi: ")
    oodatav_värav = int(input("Sisesta, kui palju väravaid peaks lööma? "))

    print("Jalgpallurite keskmised on:")

    kesk_list = leia_keskmised(fail)
    for arv in kesk_list:
        print(arv) 

    boolean = kas_rohkem_väravaid(kesk_list, oodatav_värav, fail) 
    if boolean == True:
        print("Kõik mängijad löövad tõenäoliselt piisavalt väravad.")
    elif boolean == False:
        print("kõik mängijad ei löö tõenäoliselt piisavalt väravaid")


if __name__=="__main__":
    main()


# print(kas_rohkem_väravaid([1.55, 0.91, 0.82], 30, "./väravad.txt"))

# print(leia_keskmised("./väravad.txt"))