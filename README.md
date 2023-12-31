# wine_ing


---
## Project Description 
The data science team assisting the California Wine Institute is interested to see if clustering the wine data will produce better results. The data will be clustered accordingly and the working team will report findings.

## Project Goals
---
- Discover independence of features within data
- Utilizing said features to develop machine learning models that will determine the quality of wine 
- Determine the drivers of quality
- The insights discovered will be used to estimate quality and provide a more robust understanding of the attributes of a the wine and it's associated quality

## Initial Thoughts
--- 
The drivers will likely have an equal weight when determining the quality -- this will be due to the quality likely scored by a professional who is cognizant of their biasis and would like to score on an objective scale. There will still likely be clusters based on data for the wines, since different wines will share qualities. 

## Planning
--- 
1. Acquire data from 
    * data.world
2. Prepare data accordingly for exploration & machine learning needs
    * Creating dummy columns of multi categorical data
    * Cleaning numeric data
    * spliting the data 
3. Explore data for assocations with quality
    * Determine our baseline prediction
    * Determine which features would be best to cluster
    * Create new column of clustered data
    * scale data appropriately
4. Develop a model to further understand
    * Use Classification ML models
    * Use various models to determine what algorithm are best for the data
    * Select best model based on evaluation metrics
    * Evaluate all models on respective test data
 

## Data Dictionary
--- 
| Feature        | Definition                                   |
| ---            | ---                                          |
| fixed_acidity  | calculated fixed acidity - organic acids|
| volatile_acidity  | calculated volatile acidity - steam distillable acids |
| citric_acid   |the amount of citric acid - provide haze|
| residual_sugar  | the amount of residual sugar - (leftover sugars after fermentation)|
| chlorides  | the amount of sodium chlorides |
| free_sulfur_dioxide | free sulfur dioxide content - free sulfur reaction agents |
| total_sulfur_dioxide | total sulfur dioxide content - free and other SO2 levels|
| density | density value - denotes fermentation conditions and yeast growth|
| ph | ph level - acidity|
| sulfite | sulphate content|
| alcohol | alcohol content|
| quality | rating given by wine sommelier|



## Reproducability Requirements
---
1. Clone repo
2. Run notebook

## Conclusions 
 * In conclusion after going through our tests and modeling along with our vizualiziations we have come to the conclusion based on the information given that alcohol was a main driver for quality. 
 * It is difficult to predict accurately more main drivers for quality due to human elements when it comes to wine. We as well did notice alot of our data overall was white wine. 
 * I think there are some factors to include in your continued research. Like types of grapes location and how long to ferment are just a few other factors that may need to be considered when seeing what makes a good quality wine. 



---