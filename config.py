workingDirectory: str = "C:\\WorkingDirectory"
backupDirectory: str = "C:\\BackupDirectory"

verboseLogs: bool = False

acceptedExtensions: list[str] = ["py", "txt", "bat", "db", "json"]
inspectExtensions: list[str] = ["py"]
folderSeperator: str = """\\"""
folderSpace: str = """_"""
statementsImport: list[str] = ["from ","import ", "def "]
folderNameMaxLen: int = 200 # Prevents from making a folder name too long