# What is Machine Learning? 

Before we get into individual algorithms, it's important to know and understand high level Machine Learning Algorithm implementation flow. 

What does it mean by implementing a Machine Learning algorithm? What are it's components? What broad steps are there? We will try to answer these here. 

A Machine Learning algorithm revolves around "something" to be learnt from given data. "Something" could be a classification task – classify dog vs 
cat image from a pool of cats and dogs images or it could be a problem of predicting a continuous value (e.g. house price, stock price, etc.) 
– this is also called as Regression. Don't worry if you never heard this word before (I did not know what it really *meant* either, 
even after looking into a dictionary – as you might have guessed, English is not my first language :) 
Having spent some time on finding it's *true* meaning, just trust me when I say, *don't worry about it, you don't need to know it*.

Now, coming to the task at hand. We want to teach our algorithm a task. Think over it, if you want to teach someone something, how would you do it? 
What tools, measures/metrics would you fomulate? <i> Think </i> about your approach for a bit before moving to next part. 

From the outset, you will need:
<ol> 
<li> A hypothesis/assumption that the algorithm has learnt. A way to predict – to compute what your algorithm "thinks" about the input. 
  This will be our instrument to get the response when we provide with raw data. Standard term for this is <b> Model </b> </li> 
<li> A way to measure it's (model's) performance – how well your algorithm has learnt the task that you are trying to teach. We call this
  a <b> Cost Function </b> </li>
<li> Once you have prediction and a way to measure it's performance, you need a way to optimize your model's performance based on it's Cost.
  We call this an <b> Optimization Algorithm </b> </li> 
</ol> 

Thus broadly, you can draw an anology of teaching something to your younger self or a toddler, like: 

If we want to teach them something, we would not just read it load once and assume that they understood everything. Interestingly, same 
  goes with machines/computers. We need to tell them once (<i>train for one epoch</i>), ask some questions (<i>validate on unseen data</i>), 
  see how well it understood (<i>calculate cost</i>) and continue this until it understands per our standards 
  (<i>repeat until convergence</i>). Once their performance is satisfactory during teaching along with quiz scores, we give then an un-assited exam (<i>run our 
  algorithm against test data</i> ). The score of that exam decides how well the toddler learnt and if it can generalize well. 

  
Concretely, we can draw 3 important things that we need in our toolset to teach machine a given task: 
<ol> 
<li> A Model </li> 
<li> A Cost Function </li> 
<li> An Optimization Algorithm to minimize the Cost </li> 
<li> Metrics to decide if the algorithm performs well on unseen data (e.g. accuracy, loss, etc.) </li>
  <br>
<i> NOTE: Sometimes your metrics and Cost Function can be same. BUT Metrics are mostly understandable by humans while Cost Functions
  are for optimizing algorithms. </i> 
</ol> 

Let's look at how you would go on implementing each of these steps in Python code in the next post!

Om Shanti, <br>
Indra.
