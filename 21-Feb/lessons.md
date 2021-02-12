# Lessons on 01

Need to focus on basics, use variables and such over compelx solutions first. I am getting better at complexity

I have the right solutions and ideas, focus on the code for it.

Focus areas: Dynamic programming. Kandanes algorithim.   
https://leetcode.com/problems/maximum-subarray/discuss/20193/DP-solution-and-some-thoughts

# Lessons on 02

Focus on BST, BST traversal and recursion. 

 Cleared Med-669 on my own without hints! Woot! 

 # Lesson on 03

 Valid Parenthesis
 
 # Lesson 09

 Today's challenge threw me for a loop. Appropriate given that it was recursion! Problem was to convert a BST into a greater BST. 
 '''
 Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
'''  

My idea was to go down all the way to the right, and add the sum, then take the parent and make it parent value +right tree. Left of the parent
would be the parent+each value above. In the end, I had to give up, as I could only get a few nodes to correctly add up. However, after seeing the solution, I was able to learn a lot.

What I got right:  
 Had the right idea. I knew the solution involved recursion or a stack, reversed BST traversal.  
 Was able to get some of the nodes to add correctly.  
 I knew I had to make a function in the class.  
 
 What I learned:  
 My grasp of recursion is weak. Even after seeing the solution and coding it out I still didn't understand it fully.  
 I need to think outside the box. A solution involved using class methods, while I was stuck on the function. I should focus on class methods in Python or other languages more.  

 This was a good way to re-learn BST traversal, recursion, and class members for me. While I failed, I feel good about it.  

 # Lesson on 10

 Once again need to focus on class members outside the function of interest. Hash tables seem to be showing up in more and more solutions. I should keep them more in mind.

 # Lesson on 11

Today's leetcoding challenge was Valid Anagram. Easy- found the solution by using a hash table(dictionary), on the reasoning that each string have to have the same number of each letter in them. 