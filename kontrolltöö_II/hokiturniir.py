def loe_tulemused(fail):
    with open(fail, 'r', encoding="UTF-8") as f:
        maatriks = []
        for rida in f:
            rida_list = rida.strip().split(";")
            maatriks.append(rida_list)
        return maatriks

def kes_võitis(maatriks):
    new_dict = {}
    loendur = 1
    for arr in maatriks:
        loendur_voit = 0
        for element in arr:
            if element == "V":
                loendur_voit += 1

        new_dict[loendur] = loendur_voit
        loendur += 1

    parim_key = None
    parim_value = -1

    for key, value in new_dict.items():
        if value > parim_value:
            parim_value = value
            parim_key = key
    return parim_key
        
def main():
    fail = input("Sisesta failinimi: ")
    tulemused_maatriks = loe_tulemused(fail)
    tiimi_number = kes_võitis(tulemused_maatriks)
    print(f"Turniiri võitis {tiimi_number}. võistkond.")

if __name__=="__main__":
    main()



