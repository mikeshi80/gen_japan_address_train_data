import sys
import os
import json

if len(sys.argv) not in (2, 3):
    print("Usage: python trans_labels.py labels.json [labels.txt]")
    sys.exit()

j = json.load(open(sys.argv[1], 'r', encoding='utf8'))

lines = []
output = sys.stdout if len(sys.argv) == 2 else open(sys.argv[2], 'w', encoding='utf8')
for k, v in j['labels'].items():
    lines.append('images/%s.jpg\t%s' % (k, v))

output.writelines('\n'.join(lines))
