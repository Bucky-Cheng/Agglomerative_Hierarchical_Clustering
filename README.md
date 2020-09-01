Agglomerative hierarchical clustering

Unsupervised learning




A. Instructions of program

Environment: macOS Catalina 10.15

Python Version: Python 3.7.5

IDE: PyCharm 2019.2.5(Professional Edition)

Runnig Command Line: python3 AHC.py SCOV2_96_matrix.txt

The output is the contents and heatmap figures of K=2,3,4,5 clusters. Notice, the program will show the contents and heatmap figure of K=2 clusters firstly, and close the figure, the contents and heatmap figures of next K clusters will be showing.



B. Description about generate different number of clusters

Put the cluster result of every merge into a list, and K=1 cluster is the last object in list, K=2 clusters are second-last object in list, K=3 clusters is third-last object in list. Generate a loop and loop parameter K form 2 to 5, 2 clusters are list[list.length-2], 3 clusters are list[list.length-3], so 2-5cluster is list[list.length-k]
