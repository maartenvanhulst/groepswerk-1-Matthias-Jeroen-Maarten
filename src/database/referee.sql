create table referees_referee
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
        constraint referees_referee_site_id_10e079aa_fk_sites_site_id
            references sites_site
            deferrable initially deferred
);

alter table referees_referee
    owner to django_soccer;

create index referees_referee_site_id_10e079aa
    on referees_referee (site_id);


