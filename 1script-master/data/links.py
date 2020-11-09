import glob
from collections import OrderedDict
import xml.etree.ElementTree as eTree

from data.format import *

def scrubWebloc(itemDict):
  linkDict = OrderedDict()
  for key in itemDict:
    tree = eTree.parse(itemDict[key]["Raw Link"])
    root = tree.getroot()
    elem = root[0][1].text
    linkDict[key] = elem
  return linkDict

def scrubUrl(itemDict):
  linkDict = OrderedDict()
  txtDoc = []
  for key in itemDict:
    with open(itemDict[key]["Raw Link"]) as f:
      for lines in f:
        txtDoc.append(lines)
    urlLine = txtDoc.index("URL=*")
    exec(txtDoc[urlLine])
    linkDict[key] = URL
  return linkDict

def scrubRawLink(itemDict):
  urlDict = OrderedDict()
  webDict = OrderedDict()
  dictList = [webDict, urlDict]
  testKeys = []
  for key in itemDict:
    for i in range(0,2):
      #print(itemDict[key]["Raw Link"])
      #print(str(i))
      ext = fileExtList[i]
      lng = fileList[ext]
      if(itemDict[key]["Raw Link"][lng:]==ext[lng:]):
        dictList[i][key] = itemDict[key]
        testKeys.append(key)
      elif(key in testKeys):
        continue
      else:
        print("Something unexpected occured with item {}.".format(key))
  linkDict = scrubUrl(urlDict)
  for key in linkDict:
    itemDict[key] = linkDict[key]
  linkDict = scrubWebloc(webDict)
  for key in linkDict:
    itemDict[key]["Link"] = linkDict[key]
  return itemDict
