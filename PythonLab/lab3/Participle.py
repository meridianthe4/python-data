# Q.3.In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A simple set of rules can be given as follows:
#  a. If the verb ends in e, drop the e and add ing 
#  b. If the verb ends in ie, change ie to y and add ing
# Write a function make_ing_form() which accepts a list of verbs and returns a dictionary with verb : present participle


def make_ing_form(verbs):
    result = {}
    for verb in verbs:
        # if verb.endswith("ie"):
        if verb[-2:] == "ie":        
            result[verb] = verb[:-2] + "ying"
        elif verb[-1:] == "e":       
            result[verb] = verb[:-1] + "ing"
        else:                   
            result[verb] = verb + "ing"
    return result

verbs = ["drive", "make", "lie", "die", "run", "swim"]
print(make_ing_form(verbs))




        