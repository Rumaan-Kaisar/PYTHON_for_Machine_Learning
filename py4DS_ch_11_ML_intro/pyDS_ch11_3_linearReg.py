
################# 15.1:
# copy: house data, py, ipynb
#       
#   
#
################# (01-Jul-25 for 02-Jul-25)

# Courses: PrTla PY for DS & ML >  15.1 (ipynb), 15.3, 15.4, 15.5, 14.6  >>  details in ipynb

# a clear, pointwise simplification with mid-ground details while preserving full context:
# Use folloing as interactive note-code


""" 
    Project 1:
        Now we'll use scikit-learn in Python to create a linear regression model.

        After that, we'll work on your own portfolio project exercise, and once completed, the solutions will be reviewed and discussed.

"""


Linear Regression with Python: Practical Implementation









# Let's focus on scikit leanrn and training a linear regression model 6.30

# Getting feature and target


# interpret 13.35 rev[18-Jul-2025]

-------------------------------------



# NXT >> review lecture ipynb -> Part 2



Hello everyone and welcome to part two of the linear regression of Python lecture series in part 2.
We're going to focus on getting predictions from our model.
Let's go ahead and jump right back to the notebook where we left off last time.
All right.
Here I am at the Jupiter notebook.
Last time we were able to create our model and fit the model to the training set.
Now we want to do is grab predictions from our test set what you can do is say predictions is equal
to L-M.
And then we're going to call the Predict method and predict method used passen X just the features.
And in this case we want to pass in features that the models never seen before.
So we want to pasan X underscore test which is the testing set and just the features then we can go
ahead and check out the predictions and if we just look at the array of predictions there's a thought
thought thought here.
These are the predicted prices of the house.
However since we did the train test split we know that Y test contains the correct prices of the house
and we want to know how far off are the predictions from the tests prices the actual prices.
There is one quick way you can visually analyze this which is just by doing a scatterplot.
So you can say something like Piazzi thoughts scatter from that plot limb and compare Whitehurst versus
the predictions you just made.
And if they line up something like this you know you've done a pretty good job.
It means that a perfect straight line would be perfectly correct predictions.
So a little bit off the sort of straight line is actually a very good job.
Let's go ahead and actually create a histogram of the distribution of our residuals.
I'm going to say s this plot
and the residuals remember are the difference between the actual values why test and the predicted values
.
So go ahead and passen why test minus predictions
and we can go ahead and create a plot that looks like this.
And this is going to be a histogram of the residuals.
Notice here that our residuals looked to be normally distributed.
That's a very good sign if you have normally distributed residuals.
It means your model was a correct choice for the data.
If this is not normally distributed and you have some sort of weird behavior going on you may want to
look back at your data and check to see if a linear regression model was the correct choice for the
data set later on in the machine learning section.
We'll discuss other ways to analyze the correct choice of a model.
Let's go ahead and continue with regression evaluation metrics.
There are three common evaluation metrics for regression problems.
I'm going to go ahead and hop quickly to the Jupiter note book that contains the notes for this lecture
in order to explain these evaluation metrics.



All right.
I'm going to go ahead and hop over to the linear regression of Python notebook and like I mentioned
there's three regression evaluation metrics.
At least the most common ones there's the mean absolute error which is the mean of the absolute value
of the errors.
There's the mean squared error MSCE which is the mean of the square to errors and then there's the root
mean squared error.
Our MSCE which is the square root of the mean of the squared errors.
And these are all basic variations on the difference between what you predicted and the true values
.
Let's go at and compare these metrics and see which was mean absolute air is the easiest to understand
because just your average error you take your error take the absolute value of it and average it out
and S E mean square it.
Air is more popular than the mean absolute error because MSE will punish larger errors meaning it tends
to be more useful in the real world because it takes into account larger errors because it's squaring
them are.
MSE is even more popular than MSE because our MSCE is interpretable in the Y units meaning you can directly
interpret our Amasa me in the Y units whatever your target was and all of these are lost functions because
we want to minimize them.
All of these values here is something we want to minimize we want to minimize all these errors in order
to create the best model.
Let's go ahead and hop back and finish calculating out these metrics in our notebook.
Okay back to the notebook.
We can calculate all of these by just saying from S-K learn import metrics and offer this metrics.
You can say mean underscore absolute error and this will take in your y true and y predictions.
In this case that's why tests in our predictions.
And you can go ahead and prints out.
In this case your mean absolute error.
And similarly you can go ahead and calculate the same thing for your mean squared error.
And no I'm just using tab to autocomplete here for white test and predictions and the other thing can
also do is grab the root mean squared error and you can do this easily just by taking using some PI
and p s q r t one or under one of those universal functions and then just passing in our previous result
here.
Since that was the means operator if you want the root means squirter we just pass that in and that
gets us the root means Quader.
OK and that brings us to a conclusion for our linear regression model.
We were able to successfully taken the data split the data into a training set and a testing set based
on the features and the target.
Then we were able.
Please go ahead and scroll back up here to train a linear model from sikat learn fit the model check
up the coefficients and the intercepts to try to learn a bit about the model and then actually make
predictions using the model and analyze our residuals.
Basically our error of the model based off the test set and we can actually check out the metrics themselves
.
Ok like I mentioned you can go ahead and explore the Boston data set that I mentioned earlier and that's
linked in your note book.
If you want to redo this analysis on a real dataset.
But coming up next is going to be your exercise for your portfolio project.
Or we're going to give you some e-commerce data and you'll have to create a linear regression model
by following the directions in the exercise and then afterwards we'll go over the solutions.
I hope you enjoy your first foray into machine learning.
Later on we'll delve into real data sets from Kaggle dot com and perform machine learning projects that
are even more in-depth.
Thanks everyone and I'll see you at the next lecture

