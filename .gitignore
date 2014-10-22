import urllib2
import csv
from bs4 import BeautifulSoup

Tag = '<div class="scoreWrapper">'
div = '</div>'

movie_start = 0

url_list = ['http://www.rottentomatoes.com/m/sharknado_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/superman_man_of_steel/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/the_hunger_games_catching_fire/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/gravity_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/argo_2012/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/pacific_rim_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/american_hustle/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/despicable_me_2/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/warm_bodies/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/after_earth/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/the_internship_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/elysium_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/the_wolf_of_wall_street_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/battlefield_earth/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/frozen_2013/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/12_years_a_slave/reviews/?type=user&page=',
            'http://www.rottentomatoes.com/m/godfather/reviews/?type=user&page=',
            ]
movie_list = ['sharknado', 'manofsteel', 'catchingfire', 'gravity',
              'argo', 'pacificrim', 'americanhustle', 'dispicableme2',
              'warmbodies', 'afterearth', 'theinternship', 'elysium',
              'wolfofwallstreet', 'battlefieldearth', 'frozen',
              'twelveyearsslave', 'thegodfather'
              ]
#Loop through movies
for movie in range(movie_start,len(url_list)):

    url_base = url_list[movie]
    title = movie_list[movie]
    pg = 1

    #Create a csv file to write results to
    out = open('csv/' + title + '.csv', 'wb')
    writer = csv.writer( out )

    #Loop through pages of reviews
    more_reviews = True
    while more_reviews:
        url = url_base + str(pg)
        
        site = urllib2.urlopen(url)
        doc = site.read()
        
        review_counter = 0
        #Loop through to extract each review as long as it can find the tag
        while doc.find(Tag) > 0:

            #Count reviews to determine if we should go to the next page
            review_counter = review_counter + 1
            
            #The tag marks the beginning of a review so find the next instance
            ind = doc.find(Tag)
            
            #Shorten the document by removing everything before next review
            doc = doc[ind:]
            
            #Div tag immediately precedes each review
            ind = doc.find(div)
            
            #Shorten to remove the div tag
            doc = doc[ind+len(div):]
            
            #Div tag also immediately follows each review, find the next one
            ind = doc.find(div)
            
            #The review is everything up the div tag so save it
            review = doc[:ind]
            
            #Shorten the doc so it starts after the review that was just extracted
            doc = doc[ind:]
            
            #Remove leading linebreaks/tabs
            switch = True
            while switch:
                if review[0] == '\n' or review[0] == '\t':
                    review = review[1:]
                else:
                    switch = False
            switch = True

            #Remove trailing linebreaks/tabs
            while switch:
                if review[-1] == '\n' or review[-1] == '\t':
                    review = review[:-1]
                else:
                    switch = False

            #Replace html coded special characters
            review = review.replace('&#39;',"'")
            review = review.replace('&quot;','"')
            review = review.replace("<br/>",' ')
            review = review.replace('&lt;','<')
            
            #Write the review to csv
            writer.writerow( [review] )

        #Increment for page number in url
        pg = pg + 1
        if review_counter == 0:
            more_reviews = False
        
    #Close csv
    out.close()
    print title + '.csv saved'
