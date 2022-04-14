from linkedlist import LinkedList
import pdb

test_list = LinkedList([45, 53, 2, 349, 43, 390, 209, 390234, 1823, 38, 41])
# pdb.set_trace()
print(test_list)
print(test_list.tree)
test_list.remove([2, 45, 41])
print(test_list)
print(test_list.tree)