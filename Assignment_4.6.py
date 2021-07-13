hrs = input("Enter Hours:")
rate = input("Enter Rate:")

h = float(hrs)
r = float(rate)

def computepay(h,r):
    if h > 40 :
        extra_h = (h - 40)
        extra_pay = extra_h*r*1.5
        full_pay = extra_pay + (h - extra_h)*r
    else :
        full_pay = h*r
    return full_pay

p = computepay(h,r)
print("Pay",p)
