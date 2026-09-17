class Utils:
    def reversed(self, number: int) -> int:
        if not isinstance(number, int):
            raise TypeError("value must be an integer")

        is_negative = number < 0

        reversed_number = 0
        number = abs(number)
        while (number):
            reversed_number = reversed_number * 10
            reversed_number += number % 10 
            number = number // 10

        return -reversed_number if is_negative else reversed_number
        
    def formatter(self, number: int) -> tuple[str, str]:
        if not isinstance(number, int):
            raise TypeError("value must be an integer")

        return bin(number), oct(number)