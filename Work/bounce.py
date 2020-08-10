#!/usr/bin/env python3

# bounce.py

height = 100 # (meters)
recoil_height = 0.6 * height #(3/5 of height)
bounce = 1


while bounce < 11:
    print(bounce, round(recoil_height, 4))
    bounce = bounce + 1
    recoil_height = recoil_height * 0.6
