create table seasons_league
(
    id        bigserial
        primary key,
    name      varchar(50) not null,
    season_id bigint      not null
        constraint seasons_league_season_id_180dd10b_fk_seasons_season_id
            references seasons_season
            deferrable initially deferred
);

alter table seasons_league
    owner to django_soccer;

create index seasons_league_season_id_180dd10b
    on seasons_league (season_id);