-------------------------------------------
PART 2:

In the second part of the linear regression workflow, the focus shifts to generating predictions from the trained model. After creating and fitting the linear regression model to the training dataset, the next step is to use this model to predict target values based on new, unseen data — specifically, the features from the test dataset.

To make predictions, the .predict() method of the trained model is called, with the test feature set (X_test) passed as an argument. This generates an array of predicted values corresponding to the test data. Since the original dataset was split into a training and test set, the true values for the test set are stored in y_test. Comparing these true values against the model's predictions helps assess the model's accuracy.

A quick and useful way to visualize this comparison is by creating a scatter plot of the actual target values (y_test) against the predicted values. Ideally, if the model performed perfectly, the points would lie along a straight diagonal line. A well-performing model will show points clustering closely around this line, indicating accurate predictions.

Another important diagnostic step is to examine the distribution of residuals — the differences between the actual values and the predicted values. This can be visualized using a histogram of residuals, calculated as y_test - predictions. If the residuals are roughly normally distributed, it suggests that the linear regression model is an appropriate fit for the data. An abnormal distribution of residuals, on the other hand, may indicate issues with the data or suggest that a different type of model would be more suitable.

Finally, evaluating the model numerically involves calculating standard regression evaluation metrics. There are three commonly used metrics for this purpose: Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). These metrics quantify the average difference between predicted and actual values in various ways, providing a clearer understanding of the model's performance.

This structured workflow — generating predictions, visualizing actual vs. predicted values, analyzing residuals, and applying quantitative performance metrics — forms the basis for assessing and refining regression models in practical machine learning tasks.


There are three commonly used evaluation metrics for regression problems: Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE). These metrics measure the difference between predicted and actual values in various ways, providing insight into the model’s accuracy.

Mean Absolute Error (MAE) is the simplest to interpret. It represents the average of the absolute differences between predicted values and the actual values. This gives a straightforward measure of the model’s average error.

Mean Squared Error (MSE), on the other hand, calculates the average of the squared differences between the predicted and actual values. Squaring the errors penalizes larger errors more severely, making MSE particularly useful in real-world applications where larger errors are more problematic.

Root Mean Squared Error (RMSE) is the square root of the MSE. It is often preferred because it expresses the error in the same units as the target variable, making it more interpretable in practical terms. Like MAE and MSE, RMSE serves as a loss function that the model aims to minimize.

These metrics can be easily computed in Python using the sklearn.metrics module. The mean_absolute_error() and mean_squared_error() functions accept the true target values and the model’s predictions as inputs. The RMSE can be calculated by taking the square root of the MSE using NumPy’s sqrt() function.

Once the evaluation metrics are computed, they provide a clear numerical summary of the model’s performance on the test data. Lower values for these metrics indicate a better-fitting model.

The full workflow of this linear regression implementation involves several steps: importing the necessary libraries, loading and inspecting the data, splitting it into training and testing sets, fitting a linear regression model, making predictions, and then evaluating those predictions both visually (using residual plots and scatterplots) and numerically (using regression metrics).

This process demonstrates the fundamental cycle of building and assessing a supervised machine learning model. To extend this practice, learners are encouraged to apply the same workflow on real datasets such as the Boston housing dataset or datasets from sources like Kaggle. These exercises help reinforce concepts and develop skills for applying machine learning to real-world data problems.
