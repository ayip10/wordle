import string
# ECS 32A
# Assignment 6
#
# Word Counting Class
import wordle
# the Count class.  The wordleFromObject function takes a Count object as
# input, and calls its getTopWords method. 
class Count:
        # method to initialize any data structures, such as a dictionary to
        # hold the counts for each word, and a list of stop words
        def __init__(self):
                print("Initializing Word Counter")
                # set the attrbute wordCounts to an empty dictionary
                self.wordCounts = {}
##                The file "stop_words.txt" contains a list of frequent words
##                in English. In the __init__
##                method of Counts, read in this file and store
##                the stop words in a list or dictionary (either
##                one could work; what are the pros and cons?

                self.liststopword = []
                stopWords = open("stop_words.txt","r")
                                      
               
                for line in stopWords:
                    line = line.strip()
                    line = line.rstrip()
                    self.liststopword.append(line)
                    


        def incCount(self,word):
##                        
##You'll find that words tend to show up in the document in different forms, for instance
##"Well", "'Well", "well," and "well". To count them all together, we'd like to convert the
##first three forms to "well" before inserting or incrementing the dictionary item. Clean
##words by converting them to lower case and stripping punctuation off the ends. See
##the latest word counting program on canvas to see how this is done.

                word = word.lower()
                word = word.strip(string.punctuation)

                 # method to add one to the count for a word in the dictionary.
        # if the word is not yet in the dictionary, we'll need to add a
        # record for the word, with a count of one.
        #If, after cleaning, the word is the empty string, don't insert it into the dictionary!
                
                if word != "" and word not in self.liststopword: 

        # If the word is already in the dictionary,
        #your code should increment its count.

                    if word in self.wordCounts:
                        self.wordCounts[word] = self.wordCounts.get(word,0) +1
                    else:
                        self.wordCounts[word] = 1                    
                        

      
        
                return                        

        # method to look up the count for a word
        def lookUpCount(self,word):
           return self.wordCounts.get(word,0)     
           

        # method to get the most frequent words out of the dictionary.
        # The argument "num" indicates how many words to return. 
        def getTopWords(self,num):
##                Unfortunately dictionaries do not come with a built-in sort method;
##                only lists have a  sort method, so we'll need
##                to put the dictionary items into a list. For instance, given  this dictionary:
                #put dictionary items into a list
                dictionaryitems = []

                for word,count in self.wordCounts.items():
                        t = (count,word)
                        dictionaryitems.append(t)
                dictionaryitems.sort(reverse=True)
                topwords = []        
                for i in range(num):
                                t = dictionaryitems[i]
                                topwords.append(t)
                                
                return topwords

        
        

                
# The main program 
def main():
                                
        # Make a new counter object 
        # the counter holds the counts for all the words
        counter = Count()
##
##        # Test code for Part 1
##        # These lines test out the methods you write in part 1.  
##        # Comment this code once you have completed part 1.
##        # It should print 1, 2, 0, and finally 0. 
##        counter.incCount("Well,")
##        counter.incCount("oven")
##        counter.incCount("well")
##        counter.incCount("....'")
##        print(counter.lookUpCount("oven"))
##        print(counter.lookUpCount("well"))
##        print(counter.lookUpCount("pizza"))
##        print(counter.lookUpCount(""))
##        return

        # open the file
        filename = input("Enter book file:")
        infile = open(filename,"r")


        # put a loop here that extracts all words and
        # inserts each word into the counter object by calling
        # the counter.incCount() method
##         You can divide every line
##of the file into words using the "split" string method, and use your
##incCount method to count each word.

        for line in infile:
            #no argument on split defaults to all whitespace chars
            firstword = line.split()
            for word in firstword:
                counter.incCount(word)

        # close the file
        infile.close()
        
        # Test code for Part 2 and 3  
        # Comment this code once you have completed part 3.
##        print(counter.lookUpCount("alice"))
##        print(counter.lookUpCount("rabbit"))
##        print(counter.lookUpCount("and"))
##        print(counter.lookUpCount("she"))
##        return

        # Test code for Part 4 and 5
        topTen = counter.getTopWords(10)
        print(topTen)

        # Test code for Part 5
        # Import the wordle module and uncomment the call to the wordle function! 
        wordle.wordleFromObject(counter,30)
        

# run the main program
main()
        
