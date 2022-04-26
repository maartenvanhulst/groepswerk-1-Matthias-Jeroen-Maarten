create table clubs_clubcontact
(
    id           bigserial
        primary key,
    mobile_phone varchar(30)  not null,
    fixed_phone  varchar(30),
    alt_phone    varchar(30),
    email_1      varchar(100) not null,
    email_2      varchar(100),
    first_name   varchar(50)  not null,
    middle_names varchar(100),
    last_name    varchar(100) not null,
    role         varchar(50),
    club_id      bigint       not null
        constraint clubs_clubcontact_club_id_4f72a96c_fk_clubs_club_id
            references clubs_club
            deferrable initially deferred
);

alter table clubs_clubcontact
    owner to django_soccer;

create index clubs_clubcontact_club_id_4f72a96c
    on clubs_clubcontact (club_id);


