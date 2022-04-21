# SpaceX Falcon 9's 1st Stage Rocket Prediction: Project Overview
Companies such as SpaceX, Virgin Galactic, Blue Origin, and Rocket Lab are working towards making space travel accessible and affordable for everyone. SpaceX is arguably the most successful of these companies, advertising the Falcon 9 rocket as roughly $62 million while other company rockets can cost upward of $165 million. The key behind SpaceX’s success is that 1st stage of the rocket launch, which is where the majority of costs lie, can be reused for future launches. The goal of this project is to predict when the 1st stage of the Falcon 9 rocket will land successfully so that the overall cost of a rocket launch can be better evaluated.

## Main Python Packages Used
- Jupyter Notebooks
- Pycharm
- scikit-learn
- pandas
- matplotlib
- seaborn
- BeautifulSoup4
- plotly dash
 
## Data Collection
- Data was collected using two methods:
  - Using the requests library to collect data from the SpaceX API
  -  Using the BeautifulSoup4 library to to extract Falcon 9 launch records from an HTML table on SpaceX's Wikipedia page
- The following features were extracted and used to predict the outcome of the 1st stage rocket landing:
  - Booster Version
  - Payload Mass
  - Orbit Type
  - Launch Site
  - Flights
  - Grid Fins
  - If the rocket was reused
  - Number of Uses
  - Date
  - Longitude
  - Latitude
  - Legs
  - Blocks
  
  
## Data Preprocessing
- NaN values in the "PayloadMass" column were replaced with with the mean value of the column
- Using the "Outcome" column, a "Class" column was created to represent if the landing was unsuccessful
   - 0 = unsuccessful, 1 = successful
- Removed features that seemed unnecessary to the final prediction (i.e. Data from rockets other than Falcon 9)
- Replaced categorical features with dummy variables for future calculations

## Exploratory Data Analysis
- A combination of scatter plots, bar graphs, and line graphs were used to visualize the relation between different features. Below are four graphs created in Jupyter Notebook:

![Payload vs Flight Number](https://user-images.githubusercontent.com/74473048/156845611-87633c3b-4f49-4e92-b09d-ee30220363c6.JPG)

![Flight Number vs Launch Site](https://user-images.githubusercontent.com/74473048/156844932-5d66d26b-b4a0-42f2-b0d6-fcb4c31f7559.JPG)    

![Success Rate vs Orbit Type](https://user-images.githubusercontent.com/74473048/156844984-fb3eb876-1498-4026-aed0-77098b258dd1.JPG)

![Yearly Trend](https://user-images.githubusercontent.com/74473048/156845149-c0b88e4c-ff6c-455a-ad4a-1132d21a944c.JPG)

- Insights gained from visualizing the data in Jupyter Notebook:
  - As the number of flights increase at a launch site, the number of successful outcomes increases 
  - Success rate seems to increase as the payload mass increases
  - The SSO and VLEO orbits have the highest success rates
     - I chose not to include ES-L1, GEO, and HEO due to each only having 1 therefore more data is needed 
  - Success rate to increase as the years progress 


- Below are two graphs created using the plotly dash library:


![Plotly Dashboard All Sites](https://user-images.githubusercontent.com/74473048/156847121-dab0f958-3ca4-4b23-b156-84e4db3aee68.JPG)

- Insights gained from visualizing the data using Plotly Dash:
  - Launch site KSC LC-39A had the highest success rates, followed by launch site CCAFS LC-40
  - The majority of succesful outcomes occured with payloads between 2,000kg and 6,000kg

## Predictive Analysis
- The data was split into a train and test set (80% training, 20% testing)
- The following models were used to predict the outcome of the 1st stage of the Falcon 9's rocket with the associated accuracy score:
  - Logistic Regression: 83%
  - Support Vector Machine: 83%
  - K Nearest Neighbors: 78%
  - Decision Tree: 89%
- GridSearchCV was used for each model to determine which set of parameters would yield the highest accuracy 
- Based on the results above the decision tree model should have a nearly 90% chance of predicting if the 1st stage of the Falcon 9's rocket will land successfully
 
