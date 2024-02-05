'''
An array a is called ugly if it contains at least one element which is equal to the sum of all elements before it. If the array is not ugly, it is beautiful.

For example:

the array [6,3,9,6] is ugly: the element 9 is equal to 6+3;
the array [5,5,7] is ugly: the element 5 (the second one) is equal to 5;
the array [8,4,10,14] is beautiful: 8≠0, 4≠8, 10≠8+4, 14≠8+4+10, so there is no element which is equal to the sum of all elements before it.
You are given an array a such that 1≤a1≤a2≤⋯≤an≤100. You have to reorder the elements of a in such a way that the resulting array is beautiful. Note that you are not allowed to insert new elements or erase existing ones, you can only change the order of elements of a. You are allowed to keep the array a unchanged, if it is beautiful.

Input
The first line contains one integer t (1≤t≤2000) — the number of test cases.

Each test case consists of two lines. The first line contains one integer n (2≤n≤50). The second line contains n integers a1,a2,…,an (1≤a1≤a2≤⋯≤an≤100).

Output
For each test case, print the answer as follows:

if it is impossible to reorder the elements of a in such a way that it becomes beautiful, print NO;
otherwise, in the first line, print YES. In the second line, print n integers — any beautiful array which can be obtained from a by reordering its elements. If there are multiple such arrays, print any of them.
'''






'''
For a square matrix of integers of size n×n, let's define its beauty as follows: for each pair of side-adjacent elements x and y, write out the number |x−y|, and then find the number of different numbers among them.

For example, for the matrix (1432) the numbers we consider are |1−3|=2, |1−4|=3, |3−2|=1 and |4−2|=2; there are 3 different numbers among them (2, 3 and 1), which means that its beauty is equal to 3.

You are given an integer n. You have to find a matrix of size n×n, where each integer from 1 to n2 occurs exactly once, such that its beauty is the maximum possible among all such matrices.

Input
The first line contains a single integer t (1≤t≤49) – the number of test cases.

The first (and only) line of each test case contains a single integer n (2≤n≤50).

Output
For each test case, print n rows of n integers — a matrix of integers of size n×n, where each number from 1 to n2 occurs exactly once, such that its beauty is the maximum possible among all such matrices. If there are multiple answers, print any of them.
'''
'''
You are participating in Yet Another Tournament. There are n+1 participants: you and n other opponents, numbered from 1 to n.

Each two participants will play against each other exactly once. If the opponent i plays against the opponent j, he wins if and only if i>j.

When the opponent i plays against you, everything becomes a little bit complicated. In order to get a win against opponent i, you need to prepare for the match for at least ai minutes — otherwise, you lose to that opponent.

You have m minutes in total to prepare for matches, but you can prepare for only one match at one moment. In other words, if you want to win against opponents p1,p2,…,pk, you need to spend ap1+ap2+⋯+apk minutes for preparation — and if this number is greater than m, you cannot achieve a win against all of these opponents at the same time.

The final place of each contestant is equal to the number of contestants with strictly more wins + 1. For example, if 3 contestants have 5 wins each, 1 contestant has 3 wins and 2 contestants have 1 win each, then the first 3 participants will get the 1-st place, the fourth one gets the 4-th place and two last ones get the 5-th place.

Calculate the minimum possible place (lower is better) you can achieve if you can't prepare for the matches more than m minutes in total.

Input
The first line contains a single integer t (1≤t≤104) — the number of test cases.

The first line of each test case contains two integers n and m (1≤n≤5⋅105; 0≤m≤∑i=1nai) — the number of your opponents and the total time you have for preparation.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤1000), where ai is the time you need to prepare in order to win against the i-th opponent.

It's guaranteed that the total sum of n over all test cases doesn't exceed 5⋅105.

Output
For each test case, print the minimum possible place you can take if you can prepare for the matches no more than m minutes in total.
'''


'''
You are given an array a consisting of n integers.

You have to perform the sequence of n−2 operations on this array:

during the first operation, you either add a2 to a1 and subtract a2 from a3, or add a2 to a3 and subtract a2 from a1;
during the second operation, you either add a3 to a2 and subtract a3 from a4, or add a3 to a4 and subtract a3 from a2;
...
during the last operation, you either add an−1 to an−2 and subtract an−1 from an, or add an−1 to an and subtract an−1 from an−2.
So, during the i-th operation, you add the value of ai+1 to one of its neighbors, and subtract it from the other neighbor.

For example, if you have the array [1,2,3,4,5], one of the possible sequences of operations is:

subtract 2 from a3 and add it to a1, so the array becomes [3,2,1,4,5];
subtract 1 from a2 and add it to a4, so the array becomes [3,1,1,5,5];
subtract 5 from a3 and add it to a5, so the array becomes [3,1,−4,5,10].
So, the resulting array is [3,1,−4,5,10].

An array is reachable if it can be obtained by performing the aforementioned sequence of operations on a. You have to calculate the number of reachable arrays, and print it modulo 998244353.

Input
The first line contains one integer n (3≤n≤300).

The second line contains n integers a1,a2,…,an (0≤ai≤300).

Output
Print one integer — the number of reachable arrays. Since the answer can be very large, print its remainder modulo 998244353
'''


