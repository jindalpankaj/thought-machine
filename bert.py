#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Han Xiao <artex.xh@gmail.com> <https://hanxiao.github.io>

# NOTE: First install bert-as-service via
# $
# $ pip install bert-serving-server
# $ pip install bert-serving-client
# $

# simple similarity search on FAQ

import numpy as np
import pandas as pd
from bert_serving.client import BertClient

def getSimilarSentences(current_sentence, previous_sentences, threshold):

    bc = BertClient(port=4000, port_out=4001)
    doc_vecs = bc.encode(previous_sentences)

    query_vec = bc.encode([current_sentence])[0]

    # compute normalized dot product as score
    cosine_similarity = np.sum(query_vec * doc_vecs, axis=1) / np.linalg.norm(doc_vecs, axis=1)

    prev_cos = pd.DataFrame(list(zip(previous_sentences, cosine_similarity)),
                            columns=['Sentences', 'Cosine'])

    prev_cos.sort_values(by=['Cosine'], ascending=False, inplace=True)
    # print(prev_cos)

    matching_sentences = prev_cos.loc[prev_cos['Cosine'] > threshold, 'Sentences', ]
    matching_sentences = matching_sentences.tolist()

    return matching_sentences
