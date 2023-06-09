# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina.
# Funkcja przyjmuje jako argument temperaturę w C, a funkcja zwraca temperaturę w K.
# Więcej informacji o konwersji: https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
# Obie wartości maja być typu float

def C_to_K(celcius: float) -> float:
    kelvin = celcius + 273,15
    return kelvin


# Zadanie 02
# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy,
# a następnie zwraca słownik zliczający ilość wystąpień każdego słowa (kot =/= kota).
# Podpowiedź możemy użyć metody split(" ").

def words_counter(sentence: str) -> dict:
    many_words = {}
    for w in sentence.lower().split(" "):
        many_words[w] = count(w)

# Zadanie 03
# Użytkownik podaje trzy liczby całkowite. Następnie program zwraca informację,
# która z podanych liczb jest największa
# (dla odważnych - możecie również weryfikować czy dane liczbą są takie same).

def greatest_number(a: int, b: int, c: int):
    for n in [a, b, c]:
        if a == b or a == c or b == c:
            return "Some of the values are the same."
        elif a == b and b == c:
            return "All of the values are the same."
    largest = max([a, b, c])
        return f"The largest value is {largest}."


# Zadanie 04
# Napisać program, gdzie użytkownik podaje liczby całkowite i je sumuje.
# Program działa dopóki użytkownik nie poda liczby ujemnej.
# Po podaniu liczby ujemnej program wyświetla sumę podanych poprzednich liczb.

value = int(input("Enter an integer value: "))
list_of_values = []
the_sum = 0

while n >= 0:
    list_of_values.append(value)
    the_sum = sum(list_of_values)
    value = int(input("Enter another integer value: "))

print(f"The total of your inputs is {the_sum}.")


# Zadanie 05
# Napisać funkcję, która konwertuje liczbę z systemu dziesiętnego na binarny
# (nie używamy funkcji wbudowanych w Pythonie)

# Zadanie 06
# Użytkownik podaje liczbe całkowitą.
# Następnie program zwraca sumę CYFR z których składa się podana liczba.
# Przykładowo: użytkownik podaje 1307, program zwraca 11 (1+3+0+7). Podpowiedź: konwersja na str

number = input("Enter your number: ")
sum_of_digits = sum(int(digit) for digit in number)
print(f"The sum of the digits in your number is {sum_of_digits}.")

# Zadanie 07
# Napisać program, gdzie użytkownik podaje n łańcuchów znakowych
# (ilość n również definiuje wcześniej użytkownik).
# Następnie program zwraca informacje ile łańcuchów znakowych jest unikatowych. :)
# Przykładowo: użytkownik podał n = 3. Następnie podał trzy łańcuchy znakowe:
# Kot, Pies, Kot. Program zwróci informacje, że ilość UNIKATOWYCH łańuchów znakowych to: 2.

n = int(input("Enter the number of strings: "))
all_strings = []
strings_dict = {}
unique_list = []
unique = 0

while len(all_strings) < n:
    strings = str(input("Input your string here: "))
    all_strings.append(strings)
    if len(all_strings) == n:
        for s in all_strings:
            if s not in strings_dict.keys():
                strings_dict[s] = all_strings.count(s)
        for k, v in strings_dict.items():
            if v == 1:
                unique_list.append(k)
        unique = len(unique_list)
        print(f"There are {unique} unique strings in your input.")
        break


# start - godzina rozpoczęcia seansu
# playtime - ile sekund oglądaliśmy
#
# Program ma podzielić playtime na poszczególne grupy
#
# p = 3.5
# s = 5.6
#
# 5: 0.4 (do 6)
# 6: 1.0 (do 7)
# 7: 1.0 (do 8)
# 8: 1.0 (do 9)
# 9: 0.1 (do 10) <-- p + s
#
# 0: 0.0 - 1.00
# 1: 1.01 - 2.00
# 2: 2.01 - 3.00
# ...
# 10: 10.01 - 11.00


def time_split(start: float, playtime: float):
    start_hour = int(start)
    end = start + playtime
    end_hour = int(end)