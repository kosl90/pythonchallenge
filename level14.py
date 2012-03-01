#! /usr/bin/env python
'''python challenge level 14
question url: http://www.pythonchallenge.com/pc/return/italy.html
answer url: http://www.pythonchallenge.com/pcc/return/uzi.html
'''

l = [[i, i - 1 , i - 1, i - 2] for i in xrange(100, 1, -2)]
l = reduce(lambda x, y: x+y, l)
# print l, len(l)

import Image
w = Image.open('level14.d/wire.png')
w_data = list(w.getdata())
res = Image.new(w.mode, (100, 100))
res_data = res.load()

# (0,0)
#    ---->x
#    |
#    vy
dire = [(1, 0),  # > (x+1, y) right
        (0, 1),  # v (x, y+1) down
        (-1, 0),  # < (x-1, y) left
        (0, -1),  # ^ (x, y-1) up
        ]

# init
v = 0
w_index = 0
res_pos = (-1, 0)
for times in l:
    for i in xrange(times):
        # pos will out of index if reset position after setting color
        res_pos = tuple(map(lambda x, y: x + y, res_pos, dire[v]))
        # f = open('level14.d/log.log','a')
        # print >> f, pos
        # f.close()
        res_data[res_pos] = w_data[w_index]
        w_index += 1

    v = (v + 1) % 4  # j + 1 if j != 4 else 0

res.save('level14.d/res.png')
