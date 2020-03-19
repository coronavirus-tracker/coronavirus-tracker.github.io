# Authors: Abhijith Balijepalli, Ved Dave, Akhil Chinnakotla
# Date: 3/18/2020
# Description: Locationziled Data analysis on COVID-19 virus, using real time data from John Hopkins, WHO, CDC...etc.

import numpy
import math
import scipy
import csv
import matplotlib.pyplot as plt
import os

CountryName = ''
SubRegion = ''
cwd = os.getcwd() #Create Path


def graphingTest(myList):
    #x1 = list(range(0,len(myList)))
    fig = plt.figure()
    x = list(range(0, len(myList)))
    print(max(myList))
    plt.scatter(x, myList)
    plt.xlabel('Days since 1/22/20')
    plt.ylabel('Confirmed Cases')
    plt.title(CountryName+', '+SubRegion)
    fig.savefig(cwd+'/imgsrc/'+ CountryName+'_'+SubRegion)
    plt.close(fig)
    
    
if __name__ == '__main__':
    with open('COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv') as csv_file: # load raw data from JHU
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader: # iterate through each location
                if line_count == 0: # initialize first row of dates
                    print('The countries/regions are:')
                    line_count += 1
                else:
                    if not row[0]: # check if location has a subregion
                        print('\tLocation: {}. '.format(row[1]), end= '')
                    else:
                        print('\tLocation: {}, {}'.format(row[0], row[1]), end= '')
                    CountryName = row[1]
                    SubRegion = row[0]
                    index = 0
                    cases_list = [] # create a list for location
                    for elem in row:
                        if index > 3:
                            cases_list.append(int(elem)) # add cases for each day to the list
                            #print(cases_list, end='')
                        index += 1
                    print(cases_list)
                    graphingTest(cases_list)
                    
