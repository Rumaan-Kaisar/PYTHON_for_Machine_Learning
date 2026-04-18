
################# 0: FULL
# copy:  
# ----  rev[17-apr-26] start: 502 (Titanic example)  ----
# use SRT for detailed example with images
# NXT >> Create ipynb "rouping part by part by GPT QWEN stylized form" >> add FIGS

################# (17-apr-26 for 18-Apr-26)

# Courses: PrTla PY for DS & ML >    1



"""  

    This section introduces classification problems, how logistic regression is used to solve them, 
        and shows how to interpret results using a "confusion matrix". 
        
    For the full mathematical details, see Sections 4-4.3 of "An Introduction to Statistical Learning by Gareth James".


    --------  Logistic Regression (Classification Overview)  --------

    Purpose of Logistic Regression:
        Logistic regression is a method used in "Classification Problems" within machine learning and STATISTICS.
        It is designed to predict "discrete categories", not continuous values (like linear regression).

        The name may be confusing at first-
        Although the name includes “regression,” its primary use is CLASSIFICATION, especially "binary classification".
            where outcomes belong to one of two classes, typically labeled as 0 and 1.


    ----  Classification Problems  ----

    Classification involves "determining the category" to which a "new observation" belongs, 
        Based on patterns learned from labeled training data.
        Usually several categories predefined based on training data.

        Common example:
            Distinguishing spam from non-spam emails.
            Predicting loan default risk.
            Diagnosing the presence of a disease such as cancer.

        These examples represent "binary classification", where there are only two possible classes.


    Linear Regression is unsuitable for Classification:
        In binary classification, class labels are typically represented as '0' and '1'.

        For instance, when modeling the likelihood of loan repayment based on income, 
            actual training data consists of binary outcomes (default or full repayment).

        But Linear Regression predicts continuous values (can be less than 0 or greater than 1).
            i.e. Linear Regression produce predictions outside the valid probability range of [0, 1]
            When interpreting outputs as probabilities, such values are invalid.
        So linear regression produces a poor fit for binary classification tasks.
        Therefore, we can't use a normal linear regression model on a binary group.



    ----  Logistic Regression (Modeling Probabilities)  ----

    The Role of the Sigmoid Function in Logistic Regression:
        Logistic regression solves above limitation by applying the sigmoid (or logistic) function to the output of a linear equation like "z = (w^T)*x + b".

        The sigmoid function maps any real-valued input to a range strictly between 0 and 1.

        The sigmoid function is defined as:

                sigma(z) = 1/(1 + e^(-z))
            
            where z is is the linear function that produce any real value.

                z = (w^T)x + b

            No matter how large or small the input value z is, 
            the "output" always lies between 0 and 1
            i.e. 0 < sigma(z) < 1.

        This property makes the sigmoid function ideal for "Modeling Probabilities".

        Example:
            For example, by substituting the linear combination "z = b0 + b1*x" into the sigmoid function,
                logistic regression produces outputs that can be interpreted as-
                "the probability of belonging to class 1 or class 0".        



        ----####  FIG_1 from lecture (logistic only)  ####----
                

        
    ----  From Linear Model to Logistic Model  ----

        A standard linear model has the form:

                z = b_0 + b_1*x

            or more generally
                
                z = (w^T)*x + b

            Here, z is the linear combination of the input features x with weights w and bias b.
            Since x, w and b are real numbers, z can be any real number.

        Logistic regression applies the sigmoid (logistic) function to this linear combination z.
        (i.e. we can take the linear regression solution and place it into this sigmoid function.)

                P(y=1|x) = sigma(z) = 1/(1 + e^(-z))

        P(y=1|x):
            The conditional probability that the outcome y is 1 (e.g., "True," "Spam," "Positive") 
            given input features x.
                
        The logistic (sigmoid) function used to predict the probability of a binary outcome (y=1) given input features x.
        
        This transformation ensures the final output is a valid probability in range [0. 1].
        As a result, logistic regression predicts the probability of belonging to "class 0" or "class 1".
        Notice folloing FIG.
        
        
        ----####  FIG_2 "putting liner function into sigmoid function yeilds linear regression" from lecture (logistic above linear, change variable, y to z in fig)  ####----

        Here we have a linear model as:
                z = b_0 + b_1*x
            If we take that linear model and put it into the "sigmoid function"
            we are transforming this linear regression to a logistic model.

            i.e. whatever output 'z' is produced, after putting 'z' into the sigmoid function the result will be between 0 and 1
            i.e. it doesn't matter what we put in on the horizontal axis, 
                on the vertical axis we'll always get a probability between 0 and 1.

        Graph shape: S-shaped curve
            As z gets very large → output approaches 1  
            As z gets very small (negative) → output approaches 0  
            At z = 0 → output = 0.5

        How it works step by step:                        
            Linear regression can output any number (even -5 or +10), which doesn't work for probabilities.
            But with the sigmoid, we transform the linear model's output so it stays between 0 and 1.

            STEPS:
                Start with a linear model:  
                        z = b_0 + b_1*x
                    (This could be based on features like income, credit score, etc.)

                Plug this z into the sigmoid function: 

                        sigma(z) = 1/(1 + e^(-z))
                i.e     Probability = 1/(1 + e^-(b_0 + b_1*x))

                Now the output is a valid probability between 0 and 1.
                We use this probability to make decisions.

                
    SUMMARY:
        z = (w^T)*x + b  ->  linear function  ->  outputs any real number.
        sigma(z)  ->  sigmoid function  ->  outputs a valid probability in (0, 1).



    ----  Decision Boundary and Classification Rule  ----

    Once a probability is obtained from the logistic model,
        a cutoff (decision threshold) value is chosen, commonly "0.5"

    This "cutoff point" (can be adjusted if needed) is used  to assign class labels.

    Classification rule:
        If predicted probability < 0.5 of belonging to class 1 :    assign "class 0"
        If predicted probability ≥ 0.5 of belonging to class 1 :    assign "class 1"

        This converts probabilistic output into discrete class labels.
        i.e. this rule transforms "continuous probability estimates" into binary values like 0 and 1.        

        Example:  
            - 40% chance of repaying loan → Class 0 (likely to default)
            - 70% chance of repaying loan → Class 1 (likely to repay)

        
    ----####  FIG_3 from lecture (logistic with threshold)  ####----

    STEPS to transforms regression into classification:
        - We start with a linear model (which can give any number)  
        - Pass it through the sigmoid → get a probability  
        - Apply threshold → get a final class (0 or 1)  

        This is how **logistic regression** works!        




    ----------------    Model Evaluation : CONFUSION MATRIX    ----------------

    After training a logistic regression model, its PERFORMANCE is evaluated using CONFUSION MATRIX on "test data".
    A confusion matrix summarizes prediction results when true labels are already known.
    It is commonly used for "binary classification problems", such as disease detection.

    Confusion Matrix is a table that compares:
            Actual (true) values  VS  Predicted (model's) values

    Confusion Matrix:
        A confusion matrix is a table that visualizes a machine learning model's performance by 
            comparing its predicted classifications against the actual outcomes.

        revealing:
            correct predictions (True Positives, True Negatives) and 
            errors (False Positives, False Negatives) 
            
        It shows where the model gets "confused" between classes, 
        It gives a detailed view beyond simple accuracy, especially for binary or multi-class problems. 
        
        A Confusion Matrix, also known as "Error Matrix"


    Confusion Matrix Components:

        True Positive (TP):
            Correctly predicted positive cases.
            i.e. Predicted positive and actually positive.

        True Negative (TN):
            Correctly predicted negative cases.
            i.e. Predicted negative and actually negative.

        False Positive (FP) (Type I Error): 
            Incorrectly predicted as positive.
            i.e. Predicted positive but actually negative.
            Also called Type I error.

        False Negative (FN) (Type II Error): 
            Incorrectly predicted as negative.
            i.e. Predicted negative but actually positive.
            Also called Type II error.

        Above trems are whole numbers (not rates or ratio)
        These terms are widely used in statistics, medicine, and hypothesis testing.

        
            
    How it Works:
        It's an N x N table where N is the number of classes, 
        showing counts for each combination of actual vs. predicted class.

        Rows:
            typically represent actual classes 
        Columns:
            represent predicted classes (or vice versa).

        Diagonal entries are correct predictions; 
        off-diagonal entries show misclassifications. 



    Why It's Used:
        Reveals which classes are being confused with which other classes
        i.e. understanding model weaknesses.

        Accuracy metrics:
                Precision, 
                Recall (Sensitivity), 
                Specificity, and 
                F1-Score, 

            these are crucial for imbalanced datasets or critical applications 
            e.g., medical diagnosis where one type of error is more costly than another.

            
        Model Comparison:
            Helps compare the performance and error patterns of different classification algorithms.



    Model Evaluation Using the Confusion Matrix:

        The proportion of correct predictions:
            Accuracy = (TP + TN)/(TP + TN + FP + FN)
                        = (TP + TN)/(Total predictions)

        The proportion of incorrect predictions:    
            Misclassification Rate = (FP + FN)/(TP + TN + FP + FN)
                                    = (FP + FN)/(Total predictions)

                                    
        ----------------    EXAMPLE    ----------------

        For EXAMPLE, in a test involving 165 patients where 105 had a disease and 60 did not, 
            a model yielding:
                100 true positives, 
                50 true negatives, 
                10 false positives, and 
                5 false negatives 
            would achieve an accuracy of approximately 91% and a misclassification rate of 9%.

            Presence of a disease where:

                NO  = negative test = FALSE = 0
                YES = positive test = FALSE = 0

            ------------------------|---------------------------|-----------------------------
            n = 165                 |   Predicted "NO" = 55     |   Predicted "YES" = 100
            ------------------------|---------------------------|-----------------------------
            Actual "NO" = 60        |   TN = 50                 |   FP = 10
            ------------------------|---------------------------|-----------------------------
            Actual "YES" = 105      |   FN = 5                  |   TP = 100            
            ------------------------|---------------------------|-----------------------------

            What can we learn from this matrix:
                Binary classification: there are two possible predicted classes- YES and NO.

                    YES: it would mean that patients have disease
                    NO: it would mean that patients don't have disease. 

                The classifier made a total of a 165 predictions 
                    meaning 165 patients were tested for the presence of the disease.

                Out of those 165 cases, the classifier predicted: "YES" 110 times and "NO" 55 times.
            
                In actual data, we already have labeled test data where
                    105 patients in the sample have the disease and 
                    60 patients do not.

                - The model correctly identified "100 out of 105" sick patients (great recall for positives).
                - It incorrectly told "5 sick people they were healthy" (dangerous false negatives, Type II).
                - It falsely alarmed "10 healthy people" that they had the disease (false positives).
                
            Accuracy:
                - Overall accuracy = (TP + TN) / Total = (100 + 50) / 165 ≈ 90.9%
                  (i.e. how often it gives correct prediction)

                - Error rate = (FP + FN) / Total = (10 + 5) / 165 ≈ 9.1%
                  (Misclassification rate, i.e. Overall how often the model is wrong)
                  

                But wait — even with high accuracy, "false negatives" can be critical in medical cases!

        Tip: 
            Always look at both types of errors 
            Sometimes reducing "false negatives" is more important than overall accuracy.



    --------  Understanding Type I and Type II Errors  --------

    Type I errors (false positives) occur when the model incorrectly predicts a positive outcome-
    such as diagnosing a "healthy" person with a disease. 

    Type II errors (false negatives) occur when the model fails to detect a true positive-
    such as "missing" an actual case of disease. 


    ----  SEVERITY of these errors  ----
    The severity of Type I vs. Type II errors depends on the context. 
    In some situations, Type II errors can be much more dangerous than Type I.

    Real-world scenarios: cyclone prediction and cancer diagnosis.

    
    Cyclone Prediction:
        Imagine a model predicts whether a cyclone will hit 
        (Positive = cyclone expected; Negative = no cyclone).

        Type I Error (False Positive):
            The model predicts a cyclone is coming, but it doesn't happen.
            Results unnecessary evacuations, panic, economic loss, wasted resources.

        Type II Error (False Negative):
            The model says no cyclone, but a cyclone actually hits.
            No preparation, high risk of death, destruction, and disaster.
            
        Which is worse?
            Type II error (false negative) is far more dangerous here.
            Failing to warn people when danger is real can cost lives.

        So its better to have a few false alarms than miss a real cyclone.

        
    Disease Detection (e.g., Cancer):
        Model predicts whether a patient has cancer 
        (Positive = cancer; Negative = no cancer).

        Type I Error (False Positive):
            The model says the person has cancer, but they are healthy.
            Results Anxiety, stress, extra tests (more cost)

        Type II Error (False Negative):
            The model says "no cancer," but the person actually has it.
            Delayed treatment, disease progresses, lower survival chances.

        Which is worse?
            Type II error (false negative) is again more serious.
            Missing cancer early can mean losing the best chance for cure.

        It's far better to flag someone unnecessarily (and confirm with more tests) than to miss a real case.


    --------  Practical Applications  --------

    Logistic regression is widely applied in real-world scenarios. For instance: 
        it can be used with the Titanic dataset to predict "passenger survival"
        based on features like: age, gender, and class. 

    Similarly, it can model "customer behavior", such as:
        predicting "whether a user will click on an online advertisement"
        based on: demographic and behavioral data.

    For a deeper mathematical understanding of logistic regression, including derivation and optimization, 
    READ Sections 4 to 4.3 of "An Introduction to Statistical Learning" by Gareth James et al.

"""





