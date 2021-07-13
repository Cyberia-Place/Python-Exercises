text = "X-DSPAM-Confidence:    0.8475";

extr_value = text[text.find('0'):]

print(float(extr_value))
