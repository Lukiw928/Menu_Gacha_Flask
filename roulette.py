# 0,1,2を指定 0なら弁当 1なら単品 2なら定食
# 0,1,2,3でサイズ指定 S,M,L,LL もし-1ならcontinue
# menue[0][1] ->　定食のLサイズ
# menue[0],menu[1] -> 単品の値段が260円以上でループ終了 valueに +210
# 条件分岐して弁当か定食かを出す。

# 特別扱い
# [とり天,手羽先,チキンカツ,カツ盛,豚ロースカツ,焼き鳥,カレー,フランクセット]
# [白身フライ,アジフライ,エビカツ,エビフライ,メンチカツ,ハムカツ,ハム・メンチカツ,コロッケ]
# 弁当ならvalue -= 10する
# もも弁/定 は10円安い
# ご飯付き（弁当・定食）と単品のみに分ける

import momokara_menue as mm
import random

makura = ["[弁当]","[単品]","[定食]"]  # "{}メニュー名".format(makura[?])変数名は枕詞から
size_name = [" S"," M"," L"," LL"]  # サイズ表記に使用

choice = mm.choice()
tanpin = mm.tanpin()
TB_menue = mm.teisyoku_bentou()
curry = mm.curry()
special_menue = mm.special_menue()
arrange = mm.arrange_menue()


def momokara_roulette(Text):

    """
    定食/弁当の中から適当に選んだもの + 金額に余があれば単品を追加するルーレット
    """
    def TorB(text):

        mx_value = int(text.split("の")[1][0:-1])
        result = []
        value = 0
        check = {}
        cnt = 0
        size_name1 = [" S"," M"," L"," LL"]  # サイズ表記に使用
        size_name2 = [" M","L","LL"]

        while not mx_value - 50 <= value <= mx_value + 50:

            if cnt == 0:
                cnt += 1
                TB_num = random.randint(0,len(TB_menue)-1)
                size_name = size_name1
                if TB_menue[TB_num][0] in special_menue:

                    attribute = random.randint(1,2)

                    if TB_menue[TB_num][0] == "カレー":
                        C_num = random.randint(0,len(curry)-1)
                        if attribute == 1:
                            result.append([makura[0]+curry[C_num][0],curry[C_num][1]-10])
                            value += curry[C_num][1]-10
                        else:
                            result.append([makura[2]+curry[C_num][0],curry[C_num][1]])
                            value += curry[C_num][1]
                        continue

                    if attribute == 1:
                        result.append([makura[0]+TB_menue[TB_num][0],TB_menue[TB_num][1]-10])
                        value += TB_menue[TB_num][1]-10
                    else:
                        result.append([makura[2]+TB_menue[TB_num][0],TB_menue[TB_num][1]])
                        value += TB_menue[TB_num][1]

                else:
                    size = random.randint(1,4)
                    attribute = random.randint(1,2)

                    if attribute == 1:
                        try:
                            if TB_menue[TB_num][size] == -1:
                                continue
                            if TB_menue[TB_num][0] not in arrange:
                                size_name = size_name2
                            result.append([makura[0]+TB_menue[TB_num][0]+size_name[size-1],TB_menue[TB_num][size]-10])
                            value += TB_menue[TB_num][size]-10
                        except IndexError:
                            size = random.randint(1,3)
                            if TB_menue[TB_num][size] == -1:
                                continue
                            if TB_menue[TB_num][0] not in arrange:
                                size_name = size_name2
                            result.append([makura[0]+TB_menue[TB_num][0]+size_name[size-1],TB_menue[TB_num][size]-10])
                            value += TB_menue[TB_num][size]-10

                    else:
                        try:
                            if TB_menue[TB_num][size] == -1:
                                continue
                            if TB_menue[TB_num][0] not in arrange:
                                size_name = size_name2
                            result.append([makura[2]+TB_menue[TB_num][0]+size_name[size-1],TB_menue[TB_num][size]])
                            value += TB_menue[TB_num][size]
                        except IndexError:
                            #print(TB_menue[TB_num])
                            size = random.randint(1,3)
                            if TB_menue[TB_num][size] == -1:
                                continue
                            if TB_menue[TB_num][0] not in arrange:
                                size_name = size_name2
                            result.append([makura[2]+TB_menue[TB_num][0]+size_name[size-1],TB_menue[TB_num][size]])
                            value += TB_menue[TB_num][size]

            if cnt > 0:

                size_name = size_name1

                while value <= mx_value:
                    TP_num = random.randint(0,len(tanpin)-1)
                    CH_num = random.randint(0,len(choice)-1)
                    attribute = random.randint(1,2)
                    
                    if attribute == 1:
                        result.append([makura[1]+ tanpin[TP_num][0],tanpin[TP_num][1]])
                        value += tanpin[TP_num][1]
                    else:
                        size = random.randint(1,4)
                        if choice[CH_num][size] == -1 or choice[CH_num][0] == "ご飯":
                            continue
                        result.append([makura[1]+choice[CH_num][0]+size_name[size-1],choice[CH_num][size]])
                        value += choice[CH_num][size]



            if value > mx_value + 50:
                value -= result.pop(-1)[1]
                cnt -= 1

        result = sorted(result,key=lambda x:x[0])

        for i in result:
            if i[0] not in check:
                check[i[0]] = 0
            check[i[0]] += 1

        for j in check:
            if check[j] == 1:
                sub_result = result.pop(0)
                result.append(sub_result[0]+"..."+str(sub_result[1])+"円")
            else:
                for _ in range(check[j]):
                    sub_result = result.pop(0)
                result.append(sub_result[0]+" x{}".format(check[j])+"..."+str(sub_result[1]*check[j])+"円")


        result = result[::-1]
        result += ["合計金額は{}円です".format(value)]
        # result += ["https://www.momokara.jp/"]
        # result = "\n".join(result)
                
        return result

    """
    
    -------------------------------------------

    ↓ここから下は単品のみのルーレット
    """

    # 単品のみのガチャ
    def only_motikaeri(text):

        text = text.split("の")
        mx_value = int(text[1][0:-1])
        result = []
        value = 0
        check = {} #重複をチェック

        while not mx_value - 50 <= value <= mx_value + 50:

            while value <= mx_value:
                TP_num = random.randint(0,len(tanpin)-1)
                CH_num = random.randint(0,len(choice)-1)
                attribute = random.randint(1,2)
                
                if attribute == 1:
                    result.append([makura[1]+ tanpin[TP_num][0],tanpin[TP_num][1]])
                    value += tanpin[TP_num][1]
                else:
                    size = random.randint(1,4)
                    if choice[CH_num][size] == -1:
                        continue
                    result.append([makura[1]+choice[CH_num][0]+size_name[size-1],choice[CH_num][size]])
                    value += choice[CH_num][size]

            if (not mx_value - 50 <= value <= mx_value + 50) and len(result) > 0:
                remove_menue = random.randint(0,len(result)-1)
                value -= result.pop(remove_menue)[1]
        
        result = sorted(result,key=lambda x:x[0]) #消すときにわかりやすくする

        for i in result:
            if i[0] not in check:
                check[i[0]] = 0
            check[i[0]] += 1

        for j in check:
            if check[j] == 1:
                sub_result = result.pop(0)
                result.append(sub_result[0]+"..."+str(sub_result[1])+"円")
            else:
                for _ in range(check[j]):
                    sub_result = result.pop(0)
                result.append(sub_result[0]+" x{}".format(check[j])+"..."+str(sub_result[1]*check[j])+"円")

        result = result[::-1]
        result += ["合計金額は{}円です".format(value)]
        # result += ["https://www.momokara.jp/"]
        # result = "\n".join(result)
                
        return result


    if "単品" in Text:
        return only_motikaeri(Text)
    else:
        return TorB(Text)

