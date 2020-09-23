# python3

_prime = 500_007    # big prime number
_multiplier = 23    # random value between 1 and _prime-1

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(string, _prime, _multiplier):
    """ not a usual hash function because it doesn't have cardinality (m) """
    ans = 0
    for c in reversed(string):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans

def precompute_hashes(text, pattern, _prime, _multiplier):
    len_substrs = len(text) - len(pattern) + 1
    hashes = [0] * len_substrs
    hashes[-1] = poly_hash(text[-len(pattern):len(text)], _prime, _multiplier)
    
    # complicated like this to reduce time instead of bare x**len(p)
    # because bare x**len(p) will likely involve large number greater than _prime
    # which greatly increases time complexity
    x_power_len_pattern = 1
    for _ in range(1, len(pattern) + 1):
        x_power_len_pattern = (x_power_len_pattern * _multiplier) % _prime
    
    for idx in range(len_substrs-2, -1, -1):
        hashes[idx] = (_multiplier * hashes[idx+1] + ord(text[idx]) - x_power_len_pattern * ord(text[idx + len(pattern)])) % _prime
    
    return hashes

def get_occurrences(pattern, text):
    result = []
    pattern_hash = poly_hash(pattern, _prime, _multiplier)
    substr_hashes = precompute_hashes(text, pattern, _prime, _multiplier)

    # don't create additional array of possible substrings to improve readability
    # it will impact the memory limit
    # use direct string slicing instead
    for idx in range(len(text) - len(pattern) + 1):
        if pattern_hash == substr_hashes[idx]:
            if pattern == text[idx:idx+len(pattern)]:
                result.append(idx)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

