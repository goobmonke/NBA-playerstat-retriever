from nba_api.stats.endpoints import leaguedashplayerstats
import time
import matplotlib.pyplot as plt





while True:
    year = input("What year would you like to see player statistics for? q to quit ")
    if year == "q":
        break
    stat = input("Would you like to visualize a specific statistic for all nba players? y/n ").lower()

    data = leaguedashplayerstats.LeagueDashPlayerStats(season = year, per_mode_detailed="PerGame",season_type_all_star="Regular Season")
    df = data.get_data_frames()[0]
    minutesplayed = int(input("Minimum Minutes Played: (Suggested: 15) "))
    gamesplayed = int(input("Minimum Games Played: (Suggested: 20) "))

    df = df[(df['GP'] >= gamesplayed) & (df['MIN'] >= minutesplayed)]
    df = df[df['TEAM_ID'].between(1610612737, 1610612766)]


    df = df.sort_values("GP", ascending=False).drop_duplicates("PLAYER_NAME")

    players = []
    mins = []
    pts = []
    if stat == "y":
 
        state = input("What statistic would you like to visualize for all nba players? pts/reb/ast/blk/stl/fg_pct/fg3_pct/ft_pct/min/gp/fg3m/fgm ").upper()
        threshold = float(input("What is your statistic minimum? (e.g at least 20 points per game) Please enter a number: "))
        df = df[df['TEAM_ID'].between(1610612737, 1610612766)]

        scores = df[df[f'{state}'] >= threshold]

        for i, rows in scores.iterrows():
        
            print(f"{rows['PLAYER_NAME']}: {rows[state]:.1f} Per Game")
            players.append(rows['PLAYER_NAME'])
            mins.append(rows["MIN"])
            pts.append(rows[state])


        graph = input("Would you like to see a graph of your stat sheet? y/n ").lower()
        if graph == "y":
            plt.scatter(mins,pts,s=5)
            for index in range(0,len(mins)):
                plt.text(mins[index], pts[index], players[index], fontsize = 7)
            plt.xlabel("Minutes Played")
            plt.ylabel(state)
            plt.show()

            
    see = input("Would you like to see the statistics of a specific player? y/n ").lower()
    
    if see == "y":
        while True:
            g = input("What player would you like to see statistics for? (Case and accent sensitive) q to quit ")
            if g =="q":
                break
            try:
                player = df[df["PLAYER_NAME"] == g]
                stats = player.iloc[0]
                print(f"Player: {stats['PLAYER_NAME']}")
                print(f"PPG: {stats['PTS']:.1f}")
                print(f"AST: {stats['AST']:.1f}")
                print(f"REB: {stats['REB']:.1f}")
                print(f"BLK: {stats['BLK']:.1f}")
                print(f"STL: {stats['STL']:.1f}")
                print(f"FG%: {stats['FG_PCT'] * 100:.1f}")
                print(f"FG3%: {stats['FG3_PCT'] * 100:.1f}")
                print(f"FT% {stats['FT_PCT'] *100:.1f}")
                print(f"GP: {stats['GP']}")
                print(f"MIN: {stats['MIN']:.1f}")
                print(f"3PM: {stats["FG3M"]:.1f}")
                print(f"FGM: {stats["FGM"]:.1f}")
            except:
                print("Couldn't find that player")
