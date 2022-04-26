create table referees_refereedistance
(
    id          bigserial
        primary key,
    start_date  date          not null,
    end_date    date,
    distance    numeric(8, 2) not null,
    location_id bigint        not null
        constraint referees_refereedist_location_id_1acdd0ea_fk_locations
            references locations_location
            deferrable initially deferred,
    referee_id  bigint        not null
        constraint referees_refereedist_referee_id_a81014f7_fk_referees_
            references referees_referee
            deferrable initially deferred
);

alter table referees_refereedistance
    owner to django_soccer;

create index referees_refereedistance_location_id_1acdd0ea
    on referees_refereedistance (location_id);

create index referees_refereedistance_referee_id_a81014f7
    on referees_refereedistance (referee_id);


