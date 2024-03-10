def calculateDiscount(price, discountPercent):
    if discountPercent >= 20:
        discount = price * (discountPercent/100)
        finalPrice = price - discount
        return finalPrice
    
    else:
        return price
    
originalPrice = float(input("Enter Item Price:"))
discountPercent =  float(input("Enter discount Percent on item"))

finalPrice = calculateDiscount(originalPrice, discountPercent)

if finalPrice == originalPrice:
    print("No Discount For This Item:", finalPrice)
else:
    print("Final price after applying {}%  discount: {:.2f}".format (discountPercent, finalPrice))
