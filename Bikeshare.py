#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def validate_input(user_input,allowed_values):
    """
    Takes the user's input and validates it against acceptable values. 
    Used to limit looping in the program.
    
    Args:
        (str) - the user's input
        (list) - list of allowed values
    Returns:
        (bool) - Boolean that describes if the user input matches an allowed value.
    """
    valid_input = False
    for x in range(len(allowed_values)):
        if user_input.lower() == allowed_values[int(x)]:    
            # break the if loop
            valid_input = True
    if not valid_input:
        print("Sorry, I can't match your input choice.  Please try again.\n")
    else:
        print("Got it.  Thanks.")
    return valid_input


def convert_input(month,day):
    """
    Converts the user's input into numeric month and day so we can avoid
    looping later in the program

    Args:
       (str) month - full string as entered by user
       (str) day - full string as entered by user

    Returns:
       (str) month - one character string
       (str) day - one character string

    """
    if month == "january":
        month = 1
    elif month == "february":
        month = 2
    elif month == "march":
        month = 3
    elif month == "april":
        month = 4
    elif month == "may": 
        month = 5
    elif month == "june":
        month = 6
    elif month == "july":
        month = 7
    elif month == "august":
        month = 8
    elif month == "september":
        month = 9
    elif month == "october":
        month = 10
    elif month == "november":
        month = 11
    elif month == "december":
        month = 12
    else: 
        #take no action
        month = "a"
    
    if day == "monday":
        day = 0
    elif day == "tuesday":
        day = 1
    elif day == "wednesday":
        day = 2
    elif day == "thursday":
        day = 3
    elif day == "friday": 
        day = 4
    elif day == "saturday":
        day = 5
    elif day == "sunday":
        day = 6
    else: 
        #take no action
        day = "a"
    
    return month, day

def reverse_convert_day(day):
    """
    Reverses the user's input into written day so we can avoid
    looping later in the program

    Args:
       (str) day - one character string 

    Returns:
       (str) day - full string as entered by user

    """
    if day == "0":
        day = "Monday"
    elif day == "1":
        day = "Tuesday"
    elif day == "2":
        day = "Wednesday"
    elif day == "3":
        day = "Thursday"
    elif day == "4": 
        day = "Friday"
    elif day == "5":
        day = "Saturday"
    elif day == "6":
        day = "Sunday"
    return day

def reverse_convert_month(month):
    """
    Converts the user's input into numeric month and day so we can avoid
    looping later in the program

    Args:
       (str) month - one character string

    Returns:
       (str) month - full string as entered by user
    """
    if month == "1":
        month = "January"
    elif month == "2":
        month = "February"
    elif month == "3":
        month = "March"
    elif month == "4":
        month = "April"
    elif month == "5": 
        month = "May"
    elif month == "6":
        month = "June"
    elif month == "7":
        month = "July"
    elif month == "8":
        month = "August"
    elif month == "9":
        month = "September"
    elif month == "10":
        month = "October"
    elif month == "11":
        month = "November"
    elif month == "12":
        month = "December"
    
    return month

def convert_seconds_to_hours_pretty(seconds): 
    """
    Converts seconds to a pretty format of hours:mins:seconds 
    Please note I want to cite my source for this work: 
    https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
    
    Args: 
        (str) seconds 
    Return:
        (str) pretty formatted time
    """
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 
      
    # Driver program 
    n = 12345
    print(convert_seconds_to_hours_pretty(n)) 

def user_formatting(d1):
    """
    Cleans up the formatting of our user queries so we can 
    reduce repetitive functionality needed to present clean 
    responses to the user.
    Takes in a DataFarm, converts it to a dictionary, then a string, then cleans it up
    
    Args: 
        (df) Takes in a dataframe
    Return: 
        (str) pretty formatted string ready to be shown to the user.
    """
    d2 = d1.to_dict()
    d3 = str(d2)
    d3 = d3.replace("(","")
    d3 = d3.replace(")","")
    d3 = d3.replace("'","")
    d3 = d3.replace("{","")
    d3 = d3.replace("}","")
    d3 = d3.replace("Customer, Customer","Customer")
    d3 = d3.replace("Dependent, Dependent","Dependent")
    d3 = d3.replace("Subscriber, Subscriber","Subscriber")
    d3 = d3.replace("Male, Male","Male")
    d3 = d3.replace("Female, Female","Female")

    return d3
    

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    # TODO: handle keyboard exception error CTRL+C
    valid_input = False
    while not valid_input:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        city = input("Enter 'C' for Chicago, 'N' for New Yor City, or 'W' for Washington: ")
        valid_input = validate_input(city,('c','n','w'))

    #reset the validate_input flage 
    valid_input = False
    while not valid_input:
        # get user input for month (all, january, february, ... , june)
        month = input("Enter 'A' for all or the month...January, February, etc.: ")
        valid_input = validate_input(month, ('a','january','february','march','april','may','june','july','august','september','october','november','december'))
    
    valid_input = False
    while not valid_input:
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Enter 'A' for all or the day of the week...Monday, Tuesday, etc.: ")
        valid_input = validate_input(day, ('a','monday','tuesday','wednesday','thursday','friday','saturday','sunday'))

    month, day = convert_input(month.lower(), day.lower())        
    
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
    #read in the data
    if city.lower() == 'c':
        df = pd.read_csv("chicago.csv")
    elif city.lower() == 'n':
        df = pd.read_csv("new_york_city.csv")
    elif city.lower() == 'w':
        df = pd.read_csv("washington.csv")
    else: 
        print("I'm sorry, I experienced an unexpected error in module load_data")
        exit

    #add new columns to the dataframe based on existing data
    #we drop these later in the program before presenting them to the user
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).weekday #Monday is 0 Sunday is 6
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    df['station_merge'] = df["Start Station"] + " and ends at " + df["End Station"]
    
    #example month_df = df[df['month'] == 1] #for January
    # the months have been turned into ints so we do not need to make them lower()
    if month != "a":
        month_df = df[df["month"] == month]
    else:
        month_df = df    
    if day != "a":
        day_df = month_df[month_df["day"] == day]
    else:
        day_df = month_df
   
    #return the data nicely sorted
    return day_df.sort_values(by="Start Time")
    
