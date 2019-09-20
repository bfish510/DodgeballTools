class TripletGroupingStrategy():

	def __init__(self):
		self.numTeamsInGroup = 3
	
	def getInitialGrouping(self, teams_remaining, prioritized_refs, prioritized_playable_teams):
		for x in range(0,len(teams_remaining)):
			team1 = teams_remaining[x]
			teams_to_play_remaining = find_first_playable_team(team1, teams_remaining)
			for y in range(0,len(teams_to_play_remaining)):
				team2 = teams_to_play_remaining[y]
				both_need = find_all_matching_needed_team(teams_remaining,team1,team2)
				
				for z in range(0, len(both_need)):
					team3 = both_need[z]
					init = [team1, team2, team3]
					return init

		return None

	def getNextGrouping(self, prevGrouping, teams_remaining, prioritized_refs, prioritized_playable_teams):
		if prevGrouping == None:
			return self.getInitialGrouping(teams_remaining, prioritized_refs, prioritized_playable_teams)

		for x in range(prevGrouping[0],len(teams_remaining)):
			team1 = teams_remaining[x]
			teams_to_play_remaining = find_first_playable_team(team1, teams_remaining)
			for y in range(prevGrouping[1],len(teams_to_play_remaining)):
				team2 = teams_to_play_remaining[y]
				both_need = find_all_matching_needed_team(teams_remaining,team1,team2)

				for z in range(prevGrouping[2], len(both_need)):
					team3 = both_need[z]
					init = [team1, team2, team3]
					return init

		return None

	def add_grouping_to_playable(self, grouping):
		global playable_team_chart

		t1 = grouping[0]
		t2 = grouping[1]
		t3 = grouping[2]
	
		playable_team_chart[t1].append(t2)
		playable_team_chart[t1].append(t3)
		
		playable_team_chart[t2].append(t1)
		playable_team_chart[t2].append(t3)
		
		playable_team_chart[t3].append(t1)
		playable_team_chart[t3].append(t2)

	def remove_grouping_from_playable(self, grouping):
		global playable_team_chart

		t1 = grouping[0]
		t2 = grouping[1]
		t3 = grouping[2]
	
		playable_team_chart[t1].remove(t2)
		playable_team_chart[t1].remove(t3)
		
		playable_team_chart[t2].remove(t1)
		playable_team_chart[t2].remove(t3)
		
		playable_team_chart[t3].remove(t1)
		playable_team_chart[t3].remove(t2)

	def get_rounds_per_depth(self):
		# n! / (n - r)! -> 3! / (3 - 1)! -> 6 / 2 -> 3
		return 3

	def get_games_per_depth(self):
		return 2

	def get_num_teams_in_group(self):
		return self.numTeamsInGroup

	def get_matchups_for_grouping(self, grouping):
		matchups = []
		matchups.append(Matchup(team_names[grouping.teams[0]], team_names[grouping.teams[1]], team_names[grouping.teams[2]]))
		matchups.append(Matchup(team_names[grouping.teams[0]], team_names[grouping.teams[2]], team_names[grouping.teams[1]]))
		matchups.append(Matchup(team_names[grouping.teams[1]], team_names[grouping.teams[2]], team_names[grouping.teams[0]]))
		return matchups

	def print_number_of_times_played(self, groupings):
		play_count = [0 for i in range(0, num_teams)]
		for g in groupings:
			play_count[g.teams[0]] += 2
			play_count[g.teams[1]] += 2
			play_count[g.teams[2]] += 2
		for index in range(0,num_teams):
			print(team_names[index] + " played " + str(play_count[index]) + " times.")

	def get_number_of_times_played(self, groupings, matchups_to_print):
		play_count = [0 for i in range(0, num_teams)]
		for g in groupings:
			play_count[g[0]] += 2
			play_count[g[1]] += 2
			play_count[g[2]] += 2
		for s in matchups_to_print:
			for r in s:
				play_count[r[0]] += 2
				play_count[r[1]] += 2
				play_count[r[2]] += 2
		return play_count

	def get_number_of_times_reffed(self, groupings, matchups_to_print):
		ref_count = [0 for i in range(0, num_teams)]
		for g in groupings:
			ref_count[g[0]] += 1
			ref_count[g[1]] += 1
			ref_count[g[2]] += 1
		for s in matchups_to_print:
			for r in s:
				ref_count[r[0]] += 1
				ref_count[r[1]] += 1
				ref_count[r[2]] += 1
		return ref_count