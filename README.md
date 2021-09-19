
# Store Sales Prediction

Nowadays, shopping malls and Big Marts keep track of individual item sales data in
order to forecast future client demand and adjust inventory management. In a data
warehouse, these data stores hold a significant amount of consumer information and
particular item details. By mining the data store from the data warehouse, more
anomalies and common patterns can be discovered.
So, We have build a solution which is able to predict the sales of the
different stores of Big Mart according to the provided dataset.

# Dataset

Dataset Link: - https://www.kaggle.com/brijbhushannanda1979/bigmart-sales-data

We have train (8523) and test (5681) data set, train data set has both input and output
variable(s). We need to predict the sales for test data set.

Item_Identifier: Unique product ID

Item_Weight: Weight of product

Item_Fat_Content: Whether the product is low fat or not

Item_Visibility: The % of total display area of all products in a store allocated to the
particular product

Item_Type: The category to which the product belongs

Item_MRP: Maximum Retail Price (list price) of the product

Outlet_Identifier: Unique store ID

Outlet_Establishment_Year: The year in which store was established

Outlet_Size: The size of the store in terms of ground area covered

Outlet_Location_Type: The type of city in which the store is located

Outlet_Type: Whether the outlet is just a grocery store or some sort of supermarket

Item_Outlet_Sales: Sales of the product in the particulat store. This is the outcome
variable to be predicted.


## Screenshots
#### Home Page
![App Screenshot](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Images/home_page.png?raw=true)

#### Input Page
![App Screenshot](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Images/predict_page.png?raw=true)

#### Prediction Page
![App Screenshot](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Images/result_page.png?raw=true)
## Demo


[![Watch the video](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Images/demo%20thumbnail.png?raw=true)](https://youtu.be/2FjLsIOO5nU)
  
## Run Locally

Clone the project

```
  git clone https://github.com/scorpion-varun/Store-Sales-Prediction-Project
```

Go to the project directory

```
  cd StoreSalesPrediction
```

Install dependencies

```
  pip install -r requirements.txt
```

Start the server

```
  python manage.py runserver
```

  
## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Python

**Framework:** Django

**Hosting Platform:** Heroku

  
## Documentation

[High Level Document](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Documentation/High_Level_Design.docx)


[Low Level Document](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Documentation/Low_Level_Design.docx)


[Wireframe](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Documentation/Wireframe.docx)

[Deatiled Project Report](https://github.com/scorpion-varun/Store-Sales-Prediction-Project/blob/main/Documentation/Detailed%20Project%20Report.pptx)

  
