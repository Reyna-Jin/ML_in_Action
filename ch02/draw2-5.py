import KNN
# from numpy import *
import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
group,labels=KNN.createDataSet()
datingDataMat,datingLabels=KNN.file2matrix('datingTestSet2.txt')
fig=plt.figure()
ax=fig.add_subplot(111)
# ax.scatter(datingDataMat[:,1],datingDataMat[:,2])
datingLabels=np.array(datingLabels)
idx_1=np.where(datingLabels==1)
p1=ax.scatter(datingDataMat[idx_1,0],datingDataMat[idx_1,1],marker='*',color='r',label='1',s=10)
idx_2=np.where(datingLabels==2)
p2=ax.scatter(datingDataMat[idx_2,0],datingDataMat[idx_2,1],marker='o',color='g',label='2',s=20)
idx_3=np.where(datingLabels==3)
p3=ax.scatter(datingDataMat[idx_3,0],datingDataMat[idx_3,1],marker='+',color='b',label='3',s=30)
plt.xlabel("每年获取的飞行里程数",fontproperties=font)
plt.ylabel("玩视频游戏所消耗的事件百分比",fontproperties=font)
ax.legend([p1,p2,p3],["不喜欢","魅力一般","极具魅力"],loc=2,prop=font)
plt.show()