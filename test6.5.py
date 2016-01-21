# Write code using find() and string slicing (see section 6.10) to extract the
# number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475";
# fining ":"
atpos = text.find(":")
print atpos

# create variable from position with ":" to end of string
pastpos = text[atpos+1:]
# cut blank (space) in string
x = float (pastpos.strip())
print x




