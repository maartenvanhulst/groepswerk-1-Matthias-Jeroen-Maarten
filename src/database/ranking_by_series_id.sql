select
    row_number() over (order by points desc, wins desc, goals_delta desc) as position,
    *
from
    (select
            (select team.name from team where team.id = team_id) as team_name,
            sum(points)                                          as points,
            sum(matches)                                         as matches,
            sum(wins)                                            as wins,
            sum(draws)                                           as draws,
            sum(losses)                                          as losses,
            sum(goals_made)                                      as goals_made,
            sum(goals_against)                                   as goals_against,
            sum(goals_made) - sum(goals_against)                 as goals_delta
     from (select home_team_id                                             as team_id,
                  sum(1)                                                   as matches,
                  sum(case when home_score > away_score then 1 else 0 end) as wins,
                  sum(case when home_score = away_score then 1 else 0 end) as draws,
                  sum(case when home_score < away_score then 1 else 0 end) as losses,
                  sum(home_score)                                          as goals_made,
                  sum(away_score)                                          as goals_against,
                  sum(case
                          when home_score > away_score then 3
                          when home_score = away_score then 1
                          else 0
                      end)                                                 as points
           from match
		   right join (select id, series_id from matchday where series_id = 1) as md
		   on md.id = match.match_day_id
           where home_score is not null
           group by home_team_id

       union

           select away_team_id                                             as team_id,
                  sum(1)                                                   as matches,
                  sum(case when home_score < away_score then 1 else 0 end) as wins,
                  sum(case when home_score = away_score then 1 else 0 end) as draws,
                  sum(case when home_score > away_score then 1 else 0 end) as losses,
                  sum(away_score)                                          as goals_made,
                  sum(home_score)                                          as goals_against,
                  sum(case
                          when home_score < away_score then 3
                          when home_score = away_score then 1
                          else 0
                      end)                                                 as points
           from match
		   right join (select id, series_id from matchday where series_id = 1) as md
		   on md.id = match.match_day_id
           where away_score is not null
           group by away_team_id
          ) as played_matches
     group by team_id) as calc_ranking

