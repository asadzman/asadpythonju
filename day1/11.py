class Soln:
    def search(self,text):
        words=text.lower().split()
        unique_words=set(words)

        pallindroms=[]
        for word in unique_words:
            if len(word)>0 and word==word[::-1]:
                pallindroms.append(word)

        return unique_words,pallindroms
    

text=str(input("enter a text "))
obj=Soln()
unique_words,pallindroms=obj.search(text)

print(f"the unique words are : {unique_words}")
print(f"palindromes are : {pallindroms}")
