---
toc: true
layout: post
description: What is Machine Learning?
categories: [markdown]
title: Machine Learning in Layman's Terms
---

# What is Machine Learning? 

Machine Learning is the process of teaching a computer from your data. The outcome of task and data at hand decides what and how we want to teach. There are different algorithms of Machine Learning, viz. **Linear Regression, Decision Trees, Neural Networks**, etc. Before we get into individual algorithms, it's important to know and understand at a high level how Machine Learning Algorithms work. 

What does it mean by implementing a Machine Learning algorithm? What are it's core components, if any? What broad steps are there? We will try to answer these here. 

A Machine Learning algorithm revolves around "something" to be learnt from given data. "Something" could be a *classification* task – classify dog vs 
cat image from a pool of cats and dogs images or it could be a problem of predicting a continuous value (e.g. house price, stock price, etc.) 
– this is also called as Regression. Don't worry if you never heard word *regression* before (I did not know what it really *meant* either, 
even after looking into a dictionary, I could not relate to it intuitively. As you might have guessed, English is not my first language :) )
Having spent some time on finding it's *true* meaning, just trust me when I say, *don't worry about it, you don't need to know it*.

Now, coming to the task at hand. We want to teach our algorithm a task. Think over it, if you want to teach someone something, how would you do it? 
What tools, measures/metrics would you fomulate? *Think* about your approach for a bit before moving to next part. 

From the outset, you will need:
1. A way to predict – to compute what your algorithm "thinks" about the input. This will be our instrument to get the response when we provide with raw data. Standard term for this is **Model**. This can also be thought as a hypothesis/assumption that the our process has learnt.
2. Then , we need a way to measure it's (model's) *performance* – how well your model has learnt the task that you are trying to teach. We call this
  a **Cost Function**
3. Once you have prediction and a way to measure it's performance, you need a way to optimize your model's performance based on it's Cost.
  We call this an **Optimization Algorithm**. This is the most crucial part, running optimization algorithm with Model predictions with Cost Function is so called **Training**. 


## Analogy
Broadly, you can draw an anology of teaching something to your younger self or a toddler, like: 

If we want to teach them something, we would not just read it out load once and assume that they understood everything. Interestingly, same 
goes with machines/computers. 
1. We need to tell it once (*train for one epoch*), 
2. Ask some questions, see how well it understood by asking them to take quizzes (*measure performance (calculate cost) on trained data*) 
3. And continue this process until it understands per our standards (*repeat* **training** *until convergence*). 

{% include info.html text="Note that in above anology, in the first step, we did not have to come up with so called *model* for the kid. The brain of the kid itslef is a model in this scenario." %}

Once their performance is satisfactory during teaching along with quiz scores, we give then an unseen questions in the form of an exam (**run our 
algorithm against test data**). The score of that exam decides how well the toddler learnt and if it can generalize well. Same goes for our model, based on the *TestScore*, we decide if this meets the standars for deploying in prodcution. 

## Core Components
Concretely, we can draw 3 important things that we need in our toolset to teach machine a given task: 1
1. A Model 
2. A Cost Function 
3. An Optimization Algorithm to minimize the Cost 
4. Metrics to decide if the algorithm performs well on unseen data (e.g. accuracy, loss, etc.)

{% include alert.html text "NOTE: Sometimes metric and Cost Function can be same. BUT Metrics are mostly understandable by humans while Cost Functions are for optimizing algorithms" %}

Let's look at how you would go on implementing each of these steps in Python code in the next post!

Om Shanti
Indra.
