# TODO: Do I need to add Null values for blank entries?

#######         Armed/unarmed       ######

# What percentage of victims are unarmed? (6.5%)
SELECT armed, COUNT(*)  * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE armed = "unarmed"

# What percentage of victims had a gun? (56.54%)
SELECT armed, COUNT(*)  * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE armed = "gun"

# What percentage of victims had a knife? (14.6%)
SELECT armed, COUNT(*)  * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE armed = "knife"

# What percentage of victims had a toy weapon? (3.4%)
SELECT armed, COUNT(*)  * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE armed = "toy weapon"



#######         RACE        ######
# Calculating percentage black killed (23.9)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "B";

# Number black killed per million for total US population black
# (Racial composition of the United States in 2017; https://en.wikipedia.org/wiki/Demographics_of_the_United_States#Race)
# White: 234,370,202
# Black: 40,610,815



# Calculating percentage white killed (45.7)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "W";

# Calculating percentage asian killed (1.7)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "A";

# Calculating percentage hispanic killed (16.6)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "H";

# Calculating percentage native american killed (1.43)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "N";

# Calculating percentage other killed (9.7)
SELECT race, count(*) * 100.0 / (SELECT COUNT(*) FROM shootings)
FROM shootings
WHERE race = "";



#
