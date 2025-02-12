import subprocess

# Run the 'lms list' command
result = subprocess.run(['lms', 'list'], capture_output=True, text=True)

# Store the output in a string
output_str = result.stdout

# Split the output into lines and store them in an array
output_lines = output_str.splitlines()

# Write the lines to a file
with open('output.txt', 'w') as file:
    for line in output_lines:
        file.write(line + '\n')

# Optionally, print a confirmation message
print("Output written to 'output.txt'")
