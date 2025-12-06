def recite(start_verse, end_verse):

    def recite_verse(verse):
        numerals = ["first",
                   "second",
                   "third",
                   "fourth",
                   "fifth",
                   "sixth",
                   "seventh",
                   "eighth",
                   "ninth",
                   "tenth",
                   "eleventh",
                   "twelfth",]
    
        presents = ["a Partridge in a Pear Tree.",
                    "two Turtle Doves,",
                    "three French Hens,",
                    "four Calling Birds,",
                    "five Gold Rings,",
                    "six Geese-a-Laying,",
                    "seven Swans-a-Swimming,",
                    "eight Maids-a-Milking,",
                    "nine Ladies Dancing,",
                    "ten Lords-a-Leaping,",
                    "eleven Pipers Piping,",
                    "twelve Drummers Drumming,",        
        ]
        response = []
        response.append(f"On the {numerals[verse-1]} day of Christmas my true love gave to me:")
        for index in range (verse, 0, -1):
             response.append(f"{'and ' if verse > 1 and index == 1 else ''}{presents[index-1]}")
    
        #print ([" ".join(response)])
        return " ".join(response)

    return [recite_verse(index) for index in range (start_verse, end_verse+1)]
 

    