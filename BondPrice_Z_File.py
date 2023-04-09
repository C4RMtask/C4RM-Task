# getBondPrice_Z function
def getBondPrice_Z(face, couponRate, times, yc):
    """
    Calculates the price of a bond using the given zero-coupon yield curve.

    Args:
        face (float): Face value of the bond.
        couponRate (float): Annual coupon rate.
        times (list): List of coupon payment times in years, including maturity.
        yc (list): Zero-coupon yield curve as a list of yields for each year from now until maturity.

    Returns:
        float: The price of the bond.
    """
    bondPrice = 0
    c = face * couponRate
    for t, y in zip(times, yc):
        pmt = c if t != times[-1] else c + face
        presentValue = pmt / ((1 + y) ** t)
        bondPrice += presentValue

    return bondPrice

#Test Values
yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04

bondPrice = getBondPrice_Z(face, couponRate, times, yc)
print("Bond price:", bondPrice)
