# About

Those who cannot remember the past are condemned to repeat it

We need to break up a problem into a series of overlapping sub-problems, and build up solutions to larger and larger sub-problems. If you are given a problem, which can be broken down into smaller sub-problems, and these smaller sub-problems can still be broken into smaller ones - and if you manage to find out that there are some over-lappping sub-problems, then you've encountered a DP problem.

## Some famous Dynamic Programming algorithms are:

* Unix diff for comparing two files
* Bellman-Ford for shortest path routing in networks
* TeX the ancestor of LaTeX
* WASP - Winning and Score Predictor


The core idea of Dynamic Programming is to avoid repeated work by remembering partial results and this concept finds it application in a lot of real life situations.

In programming, Dynamic Programming is a powerful technique that allows one to solve different types of problems in time O(n2) or O(n3) for which a naive approach would take exponential time.


Writes down "1+1+1+1+1+1+1+1 =" on a sheet of paper.
"What's that equal to?"
Counting "Eight!"
Writes down another "1+" on the left.
"What about that?"
"Nine!" " How'd you know it was nine so fast?"
"You just added one more!"
"So you didn't need to recount because you remembered there were eight! Dynamic Programming is just a fancy way to say remembering stuff to save time later!"


## Majority of the Dynamic Programming problems can be categorized into two types:

* Optimization problems.
* Combinatorial problems.

The optimization problems expect you to select a feasible solution, so that the value of the required function is minimized or maximized. Combinatorial problems expect you to figure out the number of ways to do something, or the probability of some event happening.

Every Dynamic Programming problem has a schema to be followed:

Show that the problem can be broken down into optimal sub-problems.
Recursively define the value of the solution by expressing it in terms of optimal solutions for smaller sub-problems.
Compute the value of the optimal solution in bottom-up fashion.
Construct an optimal solution from the computed information.

## Bottom up vs. Top Down:

Bottom Up - I'm going to learn programming. Then, I will start practicing. Then, I will start taking part in contests. Then, I'll practice even more and try to improve. After working hard like crazy, I'll be an amazing coder.
Top Down - I will be an amazing coder. How? I will work hard like crazy. How? I'll practice more and try to improve. How? I'll start taking part in contests. Then? I'll practicing. How? I'm going to learn programming.
Not a great example, but I hope I got my point across. In Top Down, you start building the big solution right away by explaining how you build it from smaller solutions. In Bottom Up, you start with the small solutions and then build up.

Memoization is very easy to code and might be your first line of approach for a while. Though, with dynamic programming, you don't risk blowing stack space, you end up with lots of liberty of when you can throw calculations away. The downside is that you have to come up with an ordering of a solution which works.

One can think of dynamic programming as a table-filling algorithm: you know the calculations you have to do, so you pick the best order to do them in and ignore the ones you don't have to fill in.






# Links
* https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/