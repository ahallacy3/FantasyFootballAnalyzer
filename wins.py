class wins:
    def trueWins(self, seasonResults, teamList):
        winArray = ['Real Wins']
        for team in teamList:
            wins = 0
            for week in seasonResults:
                for match in week:
                    if team == match[0]:
                        if match[1] > match[2]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
                    elif team == match[3]:
                        if match[2] > match[1]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
            winArray.append(wins)
        return winArray

    def winsAgainstEveryone(self, seasonResults, teamList):
        winArray = []
        for team in teamList:
            wins = 0
            for week in seasonResults:
                for match in week:
                    if team == match[0]:
                        if match[1] > match[2]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
                    elif team == match[3]:
                        if match[2] > match[1]:
                            wins += 1
                        elif match[1] == match[2]:
                            print('what the fuck')
            winArray.append(wins)
        return winArray

    def winsAgainstEveryoneByWeek(self, teamScores, team, week):
        score = 0
        wae = 0
        for teamScore in teamScores:
            if teamScore[0] == team:
                score = teamScore[week]
        for teamScore in teamScores:
            if score > teamScore[week]:
                wae += 1
        return wae

    def totalWinsAgainstEveryone(self, teamScores):
        waeArray = ['Wins Against Everyone']
        for team in teamScores:
            wae = 0
            for i in range(1, len(team)):
                wae += self.winsAgainstEveryoneByWeek(teamScores, team[0], i)
            waeArray.append(wae)
        return waeArray

    def normalizedWinsAgainstEveryone(self, wae):
        nwae = ['Normalized WAE']
        for i in range(1, len(wae)):
            nwae.append('%.1f' % (wae[i] / (len(wae) - 2)))
        return nwae

