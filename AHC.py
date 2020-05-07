import sys
import copy
import numpy


matrix_list = []
matrix_width=0
item_list=[]
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

item_list=matrix_list[0]
#print(item_list)
#result_list.append(copy.deepcopy(item_list))

#del item_list[0]
#result_list.append(copy.deepcopy(item_list))

#print(result_list)
matrix_width=matrix_list[0].__len__()
result_list=[]
sim_matrix=numpy.zeros(shape=(matrix_width,matrix_width),dtype=float)

for i in range(1,matrix_width+1):

    for j in range(1,matrix_width+1):

        sim_matrix[i-1][j-1]=matrix_list[i][j]


print(sim_matrix[93][93])



def Clustering():
    print('a')
    maximum = 0
    maximum_r = 0
    maximum_c = 0
    global sim_matrix
    global item_list
    for i in range(0,sim_matrix.__len__()-1):
        for j in range(i+1,sim_matrix.__len__()):
            #print("A"+str(sim_matrix.__len__()))
            if sim_matrix[i][j] != 1:
                if sim_matrix[i][j]>maximum:
                    maximum=sim_matrix[i][j]
                    maximum_r=i
                    maximum_c=j


    for i in range(0, sim_matrix.__len__()):
        new_c=0.0
        new_r=0.0
        print(sim_matrix.__len__())
        print(i)
        if i!=maximum_c and i!=maximum_r:

            if i<maximum_c:
                new_c=sim_matrix[i][maximum_c]
            else:
                new_c=sim_matrix[maximum_c][i]
            if i<maximum_r:
                new_r=sim_matrix[i][maximum_r]
            else:
                new_r=sim_matrix[maximum_r][i]

            new_sim=(new_c+new_r)/(2)

            if i < maximum_r:
                sim_matrix[i][maximum_r]=new_sim
            else:
                sim_matrix[maximum_r][i]=new_sim

    sim_matrix = numpy.delete(sim_matrix, (maximum_c), axis=0)
    sim_matrix = numpy.delete(sim_matrix, (maximum_c), axis=1)
    item_list[maximum_r]=item_list[maximum_r]+"+"+item_list[maximum_c]
    del item_list[maximum_c]








while sim_matrix.__len__()!=1:
    Clustering()
    result_list.append(copy.deepcopy(item_list))


print(result_list[result_list.__len__()-2])