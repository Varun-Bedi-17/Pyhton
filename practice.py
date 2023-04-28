def intToRoman(num):
        roman = ""
        number = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL",
            "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12

        while num:
            div = num // number[i]
            num %= number[i]

            while div:
                roman += sym[i]
                div -= 1
            i -= 1
        return roman
number = int(input())
print(intToRoman(number))