create table players_registration
(
    id         bigserial
        primary key,
    is_active  boolean not null,
    start_date date    not null,
    end_date   date,
    league_id  bigint  not null
        constraint players_registration_league_id_16a8b39f_fk_seasons_league_id
            references seasons_league
            deferrable initially deferred,
    player_id  bigint  not null
        constraint players_registration_player_id_1aebb419_fk_players_player_id
            references players_player
            deferrable initially deferred,
    team_id    bigint  not null
        constraint players_registration_team_id_d8aa35bd_fk_clubs_team_id
            references clubs_team
            deferrable initially deferred
);

alter table players_registration
    owner to django_soccer;

create index players_registration_league_id_16a8b39f
    on players_registration (league_id);

create index players_registration_player_id_1aebb419
    on players_registration (player_id);

create index players_registration_team_id_d8aa35bd
    on players_registration (team_id);


