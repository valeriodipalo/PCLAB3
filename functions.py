def word_count_col(df, text, new_col_name):
    """This function will define the number of words in each row of the considered dataframe
    df: dataframe to use
    text: the text column in the dataframe
    new_col_name: the name to which associate the column of word count"""
    tot = len(df)
    words = []
    for i in range(tot):
        words.append(len(df[text][i].split()))
    df[new_col_name] = words
    return df

def hello_what(word):
    print('hello ' + str(word))

