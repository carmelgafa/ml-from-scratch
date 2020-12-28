class Food ():

    def __init__(self, n:str, v:int, w:int) -> None:
        self.name = n
        self.value = v
        self.calories = w

    def get_value(self) -> int:
        return self.value

    def get_cost(self) -> int:
        return self.calories
    
    def density(self) -> float:
        return self.get_value() / self.get_cost()

    def __str__(self) -> str:
        return f'{self.name} : <{self.value}, {self.calories}>'


def build_menu(names:[str], values:[int], calories:[int]) -> [Food]:
    
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    
    return menu

def greedy(items:[Food], max_cost:int, key_function) -> ([Food], int):

    # sort according to key_function, ascending order
    items_copy = sorted(items, key=key_function, reverse=True)

    result = []

    total_value, total_cost = 0, 0

    for i in range(len(items_copy)):
        if(total_cost + items_copy[i].get_cost()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_cost()
            total_value += items_copy[i].get_value()
    
    return (result, total_value)

def test_greedy(items:[Food], constraint:int, key_function) -> None:
    
    taken, val = greedy(items, constraint, key_function)

    print('Total values of items taken = ', val)
    for item in taken:
        print('\t',item)

def test_greedy_functions(foods:[Food], max_units:int) -> None:
    
    # greedy using food value 
    print(f'Use greedy by value to allocate {max_units} calories')
    test_greedy(foods, max_units, Food.get_value)

    # greedy using food cost, calories
    # we need inverse of calories to start with foods having the 
    # smallest numbers, hence lambda fn
    print(f'Use greedy by cost to allocate {max_units} calories')
    test_greedy(foods, max_units, lambda x: 1/Food.get_cost(x))

    print(f'Use greedy by density to allocate {max_units} calories')
    test_greedy(foods, max_units, Food.density)



if __name__ == "__main__":
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donghut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = build_menu(names, values, calories)
    test_greedy_functions(foods, 750)