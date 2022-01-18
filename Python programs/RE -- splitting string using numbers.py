
import re

Str=" thgfvy4trv6uytcrv6y@utv76uyht6ytxrc5trce65u66y7iu"

print(re.split('\d+',Str))




import re
STRING = "1abc2x30yz67-20"

st=re.split("[^0-9]+",STRING)

print(st)