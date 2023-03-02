# Circuit-analysis
我想我已经实现了最难的部分了,剩下的就是代入各种公式和用symsy来解方程了.

I think I've done the hard part, and all that's left is to plug in the formulas and solve the equations with symsy.

很高兴你们能改进我的代码或者完成剩下的部分,用来做关于电路分析的作业

I'd be glad if you could improve my code or finish the rest of it for your homework on circuit analysis

1. 方式选择 Mode selection
对于电路图的存储,数据结构中的图或许是一个很好的方法,它能够完整的储存各个元件之间的关系
For circuit diagram storage, the graph in the data structure may be a good way 

to store the complete relationship between the various components

    ------------>-------------------------->----------------
    | --------------------------|------------------------|
    __-------------------------___----------------------___
   \   \----------------------\   \---------------------\   \
   \ 1 \----------------------\ 3 \---------------------\ 5 \
   \   \----------------------\   \---------------------\   \
    ---------------------------___------------------------__-
    |---------------------------|-------------------------|
    ^---------------------------↓-------------------------↓
    |---------------------------|-------------------------| 
    __------------------------ ____----------------------____
   \   \----------------------\   \----------------------\   \
   \ 2 \----------------------\ 4 \----------------------\ 6 \
   \   \----------------------\   \----------------------\   \
    __--------------------------__-------------------------__-
    |---------------------------|---------------------------|
    |---------------------------↓---------------------------↓
   ------------------<------------------------<-------------
   
2. 思路 thought
大多数公式的条件是需要在一个回路里
我以电流的方向来连接各个元件,但是我遇到了一些问题-- 
如何来确定每一个回路?
如图所示3,4,5,6不会以电流构成回路,怎么来确定这样的回路?

The condition for most formulas is that they need to be in a loop

I connected the components in the direction of the current, but I ran into some problems

How do you identify each loop?

As shown in the picture 3,4,5,6 does not loop with current. How do you determine such a loop?

通过图的深度优先遍历,我能找到像[1, 5, 6, 2],[1, 3, 4, 2]这样的回路

Through the depth-first traversal of the diagram, I can find loops like [1, 5, 6, 2],[1, 3, 4, 2]

通过分析[3, 4, 5, 6]这样的回路,我发现1是3和4共同的父节点,2是4和6共同的子节点

By analyzing a loop like [3, 4, 5, 6], I find that 1 is the common parent of 3 and 4, and 2 is the common child of 4 and 6

最后我用图的广度优先遍历,结合他们有着相同的父节点和子节点这一特性,找到了[3, 4, 5, 6]这样的回路

Finally, I use the breadth-first traversal of the graph to find a loop like [3, 4, 5, 6], combined with the fact that they have the same parent and child nodes


3. 遇到的问题 Problems encountered
在代码实现过程中我遇到了很多问题,最突出的就是python的深浅拷贝,我把一个个回路变量简单的赋值给回路结果列表,但是回路变量在回路的寻找中是会变化的,
由于用 = 来简单的赋值是传递的变量地址,导致不该变化的回路结果列表也跟着变化,最后我用.copy()方法解决了这一问题

In the process of code implementation, I encountered many problems, the most prominent is the python deep and shallow copy, I simply assign one loop variable to the loop result list, but the loop variable will change in the loop search,

Since the simple assignment with = is the address of the variable passed, the list of loop results that should not change also changes. I finally solved this problem by using the.copy() method

4. 学到了什么 What have me learned?
学习了图及其相关的遍历,对队列和栈有了更深的理解
Learned about graphs and their associated traversals and gained a deeper understanding of queues and stacks

