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
- dash
- plotly
 
## Data Collection
- Data was collected using to methods:
  - Using the requests library to collect data from the SpaceX API
  -  Using the BeautifulSoup4 library to to extract Falcon 9 launch records from an HTML table on Wikipedia
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

## Exploratory Data Analysis




