import os
import time
from shutil import copy2

import config
import UtilityFunctions as uf


allFilesWorking: list[str] = uf.searchDirectory(config.workingDirectory, 1)
allFoldersWorking: list[str] = uf.searchDirectory(config.workingDirectory, 0)
allFilesBackup: list[str] = uf.searchDirectory(config.backupDirectory, 1)
allFoldersBackup: list[str] = uf.searchDirectory(config.backupDirectory, 0)
mostRecentModifiedDateWorking = 0
mostRecentModifiedDateBackup = 0
for mainFolder in os.listdir(config.workingDirectory):
    mostRecentModifiedDateWorking = 0
    for file in allFilesWorking:
        if file.startswith(config.workingDirectory + config.folderSeperator + mainFolder + config.folderSeperator):
            if os.path.getmtime(file) >= mostRecentModifiedDateWorking:
                mostRecentModifiedDateWorking = os.path.getmtime(file)
            elif os.path.getctime(file) > mostRecentModifiedDateWorking:
                mostRecentModifiedDateWorking = os.path.getctime(file)
    mostRecentModifiedDateBackup = 0
    for file in allFilesBackup:
        if file.startswith(config.backupDirectory + config.folderSeperator + mainFolder + config.folderSeperator):
            if os.path.getmtime(file) >= mostRecentModifiedDateBackup:
                mostRecentModifiedDateBackup = os.path.getmtime(file)
            elif os.path.getctime(file) > mostRecentModifiedDateBackup:
                mostRecentModifiedDateBackup = os.path.getctime(file)
    if mostRecentModifiedDateWorking > mostRecentModifiedDateBackup and mostRecentModifiedDateWorking > 0:
        # Checking python files for new import statements
        currentImportsBackup: list[str] = uf.findImports(allFilesBackup, config.backupDirectory + config.folderSeperator + mainFolder + config.folderSeperator)
        currentImportsWorking: list[str] = uf.findImports(allFilesWorking, config.workingDirectory + config.folderSeperator + mainFolder + config.folderSeperator)
        newImports: list[str] = []
        for currentImport in currentImportsWorking:
            if not currentImport in currentImportsBackup:
                newImports.append(currentImport)
        if config.verboseLogs:
            print("Notification - New import statements detected:", newImports)
        # Setting end directory to copy to
        endMainFolder: str = mainFolder + config.folderSeperator + time.strftime('%Y-%m-%d', time.localtime(mostRecentModifiedDateWorking)) + config.folderSpace + time.strftime('%H-%M-%S', time.localtime(mostRecentModifiedDateWorking))
        # Adding each new import statement to the end if any
        if len(newImports) > 0 and len(currentImportsBackup) > 0:
            for newImport in newImports:
                if len(config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSpace + newImport) <= config.folderNameMaxLen:
                    endMainFolder = endMainFolder + config.folderSpace + newImport
                else:
                    break
        if config.verboseLogs:
            print("Notification - End backup folder name:", endMainFolder)
        if not os.path.exists(config.backupDirectory + config.folderSeperator + mainFolder + config.folderSeperator):
            print("Notification - Main Folder Created:", config.backupDirectory + config.folderSeperator + mainFolder + config.folderSeperator)
            os.mkdir(config.backupDirectory + config.folderSeperator + mainFolder)
        if not os.path.exists(config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator):
            print("Notification - Subfolder Created:", config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator)
            os.mkdir(config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator)
        for file in allFilesWorking:
            if file.startswith(config.workingDirectory + config.folderSeperator + mainFolder + config.folderSeperator):
                destination: str = (file.replace((config.workingDirectory + config.folderSeperator + mainFolder + config.folderSeperator), (config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator)))
                destinationFolder: str = destination.rsplit(config.folderSeperator, 1)[0] + config.folderSeperator
                if not os.path.exists(file.replace(config.workingDirectory + config.folderSeperator, config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator)):
                    currentPath: str = config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator
                    foldersSanitized: str = destinationFolder.replace(config.backupDirectory + config.folderSeperator + endMainFolder + config.folderSeperator, "")
                    foldersTo: list[str] = foldersSanitized.split(config.folderSeperator)
                    if len(foldersTo) > 0:
                        for folder in foldersTo:
                            if len(folder) > 0:
                                currentPath = currentPath + folder + config.folderSeperator
                                if not os.path.exists(currentPath):
                                    print("Notification - Creating Subfolder:", currentPath)
                                    os.mkdir(currentPath)
                if not os.path.exists(destination):
                    print("Notification - Copying file:", destination)
                    copy2(file, destination)
exit()
