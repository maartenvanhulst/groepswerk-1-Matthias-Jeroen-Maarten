create table clubs_club
(
    id           bigserial
        primary key,
    address_1    varchar(100) not null,
    address_2    varchar(100),
    post_code    varchar(10)  not null,
    city         varchar(100) not null,
    country      varchar(50),
    mobile_phone varchar(30)  not null,
    fixed_phone  varchar(30),
    alt_phone    varchar(30),
    email_1      varchar(100) not null,
    email_2      varchar(100),
    website      varchar(255),
    facebook     varchar(255),
    is_active    boolean      not null,
    name         varchar(100) not null,
    base_number  integer      not null
        unique,
    site_id      bigint       not null
        constraint clubs_club_site_id_9d4e1c3e_fk_sites_site_id
            references sites_site
            deferrable initially deferred
);

alter table clubs_club
    owner to django_soccer;

create index clubs_club_site_id_9d4e1c3e
    on clubs_club (site_id);


