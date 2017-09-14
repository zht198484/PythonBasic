import os

os.chdir('../../../')

with open('222.txt') as f:
    line = f.readline()

scores = line.replace(' ', '').split(',')
print scores

# a new sorted copy
scores1 = sorted(scores)
print scores
print scores1

# inplace sort
scores.sort()
print scores


def sanitize(score):
    if '-' in score:
        splitter = '-'
    elif ':' in score:
        splitter = ':'
    else:
        return score

    (mins, secs) = score.split(splitter)
    return mins + '.' + secs


clean_scores = [float(sanitize(score)) for score in scores]
print clean_scores

sorted_clean_scores = sorted(clean_scores)
print sorted_clean_scores

unique_sorted_clean_scores = sorted(set(clean_scores))
print unique_sorted_clean_scores
