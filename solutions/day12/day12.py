import json

with open('input.txt', 'r') as fh:
    doc = json.load(fh)


def sum_nums(d, skip_fn=lambda x: False):
    if isinstance(d, dict):
        if skip_fn(d):
            return 0
        return sum_nums(d.keys(), skip_fn) + sum_nums(d.values(), skip_fn)

    total = 0
    for x in d:
        if isinstance(x, dict) or isinstance(x, list):
            total += sum_nums(x, skip_fn)
        else:
            try:
                total += x
            except:
                pass
    return total

print 'part 1', sum_nums(doc)
print 'part 2', sum_nums(doc, skip_fn=lambda d: 'red' in d.values())
