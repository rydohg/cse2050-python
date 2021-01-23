# Author: Ryan Doherty, rdoherty2019@my.fit.edu
# Course: CSE 2050, Fall 2020
# Project: Birth Date Heat Map
"""
Birth Date Heat Map.

Generate a heat map of birthdays
from a given MySQL database
"""
from sys import stderr
import numpy
from matplotlib.widgets import Slider, Button
import matplotlib.pyplot as plot
import mysql.connector
from mysql.connector import Error
from datetime import datetime

database: mysql.connector.MySQLConnection = None
start_year_slider: Slider = None
length_slider: Slider = None


def connect_to_db():
    """Connect to the database."""
    global database
    try:
        database = mysql.connector.connect(
            host="andrew.cs.fit.edu",
            user="cse2050",
            passwd="fall2020",
            database="stansifer"
        )
    except Error as error:
        stderr.write(f"{str(error)}\n")
    finally:
        if database is not None and database.is_connected():
            return True
        else:
            return False


def read_bdays(start, end):
    """Query and read database info into the birthdays array."""
    start_date = datetime.strptime(f"{start}", "%Y")
    # Maximum of 3 leap years in a decade (max length of time)
    birthdays = numpy.zeros(365 * (end - start + 1) + 3)
    cursor = database.cursor()
    # MySQL query to get all entries between 2 years
    cursor.execute(
        f"SELECT DOB FROM SSDI WHERE year(DOB) BETWEEN {start} and {end}")

    birthday = cursor.fetchone()
    while birthday is not None:
        date = None
        try:
            date = datetime.strptime(birthday[0], "%Y-%m-%d")
        except ValueError:
            stderr.write("incorrect date\n")
        if date is not None:
            index = (date - start_date).days
            birthdays[index] += 1
        birthday = cursor.fetchone()

    try:
        cursor.close()
    except mysql.connector.errors.InternalError as e:
        stderr.write(str(e))
    database.close()
    return birthdays


def calculate_bdays_between(start, end, birthdays):
    """Calculate the number of people born on each day of the year."""
    heat_array = numpy.zeros(366, dtype=None)
    start_date = datetime.strptime(f"{start}", "%Y")
    for year in range(start, end + 1):
        start_year_index = (datetime.strptime(f"{year}-01-01", "%Y-%m-%d")
                            - start_date).days
        end_year_index = (datetime.strptime(f"{year}-12-31", "%Y-%m-%d")
                          - start_date).days
        for day in range(start_year_index, end_year_index + 1):
            # Feb 29th is 60th day of the year
            # Skip if not leap year
            # Compensate after skipping the date since birthdays
            # ignores leap days
            if year % 4 != 0:
                if day - start_year_index == 59:
                    continue
                elif day - start_year_index > 59:
                    heat_array[day - start_year_index] += birthdays[day - 1]
                    continue
            heat_array[day - start_year_index] += birthdays[day]
        if year % 4 != 0:
            heat_array[365] = birthdays[end_year_index]
    return heat_array


def on_button_click(event):
    """Calculate heat map when the submit button is clicked."""
    start = start_year_slider.val
    end = start + length_slider.val
    connect_to_db()
    birthdays = read_bdays(start, end)
    heat_array = calculate_bdays_between(start, end, birthdays)
    display_heatmap(heat_array)


def display_heatmap(heatarray=None):
    """Convert heat array into a matrix and setup the GUI for the map."""
    heat_array_counter = 0
    heat_matrix = numpy.zeros((12, 31), dtype=int)
    if heatarray is not None:
        for i in range(1, 13):
            days_in_month = 31
            if i == 2:
                days_in_month = 29
            elif i == 4 or i == 6 or i == 9 or i == 11:
                days_in_month = 30

            for j in range(31):
                if j <= days_in_month - 1:
                    heat_matrix[i - 1][j] = heatarray[heat_array_counter]
                    heat_array_counter += 1
                else:
                    heat_matrix[i - 1][j] = 0

    figure, axis = plot.subplots(figsize=(12, 10))
    axis.imshow(heat_matrix.transpose(), aspect="auto")
    axis.set_xticks(range(12))
    axis.set_yticks(range(31))
    axis.set_xticklabels(
        ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
         "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
    )
    axis.set_yticklabels([i for i in range(1, 32)])

    axis.grid(which="minor", color="w", linestyle='-', linewidth=3)
    axis.tick_params(which="minor", bottom=False, left=False)

    for edge, spine in axis.spines.items():
        spine.set_visible(False)

    plot.setp(axis.get_xticklabels(), rotation=45, ha="right",
              rotation_mode="anchor")

    axis.set_title("Birthday Heat Map")
    plot.plot()
    plot.subplots_adjust(bottom=0.25)

    start_year_axis = plot.axes([0.25, .15, 0.65, 0.03], facecolor="gray")
    length_axis = plot.axes([0.25, .1, 0.65, 0.03], facecolor="gray")
    global start_year_slider
    global length_slider
    start_year_slider = \
        Slider(start_year_axis, 'Start', 1880, 1990, valinit=1880, valstep=1)
    length_slider = Slider(length_axis, 'Length', 1, 10, valinit=1, valstep=1)
    submit_button_axis = plot.axes([0, 0.025, 0.1, 0.04])
    button = Button(submit_button_axis, 'Submit', color="gray")
    button.on_clicked(on_button_click)
    plot.show()


connect_to_db()
display_heatmap()
