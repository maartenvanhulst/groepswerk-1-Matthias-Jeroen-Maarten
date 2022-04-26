create table matches_injury
(
    id          bigserial
        primary key,
    description text   not null,
    match_id    bigint not null
        constraint matches_injury_match_id_e1d6fd67_fk_matches_match_id
            references matches_match
            deferrable initially deferred,
    player_id   bigint not null
        constraint matches_injury_player_id_9fe59f0c_fk_players_player_id
            references players_player
            deferrable initially deferred
);

alter table matches_injury
    owner to django_soccer;

create index matches_injury_match_id_e1d6fd67
    on matches_injury (match_id);

create index matches_injury_player_id_9fe59f0c
    on matches_injury (player_id);


