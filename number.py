#!/usr/bin/env python
# coding: utf-8

# In[22]:


import wiringpi as pi

pi.wiringPiSetupGpio()

A_pins  = [5, 4, 3, 2, 1, 7, 10,11] # 7セグのpin番号
A_GPIOs = [14,15,18,23,24,25,8, 7] # raspberrypiのGPIO番号

# 出力をOUTPUT、0Vに初期化
for A_GPIO in A_GPIOs: 
    pi.pinMode(A_GPIO, pi.OUTPUT)
    pi.digitalWrite(A_GPIO, pi.LOW)

numbers = {'0': [0,1,0,1,1,1,1,1],
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

def printnumber(num_strs):
    num_strs = list(num_strs)
        
    # 1数字毎の処理
    for num_str in num_strs:
        index = numbers[num_str]
        
        # 3,3V
        for i, x in enumerate(index):
            if x == 1:
                on_GPIO = A_GPIOs[i]
                
                pi.digitalWrite(on_GPIO, pi.HIGH)
            
        # 保持
        pi.delay(500)
        
        # 0V
        for i, x in enumerate(index):
            if x == 1:
                on_GPIO = A_GPIOs[i]
                
                pi.digitalWrite(on_GPIO, pi.LOW)
        
        # 保持
        pi.delay(100)
    
    # 出力をOUTPUT、0Vに初期化
    for A_GPIO in A_GPIOs: 
        pi.pinMode(A_GPIO, pi.INPUT)

if __name__ == '__main__':
    
    printnumber('12.27.2345')

