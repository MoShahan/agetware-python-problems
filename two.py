# 2 - Problem: Convert number into a comma separated Indian currency format


def main():
    number = input("Enter your floating point number: ")
    integerPart = number.split(".")[0]

    if len(integerPart) < 4:  # if number is less than 1000
        print(number)
        return
    else:
        toggleComma = False  # to add comma alternatively
        decimalPart = ""
        if "." in number:
            decimalPart = number.split(".")[1]
        res = ""
        for number in integerPart[:-3][::-1]:
            res = res + number + ("," if toggleComma else "")
            toggleComma = not toggleComma

        print(
            "Result:",
            res[::-1].strip(",")
            + ","
            + integerPart[-3:]
            + ("." if decimalPart else "")
            + decimalPart,
        )


main()
