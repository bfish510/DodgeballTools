class GroupingStrategyInterface():

	def __init__(self, groupingImpl):
		self.groupingImpl = groupingImpl

	def getInitialGrouping(self, teams_remaining, prioritized_refs, prioritized_playable_teams):
		return self.groupingImpl.getInitialGrouping(teams_remaining, prioritized_refs, prioritized_playable_teams)

	def getNextGrouping(self, prevGrouping, teams_remaining, prioritized_refs, prioritized_playable_teams):
		return self.groupingImpl.getNextGrouping(prevGrouping, teams_remaining, prioritized_refs, prioritized_playable_teams)

	def add_grouping_to_playable(self, grouping):
		return self.groupingImpl.add_grouping_to_playable(grouping)

	def remove_grouping_from_playable(self, grouping):
		return self.groupingImpl.remove_grouping_from_playable(grouping)

	def get_rounds_per_depth(self):
		return self.groupingImpl.get_rounds_per_depth()

	def get_num_teams_in_group(self):
		return self.groupingImpl.get_num_teams_in_group()

	def get_matchups_for_grouping(self, grouping):
		return self.groupingImpl.get_matchups_for_grouping(grouping)

	def get_ref_count(self, current_schedule):
		return self.groupingImpl.get_ref_count(current_schedule)

	def print_number_of_times_played(self, groupings):
		return self.groupingImpl.print_number_of_times_played(groupings)

	def get_games_per_depth(self):
		return self.groupingImpl.get_games_per_depth()

	def get_number_of_times_reffed(self, schedule, num_teams):
		return self.groupingImpl.get_number_of_times_reffed(schedule, num_teams)

	def get_number_of_times_sat(self, schedule, num_teams):
		return self.groupingImpl.get_number_of_times_reffed(schedule, num_teams)

	def get_number_of_times_played(self, schedule, num_teams):
		return self.groupingImpl.get_number_of_times_played(schedule, num_teams)