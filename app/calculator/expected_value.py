from fractions import Fraction
from scipy.special import comb

def calc_expected_value(hitPerTrial: Fraction, numberOfTrials: int, numberOfHit: int) -> Fraction:
    notHitPerTrial = 1 - hitPerTrial
    numberOfNotHit = numberOfTrials - numberOfHit
    hitComb = comb(numberOfTrials, numberOfHit, exact = True)

    return hitPerTrial ** numberOfHit * notHitPerTrial ** numberOfNotHit * hitComb
