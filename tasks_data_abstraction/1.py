import math


def make_rational(numer, denom):
    gcd = math.gcd(numer, denom)
    return {
        'numer': int(numer / gcd),
        'denom': int(denom / gcd)
    }

def get_numer(rational):
    return rational['numer']

def get_denom(rational):
    return rational['denom']

def add(rational_1, rational_2):
    numer_1 = get_numer(rational_1)
    numer_2 = get_numer(rational_2)
    denom_1 = get_denom(rational_1)
    denom_2 = get_denom(rational_2)

    return make_rational(
        numer_1 * denom_2 + numer_2 * denom_1,
        denom_1 * denom_2
    )

def sub(rational_1, rational_2):
    numer_1 = get_numer(rational_1)
    numer_2 = get_numer(rational_2)
    denom_1 = get_denom(rational_1)
    denom_2 = get_denom(rational_2)

    return make_rational(
        numer_1 * denom_2 - numer_2 * denom_1,
        denom_1 * denom_2
    )

def rat_to_string(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))



rat1 = make_rational(3, 9)
print(rat1)
rat11 = make_rational(16, 8)
print(rat11)
rat2 = make_rational(10, 3)

rat3 = add(rat1, rat2)
print(rat3)
print(rat_to_string(rat3)) # 11/3

rat4 = sub(rat1, rat2)
print(rat4)
print (rat_to_string(rat4)) # -3/1
