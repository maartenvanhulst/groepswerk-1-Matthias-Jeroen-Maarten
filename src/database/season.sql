create table seasons_season
(
    id         bigserial
        primary key,
    is_active  boolean     not null,
    name       varchar(50) not null,
    start_date date        not null,
    end_date   date,
    site_id    bigint      not null
        constraint seasons_season_site_id_826ba713_fk_sites_site_id
            references sites_site
            deferrable initially deferred
);

alter table seasons_season
    owner to django_soccer;

create index seasons_season_site_id_826ba713
    on seasons_season (site_id);


