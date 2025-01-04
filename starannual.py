import numpy as np
import matplotlib.pyplot as plt

# Using the data from https://planet4589.org/space/stats/out/starannual.txt via https://planet4589.org/space/stats/pay.html
null, year, null, null, acm, acn, star, stard, pl, px, rb, part, debasat, debcoll, deb, null, total = np.loadtxt('starannual.txt',unpack=True)

numyears = len(year)
unmovable = np.zeros(numyears)
active = np.zeros(numyears)
starlink = np.zeros(numyears)
for i in range(1,numyears):
	unmovable[i] = unmovable[i-1] + pl[i] + acn[i]
	active[i] = active[i-1] + acm[i]
	starlink[i] = starlink[i-1] + star[i] + stard[i]

print(year)
print(starlink)
print(active)
print(unmovable)

# plt.style.use('classic')

plt.figure(figsize=(6.1, 5.0), dpi=80)
fig, ax = plt.subplots()
ax.ticklabel_format(style='plain')
ax.ticklabel_format(useOffset=False)
ax.fill_between(year,unmovable,0,label='Non-maneuverable')
ax.fill_between(year,starlink+active+unmovable,active+unmovable,label='Maneuverable')
ax.fill_between(year,active+unmovable,unmovable,label='Starlink')
# ax.plot(year, unmovable, label='Unmovable')
# plt.plot(year, active, label='Active, maneuverable')
# plt.plot(year, starlink, label='Starlink')
plt.xlim(1957,2024)
plt.ylim(0,20000)
plt.xlabel('Year', fontsize=15)
plt.ylabel('Count', fontsize=15)
l = plt.legend(prop={'size':12})
l.set_zorder(20)
plt.savefig('starannual_cul.png')