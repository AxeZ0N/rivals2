from dataclasses import dataclass

@dataclass
class Fundies:
    name: str = None

class Normals(Fundies):
    pass

class Tilts(Normals):
    name = 'Down tilt'
    pass

class Aerials(Normals):
    pass

class Strongs(Normals):
    pass

class Specials(Fundies):
    pass

class Waves(Fundies):
    pass

class Etc(Fundies):
    pass



fundies_list = ['Waves',
                'Specials',
                'Ground',
                'Normal',
                'Aerial',
                'Dash',
                'Dance',
                'Strong',
                'Grab',
                'Shield',
                'Parry',
                'Ledge',
                'Crouch',
                'Babydash',
                'Shorthop',
                'Fullhop',
                'Offstage',
                'Shield Drop',
                'Fastfall'
                ]

def fcn(list_, time=60, count=2):
    newlist = [x for x in itertools.permutations(list_,count)]
    random.shuffle(newlist)
    for x in newlist:
        print(x)
        sleep(time)

#fcn(fundies_list,60,2)


