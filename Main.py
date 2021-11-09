import os
from os import walk
import re
import shutil

dl_directory = "../../Downloads/Videos"
series = open('Series.list').readlines()
patterns = ["(.*?).S(.\d)E(.\d).*.(\w\w\w)", "(.*?).S(.\d).E(.\d).*.(\w\w\w)"]


def fileTitle(title):
    return title.title().replace(' ', '.')


def normalTitle(title):
    return title.replace(".", ' ')


f = []


def organize(patterns):
    dl_directory: str = "/Users/Dana/Downloads/Video"
    done = 0
    log = []
    for item in os.listdir(dl_directory):
        matched = 0
        for pattern in patterns:
            p = re.compile(pattern)
            x = p.match(item)
            if x:
                matched = 1
                break
        if (not matched):
            continue
        fileName = x.group(1)
        fileSeason = x.group(2)
        fileEpisode = x.group(3)
        fileExtension = x.group(4)
        originalTitle = normalTitle(fileName)
        if not originalTitle in series:
            continue
        currentLoc = '{}/{}'.format(dl_directory, item)

        newLoc = '../../Videos/Series/{}/S{}'.format(originalTitle, fileSeason, fileEpisode, fileExtension)
        if not os.path.exists(newLoc):
            os.mkdir(newLoc)
        newPath = newLoc + '/E{}.{}'.format(fileEpisode, fileExtension)
        shutil.move(currentLoc, newPath)
        log.append([currentLoc, newPath])
        done += 1
    if (not done):
        print(
            "Nothing found to organize. If you're certain there's a new downloaded episode, try adding a precise Regex pattern.")
    else:
        print("{} files reorganized.".format(done))


print("Alright. What to do?(type `help` for more information.)")
while (1):
    command = input('>>')
    if command == 'org':
        organize(patterns)
    elif command == 'addSeries':
        title = input('-Title: ')
        correctedTitle = title.title()
        with open('Series.list', 'a') as file:
            if (len(series) == 0):
                file.write(correctedTitle)
            else:
                file.write('\n' + correctedTitle)
            seriesLoc = '../../Videos/Series/{}/'.format(correctedTitle)
            os.mkdir(seriesLoc)
            series.append(correctedTitle)
    elif command == 'listSeries':
        print(series)
    elif command == 'help':
        print('Available Commands:', "-listSeries  :  Lists the series previously indexed.",
              "-org         :  Sorts downloaded episodes.", "-addSeries   :  Index a new series title.",
              "-quit        :  Exits the program.", sep="\n")
    elif (command == 'quit'):
        break
        exit('See u next time.')
    else:
        print("Command not found!")
