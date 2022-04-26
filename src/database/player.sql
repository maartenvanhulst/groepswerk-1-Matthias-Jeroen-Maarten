create table players_player
(
    id                      bigserial
        primary key,
    address_1               varchar(100) not null,
    address_2               varchar(100),
    post_code               varchar(10)  not null,
    city                    varchar(100) not null,
    country                 varchar(50),
    date_of_birth           date         not null,
    city_of_birth           varchar(100) not null,
    country_of_birth        varchar(50),
    national_identification varchar(100) not null,
    mobile_phone            varchar(30)  not null,
    fixed_phone             varchar(30),
    alt_phone               varchar(30),
    email_1                 varchar(100) not null,
    email_2                 varchar(100),
    first_name              varchar(50)  not null,
    middle_names            varchar(100),
    last_name               varchar(100) not null,
    identification          varchar(100) not null,
    site_id                 bigint       not null
        constraint players_player_site_id_c3a2f8fc_fk_sites_site_id
            references sites_site
            deferrable initially deferred
);

alter table players_player
    owner to django_soccer;

create index players_player_site_id_c3a2f8fc
    on players_player (site_id);


