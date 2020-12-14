#!/usr/bin/env python
# coding: utf-8

import re
import zipfile


with open('./data/cities.txt', 'r', encoding='utf8') as r:
    cities = set([line.strip() for line in r.readlines()])



areas = set()  # 区域
numbers = set()  # 地址番号
details = set()  # 详细地址（楼层，房间号等）




num = '[０１２３４５６７８９]'
num_char = '[一二三四五六七八九十]'
dir_char = '[東南西北]'
hyphen = '[－～]'
tyoume = '丁目?'
banchi = '(?:(?:番地?)?の?)?'


tyoume_pattern_str = '(?:%s|%s)+%s%s?' % (num_char, num, tyoume, dir_char)
print(tyoume_pattern_str)
tyoume_pattern = re.compile(tyoume_pattern_str+'.*$')
num_pattern_str = '%s+(?:%s%s+)*' % (num, hyphen, num)
print(num_pattern_str)
num_pattern = re.compile(num_pattern_str+'.*$')
banchi_pattern_str = '%s%s(?:%s号?)?' % (num_pattern_str, banchi, num_pattern_str)
print(banchi_pattern_str)
banchi_pattern = re.compile(banchi_pattern_str+'.*$')


street_num_1_pattern_str = '^(?:%s)?%s' % (tyoume_pattern_str, banchi_pattern_str)
print('street_num_1_pattern_str: %s' % street_num_1_pattern_str)
street_num_1_pattern = re.compile(street_num_1_pattern_str)
street_num_2_pattern_str = '^%s+(?:%s%s)*' % (num, hyphen, num)
print('street_num_2_pattern_str: %s' % street_num_2_pattern_str)
street_num_2_pattern = re.compile(street_num_2_pattern_str)


with zipfile.ZipFile('data/alldata.zip', 'r') as z:
    for line in z.open('alldata.txt', 'r'):
        line = line.decode('utf8')
        line = line.strip()
        found = False
        for idx in range(5, 14):
            if line[:idx] in cities:
                line = line[idx:]
                found = True
                break
        if not found:
            print('Error, not found city, line is %s' % line)
            break
        
        m = tyoume_pattern.search(line)
        if m is None:
            m = banchi_pattern.search(line)
        if m is None:
            m = num_pattern.search(line)
        
        if m is None:
            if len(line.strip()) > 0:
                areas.add(line)
        else:
            area = line[:m.span()[0]].strip()
            if len(area) > 0:
                areas.add(area)
            other = m.group(0)
            m = street_num_1_pattern.search(other)
            if m is None:
                m = street_num_2_pattern.search(other)
            if m is not None:
                numbers.add(m.group(0))
                detail = other[m.span()[1]:]
                if len(detail) > 0:
                    details.add(detail)
            else:
                details.add(other)



print('len of areas: %d' % len(areas))
print('len of numbers: %d' % len(numbers))
print('len of details: %d' % len(details))



with open('output/areas.txt', 'w', encoding='utf8') as w:
    w.writelines('\n'.join(areas))



with open('output/numbers.txt', 'w', encoding='utf8') as w:
    w.writelines('\n'.join(numbers))


with open('output/details.txt', 'w', encoding='utf8') as w:
    w.writelines('\n'.join(details))

