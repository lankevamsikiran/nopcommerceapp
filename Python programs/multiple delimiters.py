

# Using any number as delimiter

import re
st="Wel7come To H8CL jwaszdf  6rt6dg f6rth f5h e0errf gb2 "

#['Wel', 'come To H', 'CL']

print(re.split('\d+', st))