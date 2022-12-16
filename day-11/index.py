import math


class Monkey:
    def __init__(self, id, items, operation, test, true_monkey, false_monkey) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey

        self.items_inspected = 0

    def recieve_item(self, num):
        self.items.append(num)
    
    def handle_worry(self, item):
        return math.floor(item/3)

    def take_turn(self, monkeys):
        new_worry_values = [self.handle_worry(self.operation(item)) for item in self.items]

        for val in new_worry_values:
            monkey_id = self.true_monkey if(self.test(val)) else self.false_monkey
            monkeys[monkey_id].recieve_item(val)
            self.items_inspected += 1
        self.items = []

# example
# monkeys = [
#     Monkey(0, [79, 98], lambda x: x*19, lambda x: x%23 == 0, 2, 3),
#     Monkey(1, [54, 65, 75, 74], lambda x: x+6, lambda x: x%19 == 0, 2, 0),
#     Monkey(2, [79, 60, 97], lambda x: x*x, lambda x: x%13 == 0, 1, 3),
#     Monkey(3, [74], lambda x: x+3, lambda x: x%17 == 0, 0, 1)
# ]

# question
monkeys = [
    Monkey(0, [50, 70, 54, 83, 52, 78], lambda x: x*3, lambda x: x%11 == 0, 2, 7),
    Monkey(1, [71, 52, 58, 60, 71], lambda x: x*x, lambda x: x%7 == 0, 0, 2),
    Monkey(2, [66, 56, 56, 94, 60, 86, 73], lambda x: x+1, lambda x: x%3 == 0, 7, 5),
    Monkey(3, [83, 99], lambda x: x+8, lambda x: x%5 == 0, 6, 4),
    Monkey(4, [98, 98, 79], lambda x: x+3, lambda x: x%17 == 0, 1, 0),
    Monkey(5, [76], lambda x: x+4, lambda x: x%13 == 0, 6, 3),
    Monkey(6, [52, 51, 84, 54], lambda x: x*17, lambda x: x%19 == 0, 4, 1),
    Monkey(7, [82, 86, 91, 79, 94, 92, 59, 94], lambda x: x+7, lambda x: x%2 == 0, 5, 3)
]

ROUND_COUNT = 20

for x in range(ROUND_COUNT):
    for monkey in monkeys:
        monkey.take_turn(monkeys)
    # print(f"{x}: {[monkey.items for monkey in monkeys]}")

items_inspected = [monkey.items_inspected for monkey in monkeys]
items_inspected.sort(reverse=True)
print(items_inspected[0] * items_inspected[1])