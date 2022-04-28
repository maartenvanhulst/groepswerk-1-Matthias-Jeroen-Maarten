drop table if exists sanction;
drop table if exists injury;
drop table if exists match;
drop table if exists refereedistance;
drop table if exists location;
drop table if exists referee;
drop table if exists registration;
drop table if exists team;
drop table if exists clubcontact;
drop table if exists club;
drop table if exists player;
drop table if exists matchday;
drop table if exists series;
drop table if exists competition;
drop table if exists league;
drop table if exists season;

create table season
(
    id         bigserial    primary key,
    is_active  boolean      not null,
    name       varchar(50)  not null,
    start_date date         not null,
    end_date   date
);

create table league
(
    id        bigserial     primary key,
    name      varchar(50)   not null,
    season_id bigint        not null
        constraint fk_season_league
            references season
            deferrable initially deferred
);

create index ix_league_season_id on league (season_id);

create table competition
(
    id                  bigserial   primary key,
    name                varchar(50) not null,
    competition_type    varchar(1)  not null,
    has_secondary_score boolean     not null,
    league_id           bigint      not null
        constraint fk_league_competition
            references league
            deferrable initially deferred
);

create index ix_competition_league_id on competition (league_id);

create table series
(
    id             bigserial    primary key,
    name           varchar(50)  not null,
    sort_order     integer      not null,
    competition_id bigint       not null
        constraint fk_competition_series
            references competition
            deferrable initially deferred
);

create index ix_series_competition_id on series (competition_id);

create table matchday
(
    id         bigserial    primary key,
    name       varchar(50)  not null,
    sort_order integer      not null,
    series_id  bigint       not null
        constraint fk_series_matchday
            references series
            deferrable initially deferred
);

create index ix_matchday_series_id on matchday (series_id);

create table player
(
    id                      bigserial       primary key,
    first_name              varchar(50)     not null,
    middle_names            varchar(100),
    last_name               varchar(100)    not null,
    address_1               varchar(100)    not null,
    address_2               varchar(100),
    post_code               varchar(10)     not null,
    city                    varchar(100)    not null,
    country                 varchar(50),
    date_of_birth           date            not null,
    city_of_birth           varchar(100)    not null,
    country_of_birth        varchar(50),
    mobile_phone            varchar(30)     not null,
    fixed_phone             varchar(30),
    alt_phone               varchar(30),
    email_1                 varchar(100)    not null,
    email_2                 varchar(100),
    national_identification varchar(100)    not null,
    identification          varchar(100)    not null
);

create table club
(
    id           bigserial      primary key,
    name         varchar(100)   not null,
    base_number  integer        not null    unique,
    address_1    varchar(100)   not null,
    address_2    varchar(100),
    post_code    varchar(10)    not null,
    city         varchar(100)   not null,
    country      varchar(50),
    mobile_phone varchar(30)    not null,
    fixed_phone  varchar(30),
    alt_phone    varchar(30),
    email_1      varchar(100)   not null,
    email_2      varchar(100),
    website      varchar(255),
    facebook     varchar(255),
    is_active    boolean        not null
);

create table clubcontact
(
    id           bigserial      primary key,
    mobile_phone varchar(30)    not null,
    fixed_phone  varchar(30),
    alt_phone    varchar(30),
    email_1      varchar(100)   not null,
    email_2      varchar(100),
    first_name   varchar(50)    not null,
    middle_names varchar(100),
    last_name    varchar(100)   not null,
    role         varchar(50),
    club_id      bigint         not null
        constraint fk_club_clubcontact
            references club
            deferrable initially deferred
);

create index ix_clubcontact_club_id on clubcontact (club_id);

