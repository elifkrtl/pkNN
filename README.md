# k-Nearest Neighbor algorithm with p-adic distance

The $k$-Nearest Neighbor ( $k$-NN ) algorithm is one of the most popular machine learning algorithms used in classification and prediction problems. 
The effect of the distance/similarity metric used in the analysis on the $k$-NN performance is very important. 
According to the theorem of Ostrowski, there are only two nontrivial absolute values on $\mathbb{Q}$, which are the usual absolute value and a $p$-adic absolute value for a prime $p$. 
In this project, the $p$-adic metric defined on rational numbers is coupled with $k$-NN algorithm. 

If you want to try <b>p-adic calculations</b> in Python, please import our <b>p_adic.py</b> script first.

This work is a part of the published paper in <a href="https://www.sciencedirect.com/science/article/pii/S0925231224001711" target="_blank">Neurocomputing</a> and supported by the Scientific and Technological Research Council of Türkiye (TÜBİTAK) [grant number 123E293].

<h2>The $p$-adic metric </h2>

Let $p$ be any prime number. For any nonzero integer $\alpha$, let $ord_p(\alpha)$ be the unique positive integer such that

$$\alpha = p^{ord_p ( \alpha )} \ \alpha', $$

where $\alpha'$ is an integer and $p  \nmid \alpha'$. \textcolor{Fatma}{$ord_p(\alpha)$ is called the $p$-adic valuation or $p$-adic order of $\alpha$.}  For all nonzero $x=\frac{a}{b} \in \mathbb{Q}$, it is defined $ord_p(x)$ as 
$$ord_p(x) = ord_p(a) - ord_p(b)$$
and $ord_p(0)=+\infty$.

<h4>Example</h4>

$$ord_2(64)=6,  ord_3(32)=0, ord_5(10)=1, ord_7(9)=0.$$

The $p$-adic absolute value $\mid \cdot \mid_p$ on $\mathbb{Q}$ is defined as

$$ 
\mid x \mid_p= 
\begin{cases}
p^{-ord_p(x)} & \textrm{if} & x \neq 0, \nonumber\\
0 & \textrm{if} & x = 0, \nonumber
\end{cases}
$$

where $x\in \mathbb{Q}$.

<h4>Example</h4> 

$\mid 625 \mid_5=\frac{1}{5^4}=\frac{1}{625}$, $\mid 625 \mid_3=\frac{1}{3^0}=1$ and $\mid \frac{18}{27} \mid_3=3$.

For more examples, please see <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.pdf" target="_blank">p_adic_examples.pdf</a> and <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.py" target="_blank">p_adic_examples.py</a>.

<h2> The $p$-adic distance </h2>

The $p$-adic metric on $\mathbb{Q}$ is given as 

$$d( x, y ) = \mid x - y \mid _p,$$
where $x, y \in \mathbb{Q}$. Using this $p$-adic metric, it can be defined the following distance function on $\mathbb{Q}^n$

$$d( x, y ) = \sum_{i=1}^n d( x_i, y_i )=\sum_{i=1}^n \mid x_i - y_i \mid _p,$$

where $x=(x_1, \dots, x_n),  y=(y_1, \dots, y_n) \in \mathbb{Q}^n$ and $n\in \mathbb{N}$. Therefore, the $p$-adic metric defined on rational numbers is suitable for working with real-world datasets. 

<h2> k-Nearest Neighbor algorithm with p-adic distance </h2>

The p-adic distance function defined here can be integrated into the k-Nearest Neighbor algorithm (such as <b> sklearn.neighbors.KNeighborsClassifier()</b>) with the help of a user-defined function.
