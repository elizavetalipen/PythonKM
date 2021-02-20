# В этой программе пользователь выбирает одну страну из списка,
# и на экран выводится цитата на языке этой страны с переводом.

def main():
    # Задаём страны, цитаты и их переводы в виде списков(массивов)
    countries = ["Chile","Norway","Iceland","Portugal","Estonia","Germany"]
    quotes = ["La verdadera amistad resiste el tiempo, la distanica, y el silencio.",
	    "Gammal kjærleik rustar inkje.",
	    "Margr lækr smár gjörir stórar ár.",
	    "Em terra de cego, quem tem olho é rei.",
	    "Kõik ei ole kuld, mis hiilgab.",
	    "Taten sagen mehr als Worte."]
    translations  =["True friendship resists time, distance, and silence.",
    "Old love does not rust.",
    "Small streams make great rivers.",
    "Among the blind, a one-eyed man is king.",
    "All that glimmers is not gold.",
    "Actions say more than words."]

    print(countries)
    c = input("\nChoose one of these countries: ")
    print()

    # Для вывода цитаты и значения используется вложенный цикл, где i - индекс элемента в списке countries.
    # Сперва проверяется условие, т.е. если введённая страна совпадает с i-ым элементом списка,
    # выведутся цитата и перевод. Если нет, i величивается на 1 и проверка повторяется.
    # Цикл for завершится, если i>5, так как с помощью функции range(), вызванной с одним аргументом (stop),
    # можно получить все числа от 0 и данного, не включая конечное число.
    i=0
    for i in range(6):
        if c == countries[i]:
            print(quotes[i])
            print(translations[i])
        else: 
            i=i+1 


if __name__ == "__main__":
    main()