create table team
(
    id           bigserial      primary key,
    name         varchar(100)   not null,
    display_name varchar(50)    not null,
    home_color_1 varchar(10)    not null,
    home_color_2 varchar(10),
    home_color_3 varchar(10),
    away_color_1 varchar(10)    not null,
    away_color_2 varchar(10),
    away_color_3 varchar(10),
    alt_color_1  varchar(10),
    alt_color_2  varchar(10),
    alt_color_3  varchar(10),
    club_id      bigint         not null
        constraint fk_club_team
            references club
            deferrable initially deferred
);

create table registration
(
    id         bigserial    primary key,
    is_active  boolean      not null,
    start_date date         not null,
    end_date   date,
    league_id  bigint       not null
        constraint fk_league_registration
            references league
            deferrable initially deferred,
    player_id  bigint  not null
        constraint fk_player_registration
            references player
            deferrable initially deferred,
    team_id    bigint not null
        constraint fk_team_registration
            references team
            deferrable initially deferred
);



create table referee
(
    id                      bigserial       primary key,
    first_name              varchar(50)     not null,
    middle_names            varchar(100),
    last_name               varchar(100)    not null,
    address_1               varchar(100)    not null,
    address_2               varchar(100),
    post_code               varchar(10)     not null,
    city                    varchar(100)    not null,
    country                 varchar(50),
    date_of_birth           date            not null,
    city_of_birth           varchar(100)    not null,
    country_of_birth        varchar(50),
    mobile_phone            varchar(30)     not null,
    fixed_phone             varchar(30),
    alt_phone               varchar(30),
    email_1                 varchar(100)    not null,
    email_2                 varchar(100),
    national_identification varchar(100)    not null,
    identification          varchar(100)    not null
);

create table location
(
    id           bigserial      primary key,
    name         varchar(100)   not null,
    address_1    varchar(100)   not null,
    address_2    varchar(100),
    post_code    varchar(10)    not null,
    city         varchar(100)   not null,
    country      varchar(50),
    mobile_phone varchar(30)    not null,
    fixed_phone  varchar(30),
    alt_phone    varchar(30),
    email_1      varchar(100)   not null,
    email_2      varchar(100),
    website      varchar(255),
    facebook     varchar(255)
);

create table refereedistance
(
    id          bigserial
        primary key,
    start_date  date          not null,
    end_date    date,
    distance    numeric(8, 2) not null,
    location_id bigint        not null
        constraint fk_location_refereedistanche
            references location
            deferrable initially deferred,
    referee_id  bigint        not null
        constraint fk_referee_refereedistance
            references referee
            deferrable initially deferred
);

create table match
(
    id              bigserial   primary key,
    date            date        not null,
    start_time      time        not null,
    home_score      integer,
    away_score      integer,
    home_alt_score  integer,
    away_alt_score  integer,
    is_forfeit_home boolean     not null,
    is_forfeit_away boolean     not null,
    is_postponed    boolean     not null,
    is_canceled     boolean     not null,
    away_team_id    bigint      not null
        constraint fk_team_match_home
            references team
            deferrable initially deferred,
    home_team_id    bigint  not null
        constraint fk_team_match_away
            references team
            deferrable initially deferred,
    location_id     bigint
        constraint fk_location_match
            references location
            deferrable initially deferred,
    match_day_id    bigint  not null
        constraint fk_matchday_match
            references matchday
            deferrable initially deferred,
    referee_id      bigint
        constraint fk_referee_match
            references referee
            deferrable initially deferred
);

create table injury
(
    id          bigserial   primary key,
    description text        not null,
    match_id    bigint      not null
        constraint fk_match_injury
            references match
            deferrable initially deferred,
    player_id   bigint not null
        constraint fk_player_injury
            references player
            deferrable initially deferred
);

create table sanction
(
    id            bigserial     primary key,
    sanction_type varchar(1)    not null,
    report        text,
    match_id      bigint        not null
        constraint fk_match_sanction
            references match
            deferrable initially deferred,
    player_id     bigint     not null
        constraint fk_player_sanction
            references player
            deferrable initially deferred
);
