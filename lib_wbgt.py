"""
2023/9/8
温度と湿度から暑さ指数を求めます。
簡易計算式もあるみたいだけれど、うまくいかなかったので、
http://www.ecoq21.jp/latest-article/no136/no136.pdf
等の暑さ指数（WBGT）の早見表を取り込みお温度、湿度から求めるようにしました。
少し切り上げ気味に一段高めのWBGTになるようにしています。
"""

def calculate_wbgt(temperature, humidity):
    wbgt_table = [
        [29, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44],
        [28, 29, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42, 43],
        [28, 28, 29, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41, 42],
        [27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 35, 36, 37, 38, 39, 40, 41],
        [26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 34, 35, 36, 37, 38, 39, 39],
        [25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 33, 34, 35, 36, 37, 38, 38],
        [25, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 33, 34, 35, 36, 37, 37],
        [24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36],
        [23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 31, 31, 32, 33, 34, 34, 35],
        [22, 23, 24, 24, 25, 26, 27, 27, 28, 29, 30, 30, 31, 32, 33, 33, 34],
        [21, 22, 23, 24, 24, 25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33],
        [21, 21, 22, 23, 24, 24, 25, 26, 26, 27, 28, 29, 29, 30, 31, 31, 32],
        [20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 28, 28, 29, 30, 30, 31],
        [19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28, 29, 29, 30],
        [18, 19, 20, 20, 21, 22, 22, 23, 24, 24, 25, 26, 26, 27, 28, 28, 29],
        [18, 18, 19, 20, 20, 21, 22, 22, 23, 23, 24, 25, 25, 26, 27, 27, 28],
        [17, 18, 18, 19, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25, 26, 26, 27],
        [16, 17, 17, 18, 19, 19, 20, 20, 21, 22, 22, 23, 23, 24, 25, 25, 26],
        [15, 16, 17, 17, 18, 18, 19, 19, 20, 21, 21, 22, 22, 23, 24, 24, 25],
        [15, 15, 16, 16, 17, 17, 18, 19, 19, 20, 20, 21, 21, 22, 23, 23, 24]
    ]
    return wbgt_table[40 - temperature ][humidity // 5 - 4]

def calc(temperature, humidity):
    # 例: 気温と湿度でWBGTを計算
    # ただし、温度、湿度に端数がある場合高めのWBGTを表示するように
    # 温度が0.4以上の端数があれば、3捨5入する
    # 湿度は四捨五入して端数が2％を超えると5%上の数値とする。
    # 40.4度以上の温度が入力されると35度を返す
    wbgt  = 0
    temp  = int(temperature + 0.6)
    humdy = int(humidity + 0.5)
    if humdy %5 > 2 :
        humdy = humdy + 3
        if humdy > 100: humdy=100
    # 表の範囲外の数値を排除
    if temp >= 21 and temp < 41:
        if humdy >= 20 and humdy <= 100:
            try:
                wbgt = calculate_wbgt(temp, humdy)
            except:
                wbgt = 0
    if temp > 40:
        # 41度以上の気温の場合は35を返す
        wbgt = 35
    return wbgt # 表にない低い範囲もしくはエラー時の場合は0を返す

def main():
    print(calc(40.3, 44.2))
    print(calc(40.3, 19.9))

if __name__=='__main__':
    main()