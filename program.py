from re import A


def sold_sale(sold, sale):
    sold = abs(sold)
    sale = abs(sale)
    return sold if sale >= 100 else sold - sold * sale / 100

one = 100
two = 200
three = 300
sale = 10
print(sold_sale(one, sale))
print(sold_sale(two, sale))
print(sold_sale(three, sale))
print(sold_sale(-1000, 99))