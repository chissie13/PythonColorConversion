import math

def RGBtoCMY(R, G, B):      #RGB all converted from between 0-1
    C = 1 - R
    M = 1 - G
    Y = 1 - B

    return [C,M,Y]

def CMYtoRGB(C, M, Y, Kaas):#CMYK all converted from between 0-1
    R = (1 - C) * (1 - Kaas)
    G = (1 - M) * (1 - Kaas)
    B = (1 - Y) * (1 - Kaas)

    return [R, G, B]

def RGBtoHSL(R, G, B):      #RGB all converted from between 0-1
    minimum = min(R, G, B)
    maximum = max(R, G, B)

    L = (minimum + maximum)/2

    if(minimum == maximum):
        S = 0
    else:
        if(L<0.5):
            S = (maximum - minimum)/(maximum+minimum)
        else:
            S = (maximum - minimum)/(2.0 - maximum - minimum)

    if (R == G and G==B):
        H = 0
    else:
        if (maximum == R):
            H = (G-B)/(maximum-minimum)
        elif (maximum == G):
            H = 2.0 + (B-R)/(maximum-minimum)
        elif (maximum == B):
            H = 4.0 + (R-G)/(maximum-minimum)
    H*=60
    if(H<0):
        H+=360

    return [H, S, L]

def HSLtoRGB(H, S, L):          #H in degrees, S in %, L in %
    if(S == 0):
        R = 0.4
        G = 0.4
        B = 0.4
    else:
        if(L<0.5):
            temp1 = L *(1.0+S)
        else:
            temp1 = L + S - (L*S)

        temp2 = (2 * L) - temp1
        H/= 360
        tempR = correction(H + 0.333)
        tempG = correction(H)
        tempB = correction(H-0.333)

        R = fromTempToFinal(tempR, temp1, temp2)
        G = fromTempToFinal(tempG, temp1, temp2)
        B = fromTempToFinal(tempB, temp1, temp2)

    return [R, G, B]


def correction(correctable):    #corrects numbers which are above 1 or below 0
    while(correctable<0 or correctable>1):
        if(correctable>1):
            correctable-=1
        elif(correctable<0):
            correctable+=1
    return correctable


def fromTempToFinal(tempCol, temp1, temp2): #converts the temparary collors to the actual numbers
    if ((6 * tempCol) < 1):
        Col = temp2 + ((temp1 - temp2) * 6 * tempCol)
    elif ((2 * tempCol) < 1):
        Col = temp1
    elif ((3 * tempCol) < 2):
        Col = temp2 + ((temp1 - temp2) * (0.666 - tempCol) * 6)
    else:
        Col = temp2

    return Col


def transparancy(R1, G1, B1, alpha, R2, G2, B2):        #calculates new color from the 2 overlay colors
    R3 = math.ceil(R1 * alpha) + math.ceil(R2 * (1 - alpha))
    G3 = math.ceil(G1 * alpha) + math.ceil(G2 * (1 - alpha))
    B3 = math.ceil(B1 * alpha) + math.ceil(B2 * (1 - alpha))
    return [R3, G3, B3]


#print(RGBtoCMY(1,0.5,0.3))             #testdata
#print(CMYtoRGB(1, 0.2, 0.3, 0.5))
#print(RGBtoHSL(24/255,98/255,118/255))
#print(HSLtoRGB(193, 67/100, 28/100))
#print(transparancy(200/255,200/255,200/255,0.9,50/255,50/255,50/255))
