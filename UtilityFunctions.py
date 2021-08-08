import os
import config


# Compiling a list of all files in a directory including subdirecties
def searchDirectory(argWorkdingDirectory: [str], argFileFolder: [int] = 0):
    foldersListed: list[str] = [argWorkdingDirectory]
    filesListed: list[str] = []
    foldersLen: int = 0
    foldersLenNew: int = -1
    currentFileDirectory: str = argWorkdingDirectory
    while foldersLen > foldersLenNew :
        foldersLen = foldersLenNew
        if len(foldersListed) > 0:
            for folder in foldersListed:
                currentFileDirectory = folder
                for fileFolder in os.listdir(currentFileDirectory):
                    currentFilePath: str = currentFileDirectory + config.folderSeperator + fileFolder
                    if os.path.isfile(currentFilePath) and currentFilePath not in filesListed:
                        valid: bool = False
                        for extension in config.acceptedExtensions:
                            if currentFilePath.rsplit(".", 1)[1] == extension:
                                valid = True
                        if valid:
                            filesListed.append(currentFilePath)
                    if os.path.isdir(currentFilePath) and currentFilePath not in foldersListed:
                        foldersListed.append(currentFilePath)
    if argFileFolder == 0:
        if config.verboseLogs:
            print(len(foldersListed))
            print("Notification - Folders:", foldersListed)
        return foldersListed
    else:
        if config.verboseLogs:
            print(len(filesListed))
            print("Notification - Files:", filesListed)
        return filesListed

# Checking python files in a list for any import or def statements
def findImports(argAllFilesList: list, argSubDirectory: str = ""):
    currentImports: list[str] = []
    for file in argAllFilesList:
        if file.startswith(argSubDirectory):
            for extension in config.inspectExtensions:
                if file.endswith(extension):
                    with open(file) as f:
                        lines = [line.rstrip() for line in f]
                        for line in lines:
                            for statement in config.statementsImport:
                                if line.startswith(statement):
                                    tempLine: str = line.split("#", 1)[0].split("as ", 1)[0]
                                    for statement2 in config.statementsImport:
                                        tempLine = tempLine.replace(statement2,"")
                                    tempLine = tempLine.split(" ", 1)[0]
                                    tempLine = tempLine.split("(", 1)[0] # This will sanitize def statements
                                    tempLine = tempLine.replace(" ", "")
                                    if not tempLine in currentImports:
                                        if len(tempLine) > 0:
                                            currentImports.append(tempLine)
    if config.verboseLogs:
        print("Notification - Current imports:", currentImports)
    return currentImports
