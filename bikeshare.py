import time
import pandas as pd
import numpy as np

## City data is here
CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n')
        if city == 'Chicago' or city == 'New York' or city == 'Washington':
            break
        else:
            print ('Please ensure you input is Chicago, New York or Washington') 
 
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich month? january, february, march, april, may, june or all?\n')
        if month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all':
            break
        else:
            print ('Please ensure you input is january, february, march, april, may,  june or all') 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all?\n')
        if day == 'Sunday' or day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'all':
            break
        else:
            print('please ensure your  input is Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or all')
    
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january','february','march','april','may', 'june']
        month = months.index(month)+1
        
        df = df[df['month']==month]
     
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def summary(df):
    """Displays statistics on the summary data."""
    while True:
        summary_request = input('\nDo you want to see the raw data? Enter yes or no\n')
        if summary_request == 'no':
            break
        elif summary_request == 'yes':
            i = 0
            for i in range (100):
                print(df.iloc[i*5:i*5+5])
                summary_request2 = input('\nDo you still want to see the raw data? Enter yes or no\n')
                if summary_request2 == 'no':
                    break
                elif summary_request2 == 'yes':
                    i += 1
                else:
                    print('please ensure your input is yes or no')
        else:
            print('please ensure your input is yes or no')                
    print('-'*40)
    
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Month:', popular_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day of week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day of week'].mode()[0]
    print('Most Frequent Day of Week:', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Frequent Used Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].value_counts().idxmax()
    print('Most Frequent Used End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df.groupby('Start Station')['End Station'].value_counts().idxmax()
    print('Most Frequent Combination of Start Station and End Station:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    
#    if city !=  'Washington':
    # TO DO: Display counts of gender
    gender = df['Gender'].value_counts()
    print(gender)
        
     # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_birth = df['Birth Year'].max()
    most_recent_year_birth = df['Birth Year'].min()
    most_common_year_birth = df['Birth Year'].mode()
    
    print('Earliest Year of Birth:', earliest_year_birth)
    print('Most Recent Year of Birth:', most_recent_year_birth)
    print('Most Common Year of Birth:', most_common_year_birth)
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        summary(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        
        if city != 'Washington':
            user_stats(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
