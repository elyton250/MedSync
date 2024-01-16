#!/bin/bash

echo "Testing adding random information to the database"

for i in {1..10}; do
    echo "Adding entry $i"

    f_name=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.first_name())")
    l_name=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.last_name())")

    country_origin=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.country())")
    national_id=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.random_int(min=100000000, max=999999999))")
    gender=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.random_element(elements=('Male', 'Female')))")
    phone_number=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.phone_number())")
    email=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.email())")
    allergies=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.sentence())")

    country_residence=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.country())")
    province=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.state())")
    district=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.city())")
    sector=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")
    cell=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")
    village=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")

    medication_name=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")
    dosage=$(python3 -c "from faker import Faker; fake = Faker(); print(int(fake.random_int(min=1, max=100)))")
    frequency=$(python3 -c "from faker import Faker; fake = Faker(); print(int(fake.random_int(min=1, max=10)))")
    route=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")

    vaccine_name=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")
    vaccinated_pathogen=$(python3 -c "from faker import Faker; fake = Faker(); print(fake.word())")

    python3 add_info.py <<EOF
$f_name
$l_name
$country_origin
$national_id
$gender
$phone_number
$email
$allergies
$country_residence
$province
$district
$sector
$cell
$village
$medication_id
$medication_name
$dosage
$frequency
$route
$vaccine_id
$vaccine_name
$vaccinated_pathogen
EOF

    echo "Entry $i added successfully"
done
