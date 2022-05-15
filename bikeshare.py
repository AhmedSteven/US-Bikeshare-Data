import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    #Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input('Please choose the city that you want data for from (chicago, new york city, washington) :').lower()
        if city not in  CITY_DATA :
            print('Your choice is incorrect , please choose again')
        else :
            break
      
    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
        month = input('Please choose the month that you want or type "all" to display all months :').lower()
        months  = ['january','february','march','april','may','june']
        if month != 'all' and month not in months :
            print('Please try entering a valid month name')
        else :
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose the day that you want or type "all" to display all days :').lower()
        days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
        if day != 'all' and day not in days :
            print('Please try entering a valid day name')
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months= ['january','february','march','april','may','june']
        month= months.index(month) + 1

        df= df[df['month'] == month]

    if day != 'all':
        df=df[df['day_of_week'] == day.title()] # i used .title() to capitalize the week days to adapt with the data set

    return df

def raw_data(df):
    i=0
    input_by_me= input("would you like me to show you the first 5 rows of data ? , choose yes/no :  ").lower()
    pd.set_option('display.max_columns',None)

    while True:
        if input_by_me == "no":
            break
        else:
            print(df[i:i+5])
            input_me = input( "would you like to see more  5 rows of this data ? , choose yes/no: ").lower()
            i+=5



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month  = df['month'].mode()[0]
    print('most common month is :',most_month)

    # TO DO: display the most common day of week
    most_day_of_week = df['day_of_week'].mode()[0]
    print('most common day is :',most_day_of_week)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_hour = df['hour'].mode()[0]
    print('most common hour is :',most_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('most common station used as a start is :',most_start_station)
    

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('most common station used as a end is :',most_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    start_and_end_station = (f'{most_start_station} , {most_end_station}')
    print('most frequent combination of start and end stations :',start_and_end_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("total travel time",total_travel, 'seconds, or ' , total_travel/3600,'hours')
    
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("mean travel time is ",total_travel, 'seconds or ' , mean_travel/3600,'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display countءs of user types
    print('couns of user types :\n',df['User Type'].value_counts())
   
          
    # TO DO: Display counts of gender
    if "Gender" in df:
        print('\n counts of gender:\n', df['Gender'].value_counts())
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        earliest = int(df['Birth Year'].min())
        print('\n earliest year of birth is : \n'  , earliest)
          
        most_recent = int(df['Birth Year'].max())
        print('\n most recent year of birth is :\n', most_recent)
          
        most_common = int(df['Birth Year'].mode()[0])
        print('\n most common year of birth is :\n', most_common)
    else:
        print('Birth year stats cannot be calculated because Birth year does not appear in the dataframe')
        


          


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
