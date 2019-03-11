# recursive-pyang-dependencies
Gets a list of files as input.
Runs "Pyang -f depend" on each file in the list and saves the results in an another list.
Keeps two lists, one containing the "unexplored files" and another with the explored ones.
If a new file appears as a result from a "Pyang -f depend" it is saved in the "unexplored files" list, if it already exists in any of the lists, it is ignored.
The result is the full list of files that are (at any level required to) the input files to work.