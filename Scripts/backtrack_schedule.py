import numpy as np
import time
import math

num_teams = 42
num_courts = 12
num_rounds_needed = 30

teams = list(range(0, num_teams))
primes = [1,2,3,5,7,11,13,17,19,23,29,31,27,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181]

depth_needed = num_rounds_needed / 3;
depth_hit = 0;

predefined_state = []

matchups_done = dict()

matchups_to_print = []

inc = 0

debug = False

t_init = time.time()
t1 = time.time()

playable_team_chart = []

finished = False

readable_printout = False
sheets_printout = True

sit_once = True
times_sat = [0 for i in range(0, num_teams)]
max_times_sitting = math.ceil(((num_teams-(num_courts*3)) * num_rounds_needed)/num_teams)

team_names = []

def init():
	print_parameters()
	ret = input("Does everything look right? Yes or No.\n")
	if ret.lower() != "yes":
		return "Quitting"

	for team_number in range(0,len(teams)):
		playable_teams = list(range(0,len(teams)))
		del playable_teams[team_number]
		playable_team_chart.append(playable_teams)
	print(playable_team_chart)

def print_parameters():
	print("Number of Teams: " 			+ str(num_teams))
	print("Team Names: " 				+ str(team_names))
	print("Max times sitting: " 		+ str(max_times_sitting))
	print("Number of rounds required: " + str(num_rounds_needed))

def backtrack_schedule_depth(teams_remaining, current_depth, depth_needed, current_matchup, prioritized_teams, cant_sit, times_sat):
	global matchups_done
	global depth_hit
	global matchups_to_print
	global t1
	global inc
	global playable_team_chart
	global finished

	for x in range(0,len(teams_remaining)):
		if finished:
			return
		
		team1 = teams_remaining[x]
		teams_to_play_remaining = find_first_playable_team(team1, teams_remaining)
		
		for y in range(0,len(teams_to_play_remaining)):
			
			if finished:
				return
			
			team2 = teams_to_play_remaining[y]
			both_need = find_all_matching_needed_team(team1,team2,teams_remaining)
			
			for z in range(0, len(both_need)):
				
				if finished:
					return

				team3 = both_need[z]

				(new_current_matchup, new_teams_remaining) = update_state(team1, team2, team3, teams_remaining, current_matchup)
				
				if debug:
					print("New Teams Remaining: " + str(new_teams_remaining))
				
				if new_matchup_found(new_teams_remaining, teams, cant_sit, new_current_matchup):
					matchups_to_print.append(new_current_matchup)
					if (current_depth > depth_hit):
						depth_hit = current_depth;
						print("New schedule found with depth: " + str(current_depth))
						print_new_best_state(matchups_to_print)
					
					(new_prioritized_teams, new_cant_sit, new_times_sat) = update_priority(prioritized_teams, cant_sit, times_sat, new_teams_remaining)
					
					if current_depth == depth_needed:
						finished = True

					backtrack_schedule_depth(new_prioritized_teams, current_depth + 1, depth_needed, [], new_prioritized_teams, new_cant_sit, new_times_sat)
					matchups_to_print.pop()
				else:
					backtrack_schedule_depth(new_teams_remaining, current_depth, depth_needed, new_current_matchup, prioritized_teams, cant_sit, times_sat)
				
				add_team_to_playable(team1, team2, team3)

def update_priority(prioritized_teams, cant_sit, times_sat, new_teams_remaining):
	new_prioritized_teams = list(prioritized_teams)
	new_cant_sit = list(cant_sit)
	for non_used_team in new_teams_remaining:
		new_prioritized_teams.remove(non_used_team)
		new_prioritized_teams.insert(0, non_used_team)

	new_cant_sit = updateWhoSat(new_teams_remaining, times_sat)
	if debug:
		print("Can't sit: " + str(new_cant_sit))
			
	return (new_prioritized_teams, new_cant_sit, times_sat)

def updateWhoSat(new_teams_remaining, times_sat):
	for non_used_team in new_teams_remaining:
		times_sat[non_used_team] += 1
	cant_sit = []
	for team_num in range(0, num_teams):
		if times_sat[team_num] == max_times_sitting:
			cant_sit.append(team_num)
	return cant_sit


def print_new_best_state(matchups_to_print):						
	for m2p in matchups_to_print:
		print()
		for ncm in m2p:
			if readable_printout:
				print(printableNewCurrentMatchup(ncm))
			if sheets_printout:
				print(printableNewCurrentMatchupForGoogleSheets(ncm))

def new_matchup_found(new_teams_remaining, teams, cant_sit, new_current_matchup):
	return ((len(new_teams_remaining) == (len(teams) % 3)) or allCourtsFilled(new_current_matchup)) and sittingTeamsAllowedToSit(new_teams_remaining, cant_sit)

def allCourtsFilled(new_current_matchup):
	return len(new_current_matchup) == num_courts

def update_state(team1, team2, team3, teams_remaining, current_matchup):
	remove_team_from_playable(team1, team2, team3)

	if debug:
		print("Team Remaining: " + str(teams_remaining))
		
	new_current_matchup = list(current_matchup)
	new_current_matchup.append([team1, team2, team3])
	new_teams_remaining = list(teams_remaining)

	new_teams_remaining.remove(team1)
	new_teams_remaining.remove(team2)
	new_teams_remaining.remove(team3)

	return (new_current_matchup, new_teams_remaining)


def remove_team_from_playable(t1,t2,t3):
	global playable_team_chart

	playable_team_chart[t1].remove(t2)
	playable_team_chart[t1].remove(t3)
	playable_team_chart[t2].remove(t1)
	playable_team_chart[t2].remove(t3)
	playable_team_chart[t3].remove(t1)
	playable_team_chart[t3].remove(t2)

def add_team_to_playable(t1,t2,t3):
	global playable_team_chart

	playable_team_chart[t1].append(t2)
	playable_team_chart[t1].append(t3)
	playable_team_chart[t2].append(t1)
	playable_team_chart[t2].append(t3)
	playable_team_chart[t3].append(t1)
	playable_team_chart[t3].append(t2)

def find_first_playable_team(team_pos_1, teams_remaining):
	return list(set.intersection(set(playable_team_chart[team_pos_1]), set(teams_remaining)))

def find_all_matching_needed_team(team_pos_1, team_pos_2, teams_remaining):
	return list(set.intersection(set(playable_team_chart[team_pos_1]), set(playable_team_chart[team_pos_2]), set(teams_remaining)))

def printableNewCurrentMatchup(new_current_matchup):
	return str(new_current_matchup[0]) + "," + str(new_current_matchup[1]) + "," + str(new_current_matchup[2])

def printableNewCurrentMatchupForGoogleSheets(new_current_matchup):
	return str(new_current_matchup[0]) + "\t" + str(new_current_matchup[1]) + "\t" + str(new_current_matchup[2])

def sittingTeamsAllowedToSit(teams_remaining, cant_sit):
	for team in cant_sit:
		if team in teams_remaining:
			return False
	return True

init()
#predefinedstatebacktrack()
backtrack_schedule_depth(teams, 1, depth_needed, [], teams, [], times_sat)