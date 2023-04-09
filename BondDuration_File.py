# getBondDuration function
def getBondDuration(y, face, couponRate, m, ppy=1):
    """
    Calculates the modified duration of a bond.

    Args:
        y (float): Yield to maturity
        face (float): Face value of the bond
        couponRate (float): Annual coupon rate
        m (int): Years to maturity
        ppy (int, optional): Number of coupon payments per year. Defaults to 1.

    Returns:
        float: The modified duration of the bond.
    """
    n = m * ppy
    c = face * couponRate / ppy

    bondPrice = getBondPrice(y, face, couponRate, m, ppy)
    
    bondDuration = 0
    for i in range(1, n+1):
        if i == n:
            pmt = c + face
        else:
            pmt = c
        presentValue = pmt / ((1 + y / ppy) ** i)
        bondDuration += i * presentValue / bondPrice

    bondDuration /= ppy

    return bondDuration

# getBondPrice function
def getBondPrice(y, face, couponRate, m, ppy=1):
    """
    Calculates the price of a bond.

    Args:
        y (float): Yield to maturity
        face (float): Face value of the bond
        couponRate (float): Annual coupon rate
        m (int): Years to maturity
        ppy (int, optional): Number of coupon payments per year. Defaults to 1.

    Returns:
        float: The price of the bond.
    """
    n = m * ppy
    c = face * couponRate / ppy

    bondPrice = 0
    for i in range(1, n+1):
        if i == n:
            pmt = c + face
        else:
            pmt = c
        presentValue = pmt / ((1 + y / ppy) ** i)
        bondPrice += presentValue

    return bondPrice

# Test Values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

bondDuration = getBondDuration(y, face, couponRate, m, ppy)
print("Bond duration with ppy = 1:", bondDuration)

ppy = 2

bondDuration = getBondDuration(y, face, couponRate, m, ppy)
print("Bond duration with ppy = 2:", bondDuration)
