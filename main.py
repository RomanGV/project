
import translit_parser as tp
import translit as tr
import dictionary_parser as dp
from sys import argv

script, one, *args = argv

# 1
if one == '-translate_er':
    strin = ' '.join(argv[2:])
    strin2 = dp.remove_punctuation(strin)
    word_dict = dict(dp.en_ru)
    strin2 = strin2.lower().split()
    out = ''
    for t in range(len(strin2)):
        try:
            out += ' ' + word_dict[strin2[t]]
        except KeyError:
            out += ' ' + strin2[t]
    print(out)

# 2

if one == '-translate_re':
    strin3 = ' '.join(argv[2:])
    strin4 = dp.remove_punctuation(strin3)
    word_dict2 = dict(dp.en_ru)
    word_dict3 = dict(zip(word_dict2.values(), word_dict2.keys()))
    strin4 = strin4.lower().split()
    out = ''
    for t in range(len(strin4)):
        try:
            out += ' ' + word_dict3[strin4[t]]
        except KeyError:
            out += ' ' + strin4[t]
    print(out)

# 3

if one == '-translit_re':
    out2 = ''
    dic1 = dict(zip(tp.t_list[::2], tp.t_list[1::2]))
    dic1.pop('Ь')
    dic1.pop('Ъ')
    dic2 = {'С': 'S', 'Т': 'T', 'А': 'A', 'Ь': '', 'Ъ': ''}
    dic1.update(dic2)
    stri2 = ' '.join(argv[2:])
    for t in range(len(stri2)):
        try:
            out2 += dic1[stri2[t].upper()]
        except KeyError:
            out2 += stri2[t]
    print(out2.lower())

# 4

if one == '-translit_er':
    out3 = ''
    stri3 = ' '.join(argv[2:])
    for t in range(len(stri3)):
        # out3+=tr.er[stri[t].lower()]
        try:
            out3 += tr.er[stri3[t].lower()]
        except KeyError:
            out3 += stri3[t]
    print(out3.lower())
