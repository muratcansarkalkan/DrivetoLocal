# DrivetoLocal
The script that will identify missing files in local and download them from Google Drive
<ul>
  <li>Progress 25.2.2022: Now we are able to pack what we want and have what we want.</li>
  <li>Progress 25.2.2022: I can pack 7z's that has the empty file "complete.txt"</li>
  <li>Progress 27.2.2022: I can pack 7z's if they are not packed yet.</li>
  <li>Progress 27.2.2022: Instead of using a list to retrieve ID data I used a dictionary. The output 7z will have now both team name and ID, for clear download</li>
  <li>Progress 27.2.2022: Now the 7z files are organized with respective country folders</li>
  <li>Progress 27.2.2022: Recursive error fixed</li>
  <li>Progress 2.3.2022: Added littlecopy.py that adds an empty txt file for teams in database, also changed comments in main.py</li>
  <li>Progress 3.3.2022: Fixed bug that created empty folders for national teams</li>
  <li>Progress 5.3.2022: Added extracting tool for 7z packages</li>
  <li>Progress 5.3.2022: The stadiums will be now packed by the date of script run, therefore added functions such as if folder is previously packed, date return</li>
  <li>Progress 5.3.2022: User will be able to view what is in the bundle before downloading the packages by viewing Contents-date.txt</li>
  <li>Progress 12.3.2022: Removed repeated line in main.py and defined it in a new function</li>
  <li>Progress 18.3.2022: Added Regex expression to teamsearch.py</li>
</ul>
