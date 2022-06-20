SELECT date, home_team.name as home_team, 'VS' as vs, away_team.name as away_team, home_score, away_score, match.id
FROM public.match
INNER JOIN team home_team on match.home_team_id  = home_team.id
INNER JOIN team away_team on match.away_team_id  = away_team.id
INNER JOIN location on match.location_id  = location.id
ORDER BY match.id desc
