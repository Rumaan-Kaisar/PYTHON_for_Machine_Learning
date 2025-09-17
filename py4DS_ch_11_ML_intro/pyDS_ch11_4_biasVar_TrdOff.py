
################# 16.1 :
# copy: 
#       
#   
#
################# (17-Sep-25 for 19-Sep-25)

# Courses: PrTla PY for DS & ML >  16.1

# ----------------    Cross Validation and Bias-Variance Trade-Off    ----------------

""" 
Hello everyone and welcome to the biased variance tradeoff lecture and this lecture.

We're going to discuss the bias various straight off and how you can use it to evaluate your model's

performance by his various tradeoff as a fundamental topic of understanding model performance and evaluation

.

Go ahead and review chapter two of an introduction to learning for more in-depth look on this topic

.

The bias variance tradeoff is the point where we are just adding noise by adding model complexity or

flexibility.

The training error goes down as it has to put the test error will start to go up the model after the

bias tradeoff begins to overfit Let's go ahead and discuss this topic by imagining a dartboard.

So imagine that the center of this target or a dartboard is a model that perfectly predicts the correct

values as we move away from the bullseye.

Our predictions will get worse and worse and we're going to go ahead and make a quadrant of low variance

versus high variance and high bias vs. low bias.

So we can get an understanding of what the bias in variance terms mean generally.

Imagine we can repeat our entire model building process to get a number of separate hits on the target

each hit represents an individual realisation of our model.

Given the chance variability in the training data we gather sometimes we will get a good distribution

of training data so we predict very well and we are close to the bull's eye.

While sometimes our training data might full of outliers or non-standard values resulting in poor predictions

and these different realizations result in a scatter of hits on the target or aiming for something for

low bias and low variance.

But realistically which you'll have to do is tradeoff variance or bias.

And here we can see in the quarter of the target a low variance low bias model will predict correct

values on the bullseye.

A low bias high variance model will predicts values around the bullseye but with a high degree of variance

versus a high bias low variance model in that lower quadrant will have a high bias to a certain location

but low variance.

All your models predictions are in a certain area and in the worst high variance high bias means you

just all over the place basically a common temptation for beginners is to continually add complexity

to a model until it fits the training set very well.

And let's go ahead and begin to understand this in a machine learning algorithm or to learn about linear

regression.

What you may want to do is let's say you are given a set of red training data.

Now you testing data distric training data.

You might have a simple model such as the blue line and you get a certain error on your training data

and you decide as a beginner.

Hey maybe I should just make the model more and more complex or flexible so that it hits all those training

points.

However for hitting all those training points you're going to.

Your model is going to fail to predict for new test points.

Which is why we do that train test split.

Doing that can cause a model to overfit to your training data.

And like I mention cause large errors on new data such as the tests that were going to do is take a

look at an example model on how we can see overfitting occur from an air standpoint using test data

.

We'll use a black curve with some noise points off of it to represent the true shape.

The data follows.

All right.

We have three images here.

The first one is the X versus the Y.

And here we have model flexibility as different linear fits a linear fit a quadratic fit or a spline

fit with each one getting more complex.

So the simplest is just a linear fit more complicated that is quadratic.

And then you can have a spline fit and you'll notice that the black curve is the truth that the model

actually follows.

So all the points are just noise around the actual black curve which is the truth.

In order to evaluate your models and compare the complexities to each other which you'll have to do

is plot out the complexity or flexibility of the model.

For instance the polynomial level of a regression fit versus the error metric such as mean square error

.

And you can see here in that middle plot that's exactly what we've done and we've plotted out for the

training data versus the test data.

You'll notice all the way to the left.

We have a simple model that yellow linear model for this model.

We have a high error on both the test data and the training data as we begin to get more complicated

with the quadratic model.

In blue we begin to lower the error for the test data and the training data as we get even more complex

however we begin to lower the lower the error for the training data significantly.

But as a result you begin to have raised the error on the test data.

The new data show you want to find the point that's going to balance out the bias and the variance.

In this particular case it's going to be closer to the quadratic fit that Bluepoint.

So you want to balance out the bias and variance of your model to the point where your test data and

training data have reached some sort of minimum and grouping together.

This is the classic plot to show this as a general stance where you have low versus high model complexity

on the X-axis and some sort of prediction error on the y axis.

And as you moved to the left you get a higher bias but lower variance.

And as he moves to the right to a higher complexity model you get a lower bias the high variance in

what you want to do is pick a point where you are comfortable with the bias tradeoff.

If you go to the left of it you'll start to under fit to the data and if you go to the right of it you'll

start to overfit the data.

Meaning you're hitting all of those points and your training data and new data is cutting a larger error

because of that.

All right.

Keep that in mind as we continue on using Python for machine learning.

This is more of just a theoretical background.

Go ahead and read Chapter 2 of the introduction to Cisco learning.

If you want a more in-depth look of this this is a topic you want to keep in mind as you begin to work

with real world data.

OK thanks everyone and I'll see you at the next lecture.
 
"""


