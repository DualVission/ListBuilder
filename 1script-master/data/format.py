import glob
from collections import OrderedDict

fileExtList = [".webloc",".url"]
fileList = OrderedDict()
for fileExt in fileExtList:
  fileLen = len(fileExt)*(-1)
  fileList[fileExt] = fileLen
exemptList = ["1script-master"]
formatList = ["../{0}/"]
ignoreList = []
for exemption in exemptList:
  for format in formatList:
    ignoreList.append(format.format(exemption))
