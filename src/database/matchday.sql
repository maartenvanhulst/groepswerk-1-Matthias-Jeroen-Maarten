create table matches_matchday
(
    id         bigserial
        primary key,
    name       varchar(50) not null,
    sort_order integer     not null,
    series_id  bigint      not null
        constraint matches_matchday_series_id_c8b54227_fk_seasons_series_id
            references seasons_series
            deferrable initially deferred
);

alter table matches_matchday
    owner to django_soccer;

create index matches_matchday_series_id_c8b54227
    on matches_matchday (series_id);


