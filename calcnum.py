from typing import NoReturn

def natural_numbers_representation_theorem_any_base(number: int, base: int) -> None | NoReturn:
    """
        Restrictions:
            number > 0
            base > 1

        Prints how to represent any number using the sum of the remainders of sucessives divisions
    """

    if number == 0 or base < 1:
        raise Exception("Input does not obey restrictions: number != 0 e base > 1")
    
    if number < base:
        print(f"{number} = {number} * {base}^0")
        return 

    answer = f"{number} = "    
    digits = []

    digits.append(number % base)
    while number >= base:
        number = int(number / base)
        digits.append(number % base)
    
    for i, e in enumerate(reversed(digits)):
        if i == 0:
            answer = answer + f"{e} * {base}^{len(digits) - 1 - i} "
        else:
            answer = answer + f"+ {e} * {base}^{len(digits) - 1 - i} "
    
    print(answer)

if __name__ == "__main__":
    natural_numbers_representation_theorem_any_base(1, 2)