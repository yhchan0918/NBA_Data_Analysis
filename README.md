# What is NBA
* The National Basketball Association (NBA) is a professional basketball league in North America. It is the premier men's professional basketball league in the world

# NBA Data Analysis & NBA Game Winner Team Estimator: Project Overview
* Created a NBA Game Winner Team Estimator to determine the winner team based on previous data for home team and away team from Season 2003 - 2020
* Managed to achieve 0.6968 ROC AUC score with the Logistic Regression model
* Optimized KNN, Logistic Regression, Random Forest Classifiers and XGBoost using GridsearchCV to reach the best model. 
* Built backend API using FastAPI & Built frontend app using Streamlit
* Live Project Link: https://nba-game-predict-app.herokuapp.com/

## Data Source
https://www.kaggle.com/nathanlauga/nba-games

## Data Cleaning
- Every row has 43 columns. Note: Record is calucated by total wins over sum of total wins and total losses
- Columns: Meaning
GAME_ID: ID of match                 
G_home: Number of games played on the season of Home Team                    
W_PCT_home: Win % on current season of Home Team                     
HOME_RECORD_home: Home record on the current season of Home Team        
ROAD_RECORD_home: Road record on the current season of Home Team        
W_PCT_prev_home: Win % on previous season of Home Team         
HOME_RECORD_prev_home: Home record on the previous season of Home Team          
ROAD_RECORD_prev_home: Road record on the previous season of Home Team          
G_away: Number of games played on the current season by Away Team                 
W_PCT_away: Win % on current season of Away Team              
HOME_RECORD_away: Home record on the current season of Away Team         
ROAD_RECORD_away: Road record on the current season of Away Team        
W_PCT_prev_away: Win % on previous season of Away Team         
HOME_RECORD_prev_away: Home record on the previous season of Away Team   
ROAD_RECORD_prev_away: Road record on the previous season of Away Team    
WIN_PRCT_home_3g: Mean Win % on previous 3 games of Home Team        
PTS_home_3g: Mean Number of points scored by Home Team on previous 3 games             
FG_PCT_home_3g: Mean Field Goal Percentage by Home Team on previous 3 games         
FT_PCT_home_3g: Mean Free Throw Percentage by Home Team on previous 3 games         
FG3_PCT_home_3g: Mean Three Point Percentage by Home Team on previous 3 games        
AST_home_3g: Mean Assists by Home Team on previous 3 games             
REB_home_3g: Mean Rebounds by Home Team on previous 3 games             
WIN_PRCT_away_3g: Mean Win % by Away Team on previous 3 games      
PTS_away_3g: Mean Number of points scored by Away Team on previous 3 games             
FG_PCT_away_3g: Mean Field Goal Percentage by Away Team on previous 3 games           
FT_PCT_away_3g: Mean Free Throw Percentage by Away Team on previous 3 games          
FG3_PCT_away_3g: Mean Three Point Percentage by Away Team on previous 3 games         
AST_away_3g: Mean Assists by Away Team on previous 3 games             
REB_away_3g: Mean Rebounds by Away Team on previous 3 games             
WIN_PRCT_home_10g: Mean Win % on previous 10 games of Home Team       
PTS_home_10g: Mean Number of points scored by Home Team on previous 10 games            
FG_PCT_home_10g: Mean Field Goal Percentage by Home Team on previous 10 games         
FT_PCT_home_10g: Mean Free Throw Percentage by Home Team on previous 10 games         
FG3_PCT_home_10g: Mean Three Point Percentage by Home Team on previous 10 games        
AST_home_10g: Mean Assists by Home Team on previous 10 games            
REB_home_10g: Mean Rebounds by Away Team on previous 10 games            
WIN_PRCT_away_10g: Mean Win % by Away Team on previous 10 game       
PTS_away_10g: Mean Number of points scored by Away Team on previous 10 games            
FG_PCT_away_10g: Mean Field Goal Percentage by Away Team on previous 10 games         
FT_PCT_away_10g: Mean Free Throw Percentage by Away Team on previous 10 game         
FG3_PCT_away_10g: Mean Three Point Percentage by Away Team on previous 10 games         
AST_away_10g: Mean Assists by Away Team on previous 10 games             
REB_away_10g: Mean Rebounds by Away Team on previous 10 game            
GAME_DATE_EST: Game's date           
SEASON: Season when the game occured                  
HOME_TEAM_WINS: Have Home Team Win(Target Variable)   

## EDA
I have done some EDA for final games data. Out of curiousity, I have done EDA regarding LeBron's stats. Below are some highlights

### Overall Games From All Seasons
![alt text](https://github.com/yhchan0918/NBA_Data_Analysis/blob/main/images/home_win%25_relationship.png "Relationship between Win % on previous games and Win % on current game for Home Team")
![alt text](https://github.com/yhchan0918/NBA_Data_Analysis/blob/main/images/away_win%25_relationship.png "Relationship between Win % on previous games and Win % on current game for Away Team")

### LeBron's stats
![alt text](https://github.com/yhchan0918/NBA_Data_Analysis/blob/main/images/bron_free_throw_percentage_per_game_each_season.png "Bron's Free Throw Percentage Per Game Each Season")
![alt text](https://github.com/yhchan0918/NBA_Data_Analysis/blob/main/images/bron_vs_others.png "Lebron's Stats vs Other Players Since 2003")


## Model Building 

First, I use season 2004 - 2018 as train set while season 2019 as test set. I ignore data from season 2020 because of covid-19 which is an unexpected variable & causing the games in season 2020 not relatively balanced. After that, I have prepared standard-scaled data for Logistic Regression model and minmax-scaled data for K-Nearest Neighbors model.

I tried four different models and evaluated them using ROC AUC score. I chose ROC AUC score as the dataset has almost balanced classes which is relatively suitable. Also, its more clearer to check the ability of model to classify true-positive & true-negative.  

I tried four different models:
*	**Logistic Regression** 
*	**K-Nearest Neighbors** 
*	**Random Forest**
*	**XGboost**

## Model performance
The Logistic Regression model slightly outperformed the other approaches using cross validation evaluation
*	**Logistic Regression** : ROC AUC score = 0.6968
*	**K-Nearest Neighbors** : ROC AUC score = 0.6496
*	**Random Forest**.      : ROC AUC score = 0.6959
*	**XGboost**             : ROC AUC score = 0.6961

## Productionization 
In this step, I built a FastAPI backend endpoint & frontend app using Streamlit. Both backend and frontend app are deployed using docker. In the end, both are deployed live using Heroku. The API endpoint takes in a request with a list of values from a home team's stats & away team's stats and returns an estimated outcome of the current game. 

      
