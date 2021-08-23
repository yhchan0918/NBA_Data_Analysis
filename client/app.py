import streamlit as st
import requests
import json
import pandas as pd


def run():
    # Collects user input features into dataframe

    st.title("NBA Game Classifier")
    st.sidebar.markdown(
        """
[Example CSV input file](https://raw.githubusercontent.com/yhchan0918/NBA_Data_Analysis/main/data/example.csv)
"""
    )
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df)
        input_data = json.loads(df.to_json(orient="records", lines=True))
    else:

        def user_input_features():
            G_home = st.number_input("Number of games played on the season of Home Team")
            W_PCT_home = st.number_input("Win % on current season of Home Team")
            HOME_RECORD_home = st.number_input("Home record on the current season of Home Team")
            ROAD_RECORD_home = st.number_input("Road record on the current season of Home Team")
            W_PCT_prev_home = st.number_input("Win % on previous season of Home Team")
            HOME_RECORD_prev_home = st.number_input(
                "Home record on the previous season of Home Team"
            )
            ROAD_RECORD_prev_home = st.number_input(
                "Road record on the previous season of Home Team"
            )
            G_away = st.number_input("Number of games played on the current season by Away Team")
            W_PCT_away = st.number_input("Win % on current season of Away Team")
            HOME_RECORD_away = st.number_input("Home record on the current season of Away Team")
            ROAD_RECORD_away = st.number_input("Road record on the current season of Away Team")
            W_PCT_prev_away = st.number_input("Win % on previous season of Away Team")
            HOME_RECORD_prev_away = st.number_input(
                "Home record on the previous season of Away Team"
            )
            ROAD_RECORD_prev_away = st.number_input(
                "Road record on the previous season of Away Team"
            )
            WIN_PRCT_home_3g = st.number_input("Mean Win % on previous 3 games of Home Team")
            PTS_home_3g = st.number_input(
                "Mean Number of points scored by Home Team on previous 3 games"
            )
            FG_PCT_home_3g = st.number_input(
                "Mean Field Goal Percentage by Home Team on previous 3 games"
            )
            FT_PCT_home_3g = st.number_input(
                "Mean Free Throw Percentage by Home Team on previous 3 games"
            )
            FG3_PCT_home_3g = st.number_input(
                "Mean Three Point Percentage by Home Team on previous 3 games"
            )
            AST_home_3g = st.number_input("Mean Assists by Home Team on previous 3 games")
            REB_home_3g = st.number_input("Mean Rebounds by Home Team on previous 3 games")
            WIN_PRCT_away_3g = st.number_input("Mean Win % by Away Team on previous 3 games")
            PTS_away_3g = st.number_input(
                "Mean Number of points scored by Away Team on previous 3 games"
            )
            FG_PCT_away_3g = st.number_input(
                "Mean Field Goal Percentage by Away Team on previous 3 games"
            )
            FT_PCT_away_3g = st.number_input(
                "Mean Free Throw Percentage by Away Team on previous 3 games"
            )
            FG3_PCT_away_3g = st.number_input(
                "Mean Three Point Percentage by Away Team on previous 3 games"
            )
            AST_away_3g = st.number_input("Mean Assists by Away Team on previous 3 games")
            REB_away_3g = st.number_input("Mean Rebounds by Away Team on previous 3 games")
            WIN_PRCT_home_10g = st.number_input("Mean Win % on previous 10 games of Home Team")
            PTS_home_10g = st.number_input(
                "Mean Number of points scored by Home Team on previous 10 games"
            )
            FG_PCT_home_10g = st.number_input(
                "Mean Field Goal Percentage by Home Team on previous 10 games"
            )
            FT_PCT_home_10g = st.number_input(
                "Mean Free Throw Percentage by Home Team on previous 10 games"
            )
            FG3_PCT_home_10g = st.number_input(
                "Mean Three Point Percentage by Home Team on previous 10 games"
            )
            AST_home_10g = st.number_input("Mean Assists by Home Team on previous 10 games")
            REB_home_10g = st.number_input("Mean Rebounds by Away Team on previous 10 games")
            WIN_PRCT_away_10g = st.number_input("Mean Win % by Away Team on previous 10 game")
            PTS_away_10g = st.number_input(
                "Number of points scored by Away Team on previous 10 games"
            )
            FG_PCT_away_10g = st.number_input(
                "Mean Field Goal Percentage by Away Team on previous 10 games"
            )
            FT_PCT_away_10g = st.number_input(
                "Mean Free Throw Percentage by Away Team on previous 10 game"
            )
            FG3_PCT_away_10g = st.number_input(
                "Mean Three Point Percentage by Away Team on previous 10 games"
            )
            AST_away_10g = st.number_input("Mean Assists by Away Team on previous 10 games")
            REB_away_10g = st.number_input("Mean Rebounds by Away Team on previous 10 game")

            data = {
                "G_home": G_home,
                "W_PCT_home": W_PCT_home,
                "HOME_RECORD_home": HOME_RECORD_home,
                "ROAD_RECORD_home": ROAD_RECORD_home,
                "W_PCT_prev_home": W_PCT_prev_home,
                "HOME_RECORD_prev_home": HOME_RECORD_prev_home,
                "ROAD_RECORD_prev_home": ROAD_RECORD_prev_home,
                "G_away": G_away,
                "W_PCT_away": W_PCT_away,
                "HOME_RECORD_away": HOME_RECORD_away,
                "ROAD_RECORD_away": ROAD_RECORD_away,
                "W_PCT_prev_away": W_PCT_prev_away,
                "HOME_RECORD_prev_away": HOME_RECORD_prev_away,
                "ROAD_RECORD_prev_away": ROAD_RECORD_prev_away,
                "WIN_PRCT_home_3g": WIN_PRCT_home_3g,
                "PTS_home_3g": PTS_home_3g,
                "FG_PCT_home_3g": FG_PCT_home_3g,
                "FT_PCT_home_3g": FT_PCT_home_3g,
                "FG3_PCT_home_3g": FG3_PCT_home_3g,
                "AST_home_3g": AST_home_3g,
                "REB_home_3g": REB_home_3g,
                "WIN_PRCT_away_3g": WIN_PRCT_away_3g,
                "PTS_away_3g": PTS_away_3g,
                "FG_PCT_away_3g": FG_PCT_away_3g,
                "FT_PCT_away_3g": FT_PCT_away_3g,
                "FG3_PCT_away_3g": FG3_PCT_away_3g,
                "AST_away_3g": AST_away_3g,
                "REB_away_3g": REB_away_3g,
                "WIN_PRCT_home_10g": WIN_PRCT_home_10g,
                "PTS_home_10g": PTS_home_10g,
                "FG_PCT_home_10g": FG_PCT_home_10g,
                "FT_PCT_home_10g": FT_PCT_home_10g,
                "FG3_PCT_home_10g": FG3_PCT_home_10g,
                "AST_home_10g": AST_home_10g,
                "REB_home_10g": REB_home_10g,
                "WIN_PRCT_away_10g": WIN_PRCT_away_10g,
                "PTS_away_10g": PTS_away_10g,
                "FG_PCT_away_10g": FG_PCT_away_10g,
                "FT_PCT_away_10g": FT_PCT_away_10g,
                "FG3_PCT_away_10g": FG3_PCT_away_10g,
                "AST_away_10g": AST_away_10g,
                "REB_away_10g": REB_away_10g,
            }

            return data

        input_data = user_input_features()

    if st.button("Predict"):
        response = requests.post("http://server:8000/predict", json=input_data)
        prediction = response.text
        st.success(f"The prediction from model: {prediction}")


if __name__ == "__main__":
    # by default it will run at 8501 port
    run()
