
from random import choice


#gene_group:['aA', 'aA', 'aa', 'Aa', 'Aa', 'aA', 'aa', 'aa', 'AA', 'aa', 'Aa']
#10个个体 选择五个和另外五个配种

def generate(num):
    #num=10
    gene_list = ['a','A']#a:A=1:1
    genotype_list = ['aa','Aa','AA']
    genotype=''
    gene_group=[]
    count = 0
    while count < num+1:
        gene= choice(gene_list)
        genotype= gene+choice(gene_list)
        #print(genotype)
        gene_group.append(genotype)
        count+=1
    #print(gene_group)
    return(gene_group)


def mate(gene_group1):
    #gene_group1=generate(10)
    child_list=[]
    generation=10
    count =0
    while count< generation+1:
        father=choice(gene_group1)
        mother=choice(gene_group1)
        n=choice([0,1])
        m=choice([0,1])
        
        child=father[n]+mother[m]
        child_list.append(child)
        count+=1
    # gene_group1=child_list
    #print(child_list)
    #mate(10)
    return child_list

#怎么创建一个递归啊啊啊啊啊
print(mate(generate(10)))
print(mate(mate(generate(10))))
print(mate(mate(mate(generate(10)))))





'''
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
print(mate(mate(generate(10))))

#generate(10)
'''
'''
i=0
while i<11:
    print(mate(10))
    '''




