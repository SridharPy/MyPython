def printfromdic(dic):
    value = dic["under_bed"][1]
    return value

def printFromDicOtherWay(dic):
    value = dic["under_bed"]
    finalValue = value[1]
    return finalValue

money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
print(printfromdic(money))
print(printFromDicOtherWay(money))
