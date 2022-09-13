<h1 align="center"><u>Moving averages and correlation</u></h1>
<br>
<br>
<h2>INTRODUCTION</h2>
<ul>
<li>Stock Trend Predictor is python program that utilizes data in a excel table to predict the general Stock Trend using moving averages and basic concepts of corellation and regression
<li>The project is helpful for both long term and short-term investors for analyzing a stock before investing in it.
<li>The Stock Trend Predictor in this project is based on the indicator moving averages, but the program can be modified to plot other indicators.
</ul>

<h2>FUNCTION</h2>
<ul>
<li>It works on the basic principle of moving averages and uses python to handle the mathematics behind the same.
<li>We have tried to find the correlation between time and the share pice of the company Mindtree Ltd(NSE: MINDTREE)
<li>The python script will first read into the excel data base and store the Price of the stock for past n days in a list Y and the day number in another list X
<li>Our predictions for a particular day will be the mean of the price of the stock on previous k days and these values will be stored in another list Y1.
<li>We will plot Y and Y1 on y-axis and X on x-axis using the matplotlib library
</ul>

<h2>CONCEPTS USED</h2>
<ul>
<li>CORRELATION
<li>REGRESSION
<li>MOVING AVERAGES
</ul>

<h2>WHAT IS CORRELATION?</h2>
<ul>
<li>Correlation studies and measures the direction and intensity of relationship among variables.
<li>Correlation measures covariation, not causation.
<li>The presence of correlation between two variables X and Y simply means that when the value of one
variable is found to change in one direction, the value of the other variable is found to change either
in the same direction (i.e. positive change) or in the opposite direction (i.e. negative change), but in a
definite way
</ul>

<h2<KARL PEARSON'S COEFFICIENT OF CORRELATION</h2>
$$\frac{n\sum x_iy_i -\sum x_i\sum y_i }{\sqrt{n\sum x_i^2-(\sum x_i )^2}-\sqrt{n\sum y_i ^2-(\sum y_i )^2}}$$
<ul>
<li>This is also known as product
moment correlation coefficient
or simple correlation
coefficient.
<li>This is also known as product
moment correlation coefficient
or simple correlation
coefficient.
</ul>

<h2>WHAT IS REGRESSION?</h2>
<ul>
<li>In statistical modeling, <b>regression</b> analysis is a set of statistical processes for estimating the
relationships between a dependent variables and one or more independent variables.
<li>The most common form of regression analysis is linear regression, in which one finds the
line that most closely fits the data according to a specific mathematical criterion
</ul>

$$Y_i = f(X_i,\beta)+e_i$$

<h3>WHERE:</h3>
<ul>
<li>The unknown parameters denoted as
a scalar or vector β
The independent variables, which are observed
in data and are often denoted as a vector Xi
The dependent variable, which are observed in
data and often denoted using the scalarYi
<li>The error terms, which are not directly
observed in data and are often denoted using
the scalar ei
</ul>

<h2>WHAT ARE MOVING AVERAGES?</h2>
<ul>
<li>moving average (rolling average or running average) is a calculation to analyze data points by
creating a series of averages of different subsets of the full data set. It is also called a moving
mean (MM) or rolling mean
<li>The mean over the last k data-points (days in this example) is denoted as SMAk and
calculated as:
</ul>

$$SMA_k = \frac{p_{k-n+1}+p_{k-n+2}+\vdots+p_{n-1}+p_{n}}{k}=\frac{1}{k}\cdot\sum_{i=k-n+1}^{n}(p_i)$$

<h2>Contributions</h2>
The project was made by the following students</b>
<ol>
<li>Eshan M.J
<li>Gopi Krishna
<li>Shelson Shelly
<li>Rayan Paul
</ol>
 
 <h2>Special Thanks to:</h2>
 This project wouldn’t have been possible
without the help and guidance from our
beloved teachers 
 <ul>
 <li>Ms.Leena Iteera
 <li>Ms.Jisha Rijo 
  <li>Ms.Latha(HOD)
 </ul>
 and many other including our class teacher.

