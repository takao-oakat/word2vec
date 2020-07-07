from gensim.models import word2vec

model = word2vec.Word2Vec.load("./wiki.model")
# a、bに任意のテキストを入力してその文字の類似性を算出する
results = model.wv.similarity(["a"], "b")
print(results)
