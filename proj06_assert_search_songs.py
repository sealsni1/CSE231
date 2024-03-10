from proj06 import search_songs

data_dict = {'Adele': {'All I Ask': {'use', 'honesty', 'scared', 'hand', 'tell', 'door', 'pretend', 'last', 'sure', 'lovers', 'leave', 'forgiveness', 'say', 'ask', 'night', 'vicious', 'ends', 'love', 'coming', 'left', 'knows', 'asking', 'lesson', 'memory', 'wanna', 'heart', 'eyes', 'let', 'take', 'matters', 'give', 'way', 'play', 'cruel', 'friend', 'run', 'since', 'get', 'cause', 'hold', 'one', 'said', 'next', 'wrong', 'like', 'remember', 'tomorrow', 'need', 'speak', 'know', 'word'}, "Can't Let Go": {'lied', 'write', 'lump', 'truth', 'even', 'baby', 'tell', 'gave', 'die', 'save', 'dark', 'heaven', 'thinking', 'round', 'platter', 'go', 'went', 'feel', 'everything', 'hid', 'seam', 'loved', 'let', 'sometimes', 'throat', 'hope', 'yet', 'thought', 'wanted', 'oooh', 'time', 'kill', 'find', 'note', 'told', 'coat', 'slow', 'said', 'much', 'faked', 'life', 'like', 'hard', 'arms', 'know'}}, 'Bob Dylan': {'4Th Time Around': {'threw', 'else', 'filled', 'dirt', 'forgotten', 'waste', 'wasted', 'last', 'must', 'leave', 'words', 'worked', 'breaking', 'handed', 'ask', 'back', 'pockets', 'gallantly', 'go', 'went', 'picture', 'crutch', 'jamaican', 'loved', 'stood', 'better', 'screamed', 'till', 'tapped', 'waited', 'give', 'got', 'straightened', 'sense', 'brought', 'cried', 'covered', 'thought', 'forced', 'took', 'get', 'rum', 'finding', 'something', 'spit', 'make', 'buttoned', 'tried', 'look', 'face', 'wheelchair', 'hands', 'drum', 'felt', 'shoe', 'fell', 'piece', 'everybody', 'leaned', 'asked'}, 'A Satisfied Mind': {'fame', 'ones', 'money', 'start', 'old', 'certain', 'dreamed', 'leave', 'say', 'game', 'things', 'someone', 'suddenly', 'man', 'world', 'lifes', 'comes', 'everything', 'dime', 'loved', 'richer', 'ten', 'little', 'way', 'run', 'lost', 'fortune', 'get', 'time', 'one', 'far', 'times', 'satisfied', 'find', 'wading', 'life', 'doubt', 'hard', 'friends', 'heard', 'happened', 'know', 'many'}}}

student_data = search_songs(data_dict, {'heaven'})
instructor_data = [('Adele', "Can't Let Go")]
print("student data:   ", student_data)
print("instructor data:", instructor_data)

assert student_data == instructor_data

student_data = search_songs(data_dict, {'time'})
instructor_data = [('Adele', "Can't Let Go"), ('Bob Dylan', 'A Satisfied Mind')]
print("student data:   ", student_data)
print("instructor data:", instructor_data)

assert student_data == instructor_data

student_data = search_songs(data_dict, {'time', 'tell', 'let'})
instructor_data = [('Adele', "Can't Let Go")]
print("student data:   ", student_data)
print("instructor data:", instructor_data)

assert student_data == instructor_data