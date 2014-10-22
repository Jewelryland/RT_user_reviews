from anew_module import anew
import csv
import string

#List of movie review files as extracted from rotten tomatoes website
movie_list = ['sharknado.csv', 'manofsteel.csv', 'catchingfire.csv', 'gravity.csv',
              'argo.csv', 'pacificrim.csv', 'americanhustle.csv', 'dispicableme2.csv',
              'warmbodies.csv', 'afterearth.csv', 'theinternship.csv', 'elysium.csv',
              'wolfofwallstreet.csv', 'battlefieldearth.csv', 'frozen.csv',
              'twelveyearsslave.csv', 'thegodfather.csv'
              ]

#These words will be removed from the corresponding movies' reviews
movie_words = [['shark'],
            ['man', 'steel'],
            ['hunger', 'games', 'catching', 'fire'],
            ['gravity'],
            ['argo'],
            ['pacific', 'rim'],
            ['american', 'hustle'],
            ['dispicable', 'me'],
            ['warm', 'bodies'],
            ['after', 'earth'],
            ['internship'],
            ['elysium'],
            ['wolf', 'wall', 'street'],
            ['battle', 'field', 'earth', 'battlefield'],
            ['frozen'],
            ['twelve', 'years', 'slave'],
            ['godfather', 'god', 'father']
        ]

mov_count = 0
for movie in movie_list:
    total_sent = 0
    review_counter = 0

    #Open csv reader and writer
    inp = open('csv/' + movie,'rb')
    i_reader = csv.reader(inp)
    out = open('output/output_' + movie, 'wb')
    writer = csv.writer(out)

    for row in i_reader:
        #Make all letters lowercase
        row_str = row[0].lower()
        
        #Replace emoticons
        row_str = row_str.replace(':)',' happy ')
        row_str = row_str.replace(':-)',' happy ')
        row_str = row_str.replace('(:',' happy ')
        row_str = row_str.replace('(-:',' happy ')
        row_str = row_str.replace(':D',' happy ')
        row_str = row_str.replace(':-D)',' happy ')
        row_str = row_str.replace(';)',' happy ')
        row_str = row_str.replace(';-)',' happy ')
        row_str = row_str.replace(';D',' happy ')
        row_str = row_str.replace(';-D',' happy ')
        row_str = row_str.replace(':(',' sad ')
        row_str = row_str.replace(':-(',' sad ')
        row_str = row_str.replace('):',' sad ')
        row_str = row_str.replace(')-:',' sad ')
        row_str = row_str.replace('D:',' sad ')
        row_str = row_str.replace('D-:',' sad ')
        row_str = row_str.replace('<3',' love ')

        #remove movie title words from review
        for word in movie_words[mov_count]:
            row_str = row_str.replace(word,'')

        #Remove all non lowercase letters/spaces
        i=0
        ascii_list = string.ascii_lowercase + ' '
        while i < len(row_str):
            if row_str[i] not in ascii_list:
                row_str = row_str.replace(row_str[i],'')
            else:
                i = i + 1

        #Calcualte sentiment for each review
        sent = anew.valence(row_str.split())
        
        #Count number of anew terms found, only output if > 1
        num_found = sum(anew.exist(row_str.split()))
        
        if num_found > 1:
            writer.writerow([row[0],row_str,sent])
            review_counter = review_counter + 1
            total_sent = total_sent + sent
            
    out.close()
    avg_sent = total_sent / review_counter
    
    print movie[:-4] + ' has ' + str(review_counter) + " usable reviews with an average sentiment of " + str(round(avg_sent,4))
    mov_count = mov_count + 1

