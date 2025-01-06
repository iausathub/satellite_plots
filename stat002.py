import numpy as np
import matplotlib.pyplot as plt

# Following https://stackoverflow.com/questions/51086732/how-can-i-remove-the-negative-sign-from-y-tick-labels-in-matplotlib-pyplot-figur
def major_formatter(x, pos):
    label = str(-int(x)) if x < 0 else str(int(x))
    return label

# Using the data from https://planet4589.org/space/stats/out/stat002.txt via https://planet4589.org/space/stats/active.html
null, year, acm, acn, star, stard, pl, px, rb, part, debasat, debcoll, deb, null, null = np.loadtxt('stat002.txt',unpack=True)

numyears = len(year)
active = np.zeros(numyears)
dead = np.zeros(numyears)
leftovers = np.zeros(numyears)
debris = np.zeros(numyears)
starlink = np.zeros(numyears)
for i in range(0,numyears):
	starlink[i] = star[i] + stard[i]
	active[i] = acm[i] + acn[i]
	dead[i] = pl[i] + px[i]
	leftovers[i] = rb[i] + part[i]
	debris[i] = debasat[i] + debcoll[i] + deb[i]

# plt.style.use('classic')

# plt.figure(figsize=(13.0, 6.0), dpi=300)
fig, ax = plt.subplots(figsize=(6.0, 4.0), dpi=300)
ax.ticklabel_format(style='plain')
ax.ticklabel_format(useOffset=False)
ax.fill_between(year,leftovers+dead+active+starlink,leftovers+dead+active,label='Starlink',color='tab:purple')
ax.fill_between(year,leftovers+dead+active,leftovers+dead,label='Active',color='tab:green')
ax.fill_between(year,leftovers+dead,leftovers,label='Dead',color='tab:red')
ax.fill_between(year,leftovers,0,label='Leftovers',color='tab:orange')
ax.fill_between(year,0,-debris,label='Tracked Debris',color='tab:blue')
plt.xlim(1957,2025)
# plt.ylim(0,20000)
ax.yaxis.set_major_formatter(major_formatter)
plt.xlabel('Year', fontsize=11)
plt.ylabel('Count', fontsize=11)
l = plt.legend(prop={'size':11})
l.set_zorder(20)
plt.tight_layout()
# plt.savefig('stat002.png')
plt.savefig('stat002.jpg')
# plt.savefig('stat002.pdf')
print(starlink)
print(active+starlink)