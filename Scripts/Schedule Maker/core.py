class BackTrackSchedule():

	def __init__(self, parameters):
		self.parameters = parameters
		self.

	def init_backtrack(self):
		self.backtrack_schedule_until_depth(self.parameters.teams, [], Schedule.empty(), 0, 0)

	def backtrack_schedule_until_depth(self, teams_available, matchups_in_current_round, current_schedule, round_depth, call_depth):
		ref_count_per_team = self.parameters.grouping_strat.get_number_of_times_reffed(current_schedule, self.parameters.team_count)
		playing_count_per_team = self.parameters.grouping_strat.get_number_of_times_played(current_schedule, self.parameters.team_count)
		sitting_count_per_team = self.parameters.grouping_strat.get_number_of_times_sat(current_schedule, self.parameters.team_count)

		(prioritized_refs, cant_ref) = self.prioritize_team_num_indexed_count_list(ref_count_per_team, 1000000)
		(prioritized_playable_teams, cant_play) = self.prioritize_team_num_indexed_count_list(playing_count_per_team, 1000000)
		(prioritized_sitting_teams, cant_sit) = self.prioritize_team_num_indexed_count_list(sitting_count_per_team, 1000000)

		nextGrouping = groupingStrat.getNextGrouping(None, teams_remaining, prioritized_refs, prioritized_playable_teams, prioritized_sitting_teams)

		finished_schedule = None
		while next_grouping is not None and finished_schedule is None:

			(new_teams_available, new_matchups_in_current_round) = update_state(next_grouping, teams_available, matchups_in_current_round)

			if round_complete():

				new_current_schedule = current_schedule.copy().add(new_matchups_in_current_round)

				if (current_depth > depth_hit):
					depth_hit = current_depth;
					print("New schedule found with depth: " + str(current_depth) + " or " + str(current_depth * groupingStrat.get_rounds_per_depth()) + " rounds.")
					print_new_best_state(matchups_to_print)

				if current_depth == self.:
					finished = True
					finished_schedule = list(matchups_to_print)

		return None

	def prioritize_team_num_indexed_count_list(self, team_num_index_count_list, maximum_instances):
		sortable = []
		for x in range(0, len(team_num_index_count_list)):
			sortable.append((x, team_num_index_count_list[x]))

		sortable.sort(key=self.sort_on_second_element)

		prioritized_list = []
		cant_preform_action = []
		for ele in sortable:
			if ele[1] <= maximum_instances:
				prioritized_list.append(ele[0])
			else:
				cant_preform_action.append(ele[1])

		return (prioritized_list, cant_preform_action)

	def sort_on_second_element(self, elem):
		return elem[1]

class Parameters():

	def __init__(self, rounds_required, team_count, team_names, grouping_strat, court_count, do_teams_ref):
		self.rounds_required = rounds_required
		self.team_count = team_count
		self.team_names = team_names
		self.grouping_strat = grouping_strat
		self.court_count = court_count
		self.do_teams_ref = do_teams_ref
		self.compute_additional_properties()

	def compute_additional_properties(self):
		self.teams = [i for i in range(0, self.team_count)]


class Schedule():

	def empty():
		return Schedule([], [])

	def __init__(self, assignments, teams_off_each_round):
		self.assignments = assignments
		self.teams_off_each_round = teams_off_each_round

	def copy(self):
		return Schedule(list(assignments), list(teams_off_each_round))

