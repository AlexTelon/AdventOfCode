# accumulate trick learned from 4HbQ https://topaz.github.io/paste/#XQAAAQA7AQAAAAAAAAAzHIoib6p4r/McpYgEEgWhHoa5LSRMkLbuJZj6LtAOjHfzzf02mB4dRQBrzlH0+2It4hAK1HNMA7zsaG0mpn5DTV3hIaNixpVJm8WD4hIOThdyrMWcu56/2sI/bC/dpgO0rBvREQkIi2mPA65QImF1AFNy4CtHvk6YZABZhUiFV66tZpYqofStrTdmDrI5rtqSPuiD2EFrPfBgDtuMQHlTxwqoqQHjFKMgIrLP81JfCMNKmO18DBRkDga59Ko/A7fGL23y7a5lVGJvKIlzNJB9wNB/nIjtujeOI/lKmoDxeGobLZHh75vJ//lt85Q=

from itertools import accumulate
import re

nums = map(int,re.sub(r'[noop|addx]+','0', open('input.txt').read()).split())
series = list(enumerate(accumulate(nums, initial=1), start=1))
print('p1', sum(i*x for i,x in series[19:240:40]))
print(''.join([' #'[(i-1) % 40 in [x-1,x,x+1]] + ('\n' if i % 40 == 0 else '') for i, x in series]))
#342

11960
####   ##  ##  #### ###   ##  #    #  #
#       # #  # #    #  # #  # #    #  #
###     # #    ###  #  # #    #    ####
#       # #    #    ###  # ## #    #  #
#    #  # #  # #    #    #  # #    #  #
####  ##   ##  #    #     ### #### #  #



from itertools import*
import re
N=map(int,re.sub(r'[noop|addx]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print('p1',sum(i*x for i,x in S[19:240:40]))
print(''.join([' #'[(i-1)%40 in[x-1,x,x+1]]+('\n'if i%40==0 else'')for i,x in S]))
#279

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print('p1',sum(i*x for i,x in S[19:240:40]))
print(''.join([' #'[(i-1)%40 in[x-1,x,x+1]]+('\n'if i%40==0 else'')for i,x in S]))
#273

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join([' #'[(i-1)%40 in[x-1,x,x+1]]+('\n'if i%40==0 else'')for i,x in S]))
#268 (removed printing p1)

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join([' #'[(i-1)%40-x in[-1,0,1]]+('\n'if i%40==0 else'')for i,x in S]))
# 267

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join(' #'[(i-1)%40-x in[-1,0,1]]+('\n'if i%40==0 else'')for i,x in S))
#265 (removed [] around p2 join call)

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join(' #'[(i-1)%40-x in[-1,0,1]]+(''if i%40 else'\n')for i,x in S))
#262

from itertools import*
import re
N=map(int,re.sub(r'[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join(' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S))
# 256

from itertools import*
import re
N=map(int,re.sub('[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(''.join(' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S))
#255

from itertools import*
import re
N=map(int,re.sub('[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(f"{sum(i*x for i,x in S[19:240:40])}\n"+''.join(' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S))
#254

from itertools import*
import re
N=map(int,re.sub('[a-z]+','0',open('input.txt').read()).split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(*[' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S])
#249 (the output is now different but readable)
11960
# # # #       # #     # #     # # # #   # # #       # #     #         #     #
 #               #   #     #   #         #     #   #     #   #         #     #
 # # #           #   #         # # #     #     #   #         #         # # # #
 #               #   #         #         # # #     #   # #   #         #     #
 #         #     #   #     #   #         #         #     #   #         #     #
 # # # #     # #       # #     #         #           # # #   # # # #   #     #



from itertools import*
N=map(int,open('input.txt').read().replace('noop','0').replace('addx','0').split())
S=[*enumerate(accumulate(N,initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(*[' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S])
#257 (note, this is longer, just wanted to double check without re lib)

from itertools import*
import re
S=[*enumerate(accumulate(map(int,re.sub('[a-z]+','0',open('input.txt').read()).split()),initial=1),1)]
print(sum(i*x for i,x in S[19:240:40]))
print(*[' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S])
#244 now inlining, waited to do this for readability.

from itertools import*
import re
S=[*enumerate(accumulate(map(int,re.sub('[a-z]+','0',open('input.txt').read()).split()),initial=1),1)]
print(*[sum(i*x for i,x in S[19:240:40]),'\n']+[' #'[-2<(i-1)%40-x<2]+(''if i%40 else'\n')for i,x in S])
#243 and now the output is correctly aligned again!
11960
 # # # #       # #     # #     # # # #   # # #       # #     #         #     #
 #               #   #     #   #         #     #   #     #   #         #     #
 # # #           #   #         # # #     #     #   #         #         # # # #
 #               #   #         #         # # #     #   # #   #         #     #
 #         #     #   #     #   #         #         #     #   #         #     #
 # # # #     # #       # #     #         #           # # #   # # # #   #     #


from itertools import*
import re
S=[*enumerate(accumulate(map(int,re.sub('[a-z]+','0',open('input.txt').read()).split()),initial=1),1)]
print(*[sum(i*x for i,x in S[19:240:40]),'\n']+[[' ','#'][-2<(i-1)%40-x<2]for i,x in S])
#227 (only works if you set your terminal width to 80!)

from itertools import*
import re
S=[*enumerate(accumulate(map(int,re.sub('[a-z]+','0',open('input.txt').read()).split()),initial=1),1)]
print(*[sum(i*x for i,x in S[19:240:40]),'\n']+[' #'[-2<(i-1)%40-x<2]for i,x in S])
#222 same as above, terminal width 80 required