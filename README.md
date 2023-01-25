# pkNN: k-Nearest Neighbor Algorithm with p-adic Distance

The $k$-Nearest Neighbor ( $k$-NN ) is one of the most popular machine learning algorithms used in classification and prediction problems. 
The effect of the distance/similarity metric used in the analysis on the $k$-NN performance is very important. 
In this project, the $p$-adic metric defined on rational numbers is coupled with $k$-NN algorithm. 
According to the theorem of Ostrowski, there are only two nontrivial absolute values on $\mathbb{Q}$, which are the usual absolute value and a $p$-adic absolute value for a prime $p$. 

This project is a part of a scientfic research which is under review now. If you want to try <b>pkNN</b> in Python, please import our <b>p_adic.py</b> module first.

<h2>The $p$-Adic Metric </h2>

We know one metric on $\mathbb{Q}$ that induced by the usual absolute value $\mid \cdot \mid_\infty$. In this section, we focus on an another metric on $\mathbb{Q}$ called the $p$-adic metric and some of its properties. 

Let $p$ be any prime number. For any nonzero integer $\alpha$, let $ord_p(\alpha)$ be the unique positive integer such that

$$\alpha' = p^{ord_p ( \alpha )} \ \alpha' $$

where $\alpha'$ is an integer and $p  \nmid \alpha'$. 

<h4>Example</h4>

$$ord_5(125)=3, ord_5(50)=2, ord_2(32)=5, ord_7(99)=0$$

For more examples, please see <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.pdf" target="_blank">p_adic_examples.pdf</a> and <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_examples.py" target="_blank">p_adic_examples.py</a>.

<h2> The $p$-adic Distance </h2>

The $p$-adic metric defined on rational numbers is suitable for working with real-world datasets. The $p$-adic distance between $z$ and $x_i$ is given as follows:

$$d( z, x_i ) = \sum_{j=1}^m \mid z_j - x_{ij} \mid _p$$

<h2> k-Nearest Neighbor Algorithm with p-adic Distance </h2>

Please see the examples in <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_knn_example1.py" target="_blank">p_adic_knn_example1.py</a> and <a href="https://github.com/elifkrtl/pkNN/blob/main/p_adic_knn_example2.py" target="_blank">p_adic_knn_example2.py</a>.
