birth_year = int(input("Enter your birth year: "))
if birth_year >= 1900:
    x = birth_year%12
    if x == 4:
        print("Your Chinese Zodiac Sign is: Rat (鼠 / Shǔ)")
    elif x == 5:
        print("Your Chinese Zodiac Sign is:  Ox (牛 / Niú)")
    elif x == 6:
        print("Your Chinese Zodiac Sign is: Tiger (虎 / Hǔ)")
    elif x == 7:
        print("Your Chinese Zodiac Sign is: Rabbit (兔 / Tù)")
    elif x == 8:
        print("Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)")
    elif x == 9:
        print("Your Chinese Zodiac Sign is: Snake (蛇 / Shé)")
    elif x == 10:
        print("Your Chinese Zodiac Sign is: Horse (马 / Mǎ)")
    elif x == 11:
        print("Your Chinese Zodiac Sign is: Goat (羊 / Yáng)")
    elif x == 0:
        print("Your Chinese Zodiac Sign is: Monkey (猴 / Hóu)")
    elif x == 1:
        print("Your Chinese Zodiac Sign is: Rooster (鸡 / Jī)")
    elif x == 2:
        print("Your Chinese Zodiac Sign is: Dog (狗 / Gǒu)")
    else:
        print("Your Chinese Zodiac Sign is: Pig (猪 / Zhū)")
else:
    print("nvalid Year, it should not be earlier than 1900")

    
