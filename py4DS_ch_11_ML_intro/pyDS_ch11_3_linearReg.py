
################# 15.1:
# copy: 
#       
#   
#
################# (22-Jun-25 for 24-Jun-25)

# Courses: PrTla PY for DS & ML >  15.1 (ipynb), 15.3, 15.4, 15.5, 14.6  >>  details in ipynb





1. In **late September 2016**, **scikit-learn version 0.18** was released.

1. A small change was made:

   * The `train_test_split` function is now imported from `model_selection` instead of `cross_validation`.

1. Old code:


from sklearn.cross_validation import train_test_split


1.  New code:


from sklearn.model_selection import train_test_split


1. The latest course notes use the new method, but some older videos may still show the old one.

1. You can still use the old method — but you’ll see a **warning message** about the update.

1. The same change happened for `GridSearchCV` (covered later in the course).


