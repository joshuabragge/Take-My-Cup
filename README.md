# Take-My-Cup
A harmless prank which might open a link to giphy every hour on your victim's computer

##What is does:
Schedules a task to run every hour that opens up a url in the random.txt file

##Features:
- changing which links open
- adjusting the propability of a link opening every hour with the threshold
- added youtube links will unmute and max out volumne

##How to work it:
- add your urls to the random.cfg file and sepearte each link by a new line
- theshold is the probability of a link opening every hour
- threshold should be in the first line and value between 0 and 1
- run the takemycup program while the random.cfg file is in the directory
- if random.cfg is not in directory, program will use default links

##How to remove:
auto
- run srry program
manual
- delete folder C:\dEkota
- remove task chckyrself from task scheduler "SchTasks /Delete /tn "chckyrslf" /f"
