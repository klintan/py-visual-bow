"""
===========================================
6. Create HTML and JSON views for closest matching images
===========================================

"""
import sys
sys.path.append('utils')
import imtools
import pickle
import cPickle
import numpy as np



f = open(sys.argv[1]+'_comparison.pickle', 'r')

all_dist = []
while 1:
    try:
        all_dist.append(pickle.load(f))
    except EOFError:
        break

f.close()
path = sys.argv[1]

html = '<html><head></head><body>'
json = []

im_list = imtools.get_imlist(path)

for idx,dist in enumerate(all_dist):
    sort_index = np.argsort(dist)
    top20 = sort_index[0:20]
    json.append({"img":"","similar":[]})
    html+="<p>"+str(idx)+"</p>"

    for idy,image in enumerate(top20):
        print json[idx]['img']
        print image
        if idy == 0:
            json[idx]['img'] = im_list[image];
            continue

        html += '<img src='+ im_list[image]+'>'
        json[idx]['similar'].append({"img":im_list[image],"pattern": str(dist[image]),"color":""})


    html += '<hr>'
    if idx == 1000:
        break


html += '</body></html>'
print json
f1 = open(sys.argv[1]+'.html', 'wb')
cPickle.dump(html,f1)
f1.close()
