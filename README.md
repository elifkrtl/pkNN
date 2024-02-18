# pkNN: k-Nearest Neighbor Algorithm with p-adic Distance

The $k$-Nearest Neighbor ( $k$-NN ) is one of the most popular machine learning algorithms used in classification and prediction problems. 
The effect of the distance/similarity metric used in the analysis on the $k$-NN performance is very important. 
In this project, the $p$-adic metric defined on rational numbers is coupled with $k$-NN algorithm. 
According to the theorem of Ostrowski, there are only two nontrivial absolute values on $\mathbb{Q}$, which are the usual absolute value and a $p$-adic absolute value for a prime $p$. 

This project is a part of a scientfic research which is under review now. If you want to try <b>pkNN</b> in Python, please import our <b>p_adic.py</b> module first.

<h2>The $p$-Adic Metric </h2>

Let $p$ be any prime number. For any nonzero integer $\alpha$, let $ord_p(\alpha)$ be the unique positive integer such that

$$\alpha' = p^{ord_p ( \alpha )} \ \alpha' $$

where $\alpha'$ is an integer and $p  \nmid \alpha'$.

Let $p$ be a prime. The map $\mid \cdot \mid_p$ on $\mathbb{Q}$ is defined as:

$$ 
\mid x \mid_p= 
\begin{cases}
p^{-ord_p(x)} & \textrm{if} & x \neq 0, \nonumber\\
0 & \textrm{if} & x = 0. \nonumber
\end{cases}
$$

This map is called the $p$-adic absolute value and is a metric on $\mathbb{Q}$.

<h4>Example</h4>

$$ord_5(125)=3, ord_5(50)=2, ord_2(32)=5, ord_7(99)=0$$

<h4>Example</h4>

For the 5-adic metric on $\mathbb{Q}$, $\mid 25 \mid_5=\frac{1}{5^2}=\frac{1}{25}$ and  for the 3-adic metric on $\mathbb{Q}$,     $\mid 25 \mid_3=\frac{1}{5^0}=1$ and     $\mid \frac{18}{27} \mid_3=\frac{3^3}{3^2}=\frac{27}{9}$=3.

For more examples, please see <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.pdf" target="_blank">p_adic_examples.pdf</a> and <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.py" target="_blank">p_adic_examples.py</a>.

<h2> The $p$-adic Distance </h2>

The $p$-adic metric defined on rational numbers is suitable for working with real-world datasets. The $p$-adic distance between $z$ and $x_i$ is given as follows:

$$d( z, x_i ) = \sum_{j=1}^m \mid z_j - x_{ij} \mid _p$$

\textcolor{red}{The $p$-adic distance between $z, x \in \mathbb{Q}$ is given as follows

$$d( x, y ) = \mid x - y \mid _p.$$

This definition can be extended to the set $\mathbb{Q}^n$ such that

$$d( x, y ) = \sum_{i=1}^n \mid x_i - y_i \mid _p,$$

where $x=(x_1, \dots, x_n),  y=(y_1, \dots, y_n) \in \mathbb{Q}^n$ and $n\in \mathbb{N}$. Therefore, the $p$-adic metric defined on rational numbers is suitable for working with real-world datasets.}

<h2> k-Nearest Neighbor Algorithm with p-adic Distance </h2>

Please see the examples in <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_knn_example1.py" target="_blank">p_adic_knn_example1.py</a> and <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_knn_example2.py" target="_blank">p_adic_knn_example2.py</a>.
