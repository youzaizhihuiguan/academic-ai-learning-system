import csv


def average_score(path, scores=None):
    if scores is None:
        scores = []
    with open(path, newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            scores.append(int(row["score"]))
    return len(scores), sum(scores) / len(scores)
