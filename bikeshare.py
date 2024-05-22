import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
day_dic={'m':'monday', 'tu':'tuesday', 'w':'wednsday', 'th':'thursday', 'f':'friday', 'sa':'saturday', 'su':'sunday',
         'all':'all'}

monthes =['january', 'february', 'march', 'april', 'may', 'june']
def get_day():
    day=" "
    try:    
        while day not in day_dic:
            day = input("which day? please type a day M, Tu, W, Th, F, Sa, Su").lower()
        return day
    except ValueError:
        print("no value")
    except KeyboardInterrupt :
        print ("no value")

def get_month():
    month = " "
    try:    
        while month not in monthes:
            month = input("chose the month january, february, march, april, may, june").lower()
        return month
    except ValueError:
        print("no value")
    except KeyboardInterrupt :
        print ("no value")

    
def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    global day_dic
    global CITY_DATA


    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    try:
        while 1==1:
            city=input("Would you like to see data for Chicago, New York, or Washington?").lower()
            if city in (CITY_DATA):
                while 1==1:
                    chose_filter = input("Would you like to filter the date by month, day, both or not all ? type 'none' for no time filter").lower()
                    if chose_filter=="both":               
                        month=get_month()
                        day=get_day()
                        break
                    elif chose_filter=="month":
                        month = get_month()
                        day="all"
                        break   
                    elif chose_filter=="day":
                        day = get_day()
                        month="all"
                        break
                    elif chose_filter=="none":
                        day="all"
                        month="all"
                        break
                break
            else:
                print("please try again")
            


                
                
        print('-'*40)
        return city, month, day_dic[day]
    except ValueError:
        print("no value")
def load_data(city, month, day): 
    """ Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if 
    
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("the most common month:")
    print(df['month'].mode()[0])
    
    # display the most common day of week
    print("the most common day of week:")
    print(df['day_of_week'].mode()[0])
   
    # display the most common start hour
    print("he most common start hour:")    
    df['hour'] = df['Start Time'].dt.hour
    print(df['hour'].mode()[0])
   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # display most commonly used start station
    print("most commonly used start station: ")
    print(df['Start Station'].mode()[0])


    # display most commonly used end station
    print("most most commonly used end station: ")
    print(df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    print("most frequent combination of start station and end station trip: ")

    counts = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    print(counts[[0]])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time: ")
    print(df["Trip Duration"].sum())


    # display mean travel time
    print("mean travel time: ")
    print(df["Trip Duration"].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('counts of user types:')
    print(df['User Type'].value_counts())


    # Display counts of gender
    print('counts of gender:')
    print(df['Gender'].value_counts())
    

    # Display earliest, most recent, and most common year of birth
    print('the oldest:')
    print(df['Birth Year'].min())
    print('the most popular year of birth:')
    print(df['Birth Year'].mode()[0])
    print('the youngest:')
    print(df['Birth Year'].max())
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_data(df):
    for index in range(5):
        print("{")
        print(df.iloc[index])
        print("}")
    while 1==1:
        q_to_continue=input("Would you like to view individual data? type 'yes' or 'no'")
        if q_to_continue=="yes":
            index=index+1
            print("{")
            print(df.iloc[index])
            print("}")
        elif q_to_continue == "no":
            break
        else:
            print("the input is incorrect ,please try agine")
            
   
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city!='washington':
            user_stats(df)
            
        show_data(df) 
        restart = input("\nWould you like to restart? Enter yes or no.\n")
        if restart.lower() != "yes":
            break


if __name__ == "__main__":
    try:
        
        main()
    except KeyboardInterrupt :
        print ("no value")