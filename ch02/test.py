import KNN
from numpy import *
import operator

#######################################
# 约会网站预测
#
# datingDataMat,datingLabels=KNN.file2matrix('datingTestSet2.txt')
# normMat,ranges,minVals=KNN.autoNorm(datingDataMat)
# print("normMat")
# print (normMat)
# # print('\n')
# print("ranges: ")
# print(ranges)
# print("minVals")
# print(minVals)

# print(KNN.classifyPerson())

#########################################
#
#
# testVector=KNN.img2vector('testDigits/0_13.txt')
# print(testVector[0,0:31])
# print(testVector[0,32:63])

KNN.handwritingClassTest()