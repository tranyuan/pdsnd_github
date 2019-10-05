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
        city = input("Please enther the city (chicago, new york city, washington):\n")
        city = city.lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Not a valid city.")
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enther the month (all, january, february, ... , june):\n")
        month = month.lower()
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Not a valid month.")
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enther the day of week (all, monday, tuesday, ... sunday):\n")
        day = day.lower()
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print("Not a valid day.")
        else:
            break

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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    print('Most Common Month: \n', common_month)
    # TO DO: display the most common day of week

    common_day = df['day'].mode()[0]

    print('Most Common Day: \n', common_day)


    # TO DO: display the most common start hour

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    print('Most Common Hour: \n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]

    print('Most Common Start Station: \n', common_start)
    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]

    print('Most Common End Station: \n', common_end)
    # TO DO: display most frequent combination of start station and end station trip

    df['S_E_Sation'] = df['Start Station'] + ' to ' + df['End Station']
    common_s_e = df['S_E_Sation'].mode()[0]

    print('Most Frequent Combination of Start Station and End Station trip: \n', common_s_e)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    t_travel_time = df['Trip Duration'].sum()

    print("Total Travel Time: \n", t_travel_time)
    # TO DO: display mean travel time
    m_travel_time = df['Trip Duration'].mean()

    print("Average Travel Time: \n", m_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Count of user types: \n", user_types)

    # TO DO: Display counts of gender

    while True:
        try:
            gender_types = df['Gender'].value_counts()
            print("Count of gender types: \n", gender_types)
            break
        except:
            print ("Not Avalible for counts of gender.")
            break

    # TO DO: Display earliest, most recent, and most common year of birth

    while True:
        try:
            earliest_birth = df['Birth Year'].min()
            recent_birth = df['Birth Year'].max()
            common_birth = df['Birth Year'].mode()[0]

            print("Earliest Birth: \n", earliest_birth)
            print("Recent Birth: \n", recent_birth)
            print("Common Birth: \n", common_birth)
            break
        except:
            print ("Not Avalible for Display earliest, most recent, and most common year of birth.")
            break





    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    '''Ask the User whether they want to see the raw data'''
    while True:
        try:
            Answer = input("Do you want to see the raw data? (yes, no):\n")
            Answer = Answer.lower()
        except:
            print("Invalid Input")
        if Answer in ('yes'):
            print("Raw Data: \n", df.head())
        elif Answer in ('no'):
            print("Not Display raw data")
            break
        else:
            print("Can't Understand.")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
