import json,sys
# args: pid upd img_id name w h x y scale src_uuid
pid,upd,iid,name,w,h,x,y,s,src=sys.argv[1:11]
en=[109124,109128,109129]
TT={109123:"Dark Purple",109124:"Iron Gray",109125:"Black",109126:"Coral",109127:"Green",109128:"Light Blue",109129:"Light Purple",109130:"Maroon"}
mv="109128"
if len(sys.argv)>11:
    en=[int(v) for v in sys.argv[11].split(",")]; mv=sys.argv[12]
print(json.dumps({"pid":pid,"bp":1515,"pp":217,"upd":upd,"vis":True,
 "mock":"https://images.printify.com/mockup/%s/%s/144651/x.jpg?camera_label=front"%(pid,mv),"en":en,
 "svgs":{str(v):"6a7f0c1f23dff1e1b50504a0" for v in en},
 "areas":[{"pos":"drinkware_front","deco":"engraving","vids":list(range(109123,109139)),"img":[iid,name,int(w),int(h),float(x),float(y),float(s),0,src]}],
 "extra":{"unavailable_enabled":[],"enabled_titles":{str(v):"12oz / "+TT[v] for v in en}}}))
