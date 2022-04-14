An example linked list using a hybrid node type that functions as both a list node and a tree node.


Supports the following data types:

- Integers
- Strings
- Lists of integers
- Lists of strings

Includes the following methods:

- insert
- append
- remove
- pop
- pop_back
- is_empty
- linear_search (searches for data from head and tail simultaneously in linear time (n/2))
- quick_search (search in logarithmic time using an embedded binary search tree)
- sorted (display the binary search tree by in-order traversal)

Using append() and pop(), the linked list can be used as a stack.  Using insert() and pop(), it can be used as a queue.  pop_back() enables deque functionality.

