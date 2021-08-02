# # 1.计算Pn（Modified n-gram Precision）
# def _modified_precision(candidate, references, n)
# # 2.计算BP惩罚因子
# def _brevity_penalty(candidate, references)
# # 3.计算BLEU值
# def bleu(candidate, references, weights)

import math
def _brevity_penalty(candidate, reference):
    c = len(candidate)
    r = len(reference)
    if c > r:
        return 1
    else:
        return math.exp(1 - r / c)
