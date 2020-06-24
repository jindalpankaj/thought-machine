# Program to measure similarity between two sentences using cosine similarity.

# Based on code from https://www.geeksforgeeks.org/python-measure-similarity-between-two-sentences-using-cosine-similarity/

# This method is just to create a first MVP. This similarity score should later be replaced by
# some clustering based methods, or, even better, BERT.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# sw contains the list of stopwords

def getSimilarSentences(current_sentence, previous_sentences, threshold):

    sw = stopwords.words('english')
    cosine_similarity = []

    X = current_sentence

    X_list = word_tokenize(X)
    X_set = {w for w in X_list if w not in sw}

    # print(X_set)

    for Y in previous_sentences:
        Y = str(Y)

        # tokenization
        Y_list = word_tokenize(Y)

        l1 = []
        l2 = []

        # remove stop words from string
        Y_set = {w for w in Y_list if w not in sw}

        # form a set containing keywords of both strings
        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set:
                l1.append(1)  # create a vector
            else:
                l1.append(0)
            if w in Y_set:
                l2.append(1)
            else:
                l2.append(0)

        # cosine formula
        c = 0
        for i in range(len(rvector)):
            c += l1[i] * l2[i]
        cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
        cosine_similarity.append(cosine)
        # print("similarity: ", cosine)

    prev_cos = pd.DataFrame(list(zip(previous_sentences, cosine_similarity)),
                            columns=['Sentences', 'Cosine'])

    prev_cos.sort_values(by=['Cosine'], ascending=False, inplace=True)
    # print(prev_cos)

    matching_sentences = prev_cos.loc[prev_cos['Cosine'] > threshold, 'Sentences', ]
    matching_sentences = matching_sentences.tolist()

    return matching_sentences


# temp = "Don't judge each day by the harvest you reap but by the seeds that you plant."
# prev = ["The future belongs to those who believe in the beauty of their dreams."]

# from app import prev_thoughts
# getSimilarSentences(temp, prev, 5)