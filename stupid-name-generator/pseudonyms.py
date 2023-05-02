"""
This is my game script
"""

import random


print("Добро пожаловать в 'Подбор имен для напарника.' как в сериале 'Ясновидец'\n")
print("Имя, наподобие того, которое Шин подбирал для Гаса:\n\n")

FIRST = (
        'Baby Oil1', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
        'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
        'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
        'Crapps', 'Dark Skies','Dennis Clawhammer', 'Dicman', 'Elphonso',
        'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
        'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
        'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
        '"Mr Peabody"', 'Oil-Сап', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
        'Pitchfork Ben', 'Potato Bug', 'Pushmeet','Rock Candy', 'Schlomo'
)

LAST = (
        'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout',
        'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott',
        'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster', 'Henderson',
        'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt',
        'Johnson', 'Kingfish', 'Listenbee', "M'Bernbo", 'McFadden', 'Moonshine', 'Nettles',
        'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
        'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney', 'Quakenbush',
        'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine',
        'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
        'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
        'Wimplesnatch', 'Winterkorn', 'Woolysocks'
)

def main():

    """
    Main Script
    """

    while True:
        first_name = random.choice(FIRST)
        last_name = random.choice(LAST)
        res = "{} {}".format(first_name, last_name)

        print('\033[31m')
        print(res)
        print('\033[0m')

        try_again = input("\n\nПопробуете еще? (Нажмите Enter либо N, чтобы выйти: ")
        if try_again.lower() == 'n':
            break

    input("\nНажмите Enter для завершения работы.")

if __name__ == '__main__':
    main()
