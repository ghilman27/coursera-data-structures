# python3

import sys

# two different prime number for solving collision
M2 = 10**9 + 13
M1 = 10**9 + 7
X = 23 # random number between 1 to min(M1, M2) - 1

class Solver:
	def __init__(self, string):
		self.string = string
		self.hashes1 = [0] * (len(string)+1)
		self.hashes2 = [0] * (len(string)+1)
		self.x_pows1 = [0]
		self.x_pows2 = [0]
		x_pow1 = 1
		x_pow2 = 1

		# save x**len(substr) for every possible length
		# as computing them in every query is expensive
		for _ in range(1, len(string)):
			x_pow1 = (x_pow1 * X) % M1
			x_pow2 = (x_pow2 * X) % M2
			self.x_pows1.append(x_pow1)
			self.x_pows2.append(x_pow2)

		# save precomputed hash such
		# hashes[0] = hash of empty string
		# hashes[i] = hash for string[0:i]
		for i in range(1, len(string)+1):
			self.hashes1[i] = (X * self.hashes1[i-1] + ord(string[i-1])) % M1
			self.hashes2[i] = (X * self.hashes2[i-1] + ord(string[i-1])) % M2

	def ask(self, a, b, length):
		# we can compute hash of string[a:length+1] equal to
		# (hash of string[0:a+length] - (x**length % prime) * hash of string[0:a]) % prime
		hash1_b = ( self.hashes1[b+length] - self.x_pows1[length]*self.hashes1[b] ) % M1
		hash1_a = ( self.hashes1[a+length] - self.x_pows1[length]*self.hashes1[a] ) % M1
		hash2_a = ( self.hashes2[a+length] - self.x_pows2[length]*self.hashes2[a] ) % M2
		hash2_b = ( self.hashes2[b+length] - self.x_pows2[length]*self.hashes2[b] ) % M2

		# string a and b is equal only when hash of different prime basis m1 and m2 is equal
		# that means, poly_hash_a == poly_hash_b only when poly_hash_a % any_number == poly_hash_b % any_number
		# a great solution to overcome collision
		return hash1_a == hash1_b and hash2_a == hash2_b

s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, length = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, length) else "No")