# ----  Example Walkthrough: Why Linear Regression is Unsuitable for Classification  ----




"""  

    Following example demonstrates why We Need Logistic Regression:

    Say we're trying to predict "likelihood of paying back a loan".
        We're predicting a yes/no outcome
        Will a person pay back their loan? (Yes = 1, No = 0)

    We can't use normal linear regression for binary outcomes it won't lead to a good fit because:
        Linear regression predicts continuous values, 
        But here we need probabilities between 0 and 1.

    
    For example if we take a look at this plot below we have:

        X-axis: Paycheck amount
            Shows how much someone "earns".

        Y-axis: Scale of Probability of "repaying" the loan
            0 = 0% chance (will default their loan)  
            1 = 100% chance (will repay their loan)

        The Y axis represents the probability of belonging to a particular group.

        
        ----  PLOT-illustration 1 (dots only)  ----

    Pattern in data:
        - Lower paycheck → Probability of "repaying" the loan closer to 0  
        - Higher paycheck → Probability of "repaying" the loan closer to 1  
        
    Training data points are only at 0 or 1:  
        Because real people either paid back (1) or didn't (0)
        so dots are only on top (1) or bottom (0).
        
    Problem with LINEAR regression: 
        - Considering this dataset as traning data if we fit a straight line, it might predict:
          (line that tries to fit those dots)
        - Probabilities below 0 (e.g., -20%) which doesn't make sense
        - Or above 1 (e.g., 120%) also impossible

        
        ----  PLOT-illustration 2 (dots & linear regression)  ----
        
        
    Solution: "Use LOGISTIC regression"
        - Fits an S-shaped curve that only stays between 0 and 1
        - Gives valid probability estimates for classification


        
    --------    sigmoid    --------

    The SIGMOID also known as LOGISTIC FUNCTION is the heart of logistic regression to perform a classification.

        Key idea:  
            Logistic regression is made for predicting categories (like yes/no) 
            by modeling "probabilities safely within 0 to 1"

        ----  PLOT-illustration 3 (linear vs logistic)  ----

            



---






========================================








Next Example:

Let's go ahead and begin to explore an example of logistic regression using the famous Titanic data
set will use Python to attempt to predict whether or not a passenger survived based off of their features
.
Then you'll have a portfolio project with some advertising data trying to predict whether or not a customer
clicked on an ad.
OK thanks everyone and I'll see if the next lecture





Here’s a clear, organized, and simplified version of your content — now structured point-by-point for better understanding:

---

### 🔹 Model Evaluation: Understanding Rates from the Confusion Matrix

After building a classification model (like logistic regression), we use **rates** to evaluate its performance more deeply.

Let’s break down the key metrics using our earlier example (disease detection with 165 patients):

|                     | Predicted No | Predicted Yes |
|---------------------|--------------|---------------|
| **Actual No**       | TN = 50      | FP = 10       |
| **Actual Yes**       | FN = 5       | TP = 100      |

---

#### 1. **Accuracy – How often is the model correct?**
- Measures overall correctness.
- Formula:
  \[
  \text{Accuracy} = \frac{\text{True Positives (TP)} + \text{True Negatives (TN)}}{\text{Total Predictions}}
  \]
- Calculation:
  \[
  \frac{100 + 50}{165} = \frac{150}{165} ≈ 0.909 → \textbf{91\% accurate}
  \]

✅ Interpretation: The model is right 91% of the time.

---

#### 2. **Misclassification Rate – How often is the model wrong?**
- Also called **error rate**.
- Formula:
  \[
  \text{Error Rate} = \frac{\text{False Positives (FP)} + \text{False Negatives (FN)}}{\text{Total}}
  \]
- Calculation:
  \[
  \frac{10 + 5}{165} = \frac{15}{165} ≈ 0.091 → \textbf{9\% error rate}
  \]

❌ Interpretation: The model makes a mistake in about 1 out of every 11 cases.

> 🔄 Note:  
> Accuracy + Error Rate = 100%

---

### 🔁 Quick Tip: Remembering False Positives vs. False Negatives

It's easy to mix up **Type I** and **Type II** errors. Here’s a fun way to remember:

#### ✅ **False Positive (Type I Error)**  
- You predict **YES**, but it’s actually **NO**  
- Example: Telling a **man** he’s pregnant ❌  
  → He doesn’t have the condition, but you said he does  
- FP = 10 in our example

🧠 Think: *"False alarm"*

---

#### ✅ **False Negative (Type II Error)**  
- You predict **NO**, but it’s actually **YES**  
- Example: Telling a **very pregnant person** they’re *not* pregnant ❌  
  → They clearly have the condition, but you missed it  
- FN = 5 in our example

🧠 Think: *"Missed diagnosis"*

> 💡 In statistics, these are also called:
> - **Type I Error** = False Positive
> - **Type II Error** = False Negative

This humorous analogy helps you remember which is which — especially when stakes are high (like medicine or safety).

---

### 🚀 What’s Next?

Now that we understand evaluation metrics, let’s apply logistic regression in real-world projects:

1. **Titanic Dataset (Python Example)**  
   - Predict whether a passenger **survived** the Titanic disaster  
   - Based on features like age, gender, class, etc.

2. **Portfolio Project: Advertising Data**  
   - Predict if a customer **clicked on an ad**  
   - Great for practicing classification and adding to your data science portfolio

---

👋 That’s it for now!  
In the next lecture, we’ll dive into coding these models and interpreting results step by step.

See you there! 😊






"""



Yes, exactly! 🎯

In **logistic regression**, we define:

$$
z = w^T x + b
$$

- Here, **\(z\)** is the **linear combination** of the input features \(x\) (with weights \(w\) and bias \(b\)).
- Since \(x\), \(w\), and \(b\) are real numbers, **\(z\) can be any real number**: \(z \in (-\infty, +\infty)\).

Then, we apply the **sigmoid (logistic) function** to \(z\):

\[
P(y = 1 \mid x) = \sigma(z) = \frac{1}{1 + e^{-z}}
\]

- The sigmoid **maps** the real-valued \(z\) to a value strictly between 0 and 1: \(\sigma(z) \in (0, 1)\).
- This transformed output **can be interpreted as a probability**.

### Summary:
- ✅ **\(z = w^T x + b\)** → linear function → outputs any real number.
- ✅ **\(\sigma(z)\)** → sigmoid function → outputs a valid probability in \((0, 1)\).

So yes—you're absolutely right: **\(z\) is the linear function that produces any real value**, and the sigmoid ensures the final prediction is a proper probability.
