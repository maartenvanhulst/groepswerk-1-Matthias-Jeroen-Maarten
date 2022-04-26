create table seasons_competition
(
    id                  bigserial
        primary key,
    name                varchar(50) not null,
    competition_type    varchar(1)  not null,
    has_secondary_score boolean     not null,
    league_id           bigint      not null
        constraint seasons_competition_league_id_d0ca9a62_fk_seasons_league_id
            references seasons_league
            deferrable initially deferred
);

alter table seasons_competition
    owner to django_soccer;

create index seasons_competition_league_id_d0ca9a62
    on seasons_competition (league_id);


