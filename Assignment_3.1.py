hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
	h = float(hrs)
	r = float(rate)
except:
	print("Error, please enter numeric input")
	quit()

if h > 40 :
	extra_h = h - 40
	extra_pay = extra_h*r*1.5
	full_pay = extra_pay + (h - extra_h)*r
	print(full_pay)
else :
    full_pay = float(hrs)*float(rate)
    print(full_pay)

score = input("Enter Score: ")