'''
Monocarp and Polycarp are playing a computer game. This game features n bosses for the playing to kill, numbered from 1 to n.

They will fight each boss the following way:

Monocarp makes k attempts to kill the boss;
Polycarp makes k attempts to kill the boss;
Monocarp makes k attempts to kill the boss;
Polycarp makes k attempts to kill the boss;
...
Monocarp kills the i-th boss on his ai-th attempt. Polycarp kills the i-th boss on his bi-th attempt. After one of them kills the i-th boss, they move on to the (i+1)-st boss. The attempt counters reset for both of them. Once one of them kills the n-th boss, the game ends.

Find all values of k from 1 to n such that Monocarp kills all bosses.

Input
The first line contains a single integer t (1≤t≤104) — the number of testcases.

The first line of each testcase contains a single integer n (1≤n≤2⋅105) — the number of bosses.

The second line contains n integers a1,a2,…,an (1≤ai≤n) — the index of attempt Monocarp kills each boss on.

The third line contains n integers b1,b2,…,bn (1≤bi≤n) — the index of attempt Polycarp kills each boss on.

The sum of n over all testcases doesn't exceed 2⋅105.

Output
For each testcase, print two lines. The first line should contain a single integer cnt — the number of values of k from 1 to n such that Monocarp kills all bosses. The second line should contain cnt distinct integers — the values of k themselves.

'''

'''
You are given two permutations a and b, both of size n. A permutation of size n is an array of n elements, where each integer from 1 to n appears exactly once. The elements in each permutation are indexed from 1 to n.

You can perform the following operation any number of times:

choose an integer i from 1 to n;
let x be the integer such that ax=i. Swap ai with ax;
let y be the integer such that by=i. Swap bi with by.
Your goal is to make both permutations sorted in ascending order (i. e. the conditions a1<a2<⋯<an and b1<b2<⋯<bn must be satisfied) using minimum number of operations. Note that both permutations must be sorted after you perform the sequence of operations you have chosen.

Input
The first line contains one integer n (2≤n≤3000).

The second line contains n integers a1,a2,…,an (1≤ai≤n; all ai are distinct).

The third line contains n integers b1,b2,…,bn (1≤bi≤n; all bi are distinct).

Output
First, print one integer k (0≤k≤2n) — the minimum number of operations required to sort both permutations. Note that it can be shown that 2n operations are always enough.

Then, print k integers op1,op2,…,opk (1≤opj≤n), where opj is the value of i you choose during the j-th operation.

If there are multiple answers, print any of them.
'''

'''
You are given a tree of n vertices and n−1 edges. The i-th vertex has an initial weight ai.

Let the distance dv(u) from vertex v to vertex u be the number of edges on the path from v to u. Note that dv(u)=du(v) and dv(v)=0.

Let the weighted distance wv(u) from v to u be wv(u)=dv(u)+au. Note that wv(v)=av and wv(u)≠wu(v) if au≠av.

Analogically to usual distance, let's define the eccentricity e(v) of vertex v as the greatest weighted distance from v to any other vertex (including v itself), or e(v)=max1≤u≤nwv(u).

Finally, let's define the radius r of the tree as the minimum eccentricity of any vertex, or r=min1≤v≤ne(v).

You need to perform m queries of the following form:

vj xj — assign avj=xj.
After performing each query, print the radius r of the current tree.

Input
The first line contains the single integer n (2≤n≤2⋅105) — the number of vertices in the tree.

The second line contains n integers a1,…,an (0≤ai≤106) — the initial weights of vertices.

Next n−1 lines contain edges of tree. The i-th line contains two integers ui and vi (1≤ui,vi≤n; ui≠vi) — the corresponding edge. The given edges form a tree.

The next line contains the single integer m (1≤m≤105) — the number of queries.

Next m lines contain queries — one query per line. The j-th query contains two integers vj and xj (1≤vj≤n; 0≤xj≤106) — a vertex and it's new weight.

Output
Print m integers — the radius r of the tree after performing each query.
'''
