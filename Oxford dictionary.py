# Dictionary of 4 words by user input
# dictionary give the meaning of the user demand meaning

dict={"accomplish":"poora karna",
      "speculators":"sattebaaj",
      "enterprising":"sahasii",
      "pitfalls":"khatara",
      "allegations":"aarop"}
print(dict)
print("Choose a word from the given options")
inpuT=input("Enter the word:\n")
print(dict.get(inpuT))