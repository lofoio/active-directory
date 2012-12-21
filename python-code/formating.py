#!/usr/bin/python
def doFilter():
    f = open("t.txt")
    groups = {}
    result = []
    dict = set(['GTAG','ATAC','GCAG'])
    try:
        rows = [x.replace("\n","") for x in f.readlines()]
        for r in rows:
            key = r.split("\t")[0]
            if (not groups.has_key(key)):
                groups[key] = []
            groups[key].append(r)
        keys = groups.keys()
        for k in keys:
            maxl = max(groups[k], key=lambda x: x.split("\t")[2])
            result.append(maxl)
            for l in groups[k]:
                diff = float(l.split("\t")[2]) - float(maxl.split("\t")[2])
                if(diff >0 and diff <= 10 and len(set(l.split("\t")[3].split(","))-dict)==0):
                    result.append(l)
        for i in result:
            print i


    finally:
        f.close()

doFilter()
