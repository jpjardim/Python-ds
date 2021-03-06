# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)


# Definition of dictionary
europe2 = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
           'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }

# Update capital of germany
europe2['germany'] = 'berlin'

# Remove australia
del(europe2['australia'])

# Print europe
print(europe2)


# Dictionary of dictionaries
europe3 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe3['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe3['italy'] = data

# Print europe
print(europe3)
