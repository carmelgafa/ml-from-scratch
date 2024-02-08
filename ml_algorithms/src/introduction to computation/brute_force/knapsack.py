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

def build_menu(names, values, calories):
    
    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    
    return menu

def max_val(to_consider, available):

    # available is an index that goes through list 

    # base case nothing left available or nothing left to consider 
    if to_consider == [] or available == 0:
        result = (0, ())
    
    # is fist element's cost enough to make item available.
    # if it is not, right branch is not considered
    elif to_consider[0].get_cost() > available:
        result = max_val(to_consider[1:], available)
    
    # consider both branches
    else:
        next_item = to_consider[0]
        
        # left branch - take
        # we took item so available is not minus the cost of taken item
        with_val, with_to_take = max_val(to_consider[1:],
            available - next_item.get_cost())

        # value of subbranch plus value of iteam as it was taken
        with_val += next_item.get_value()

        # right branch - leave
        without_val, without_to_take = max_val(to_consider[1:],
            available)

        # choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)

    return result

def test_max_val(foods, max_units):
    
    print(f'use search tree to allocate {max_units} calories')

    val, taken = max_val(foods, max_units)
    
    print(f'total value of items taken {val}')

    for item in taken:
        print(f'\t{item}')

if __name__ == "__main__":
    names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donghut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    foods = build_menu(names, values, calories)

    test_max_val(foods, 750)
