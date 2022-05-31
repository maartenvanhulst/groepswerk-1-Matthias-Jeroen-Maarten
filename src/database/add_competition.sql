INSERT INTO public.competition(
	id, name, competition_type, has_secondary_score, league_id)
	VALUES (%s, %s, %s, %s, %s);