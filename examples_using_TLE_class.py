import TLE_class as tle
import observation_simulation as obssim
import datetime

# creating an example tle
example_tle = tle.TLE(
    name="example_tle",
    mean_motion=0.5,
    eccentricity=0.0,
    inclination=30.0,
    right_asc_node=0.0,
)

# setting the tle's date to today and printing as a string
example_tle.set_date_to_today()
print("example TLE on today's date:\n" + example_tle.to_str())

# setting the tle's date to a week from today and printing as a string
today = datetime.datetime.today()
date = today.replace(day=today.day + 7)
example_tle.set_date_time(date)
print("\nexample TLE a week from today:\n" + example_tle.to_str())

# saving the tle to a text file and appending a second copy of the tle into the same text file
file_name = "example_tle.txt"
example_tle.to_txt(file_name)
example_tle.append_to_txt(file_name)
print("\nthe text file can be found in " + file_name)

# setting tle to ISS
# creating empty tle
ISS = tle.TLE()
# assigning ISS parameters to the empty tle
ISS.ISS()
# saving to a text file and printing parameters
ISS.to_txt("ISS.txt")
ISS.print_params()

# creating an empty example tle
example_tle2 = tle.TLE()
print("empty example TLE 2" + example_tle2.to_str())
print()

# reading the ISS TLE text file and making example_tle2 have the same parameters
example_tle2.create_tle_from_txt("ISS.txt")
print()

# making example_tle2 have the same parameters as the example_tle string
example_tle2.create_tle_from_str(example_tle.to_str())
