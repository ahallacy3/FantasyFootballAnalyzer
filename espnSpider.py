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

        self.wait.until(EC.element_to_be_clickable((By.XPATH,'//button')))
        self.browser.switch_to_frame('disneyid-iframe');

        userInput = self.browser.find_element_by_xpath("//div[@class='field field-username-email']//input")
        userInput.send_keys(userName)
        passInput = self.browser.find_element_by_xpath("//div[@class='field field-password']//input")
        passInput.send_keys(passWord)
        loginButton = self.browser.find_element_by_xpath('//button')
        loginButton.send_keys(Keys.RETURN)

        time.sleep(5)
        self.browser.switch_to_default_content()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'games-pageheader')))

    def getData(self, weekNum, teamCount):
        seasonResults = []
        for i in range(1, weekNum + 1):
            seasonResults.append(self.getWeekData())
            if (i <= weekNum):
                self.weekNav(i + 1)
        return(seasonResults)

    def getWeekData(self):
        weekResult = []
        matchResult = []
        allScores = self.browser.find_elements_by_xpath("//td[@class='score' or @class='winning score']")
        allOwners = self.browser.find_elements_by_xpath('//span[@class="owners"]')

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
        self.url = self.url[0:len(self.url) - 1] + str(week)
        self.wait.until(EC.visibility_of_element_located((By.ID, 'global-header')))
        self.browser.get(self.url)