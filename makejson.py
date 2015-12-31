import os, json, os.path

out = {}
for fn in os.listdir('./logs'):
  max_img = 1
  while True:
    check = './thumbs/%s_%03d.jpg' % (fn.replace('.avi.log',''), max_img)
    #print(check)
    if not os.path.exists(check):
      break
    max_img += 1
  with open('./logs/%s' % fn) as f2:
    out[fn] = (f2.read().strip(), max_img-1)

print(json.dumps(out))
