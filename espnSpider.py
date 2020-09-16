import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class espnSpider():

    def __init__(self, url):
        self.browser = webdriver.Firefox()
        self.url = url
        self.wait = WebDriverWait(self.browser, 10)


    def login(self, userName, passWord):
        # url should look like http://games.espn.com/ffl/scoreboard?leagueId=1322187&matchupPeriodId=1
        self.browser.get(self.url)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="Button Button--default Button--custom ml4"]')))
        self.browser.switch_to_frame('disneyid-iframe');

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='field field-username-email badgeable']//input")))

        userInput = self.browser.find_element_by_xpath("//div[@class='field field-username-email badgeable']//input")
        userInput.send_keys(userName)
        passInput = self.browser.find_element_by_xpath("//div[@class='field field-password badgeable']//input")
        passInput.send_keys(passWord)
        loginButton = self.browser.find_element_by_xpath('//button')
        loginButton.send_keys(Keys.RETURN)

        time.sleep(10)
        self.browser.switch_to_default_content()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'league-scoreboard-page')))

    def getData(self, weekNum):
        seasonResults = []
        for i in range(1, weekNum + 1):
            seasonResults.append(self.getWeekData())
            if (i <= weekNum):
                self.weekNav(i + 1)
        self.browser.close();
        print(seasonResults)
        return(seasonResults)

    def getWeekData(self):
        weekResult = []
        matchResult = []
        allOwners = self.browser.find_elements_by_xpath(
            "//div[@class='ScoreCell__TeamName ScoreCell__TeamName--shortDisplayName truncate db']")
        allScores = self.browser.find_elements_by_xpath(
            '//div[@class="ScoreCell__Score h4 clr-gray-01 fw-heavy tar ScoreCell_Score--scoreboard pl2"]')

        i = 0
        while i < len(allScores):
            matchResult.append(allOwners[i].text)
            matchResult.append(float(allScores[i].text))
            i += 1
            matchResult.append(float(allScores[i].text))
            matchResult.append(allOwners[i].text)
            i += 1
            weekResult.append(matchResult)
            matchResult = []
        return weekResult

    def weekNav(self, week):
        self.url = self.url[0:self.url.find('&mSPID') - 1] + str(week) + '&mSPID=' + str(week)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'league-scoreboard-page')))
        self.browser.get(self.url)