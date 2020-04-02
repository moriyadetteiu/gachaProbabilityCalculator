from fractions import Fraction
import calculator.expected_value as expected_value

limitedWeaponPerAll = 0.043 / 100
TotalNumberOfLimitedWeapon = 12

angelStonePerAll = 0.013 / 100
TotalNumberOfAngelStone = 6

hitPerTrial =Fraction(str(limitedWeaponPerAll * TotalNumberOfLimitedWeapon))
results = (
    float(expected_value.calc_expected_value(hitPerTrial, 300, n))
    for n
    in range(0, 300)
)

print(list(results))
