import sys
import numpy


matrix_list = []
matrix_width=0
maximum=0
result_list=[]

with open('SCOV2_96_matrix.txt','r')as f:
    line = f.readline();

    while line:
        #line = line.rstrip('\t')
        #print(line)
        line = line.strip('\t')
        # print(line)
        m_line = line.split()
        matrix_list.append(m_line)
        line = f.readline()

matrix_width=matrix_list[0].__len__()
sim_matrix=numpy.zeros(shape=(matrix_width,matrix_width),dtype=float)

for i in range(1,matrix_width+1):

    for j in range(1,matrix_width+1):

        sim_matrix[i-1][j-1]=matrix_list[i][j]


print(sim_matrix.__len__())



def Clustering():
    print('a')

    for i in range(1,matrix_width+1):
        for j in range(0,i):
            if sim_matrix[i][j]>maximum:
                maximum=sim_matrix[i][j]





while sim_matrix.__len__()!=1:
    maximum=0;
    Clustering()