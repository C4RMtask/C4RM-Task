# getBondPrice function
def getBondPrice_E(face, couponRate, m, yc):
    """
    Calculates the price of a bond using the given yield curve.

    Args:
        face (float): Face value of the bond.
        couponRate (float): Annual coupon rate.
        m (int): Years to maturity.
        yc (list): Yield curve as a list of yields for each year from now until maturity.

    Returns:
        float: The price of the bond.
    """
    bondPrice = 0
    c = face * couponRate
    for i, y in enumerate(yc):
        if i == m - 1:
            pmt = c + face
        else:
            pmt = c
        presentValue = pmt / ((1 + y) ** (i + 1))
        bondPrice += presentValue

    return bondPrice

# Test Values
yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5

bondPrice = getBondPrice_E(face, couponRate, m, yc)
print("Bond price:", bondPrice)

