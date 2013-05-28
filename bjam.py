from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx

class Dynam(object):pass

def generate_pattern(word, letters):

    output_pattern = []

    for l in word:
        if l in letters:
            output_pattern.append(l)
        else:
            output_pattern.append('_')

    return ''.join(output_pattern)

def get_dups(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def get_list_result_for_length(data, sub_dic, l_list):

    ul = [l for l in l_list]
    old_list = sub_dic[:]
    letters = []
    score = 0
    
    import pdb;pdb.set_trace()
    
    for letter in l_list:
        letters.append(letter)

        new_list = [word for word in old_list if letter not in word]
        old_list = [word for word in old_list if word not in new_list]

        if len(old_list) > 0:
            score+= 1
        
        patterns = [generate_pattern(word, letters) for word in old_list]

        for i, pattern in enumerate(patterns):
            if pattern in patterns[0:i] or pattern in pattern[i+1:]:
                new_list.append(old_list[i])

        if len(new_list) == 0:
            
            import pdb;pdb.set_trace()
            return score, old_list[0]
        if len(new_list)== 1:
            import pdb;pdb.set_trace()
            return score, new_list[0]

        old_list = new_list

    
        
def get_list_result(data, l_list):

    import pdb;pdb.set_trace()
    sub_dics= {}
    for word in data.dict:
        if sub_dics.has_key(len(word)):
            sub_dics[len(word)].append(word)
        else:
            sub_dics[len(word)] = [word]

    max_score = 0
    favoured_word= None
    
    for sub in sub_dics.itervalues():
        if len(sub) > 1:
            
            score, word = get_list_result_for_length(data, sub, l_list)

            if score > max_score:
                favoured_word = word

    if not favoured_word:
        favoured_word = data.dict[0]

    return favoured_word

def solver(data):

    list_results = []
    for l_list in data.lists:
        list_results.append(get_list_result(data, l_list))

    return ' '.join(list_results)

  
def data_builder(f):

    data = Dynam()

    data.dic_count, data.list_count = f.get_ints()

    data.dict = [f.readline() for i in range(data.dic_count)]
    data.lists = [f.readline() for i in range(data.list_count)]

    return data



cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "B")#, problem_size='small-attempt0')
