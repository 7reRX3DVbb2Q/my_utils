#!/usr/bin/env python3
import re
import urllib.request


epg = urllib.request.urlopen('http://epg.team/tvteam.0.7.xml')
line = epg.readline()
pattern = '(&lt;br&gt;Category:)+\s*([-A-zА-я]{3,}){1}(,rb )?([-A-zА-я]{3,})?;?<\/desc>'

file = open('epg.xml', 'w')

while (line):
    line = epg.readline().decode('utf-8')
    search = re.search(pattern, line)
    if(search):
        start, stop = search.span()
        line = line[:start] + '</desc><category>' + search.group(2) + '</category>' + line[stop:]
    file.write(line + "\n")
print('Success')
file.close()




