# Open the input file in read mode and output file in write mode
with open('temp-converter.txt', 'r') as infile, open('output1.txt', 'w') as outfile:
    # Read the temperatures from the input file
    F = int(infile.readline().strip())
    C = int(infile.readline().strip())

    # Convert Fahrenheit to Celsius
    b = (F - 32) * 5/9
    outfile.write("The temperature in Celsius is: " + str(b) + "\n")

    # Convert Celsius to Fahrenheit
    d = (C * 9/5) + 32
    outfile.write("The temperature in Fahrenheit is: " + str(d) + "\n")
