# 以下為BMI計算式:
# KG = float(input('輸入體重:'))
# CM = float(input('輸入身高(公分):'))
# M = CM / 100
# print(KG / M**2)

#以下為密碼鎖程式:
# password = input('輸入密碼')
# if password == "971013":
#     print('歡迎光臨')
# else:
#     print('do it again')
while True:
    score = float(input('你的成績:'))
    if score >= 95:
        print('A+')
    elif 95 > score >= 90:
        print('A')
    elif 90 > score >= 85:
        print('A-')
    elif 85 > score >= 80:
        print('B+')
    elif 80 > score >= 75:
        print('B')
    elif 75 > score >= 70:
        print('B-')
    elif 70 > score >= 65:
        print('C+')
    elif 65 > score >= 60:
        print('C')
    else:
        print('屁孩!')