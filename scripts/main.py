import random
#functions#
def rand_seq(length,group_amino_acids):
    list_of_amino_acids=[]
    for i in range(length):
        placement=random.randrange(0,len(group_amino_acids))
        list_of_amino_acids.append(group_amino_acids[placement])
    return list_of_amino_acids




