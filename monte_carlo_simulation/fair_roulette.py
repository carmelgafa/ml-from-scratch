import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1, 37):
            self.pockets.append(i)
        
        self.ball=None

        self.pocket_odds = len(self.pockets) - 1

        random.seed(0)

    def spin(self):
        self.ball = random.choice(self.pockets)

    def bet_pocket(self, pocket, amount):
        '''
        pocket: pocket placing bet
        amount: sum being bet
        '''
        if str(pocket) == str(self.ball):
            return amount * self.pocket_odds
        else:
            return -amount
    def __str__(self) -> str:
        return 'fair roulette'

class EURoulette(FairRoulette):
    def __init__(self):
        super().__init__()
        self.pockets.append('O')
    def __str__(self) -> str:
        return 'EU Roulette'

class USRoulette(EURoulette):
    def __init__(self):
        super().__init__()
        self.pockets.append('OO')
    def __str__(self) -> str:
        return 'US Roulette'


def play_roulette(game, num_spins, pocket, bet):
    '''
    Arguments:
    game: Roulette game being played
    num_spins: number of spins for the simulation
    pocket: pocket placing bet
    bet: amount of bet
    '''
    total_pocket = 0
    for i in range(num_spins):
        game.spin()
        total_pocket += game.bet_pocket(pocket, bet)

    print(f'{num_spins} spins of {game}')
    print(f'expected return betting {pocket} = {str(100*total_pocket/num_spins)}%')

    return total_pocket/num_spins

if __name__ == "__main__":
    game = FairRoulette()
    for num_spins in (100, 1000000):
        for i in range(3):
            # betting 1 dollar on number 2 for num-spins trials
            play_roulette(game, num_spins, 2, 1)



