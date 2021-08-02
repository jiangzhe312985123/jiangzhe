from nltk.translate.bleu_score import sentence_bleu
reference = [['It', 'is', 'a', 'boy'], ['It', 'is', 'boy']]
candidate = ['It', 'is', 'a', 'boy']
score = sentence_bleu(reference, candidate)
print(score)


# # 1-gram individual BLEU
# from nltk.translate.bleu_score import sentence_bleu
# reference = [['It', 'is', 'the', 'boy']]
# candidate = ['It', 'is', 'a', 'boy']
# score = sentence_bleu(reference, candidate, weights=(1, 0, 0, 0))
# print(score)

# # n-gram individual BLEU
# from nltk.translate.bleu_score import sentence_bleu
# reference = [['It', 'is', 'the', 'boy']]
# candidate = ['It', 'is', 'a', 'boy']
# print('Individual 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
# print('Individual 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 1, 0, 0)))
# print('Individual 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 0, 1, 0)))
# print('Individual 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0, 0, 0, 1)))



# # cumulative BLEU scores
# from nltk.translate.bleu_score import sentence_bleu
# reference = [['It', 'is', 'the', 'boy']]
# candidate = ['It', 'is', 'a', 'boy']
# print('Cumulative 1-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 0, 0)))
# print('Cumulative 2-gram: %f' % sentence_bleu(reference, candidate, weights=(0.5, 0.5, 0, 0)))
# print('Cumulative 3-gram: %f' % sentence_bleu(reference, candidate, weights=(0.33, 0.33, 0.33, 0)))
# print('Cumulative 4-gram: %f' % sentence_bleu(reference, candidate, weights=(0.25, 0.25, 0.25, 0.25)))