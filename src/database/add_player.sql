INSERT INTO public.player(
	id, first_name, middle_names, last_name, address_1, address_2, post_code, city, country, date_of_birth, city_of_birth, country_of_birth, mobile_phone, fixed_phone, alt_phone, email_1, email_2, national_identification, identification)
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);