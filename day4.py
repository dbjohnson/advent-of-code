from md5 import md5

key = 'ckczppom'
def winner(d, num_zeros):
    return md5(key + str(d)).hexdigest().startswith('0' * num_zeros)

for part, num_zeros in (('part 1', 5), ('part 2', 6)):
    x = 0
    while True:
        if winner(x, num_zeros):
            print part, x
            break
        x += 1

