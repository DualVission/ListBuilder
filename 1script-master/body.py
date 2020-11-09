import glob
from collections import OrderedDict

from data.dataScripts import *
from data.links import *

itemDict = getItems()
itemDict, cleanItemData = getItemData(itemDict)
itemDict = scrubRawLink(itemDict)
itemDict = OrderedDict(sorted(itemDict.items(), key=lambda t: t[1]["Name"][-1]))
itemDict = OrderedDict(sorted(itemDict.items(), key=lambda t: t[1]["Name"][0]))
itemDict = OrderedDict(sorted(itemDict.items(), key=lambda t: t[1]["Type"][0]))

def getShipping(item):
  isFree = ""
  if(not item["Shipping"]):
    isFree = "+Shipping"
  return isFree

'''
for key in itemDict:
  print("\nkey: {}\n\tName: {}\n\tLink: {}\n".format(key,itemDict[key]["Name"],itemDict[key]["Link"]))
'''
