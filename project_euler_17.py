# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

def int2num(n):
    """ takes in an integer and returns an alpha representation """

    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five', \
            6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten', \
            11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen', \
            15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', \
            19 : 'ninteen', 20 : 'twenty', \
            30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty', \
            70 : 'seventy', 80 : 'eighty', 90 : 'ninty' }
    k = 1000
    h = 100

    if n == k:
        return 'onethousand'

    if n == h:
        return 'onehundred'

    if n < 20:
        return d[n]

    if n < h:
        return d[n - n%10] + (d[n%10] if d[n%10] != 'zero' else '')

    if n > 100 < 1000:
        l = n%100
        if l < 20:
            l = d[l]
        else:
            l = d[l - l%10] + (d[l%10] if d[l%10] != 'zero' else '')
        
        return d[n//100] + 'hundredand' + l #d[n%10] #+ d[n%100]

c = 0
for i in range(1, 1001):
    c += len(int2num(i))
print(c) # 21070
