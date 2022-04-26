create table clubs_team
(
    id           bigserial
        primary key,
    name         varchar(100) not null,
    display_name varchar(50)  not null,
    home_color_1 varchar(10)  not null,
    home_color_2 varchar(10),
    home_color_3 varchar(10),
    away_color_1 varchar(10)  not null,
    away_color_2 varchar(10),
    away_color_3 varchar(10),
    alt_color_1  varchar(10),
    alt_color_2  varchar(10),
    alt_color_3  varchar(10),
    club_id      bigint       not null
        constraint clubs_team_club_id_c03d5fc9_fk_clubs_club_id
            references clubs_club
            deferrable initially deferred
);

alter table clubs_team
    owner to django_soccer;

create index clubs_team_club_id_c03d5fc9
    on clubs_team (club_id);


