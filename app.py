from random import choice, randint
from aquarium import aquarium
from citizens import PeacefulFish, PredatoryFish, Snail, AquaPlant

CITIZENS_SETUP = {'peaceful_fishes_list': [PeacefulFish() for _ in range(randint(10, 50))],
                  'predatory_fishes_list': [PredatoryFish() for _ in range(randint(2, 6))],
                  'snails_list': [Snail() for _ in range(randint(2, 9))],
                  'aquaplants_list': [AquaPlant() for _ in range(randint(20, 60))]
                  }


def deploy_citizens():
    try:
        for key in CITIZENS_SETUP.keys():
            aquarium.extend(CITIZENS_SETUP[key])
    except ValueError as e:
        print('{0}\nmax len aquarium 100'.format(e))

deploy_citizens()


def simulate():
    while len(aquarium) > len(CITIZENS_SETUP['predatory_fishes_list']) + len(CITIZENS_SETUP['snails_list']):
        eating_citizen = choice(aquarium)
        citizen_to_eat = choice(aquarium)
        eating_citizen.eat(citizen_to_eat)

    aquarium.sort_by_weight()

    print('SCOREBOARD'.center(36, '*'))
    for survived in aquarium:
        print('{0}(weight={1}) eat {2} feeds'.format(survived.__class__.__name__, survived.weight,
                                                     survived.eaten_citizens_count))


if __name__ == '__main__':

    simulate()
