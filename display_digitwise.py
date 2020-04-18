#!/usr/bin/env python
# coding: utf-8

import wiringpi as pi
import time
import sys


# メモ
A_PINs  = [5, 4, 3, 2, 1, 7, 10,11] # 7セグのpin番号
A_GPIOs = [14,15,18,23,24,25,8, 7] # raspberrypiのGPIO番号
DIGITS_PINs = [6, 8, 9, 12] # 7セグの桁指定用pin番号
DIGITs =      [17,27,22,10] # 桁指定用GPIO番号


# 出力数字とGPIO番号の対応
NUMBERs = {'0': [0,1,0,1,1,1,1,1],
           '1':[0,1,0,0,0,1,0,0],
           '2':[1,0,0,1,1,1,0,1],
           '3':[1,1,0,1,0,1,0,1],
           '4':[1,1,0,0,0,1,1,0],
           '5':[1,1,0,1,0,0,1,1],
           '6':[1,1,0,1,1,0,1,1],
           '7':[0,1,0,0,0,1,1,1],
           '8':[1,1,0,1,1,1,1,1],
           '9':[1,1,0,1,0,1,1,1],
           '.':[0,0,1,0,0,0,0,0]}


#str数字入力から各桁の値と桁数のarrayを作る
def analyze(input_num):
    
    nums = list(input_num)
    nums = nums[-1::-1] #桁数<4のときのため、桁を反転しておく
    selected_digits = ['0','1','2','3']
    
    return nums, selected_digits


def display_bydigit(number, selected_digit):

    # 桁指定(対応TrをON)
    digit_gpio = DIGITs[int(selected_digit)]
    pi.digitalWrite(digit_gpio, pi.HIGH)

    # 数字描画
    for i, zero_one in enumerate(NUMBERs[number]):
        if zero_one == 1:
            on_gpio = A_GPIOs[i]
            pi.digitalWrite(on_gpio, pi.HIGH)

    # 保持(ms)
    # pi.delay(7)

    # 描画の終了
    for i, x in enumerate(NUMBERs[number]):
        if x == 1:
            on_GPIO = A_GPIOs[i]    
            pi.digitalWrite(on_GPIO, pi.LOW)

    # 桁指定の終了
    pi.digitalWrite(digit_gpio, pi.LOW)


def display(input_num, display_time=5):
    """
    str4桁数字列(input_num)を7セグに表示
    nums:input_num数字列のリスト
    num:numsリストの各要素(str型1桁の数字)
    
    """

    pi.wiringPiSetupGpio()

    # 出力をOUTPUT、0Vに初期化
    for A_GPIO in A_GPIOs: 
        pi.pinMode(A_GPIO, pi.OUTPUT)
        pi.digitalWrite(A_GPIO, pi.LOW)

    for digit in DIGITs:
        pi.pinMode(digit, pi.OUTPUT)
        pi.digitalWrite(digit, pi.LOW)

    # 処理開始
    INPUT_NUM = input_num

    nums, selected_digits = analyze(INPUT_NUM)

    # diisplay_time 秒間表示
    DISPLAY_TIME = display_time
    start = time.time()
    while True:

        for i in range(len(nums)):

            num = nums[i]
            selected_digit = selected_digits[i]

            display_bydigit(num, selected_digit)

        if time.time() - start >= DISPLAY_TIME:
            break

    # 出力をINPUTに初期化
    for A_GPIO in A_GPIOs:
        pi.pinMode(A_GPIO, pi.INPUT)

    for digit in DIGITs:
        pi.pinMode(digit, pi.INPUT)


if __name__ == '__main__':
    
    argvs = sys.argv
    argc = len(argvs)

    if argc<2 :
    	print("usage:$sudo python {} <number of display>".format(argvs[0]))
    	quit()

    input_num = argvs[1]

    display(input_num)

