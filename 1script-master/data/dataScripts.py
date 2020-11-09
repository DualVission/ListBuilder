import glob
from collections import OrderedDict

from data.itemTypes import *
from data.format import *

def stripItemName(itemNames):
  newNames = []
  newPaths = []

  for item in itemNames:
    newPath = (item.split(".w"))[0]
    newPaths.append(newPath)
    newName = (newPath.split("/"))[-1]
    newNames.append(newName)

  return newNames, newPaths

def getItemImage(itemPaths):
  itemImages = []
  itemLinks = []
  for item in itemPaths:
    itemGlob = glob.glob(item+".*")
    itemTest = []
    for key in fileList:
      itemBump = glob.glob(item+key)
      for bump in itemBump:
        itemTest.append(bump)
    for path in itemGlob:
      if(path not in itemTest):
        itemImages.append(path)
      else:
        itemLinks.append(path)
  return itemImages, itemLinks

def getItems(*args):
  folderList = glob.glob("../*/")
  itemList = []

  for folder in folderList:
    if(folder in ignoreList):
      pass
    else:
      for key in fileList:
        itemGlob = glob.glob(folder+"*"+key)
        for item in itemGlob:
          itemList.append(item)

  itemNames, itemPaths = stripItemName(itemList)
  itemImages, itemLinks = getItemImage(itemPaths)
  throwList = [itemNames,itemPaths,itemImages,itemLinks]
  itemDict = OrderedDict()
  for name in itemNames:
    i = itemNames.index(name)
    iDict = OrderedDict()
    #print("{} {} {}\n".format(itemPaths[i],itemImages[i],itemLinks[i]))
    iDict["Path"] = itemPaths[i]
    type = (itemPaths[i].split("/"))[1]
    iDict["Type"] = typeDict[type]
    iDict["Image"] = itemImages[i]
    iDict["Raw Link"] = itemLinks[i]
    iDict["Valid"] = True
    #print(str(iDict))
    itemDict[name] = iDict

  return itemDict

def getItemData(itemDict):

  dataNames = "./data/cleanNames.txt"
  cleanItemData = OrderedDict()
  cleanLines = []
  keyTest = []
  rewrite = 0

  with open(dataNames, "rt") as f:
    for lines in f:
      cleanLines.append(lines)
  for line in cleanLines:
    lineData = OrderedDict()
    data = line.split("|")
    itemDict[data[0]]["Name"] = data[1]
    lineData["Name"] = data[1]
    try:
      itemDict[data[0]]["Price"] = float(data[2])
      lineData["Price"] = float(data[2])
    except:
      pass
    if((data[3]).lower() == "true"):
      itemDict[data[0]]["Shipping"] = True
      lineData["Shipping"] = True
    elif((data[3]).lower() == "false"):
      itemDict[data[0]]["Shipping"] = False
      lineData["Shipping"] = False
    else:
      itemDict[data[0]]["Shipping"] = False
      lineData["Shipping"] = False
    cleanItemData[data[0]] = lineData
    keyTest.append(data[0])

  for key in cleanItemData:
    if(key not in keyTest):
      rewrite+=1
      print("The following item, {0}, was not found in your clean names file, {1}".format(name,dataNames))
      lineData = OrderedDict()
      lineData["Name"] = "UPDATE"
      lineData["Price"] = "0.00"
      lineData["Shipping"] = "false"
      cleanItemData[name] = lineData
    else:
      pass

  if(rewrite>0):
    newValues = []
    for key in cleanItemData:
      name = cleanItemData[key]["Name"]
      pric = cleanItemData[key]["Price"]
      ship = cleanItemData[key]["Shipping"]
      newValues.append("{0}|{1}|{2}|{3}|\n".format(key,name,pric,ship))
    with open(dataNames,"wt") as g:
      for line in newValues:
        g.write(line)

  return itemDict, cleanItemData
