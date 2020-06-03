# bounce.py
#
# Exercise 1.5

bounce = 1


while bounce < 11:
    print(bounce, round(recoil_height, 4))
    bounce = bounce + 1
    recoil_height = recoil_height * 0.6
