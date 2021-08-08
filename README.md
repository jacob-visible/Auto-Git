# AutoHub
A python project to backup any changes made in your python projects locally. It will append the noticeable changes (like added def or import) to the backup folder. It also includes the date the newest file was last modified or created.

The purpose of this is a simple backup process you can add as a cronjob or windows scheduled task to backup however often as you like.\
It will restrict what is being backed up based on the extension.\
It will not backup any project folder if there is not at least 1 file which is new by virtue of modified or creation date.\
Each time it backs up it will do so into a new folder every file in each project's folder.\
It will create a new folder in the backup directory with at least the date and time of the newest modified or creation date of the newest file.\
It will also add at the end the names of any new imported libraries or defined functions. So if we add a new import or function which is not currently in the backed up directory for that project it will append this to the end of the backup folder's name. This will help us distinguish between backups when major changes happen.

-Configuration in config.py-

workingDirectory - Set the working directory main folder where you are putting your python projects. It will consider each folder in that directory to be a different project to backup. Any file in the root directory will be ignored.\
backupDirectory - Set where all our projects are going to be backed up to.\
verboseLogs - True or False to show or hide print statements if desired.\
acceptedExtensions - This list will specify all the file extensions of the files we are wanting to backup at all.\
inspectExtensions - This list will specify all the file extensions of the files we are wanting to inspect by opening and reading line by line. This is for checking for new def and import lines which will be noted in the end folder being backed up to.\
folderSeperator - What is separating each folder in the filepath.\
folderSpace - You can set what do you want spacing out this information on the folder name.\
statementsImport - A list of lines containing this string that are notable. So any line that has def/import/etc you care about if something new was added.\
folderNameMaxLen - A int of the maximum length you will accept for the folder name. This is to prevent exceeding any max file length you may have on your system. It will add as much information to the folder name that is below this length of characters and stop before exceeding this.
