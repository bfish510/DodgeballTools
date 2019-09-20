class DoublesGroupingStrategy():

	def __init__(self, teams_ref):
		self.numTeamsInGroup = 2
		#True or False
		self.teams_ref = teams_ref
	
	def getInitialGrouping(self, teams_remaining, prioritized_refs, prioritized_playable_teams):
		for x in range(0,len(prioritized_playable_teams)):
			team1 = prioritized_playable_teams[x]

			if team1 not in teams_remaining:
				break

			teams_to_play_remaining = find_first_playable_team(team1, prioritized_playable_teams)
			for y in range(0,len(teams_to_play_remaining)):
				team2 = teams_to_play_remaining[y]

				if team2 not in teams_remaining:
					break
				
				ref_candidates = find_potential_refs(teams_remaining, prioritized_refs, team1, team2)
				
				for z in range(0, len(ref_candidates)):
					ref = ref_candidates[z]
					init = [team1, team2, ref]
					return init

		return None

	def getNextGrouping(self, prevGrouping, teams_remaining, prioritized_refs, prioritized_playable_teams):
		debug("Next Grouping")
		debug("\tPrevious Grouping", prevGrouping)
		debug("\tteams_remaining", teams_remaining)
		debug("\tprioritized_refs", prioritized_refs)
		debug("\tprioritized_playable_teams", prioritized_playable_teams)


		if prevGrouping == None:
			debug("Get Init")
			return self.getInitialGrouping(teams_remaining, prioritized_refs, prioritized_playable_teams)

		for x in range(prevGrouping[0],len(prioritized_playable_teams)):
			team1 = prioritized_playable_teams[x]
			debug("Team 1", team1)

			if team1 not in teams_remaining:
				debug("not in playable teams")
				break

			teams_to_play_remaining = find_first_playable_team(team1, prioritized_playable_teams)
			for y in range(prevGrouping[1],len(teams_to_play_remaining)):
				team2 = teams_to_play_remaining[y]
				debug("Team 2", team2)

				if team2 not in teams_remaining:
					debug("not in playable teams")
					break
				
				ref_candidates = find_potential_refs(teams_remaining, prioritized_refs, team1, team2)
				debug("ref candidates", ref_candidates)
				
				for z in range(prevGrouping[2], len(ref_candidates)):
					ref = ref_candidates[z]
					debug("Ref", ref)
					init = [team1, team2, ref]
					return init

		return None

	def add_grouping_to_playable(self, grouping):
		global playable_team_chart

		t1 = grouping[0]
		t2 = grouping[1]
	
		playable_team_chart[t1].append(t2)
		
		playable_team_chart[t2].append(t1)

	def remove_grouping_from_playable(self, grouping):
		global playable_team_chart

		t1 = grouping[0]
		t2 = grouping[1]
	
		playable_team_chart[t1].remove(t2)
		
		playable_team_chart[t2].remove(t1)

	def get_rounds_per_depth(self):
		return 1

	def get_games_per_depth(self):
		return 1

	def get_num_teams_in_group(self):
		return self.numTeamsInGroup

	def get_matchups_for_grouping(self, grouping):
		matchups = []
		matchups.append(Matchup(team_names[grouping.teams[0]], team_names[grouping.teams[1]], team_names[grouping.teams[2]]))
		return matchups

	def get_dedicated_refs(self, grouping):
		if self.teams_ref:
			return [grouping[2]]
		return []

	def get_number_of_times_played(self, schedule, num_teams):
		play_count = [0 for i in range(0, num_teams)]
		for rownd in schedule.assignments:
			for matchup in rownd:
				play_count[matchup[0]] += 1
				play_count[matchup[1]] += 1
		return play_count

	def get_number_of_times_reffed(self, schedule, num_teams):
		ref_count = [0 for i in range(0, num_teams)]
		for rownd in schedule.assignments:
			for matchup in rownd:
				ref_count[matchup[2]] += 1
		return ref_count

	def print_number_of_times_played(self, groupings):
		play_count = [0 for i in range(0, num_teams)]
		for g in groupings:
			play_count[g.teams[0]] += 1
			play_count[g.teams[1]] += 1
		for index in range(0,num_teams):
			print(team_names[index] + " played " + str(play_count[index]) + " times.")