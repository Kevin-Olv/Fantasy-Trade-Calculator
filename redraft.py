{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"redraft.py","provenance":[],"collapsed_sections":[],"authorship_tag":"ABX9TyOGx7n+QrvXzalVElroJMpx"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"code","metadata":{"id":"8IUuAoqRfmMq"},"source":["position = playerStats[1]\n","num_teams = leagueInfo = [1]\n","value = 0.0\n","value = float(value)\n","rookie = input(\"Is the player a rookie?\\n\")\n","if position != \"QB\" and position != \"RB\" and position != \"WR\" and position != \"TE\":\n","    print(f'Invalid input\\n')\n","    quit()\n","if rookie == \"yes\":\n","    #draft round\n","    draft_round = int(input(\"What round were they drafted in?\\n\"))\n","    if position == \"QB\":\n","        if draft_round == 1:\n","            value = 3000\n","        elif draft_round == 2:\n","            value = 1500\n","        elif draft_round == 3:\n","            value = 500\n","        elif draft_round == 4 or draft_round == 5:\n","            value = 200\n","        elif draft_round == 6 or draft_round == 7:\n","            value = 100\n","        else:\n","            print(f'Inalid input\\n')\n","            quit()\n","    else:\n","        if draft_round == 1:\n","            value = 1500\n","        elif draft_round == 2:\n","            value = 750\n","        elif draft_round == 3:\n","            value = 150\n","        elif draft_round == 4 or draft_round == 5:\n","            value = 100\n","        elif draft_round == 6 or draft_round == 7:\n","            value = 50\n","        else:\n","            print(f'Inalid input\\n')\n","            quit()\n","elif rookie == \"no\":\n","    touchdowns = float(player[21])\n","    yards = float(player[7]+player[11]+player[16])\n","    games_season = 16\n","    games_played = float(player[3])\n","    league_scoring = leagueInfo[0];\n","    #previous years stats\n","    if position == \"QB\":\n","        value = float(0.4*yards) + (55*touchdowns)\n","    else:\n","        value = float(yards + (125*touchdowns))\n","    #fantays points\n","    if league_scoring == \"PPR\":\n","        ppr_score = float(player[25])\n","        value = float(value + (2*ppr_score))\n","    elif league_scoring == \"standard\":\n","        standard_score = float(player[24])\n","        value = float(value + (2*standard_score))\n","    else:\n","        print(f'Invalid input\\n')\n","        quit()\n","    #availability\n","    value = float(value*((games_played + 1)/games_season))\n","else: \n","    print(f'Invalid input\\n')\n","    quit()\n","#league settings\n","if position == \"QB\":\n","    num_QB = float(leagueInfo[4])\n","    if num_QB == 2:\n","        value = 1.5*float(value)\n","if num_teams != 10:\n","    value = (value*(float(num_teams)/10.0))\n","return value"],"execution_count":null,"outputs":[]}]}