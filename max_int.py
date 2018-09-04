#Setja inputtið inní while lykkju sem stoppar þegar slegið er inn negatíva tölu. í lykkjuni á að vera If fall sem athugar hvort talan sem var nýlega sleginn inn sé hærri en sú var fyrir og því mun það alltaf halda í hæstu töluna. þegar lykkjan er brotinn þá á að prenta út hæstu töluna.

num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
while num_int > 0:
    num_int = int(input("Input a number: "))
    if max_int < num_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
