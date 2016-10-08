import praw

if __name__ == '__main__':
    user_agent = "earthpornworldcup 0.1 by /u/red_can_of_cocacola"
    r = praw.Reddit(user_agent=user_agent)

    countryList = ["Namibia",
                   "South Africa",
                   "Botswana",
                   "Zimbabwe",
                   "Mozambique",
                   "Lesotho",
                   "Swaziland"]

    countries = setupCountryDictionary(countryList)
    countriesScored = scoreCountryDictionary(countries)
    resultsList = getResultsList(countriesScored)

    printResults(prettifyResultsList(resultsList))


def printResults(results):
    print("And the winners are...")
    for result in results:
        print(result)


def leftPad(stringToPad):
    paddingFactor = 20 - len(stringToPad)
    padding = ' '*paddingFactor
    return "%s%s" % (stringToPad, padding)


def prettifyResultsList(resultsList):
    prettyResults = ["%s - %d" %
                     (leftPad(countryScorePair[0]), countryScorePair[1])
                     for countryScorePair in resultsList]
    return prettyResults


def getResultsList(countryDictionary):
    results = [(country, countryDictionary[country]["score"])
               for country in countryDictionary]
    return sorted(results, key=lambda x: x[1], reverse=True)


def getTestResultsList():
    results = [("South Africa", 20), ("Namibia", 23),
               ("Botswana", 12), ("Zimbabwe", 10)]
    return sorted(results, key=lambda x: x[1], reverse=True)


def scoreCountryDictionary(countryDictionary):
    for country in countryDictionary:
        print("scoring country: %s" % country)
        countrySubmissions = getTopSubmissionsFromCountryGenerator(
            countryDictionary[country]["generator"])
        countryDictionary[country]["score"] = scoreACountry(countrySubmissions)
    return countryDictionary


def scoreACountry(countrySubmissions):
    countryScore = 0
    for submission in countrySubmissions:
        try:
            countryScore += getScore(submission)
        except Exception as e:
            print(e)
    return countryScore


def getScore(search_result):
    return int(search_result.__str__().split("::")[0])


def getTopSubmissionsFromCountryGenerator(countryGenerator):
    countrySubmissions = []
    for result in countryGenerator:
        countrySubmissions.append(result)
    return countrySubmissions


def setupCountryDictionary(countryList):
    return {country: {"generator": getEarthPornCountryGenerator(country),
                      "score": 0} for country in countryList}


def getEarthPornCountryGenerator(country_name):
    return r.search(country_name, subreddit="EarthPorn", syntax="plain")
