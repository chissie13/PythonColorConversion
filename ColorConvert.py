def RGBtoCMY(R, G, B):
    C = 1 - R
    M = 1 - G
    Y = 1 - B

    return [C,M,Y]

def CMYtoRGB(C, M, Y, Kaas):
    R = (1 - C) * (1 - Kaas)
    G = (1 - M) * (1 - Kaas)
    B = (1 - Y) * (1 - Kaas)

    return [R, G, B]

def RGBtoHSL(R, G, B):
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

def HSLtoRGB(H, S, L):
    print()

def transparancy(R1, G1, B1, alpha1, R2, G2, B2):
    print()

print(RGBtoCMY(1,0.5,0.3))
print(CMYtoRGB(1, 0.2, 0.3, 0.5))
print(RGBtoHSL(24,98,118))