create table sites_site
(
    id       bigserial
        primary key,
    mnemonic varchar(20)  not null,
    name     varchar(256) not null
);

alter table sites_site
    owner to django_soccer;


