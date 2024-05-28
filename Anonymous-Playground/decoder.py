# http://[IP_ADDRESS]/zYdHuAKjP
# hEzAdCfHzA::hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN

# Hint:  'zA' = 'a'
# zA = (25 + 1) % 26
# (25 + 1) % 26 = 0
# 0 = 'a'

encoded_string_1 = 'hEzAdCfHzA'
encoded_string_2 = 'hEzAdCfHzAhAiJzAeIaDjBcBhHgAzAfHfN'


def decode_string(string):
	encoded_lowercase = string.lower()
	string_length = len(string)
	decoded_string = ''
	ascii_lower_a_value = ord('a')
	for i in range(0, string_length, 2):
		first_letter_value = ord(encoded_lowercase[i]) - ascii_lower_a_value + 1
		second_letter_value = ord(encoded_lowercase[i + 1]) - ascii_lower_a_value + 1
		new_value = (first_letter_value + second_letter_value - 1) % 26
		decoded_string += chr(new_value + ascii_lower_a_value)
	return decoded_string
	
print(decode_string(encoded_string_1)) # magna
print(decode_string(encoded_string_2)) # magnaisanelephant

# magna::magnaisanelephant

