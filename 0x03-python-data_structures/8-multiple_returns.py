#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    if not sentence:
        return  (0, None)

    else:
        return(len(sentence), sentence[0])
        