def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (df) - Our filtered data frame
    
    Returns:
        NONE - presents the data directly to the user using print statements
    
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    d1 = df.groupby('month')['month'].value_counts()
    month_of_year = str(d1.idxmax(axis=1)).split(",")
    month_of_year = reverse_convert_month(month_of_year[0].replace("(",""))
    print("The most common month is", month_of_year, "with", d1.max(), "total trips.")

    # display the most common day of week
    d2 = df.groupby('day')['day'].value_counts()
    day_of_week = reverse_convert_day(str(d2.idxmax(axis=1))[1:2])
    print("The most common day of the week is", day_of_week, "with", d2.max(), "total trips.")
    
    # display the most common start hour
    d3 = df.groupby('hour')['hour'].value_counts()
    start_hour = str(d3.idxmax(axis=1)).split(",")
    start_hour = start_hour[0].replace("(","")
    
    #convert the hour to US
    if int(start_hour) > 12:
        start_hour = int(start_hour) - 12
        start_hour = str(start_hour) + "pm"
    else:
        start_hour = str(start_hour) + "am"
    print("The most common start hour is", start_hour, "with", d3.max(), "total trips.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (df) - Our filtered data frame
    
    Returns:
        NONE - presents the data directly to the user using print statements
    
    """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    d1 = df.groupby('Start Station')['Start Station'].value_counts()
    start_station = str(d1.idxmax(axis=1)).split(",")
    # clean up formatting prior to printing
    start_station = start_station[0].replace("(","")
    start_station = start_station.replace("'","")
    print("The most commonly used start station is", start_station, "with", d1.max(), "total trips.")

    # display most commonly used end station
    d2 = df.groupby('End Station')['End Station'].value_counts()
    end_station = str(d2.idxmax(axis=1)).split(",")
    # clean up formatting prior to printing
    end_station = end_station[0].replace("(","")
    end_station = end_station.replace("'","")
    print("The most commonly used end station is", end_station, "with", d2.max(), "total trips.")

    # display most frequent combination of start station and end station trip
    d3 = df.groupby('station_merge')['station_merge'].value_counts()
    merge_station = str(d3.idxmax(axis=1)).split(",")
    # clean up formatting prior to printing
    merge_station = merge_station[0].replace("(","")
    merge_station = merge_station.replace("'","")
    print("The most frequent trip combination starts at", merge_station, "with", d3.max(), "total trips.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        (df) - Our filtered data frame
    
    Returns:
        NONE - presents the data directly to the user using print statements
    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    d1 = df["Trip Duration"].sum()
    df["Trip Duration"].count()
    d1 = convert_seconds_to_hours_pretty(d1)
    print("The total travel time was", d1, "across a total of", df["Trip Duration"].count(), "trips.")

    # display mean travel time
    d2 = df["Trip Duration"].mean()
    d2 = convert_seconds_to_hours_pretty(d2)
    print("The mean travel time was", d2, "across a total of", df["Trip Duration"].count(), "trips.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """
    Displays statistics on bikeshare users.
    
    Args:
        (df) - Our filtered data frame
        (str) - city is needed because we have special logic due to Washington not having
                birthdate or gender
    Returns:
        NONE - presents the data directly to the user using print statements
   
    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    d1 = df.groupby('User Type')['User Type'].value_counts()
    user_info = user_formatting(d1)

    print("Here is information about the counts of user types:",user_info)
   

    #  removes gender becaues it is not available in Washington
    if city != "w":
        d2 = df.groupby('Gender')['Gender'].value_counts()
        user_info = "Here is information about the counts of gender: " + user_formatting(d2)
    else:
        user_info = "I'm sorry, there is no gender information available for Washington."
    
    print(user_info)


    # Display earliest, most recent, and most common year of birth
    # special logic needed because birth year is not available in Washington
    if city != "w":
        print("The earliest year of birth is " + str(int(df['Birth Year'].min())).strip() + ".") 
        print("The most recent birth year is " + str(int(df['Birth Year'].max())).strip() + ".")
        d3 = df.groupby('Birth Year')['Birth Year'].value_counts()
        birth_year = str(d3.idxmax(axis=1)).split(",")
        birth_year = birth_year[0].replace("(","")
        birth_year = birth_year.replace("'","")
        birth_year = birth_year.replace(".0","")
        print("The most common year of birth is",birth_year,"with",d3.max(),"total users.")
    else:
        print("I'm sorry, there is no year of birth information available for Washington.")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_rows(df, city):
    """
    Presents the user with option to review sorted raw data transactions
    
    Args:
        (df) - Our filtered data frame
        (str) - city is again needed because some data is not available in Washington
    Returns:
        NONE - presents the data directly to the user using print statements
    """    
    print("I've sorted the raw data to show you the five most recent transactions out of " + str(len(df.index)) + " total entries.")
    # delet working columns, rename, and sorting our data
    df2 = df.rename(columns={"Unnamed: 0":"ID"}) 
    df3 = df2.drop(columns=['month', 'day', 'hour', 'station_merge'], axis=1)
    df3 = df3.sort_values(by="Start Time", ascending=False)
    
    # display the first five rows
    # custom logic for washington
    i = 0
    stopper = 5
    while True:
        raw_data = input("Would you like to see the first five raw data entries? Enter yes or no.")
        while raw_data.lower() != 'yes' and raw_data.lower() != 'no':
            raw_data = input("I'm sorry, it looks like you didn't enter 'yes' or 'no'. Please try again. ")
        
        if raw_data.lower() == 'yes':
            while i < stopper:
                if city != "w": 
                    print("\n Row number "+ str(i+1) + ":",df3['ID'].iloc[i], df3['Start Time'].iloc[i],df3['End Time'].iloc[i],df3['Trip Duration'].iloc[i],df3['Start Station'].iloc[i],df3['End Station'].iloc[i],df3['User Type'].iloc[i],df3['Gender'].iloc[i],df3['Birth Year'].iloc[i])
                else: 
                    print("\n Row number "+ str(i+1) + ":",df3['ID'].iloc[i], df3['Start Time'].iloc[i],df3['End Time'].iloc[i],df3['Trip Duration'].iloc[i],df3['Start Station'].iloc[i],df3['End Station'].iloc[i],df3['User Type'].iloc[i])
                i += 1
                raw_data = True
        else:
            raw_data = False
            
        break
        
    # give the user options to view more data - five rows presented each time.
    # custom logic due to some data not being available for Washington
    while raw_data == True:
        more_rows = input("Would you like to see five more rows? Enter yes or no.")
        while more_rows.lower() != 'yes' and more_rows.lower() != 'no':
            more_rows = input("I'm sorry, it looks like you didn't enter 'yes' or 'no'.  Please try again. ")
        
        if more_rows.lower() == 'yes':        
            stopper = i + 5
            #show the next five
            while i < stopper:
                if i < len(df3.index-1):
                    if city != "w":
                        print("\n Row number " + str(i+1) + ":",df3['ID'].iloc[i], df3['Start Time'].iloc[i],df3['End Time'].iloc[i],df3['Trip Duration'].iloc[i],df3['Start Station'].iloc[i],df3['End Station'].iloc[i],df3['User Type'].iloc[i],df3['Gender'].iloc[i],df3['Birth Year'].iloc[i]) 
                    else:
                        print("\n Row number " + str(i+1) + ":",df3['ID'].iloc[i], df3['Start Time'].iloc[i],df3['End Time'].iloc[i],df3['Trip Duration'].iloc[i],df3['Start Station'].iloc[i],df3['End Station'].iloc[i],df3['User Type'].iloc[i])     
                    i += 1
                else:
                    print("No more rows to display, you've reached the end.")
        if more_rows.lower() != 'yes':
            break
    
def main():
    
    try:

        while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)
            if len(df.index) != 0:
                time_stats(df)
                station_stats(df)
                trip_duration_stats(df)
                user_stats(df,city)
                display_rows(df,city)
            else:
                print("I'm sorry, it looks like you chose a combination that has no data!")
    
            restart = input('Would you like to restart? Enter yes or no. ')
            while restart.lower() != 'yes' and restart.lower() != 'no':
                restart = input("I'm sorry, it looks like you didn't enter 'yes' or 'no'. Please try again. ")
            if restart.lower() != 'yes':
                print("Have a good day.  Take good care.")
                break
                 
    except KeyboardInterrupt:
        print("Shutdown requested. Have a good day. Take good care.")
  
    except Exception:
        print("Unexpected error. Shutting down.")


if __name__ == "__main__":
	main()
      


# In[ ]:





# In[ ]:




