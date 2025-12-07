def tally(rows):
    teams = {}

    for row in rows:
        columns = row.split(";")
        if columns[0] not in teams:
            teams[columns[0]] = (0,0,0,0,0)
        if columns[1] not in teams:
            teams[columns[1]] = (0,0,0,0,0)

        score_0 = teams[columns[0]]
        score_1 = teams[columns[1]]
        
        if columns[2] == "draw":
            teams[columns[0]] = (score_0[0] + 1, score_0[1], score_0[2] + 1, score_0[3], score_0[4] + 1)
            teams[columns[1]] = (score_1[0] + 1, score_1[1], score_1[2] + 1, score_1[3], score_1[4] + 1)
        elif columns[2] == "win":
            teams[columns[0]] = (score_0[0] + 1, score_0[1] +1, score_0[2], score_0[3], score_0[4] + 3)
            teams[columns[1]] = (score_1[0] + 1, score_1[1], score_1[2], score_1[3]+1, score_1[4])
        else:
            teams[columns[0]] = (score_0[0] + 1, score_0[1], score_0[2], score_0[3]+1, score_0[4])
            teams[columns[1]] = (score_1[0] + 1, score_1[1]+1, score_1[2], score_1[3], score_1[4]+3)


    sorted_by_keys = dict(sorted(teams.items(), key=lambda item: item[0]))

    # --- Sort by values (descending) ---
    sorted_by_values_desc = dict(sorted(sorted_by_keys.items(), key=lambda item: item[1][4], reverse=True))
        
    res = []
    res.append("Team                           | MP |  W |  D |  L |  P")

    for team in sorted_by_values_desc:
        res.append(f"{team.ljust(30)} | {str(teams[team][0]).rjust(2)} | {str(teams[team][1]).rjust(2)} | {str(teams[team][2]).rjust(2)} | {str(teams[team][3]).rjust(2)} | {str(teams[team][4]).rjust(2)}")

    return res

    
