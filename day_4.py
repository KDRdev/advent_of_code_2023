result = 0

with open("input.txt", "r") as input_file:
    # PART 1
    for line in input_file.readlines():
        winning_numbers = list(map(lambda x: int(x), filter(lambda x: x != "", line.split("|")[0].split(":")[1].strip().split(" "))))
        numbers_on_card = list(map(lambda x: int(x), filter(lambda x: x != "", line.split("|")[1].strip().split(" "))))
        numbers = [number for number in numbers_on_card if number in winning_numbers]
        card_worth = 0
        for number in numbers:
            if card_worth == 0:
                card_worth += 1
            else:
                card_worth = card_worth*2
        result += card_worth
    print(result)
    # PART 2
    result = {}
    for card, line in enumerate(input_file.readlines(), start=1):
        numbers_on_card = list(map(lambda x: int(x), filter(lambda x: x != "", line.split("|")[1].strip().split(" "))))
        winning_numbers = list(map(lambda x: int(x), filter(lambda x: x != "", line.split("|")[0].split(":")[1].strip().split(" "))))
        numbers = [number for number in numbers_on_card if number in winning_numbers]
        if not card in result:
            result[card] = 1
        else:
            result[card] += 1
        for win, num in enumerate(numbers, start=1):
            card_to_copy = card + win
            if not card_to_copy in result:
                result[card_to_copy] = result[card]
            else:
                result[card_to_copy] += result[card]
    print(sum(list(result.values())))