# ごちゃ混ぜなんでもありのガチャ
def random_menue(text):
    text = text.split("の")
    mx_value = int(text[1][0:3])
    result_names = []
    result_values = []
    value = 0
    
    while not mx_value - 50 <= value <= mx_value + 50:

        while value < mx_value:

            ram_num = random.randint(0,len(choice)-1)
            size = random.randint(1,4)
            attribute = random.randint(1,10)

            if attribute <= 3:
                attribute = 1
            else:
                attribute = 2

            makura_name = makura[attribute]

            if choice[ram_num][size] == -1 or choice[ram_num][0] == "ご飯":
                continue

            if attribute == 1:
                value += choice[ram_num][size]
                result_values.append(choice[ram_num][size])

            elif attribute == 2:
                if size == 1:
                    continue
                value += choice[ram_num][size] + 210
                result_values.append(choice[ram_num][size]+210)

                if choice[ram_num][0] == "元祖ももから":
                    result_values.pop(-1)
                    value -= 10
                    result_values.append(choice[ram_num][size]+200)
                elif choice[ram_num][0] == "フライドポテト":
                    result_values.pop(-1)
                    value -= 210
                    result_values.append(choice[ram_num][size])

            if choice[ram_num][0] == "フライドポテト":
                makura_name = "[単品]"
            result_names.append(makura_name + choice[ram_num][0] + size_name[size-1])
    

        if not mx_value-50 <= value <= mx_value + 50: 

            if len(result_names) != 0:
                q = random.randint(0,len(result_names)-1)
                result_names.pop(q)
                value -= result_values.pop(q)

    dic = {}
    result = []

    for i in range(len(result_names)):
        dic[result_names[i]] = result_values[i]
    
    for j in dic:
        result += [j + " " + str(dic[j]) + "円"]

    return result,value


# debug
# print(momokara_roulette(input()))
