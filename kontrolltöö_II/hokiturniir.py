def loe_tulemused(fail):
    with open(fail, 'r', encoding="UTF-8") as f:
        maatriks = []
        for rida in f:
            rida_list = rida.strip().split(";")
            maatriks.append(rida_list)
        return maatriks

print(loe_tulemused('hokiturniir.txt'))
            

