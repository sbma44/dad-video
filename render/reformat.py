import sys, json, re
from collections import defaultdict

def rec_dd():
    return defaultdict(rec_dd)

re_date = re.compile(r'^(.*?)(\d\d\d\d\.\d\d\.\d\d)_(\d\d-\d\d-\d\d)\.avi\.log')

with open(sys.argv[1]) as f:
    obj = json.load(f)

out = rec_dd()

for k in obj:
    m = re_date.match(k)
    if m is not None:
        out[m.group(1)][m.group(2)][m.group(3)] = obj[k]

print(json.dumps(out, indent=2))