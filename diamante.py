# 5 min cada cual tiene contorl y programa


#     * (asterisco = i)
#    * *
#   * * *
#  * * * *
# * * * * *

# tabulador = si esta en 1 => input y va restando de a 1
# entre cada * => printeamos un " "

# print(“\t”) - tab
# print(“\n”) - newline

# function (input cant) output print iterando


def printDiamond(cant):
    asterisc = "*"
    diamond = ""

    x = range(1, cant)
    j = 0
    cantTab = cant
    stringTabs = ""
    t = cant
    lstTabs = []
    for n in x:

       while t > 0:
            stringTabs = stringTabs + "."
            t -= 1
            lstTabs.append(stringTabs)
           

       while j <= n:
            # arr.length(arr.length - j) => a la ultima posicion
            diamond = diamond + " " + asterisc
            print(diamond)
            #print(j)
            j += 1

    cantTab -= 1

printDiamond(5)