# HousePricePrediction-Using-Random-Forest-Reg-Deployment-via-Flask

## Disclaimer :  Usually Data Science utilizes visualization aids as Jupyter notebook to help understand accuracy, loss and whether there is any risk of overfitting in the model. For this project, I have omitted this, as the main focus is to understand how to establish packages ready for deployment. This is due to the code structure being a bit different in notebooks vs IDE and IDLE platforms.

## The Flask deployment is very simple, and its initial focus as a Data Scientist is how to provide a Minimum Viable Product.

## We have imported the RandomForestRegressor as it is best suited for numerical predictions. I have not explored tuning the hyperparameters due to my local machine not coping. However, you can play with an tweak: "Maximum Depth of Trees", "Increase or Decrease the Number of Estimators", "Specify the Number of Features to be Included at each Node Split".
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
https://www.keboola.com/blog/random-forest-regression



## Against best practice, I cut off my tree depth at 6, due to size and the focus being on deployment.

# ADVICE ON IMPROVEMENTS 

## I would, first create the breakdown in Jupyter notebooks to explore. Then I would, tweak and play with hyperparameters, finally I would create the files in this directory for deployment.

## If interested, further development of the end user API would be a interesting development.
