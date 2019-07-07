import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city: chicago, new york city or washington:")
        if city.lower() in CITY_DATA.keys():
            city = CITY_DATA[city.lower()]
            break
        else:
            print("Please put your glasses on, and choose a relavant city")

    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month: all, january, february, ... , june:")
        if month.lower() in ["all", "january", "february", "mars", "april" "may", "june"]:
            month = month.lower()
            break
        else:
            print("Put down your coffee and try again")

                   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Choose a day: all, monday, tuesday, ... sunday:")
        if day.lower() in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            day = day.lower()
            break
        else:
            print("Is that really a day?")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city)
    
    df['Start Time'] = pd.to_datetime(df["Start Time"])
    df['month'] = df["Start Time"].dt.month
    df['day_of_week'] = df["Start Time"].dt.weekday_name

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df["month"] == month]
       
    if day != 'all':
        df = df[df["day_of_week"] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The {} month of the year is the most common month".format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("{} is the most common day of the week".format(df["day_of_week"].mode()[0]))

    # TO DO: display the most common start hour
    print("{} is the most common start hour".format(df["Start Time"].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("{} is the most commonly used start station".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("{} is the most commonly used end station".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    combined_stations = df[["Start Station","End Station"]].mode()
    print("{} to {} is the most frequent combination of start station and end station trip".format(
        combined_stations["Start Station"][0], combined_stations["End Station"][0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total traveltime is {}".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The mean travel time is {}".format(df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types")
    print(df["User Type"].value_counts())

    # TO DO: Display counts of gender
    print("Counts of gender")
    print(df["Gender"].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print("\nEarliest year of birth is {:.0f}, \nmost recent year of birth {:.0f} \nand most common year of birth is {:.0f}"
          .format(
              df["Birth Year"].min(),
              df["Birth Year"].max(),
              df["Birth Year"].mode()[0]
          ))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
