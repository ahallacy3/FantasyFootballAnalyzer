class trueWins:
    def getTrueWins(self, seasonResults, teamList):
        winArray = ['Real Wins']
        for team in teamList:
            wins = 0
            for week in seasonResults:
                for match in week:
                    if team == match[0]:
                        if match[1] > match[2]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck, who ties?')
                    elif team == match[3]:
                        if match[2] > match[1]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck, who ties?')
            winArray.append(wins)
        return winArray

