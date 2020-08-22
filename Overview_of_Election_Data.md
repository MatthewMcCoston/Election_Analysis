# Overview of Election Audit: 
    Preform a audit of tabulated results for a US Congressional precinct in Colorado. In which the total number of votes cast; the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote are reported.

## Election-Audit Results

 Based off of the information provdided from the election_results.csv file, 
https://github.com/MatthewMcCoston/Election_Analysis/blob/master/election_results.csv

  The total number of votes cast for the congressional election is 369,711 votes.

    There were three counties counted in this election:
    Dever had 306,055 votes which was 82.8% of the votes casted
    Jefferson had 38,855 votes which was 10.5% of the votes casted
    Aprapahoe had 24,801 voteswhich was 6.7% of the votes casted

        which makes Dever the county with the largest number of votes.

There were three candidates running in this election:
    Diana DeGette received 272,892 votes which was 73.8% of the votes casted
    Charles Casper Stockholm received 85,213 votes which was 23.0% of the votes casted
    Raymon Anthony Doane received 11,606 votes which was 3.1% of the votes casted

        Which made Diana DeGette the winning Candidate.

https://github.com/MatthewMcCoston/Election_Analysis/blob/master/Election_Results.txt


### Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

  It would be possible to use this script in any election process as long as certian modifcations were made. if you were to remove the county section of the code it would enable you to sort information just based on who was being voted. This allows you to then use data from any place an election is held. Another way this code could be modified would be to switch the county section of the code with the election results total, this would then allow you to shorten the code as well as sort out first where the election was being held before sorting candidates. 

  #### Additional Resources
    Code used to gather Election Results.
  https://github.com/MatthewMcCoston/Election_Analysis/blob/master/pypoll_challenge.py