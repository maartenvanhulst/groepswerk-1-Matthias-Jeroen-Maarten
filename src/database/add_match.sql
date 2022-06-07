INSERT INTO public.match(
	date, start_time, home_score, away_score, home_alt_score, away_alt_score, is_forfeit_home, is_forfeit_away, is_postponed, is_canceled, away_team_id, home_team_id, location_id, match_day_id, referee_id)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);