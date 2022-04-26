create table locations_location
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
    name         varchar(100) not null,
    site_id      bigint       not null
        constraint locations_location_site_id_fcc2fc75_fk_sites_site_id
            references sites_site
            deferrable initially deferred
);

alter table locations_location
    owner to django_soccer;

create index locations_location_site_id_fcc2fc75
    on locations_location (site_id);


