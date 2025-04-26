# Leetcode-no.21-merge-two-sorted-lists(using python3)-
一种简单易懂的解题方法(较于晦涩的递归)/A simple solution (compared to the obscure recursive method)
思路如下:/method is as followed：
1.将两个链表的值顺序（其实不是顺序也行）置入新创建的空列表中  /1.Put the value of two nodelists in an empty list  
2.因为python的优越性直接用sorted对该列表内的值进行排序  /2.  just use sorted to sort the empty list
3.排好序的列表——>新链表  /3.sorted list——>new nodelist(that is what you return)

缺点如下:/shortcomings are as followed：
1.没有利用到两个链表均为有序的性质  /1.do not utilize the property that the given two nodelists are both sorted of their values
2.新创建了一个列表  /2.craete a new list

(BUT DEFEATED 100% ANSWERS IN TIME COMPLEXITY)    :)
####
![image](https://github.com/user-attachments/assets/c31c0edd-5a0f-48fc-9293-820e7d79bd1f)
####
