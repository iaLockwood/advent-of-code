import re
rkeys = {
'byr': r'^19[2-9][0-9]|200[0-2]$',
'iyr': r'^201[0-9]|2020$',
'eyr': r'^202[0-9]|2030$',
'hgt': r'^(?:1[5-8][0-9]|19[0-3])cm|(?:59|6[0-9]|7[0-6])in$',
'hcl': r'^#[0-9,a-f]{6}$',
'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
'pid': r'^\d{9}$'
}
findvars = r'([a-z]+?):([\S]+)'
with open('input-p4.txt') as f:
raw_passes = f.read().split('\n\n')
passes = [dict(re.findall(findvars, p)) for p in raw_passes]
valids = 0
for p in passes:
if all(re.match(rkeys[k], p.get(k) or '') for k in rkeys):
valids += 1
print(valids)