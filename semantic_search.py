from sentence_transformers import SentenceTransformer
import scipy.spatial
import pandas as pd
import numpy as np
import sys

print("About to create embedder now... \n ")
embedder = SentenceTransformer('bert-base-nli-mean-tokens')
print("Just finished creating embedder now... \n ")

def getSimilarSentences(current_sentence, previous_sentences, threshold):
    corpus = previous_sentences
    
    print("\n Corpus encoding start", file=sys.stderr)
    corpus_embeddings = embedder.encode(corpus)
    print("\n Corpus encoding ends", file=sys.stderr)
    
    query = [current_sentence]

    print("\n Query encoding start", file=sys.stderr)
    query_embedding = embedder.encode(query)
    print("\n Query encoding ends", file=sys.stderr)
    
    cosine_similarity = 1 - scipy.spatial.distance.cdist(query_embedding, corpus_embeddings, "cosine")[0]

    # print("\n Cosine Similarity scores are: \n ", cosine_similarity)

    prev_cos = pd.DataFrame(list(zip(previous_sentences, cosine_similarity)),
                           columns=['Sentences', 'Cosine'])

    prev_cos.sort_values(by=['Cosine'], ascending=False, inplace=True)
    print("\n New Sentence is: ", current_sentence, file=sys.stderr)
    print("\n Top 100 Previous sentences and their cosine-similarity with new query sentence is as follow: \n", prev_cos.head(100), file=sys.stderr)

    matching_sentences = prev_cos.loc[prev_cos['Cosine'] > threshold, 'Sentences', ]
    matching_sentences = matching_sentences.tolist()

    return matching_sentences

# corpus = ['A man is eating food.',
#           'A man is eating a piece of bread.',
#           'The girl is carrying a baby.',
#           'A man is riding a horse.',
#           'A woman is playing violin.',
#           'Two men pushed carts through the woods.',
#           'A man is riding a white horse on an enclosed ground.',
#           'A monkey is playing drums.',
#           'A cheetah is running behind its prey.'
#           ]
# 
# new_query = 'Someone in a gorilla costume is playing a set of drums.'

# print(getSimilarSentences(new_query, corpus, 0.5))

