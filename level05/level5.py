#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''python challenge level 5
question url: http://www.pythonchallenge.com/pc/def/peak.html
answer url: http://www.pythonchallenge.com/pcc/def/channel.html
'''

import pickle
info = pickle.loads('''(lp1
(lp1
(S' '
p2
I95
tp3
aa(lp4
(g2
I14
tp5
a(S'#'
p6
I5
tp7
a(g2
I70
tp8
a(g6
I5
tp9
a(g2
I1
tp10
aa(lp11
(g2
I15
tp12
a(g6
I4
tp13
a(g2
I71
tp14
a(g6
I4
tp15
a(g2
I1
tp16
aa(lp17
(g2
I15
tp18
a(g6
I4
tp19
a(g2
I71
tp20
a(g6
I4
tp21
a(g2
I1
tp22
aa(lp23
(g2
I15
tp24
a(g6
I4
tp25
a(g2
I71
tp26
a(g6
I4
tp27
a(g2
I1
tp28
aa(lp29
(g2
I15
tp30
a(g6
I4
tp31
a(g2
I71
tp32
a(g6
I4
tp33
a(g2
I1
tp34
aa(lp35
(g2
I15
tp36
a(g6
I4
tp37
a(g2
I71
tp38
a(g6
I4
tp39
a(g2
I1
tp40
aa(lp41
(g2
I15
tp42
a(g6
I4
tp43
a(g2
I71
tp44
a(g6
I4
tp45
a(g2
I1
tp46
aa(lp47
(g2
I15
tp48
a(g6
I4
tp49
a(g2
I71
tp50
a(g6
I4
tp51
a(g2
I1
tp52
aa(lp53
(g2
I6
tp54
a(g6
I3
tp55
a(g2
I6
tp56
a(g6
I4
tp57
a(g2
I3
tp58
a(g6
I3
tp59
a(g2
I9
tp60
a(g6
I3
tp61
a(g2
I7
tp62
a(g6
I5
tp63
a(g2
I3
tp64
a(g6
I3
tp65
a(g2
I4
tp66
a(g6
I5
tp67
a(g2
I3
tp68
a(g6
I3
tp69
a(g2
I10
tp70
a(g6
I3
tp71
a(g2
I7
tp72
a(g6
I4
tp73
a(g2
I1
tp74
aa(lp75
(g2
I3
tp76
a(g6
I3
tp77
a(g2
I3
tp78
a(g6
I2
tp79
a(g2
I4
tp80
a(g6
I4
tp81
a(g2
I1
tp82
a(g6
I7
tp83
a(g2
I5
tp84
a(g6
I2
tp85
a(g2
I2
tp86
a(g6
I3
tp87
a(g2
I6
tp88
a(g6
I4
tp89
a(g2
I1
tp90
a(g6
I7
tp91
a(g2
I3
tp92
a(g6
I4
tp93
a(g2
I1
tp94
a(g6
I7
tp95
a(g2
I5
tp96
a(g6
I3
tp97
a(g2
I2
tp98
a(g6
I3
tp99
a(g2
I5
tp100
a(g6
I4
tp101
a(g2
I1
tp102
aa(lp103
(g2
I2
tp104
a(g6
I3
tp105
a(g2
I5
tp106
a(g6
I3
tp107
a(g2
I2
tp108
a(g6
I5
tp109
a(g2
I4
tp110
a(g6
I4
tp111
a(g2
I3
tp112
a(g6
I3
tp113
a(g2
I3
tp114
a(g6
I4
tp115
a(g2
I4
tp116
a(g6
I5
tp117
a(g2
I4
tp118
a(g6
I4
tp119
a(g2
I2
tp120
a(g6
I5
tp121
a(g2
I4
tp122
a(g6
I4
tp123
a(g2
I3
tp124
a(g6
I3
tp125
a(g2
I5
tp126
a(g6
I3
tp127
a(g2
I3
tp128
a(g6
I4
tp129
a(g2
I1
tp130
aa(lp131
(g2
I1
tp132
a(g6
I3
tp133
a(g2
I11
tp134
a(g6
I4
tp135
a(g2
I5
tp136
a(g6
I4
tp137
a(g2
I3
tp138
a(g6
I3
tp139
a(g2
I4
tp140
a(g6
I3
tp141
a(g2
I4
tp142
a(g6
I4
tp143
a(g2
I5
tp144
a(g6
I4
tp145
a(g2
I2
tp146
a(g6
I4
tp147
a(g2
I5
tp148
a(g6
I4
tp149
a(g2
I2
tp150
a(g6
I3
tp151
a(g2
I6
tp152
a(g6
I4
tp153
a(g2
I2
tp154
a(g6
I4
tp155
a(g2
I1
tp156
aa(lp157
(g2
I1
tp158
a(g6
I3
tp159
a(g2
I11
tp160
a(g6
I4
tp161
a(g2
I5
tp162
a(g6
I4
tp163
a(g2
I10
tp164
a(g6
I3
tp165
a(g2
I4
tp166
a(g6
I4
tp167
a(g2
I5
tp168
a(g6
I4
tp169
a(g2
I2
tp170
a(g6
I4
tp171
a(g2
I5
tp172
a(g6
I4
tp173
a(g2
I2
tp174
a(g6
I3
tp175
a(g2
I7
tp176
a(g6
I3
tp177
a(g2
I2
tp178
a(g6
I4
tp179
a(g2
I1
tp180
aa(lp181
(g6
I4
tp182
a(g2
I11
tp183
a(g6
I4
tp184
a(g2
I5
tp185
a(g6
I4
tp186
a(g2
I5
tp187
a(g6
I2
tp188
a(g2
I3
tp189
a(g6
I3
tp190
a(g2
I4
tp191
a(g6
I4
tp192
a(g2
I5
tp193
a(g6
I4
tp194
a(g2
I2
tp195
a(g6
I4
tp196
a(g2
I5
tp197
a(g6
I4
tp198
a(g2
I1
tp199
a(g6
I4
tp200
a(g2
I7
tp201
a(g6
I3
tp202
a(g2
I2
tp203
a(g6
I4
tp204
a(g2
I1
tp205
aa(lp206
(g6
I4
tp207
a(g2
I11
tp208
a(g6
I4
tp209
a(g2
I5
tp210
a(g6
I4
tp211
a(g2
I3
tp212
a(g6
I10
tp213
a(g2
I4
tp214
a(g6
I4
tp215
a(g2
I5
tp216
a(g6
I4
tp217
a(g2
I2
tp218
a(g6
I4
tp219
a(g2
I5
tp220
a(g6
I4
tp221
a(g2
I1
tp222
a(g6
I14
tp223
a(g2
I2
tp224
a(g6
I4
tp225
a(g2
I1
tp226
aa(lp227
(g6
I4
tp228
a(g2
I11
tp229
a(g6
I4
tp230
a(g2
I5
tp231
a(g6
I4
tp232
a(g2
I2
tp233
a(g6
I3
tp234
a(g2
I4
tp235
a(g6
I4
tp236
a(g2
I4
tp237
a(g6
I4
tp238
a(g2
I5
tp239
a(g6
I4
tp240
a(g2
I2
tp241
a(g6
I4
tp242
a(g2
I5
tp243
a(g6
I4
tp244
a(g2
I1
tp245
a(g6
I4
tp246
a(g2
I12
tp247
a(g6
I4
tp248
a(g2
I1
tp249
aa(lp250
(g6
I4
tp251
a(g2
I11
tp252
a(g6
I4
tp253
a(g2
I5
tp254
a(g6
I4
tp255
a(g2
I1
tp256
a(g6
I4
tp257
a(g2
I5
tp258
a(g6
I3
tp259
a(g2
I4
tp260
a(g6
I4
tp261
a(g2
I5
tp262
a(g6
I4
tp263
a(g2
I2
tp264
a(g6
I4
tp265
a(g2
I5
tp266
a(g6
I4
tp267
a(g2
I1
tp268
a(g6
I4
tp269
a(g2
I12
tp270
a(g6
I4
tp271
a(g2
I1
tp272
aa(lp273
(g2
I1
tp274
a(g6
I3
tp275
a(g2
I11
tp276
a(g6
I4
tp277
a(g2
I5
tp278
a(g6
I4
tp279
a(g2
I1
tp280
a(g6
I4
tp281
a(g2
I5
tp282
a(g6
I3
tp283
a(g2
I4
tp284
a(g6
I4
tp285
a(g2
I5
tp286
a(g6
I4
tp287
a(g2
I2
tp288
a(g6
I4
tp289
a(g2
I5
tp290
a(g6
I4
tp291
a(g2
I2
tp292
a(g6
I3
tp293
a(g2
I12
tp294
a(g6
I4
tp295
a(g2
I1
tp296
aa(lp297
(g2
I2
tp298
a(g6
I3
tp299
a(g2
I6
tp300
a(g6
I2
tp301
a(g2
I2
tp302
a(g6
I4
tp303
a(g2
I5
tp304
a(g6
I4
tp305
a(g2
I2
tp306
a(g6
I3
tp307
a(g2
I4
tp308
a(g6
I4
tp309
a(g2
I4
tp310
a(g6
I4
tp311
a(g2
I5
tp312
a(g6
I4
tp313
a(g2
I2
tp314
a(g6
I4
tp315
a(g2
I5
tp316
a(g6
I4
tp317
a(g2
I3
tp318
a(g6
I3
tp319
a(g2
I6
tp320
a(g6
I2
tp321
a(g2
I3
tp322
a(g6
I4
tp323
a(g2
I1
tp324
aa(lp325
(g2
I3
tp326
a(g6
I3
tp327
a(g2
I4
tp328
a(g6
I2
tp329
a(g2
I3
tp330
a(g6
I4
tp331
a(g2
I5
tp332
a(g6
I4
tp333
a(g2
I3
tp334
a(g6
I11
tp335
a(g2
I3
tp336
a(g6
I4
tp337
a(g2
I5
tp338
a(g6
I4
tp339
a(g2
I2
tp340
a(g6
I4
tp341
a(g2
I5
tp342
a(g6
I4
tp343
a(g2
I4
tp344
a(g6
I3
tp345
a(g2
I4
tp346
a(g6
I2
tp347
a(g2
I4
tp348
a(g6
I4
tp349
a(g2
I1
tp350
aa(lp351
(g2
I6
tp352
a(g6
I3
tp353
a(g2
I5
tp354
a(g6
I6
tp355
a(g2
I4
tp356
a(g6
I5
tp357
a(g2
I4
tp358
a(g6
I2
tp359
a(g2
I4
tp360
a(g6
I4
tp361
a(g2
I1
tp362
a(g6
I6
tp363
a(g2
I4
tp364
a(g6
I11
tp365
a(g2
I4
tp366
a(g6
I5
tp367
a(g2
I6
tp368
a(g6
I3
tp369
a(g2
I6
tp370
a(g6
I6
tp371
aa(lp372
(g2
I95
tp373
aa.
''')
for line in info:
    #print ''.join(map(lambda i:i[0]*i[1], line))
    print ''.join([x[0] * x[1] for x in line])

