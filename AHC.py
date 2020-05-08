import sys
import copy
import numpy
import matplotlib.pyplot as plt
import seaborn

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



matrix_width=matrix_list[0].__len__()
result_list=[]
count_list=[]
result_count_list=[]
for i in range(0,matrix_width):
    count_list.append([i])

sim_matrix=numpy.zeros(shape=(matrix_width,matrix_width),dtype=float)
copy_matrix=numpy.zeros(shape=(matrix_width,matrix_width),dtype=float)
new_matrix=numpy.zeros(shape=(matrix_width,matrix_width),dtype=float)
for i in range(1,matrix_width+1):

    for j in range(1,matrix_width+1):

        sim_matrix[i-1][j-1]=matrix_list[i][j]
        copy_matrix[i-1][j-1]=matrix_list[i][j]

#print(sim_matrix[93][93])


#start Agglomerative Hierarchical Clustering

def Clustering():
    maximum = 0
    maximum_r = 0
    maximum_c = 0
    global sim_matrix
    global item_list
    global count_list

    #only use right triangle
    #find the max similarity
    for i in range(0,sim_matrix.__len__()-1):
        for j in range(i+1,sim_matrix.__len__()):
            #print("A"+str(sim_matrix.__len__()))
            if sim_matrix[i][j] != 1:
                if sim_matrix[i][j]>maximum:
                    maximum=sim_matrix[i][j]
                    maximum_r=i
                    maximum_c=j

    #calculate average similarity between clusters
    #update sim matrix
    for i in range(0, sim_matrix.__len__()):
        new_c=0.0
        new_r=0.0
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
    #update clusters list
    item_list[maximum_r]=item_list[maximum_r]+" , "+item_list[maximum_c]
    del item_list[maximum_c]
    for i in count_list[maximum_c]:
        count_list[maximum_r].append(i)
    del count_list[maximum_c]






# clustering until only one cluster
while sim_matrix.__len__()!=1:
    Clustering()
    result_list.append(copy.deepcopy(item_list))
    result_count_list.append(copy.deepcopy(count_list))


for k in range(2,6):

    num_list=[]
    num=1
    print("K = "+str(k))
    for i in result_list[result_list.__len__()-k]:
        print('Cluster ' + str(num) + ' : '+str(i))
        num += 1
    for i in result_count_list[result_count_list.__len__()-k]:

        for j in i:
            num_list.append(j)

    for i in range(0,num_list.__len__()):
        for j in range(0,num_list.__len__()):
            new_matrix[i][j]=copy_matrix[num_list[i]][num_list[j]]



    #save right triangle and copy it to left triangle
    new_matrix=numpy.triu(new_matrix)
    new_matrix += new_matrix.T - numpy.diag(new_matrix.diagonal())
    #print(new_matrix)

    ax = seaborn.heatmap(new_matrix, vmin=0, vmax=1)
    #plt.imshow(new_matrix, cmap='hot', interpolation='nearest')
    plt.title('K = '+str(k))
    plt.show()

