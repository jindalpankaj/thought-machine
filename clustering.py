# Function 1:
# Inputs:
#   Previous thoughts, list
# Processing:
#   Train data already existing inside the DB
#       Make clusters - would be many! As starting, use thoughts from r/shower_thoughts
# Output:
#   None

# Function 2:
# Inputs:
#   New thought, t, string
#   Number of matching thoughts to return, m, integer
# Processing:
#   Call function 1 - form clusters with updated data (every single time?)
#   Use t
# Output:
#   Matched thoughts, list of size m