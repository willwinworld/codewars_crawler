Description:

Lists are data structures composed of nested objects, each containing a single value and a reference to the next object.

Here's an example of a list in JavaScript:

{value: 1, next: {value: 2, next: {value: 3, next: null}}}
In Python, lists will be represented by a preloaded LinkedList class with the members value and next. Here's an example:

LinkedList(1, LinkedList(2, LinkedList(3)))
Write a function listToArray (or list_to_array in Python) that converts a list to an array, like this:

[1, 2, 3]
Assume all inputs are valid lists with at least one value. For the purpose of simplicity, all values will be either numbers, strings, or Booleans.

In Python, lists will be represented by a preloaded LinkedList class with the members value and next. Here's an example:

LinkedList(1, LinkedList(2, LinkedList(3)))
就是遍历list 把当前节点append到list， 如果有下一个就读下一个继续这个操作。。 没有就return list 就好了。。
