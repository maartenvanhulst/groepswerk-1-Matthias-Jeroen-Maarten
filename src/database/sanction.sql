create table matches_sanction
(
    id            bigserial
        primary key,
    sanction_type varchar(1) not null,
    report        text,
    match_id      bigint     not null
        constraint matches_sanction_match_id_d19ba643_fk_matches_match_id
            references matches_match
            deferrable initially deferred,
    player_id     bigint     not null
        constraint matches_sanction_player_id_2820de5c_fk_players_player_id
            references players_player
            deferrable initially deferred
);

alter table matches_sanction
    owner to django_soccer;

create index matches_sanction_match_id_d19ba643
    on matches_sanction (match_id);

create index matches_sanction_player_id_2820de5c
    on matches_sanction (player_id);


