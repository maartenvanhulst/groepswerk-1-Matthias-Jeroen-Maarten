create table seasons_series
(
    id             bigserial
        primary key,
    name           varchar(50) not null,
    sort_order     integer     not null,
    competition_id bigint      not null
        constraint seasons_series_competition_id_2ff53332_fk_seasons_c
            references seasons_competition
            deferrable initially deferred
);

alter table seasons_series
    owner to django_soccer;

create index seasons_series_competition_id_2ff53332
    on seasons_series (competition_id);


