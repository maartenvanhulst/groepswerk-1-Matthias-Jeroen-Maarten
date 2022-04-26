create table matches_match
(
    id              bigserial
        primary key,
    date            date    not null,
    start_time      time    not null,
    home_score      integer,
    away_score      integer,
    home_alt_score  integer,
    away_alt_score  integer,
    is_forfeit_home boolean not null,
    is_forfeit_away boolean not null,
    is_postponed    boolean not null,
    is_canceled     boolean not null,
    away_team_id    bigint  not null
        constraint matches_match_away_team_id_d1513cbf_fk_clubs_team_id
            references clubs_team
            deferrable initially deferred,
    home_team_id    bigint  not null
        constraint matches_match_home_team_id_cdfabc57_fk_clubs_team_id
            references clubs_team
            deferrable initially deferred,
    location_id     bigint
        constraint matches_match_location_id_fdabbe18_fk_locations_location_id
            references locations_location
            deferrable initially deferred,
    match_day_id    bigint  not null
        constraint matches_match_match_day_id_b5012820_fk_matches_matchday_id
            references matches_matchday
            deferrable initially deferred,
    referee_id      bigint
        constraint matches_match_referee_id_632d9467_fk_referees_referee_id
            references referees_referee
            deferrable initially deferred
);

alter table matches_match
    owner to django_soccer;

create index matches_match_away_team_id_d1513cbf
    on matches_match (away_team_id);

create index matches_match_home_team_id_cdfabc57
    on matches_match (home_team_id);

create index matches_match_location_id_fdabbe18
    on matches_match (location_id);

create index matches_match_match_day_id_b5012820
    on matches_match (match_day_id);

create index matches_match_referee_id_632d9467
    on matches_match (referee_id);


