
class teams:
    def getTeams(self, seasonResults):
        teams = []
        for match in seasonResults[0]:
            teams.append(match[0])
            teams.append(match[3])
        return teams
