# Schedule Maker
A tool that makes schedules for you and fast!


## Example Workflow and Instructions
Let's use an example to demonstrate how to use the tool. In this case we'll use Elite Nationals 2018 - Coed 8.5 division. The biggest division with 45 teams and 14 courts. The organizers wanted a schedule that could fill 30 rounds of play. To use the tool they do the following:

1. Goto https://docs.google.com/spreadsheets/d/1pI5hz7NPxSS6uHmwWoXag6x_FVd1s2gQbvvgYGZ-lgs/edit?usp=sharing
2. Fill in the document
3. Download as CSV
4. Run the script with the CSV file as the first parameter
5. Get Results!

## Details on how the Schedules are Built

This tool uses the concept of "triplets" to make a schedule. A triplet is a set of three teams who will all play each other and ref the game they aren't playing. This helps reduce the amount of time swapping courts. In the future I'll play around with groupings of different sizes.

## Example Results

This program outputs the results in two ways. First, it will print everything to the terminal. Second, it will create a CSV file that can be used for the tournament. 

Future tools will be built for the CSV file format that this program outputs.

As for how the results look in the terminal:

~~~~
Round 1
Titan vs. Anarchy reffed by Doom
Task Force vs. Rise reffed by Brick Squad
Team Awesome vs. TC Boosh reffed by Dynasty
Fortune vs. Outsiders reffed by Kraken
Goat vs. Wrecking Ballz reffed by Outlaws
Havoc vs. Reign Bros reffed by Mt Olympus
Arsenal vs. Aftershock reffed by Riot
Rogue vs. Grit reffed by ARKM
Corruption vs. Space Cadets reffed by Tigers
Double Tap vs. Gamecocks reffed by Night Shift
Notorious vs. Kaiju reffed by Roybots
Showtime vs. Voodoo reffed by Final Justice
Blitz vs. Legacy reffed by Precision
Klutch Mode vs. Wildcards reffed by Category 5

Round 2
Titan vs. Doom reffed by Anarchy
Task Force vs. Brick Squad reffed by Rise
Team Awesome vs. Dynasty reffed by TC Boosh
Fortune vs. Kraken reffed by Outsiders
Goat vs. Outlaws reffed by Wrecking Ballz
Havoc vs. Mt Olympus reffed by Reign Bros
Arsenal vs. Riot reffed by Aftershock
Rogue vs. ARKM reffed by Grit
Corruption vs. Tigers reffed by Space Cadets
Double Tap vs. Night Shift reffed by Gamecocks
Notorious vs. Roybots reffed by Kaiju
Showtime vs. Final Justice reffed by Voodoo
Blitz vs. Precision reffed by Legacy
Klutch Mode vs. Category 5 reffed by Wildcards

Round 3
...
~~~~
