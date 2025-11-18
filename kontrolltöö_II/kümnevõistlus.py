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
    

            