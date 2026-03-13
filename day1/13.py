from collections import Counter
import re

class StringInsight:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\w+', text.lower())
        self.counts = Counter(self.words)

    def __len__(self):
        repetitive_words = [word for word, count in self.counts.items() if count > 1]
        total_rep_len = sum(len(word) * self.counts[word] for word in repetitive_words)
        return total_rep_len
    
    def get_most_common(self, n=3):
        return self.counts.most_common(n)
    
    def multi_length_count(self):
        methods = {
            "Method 1: Total Characters": len(self.text),
            "Method 2: Non-Space Characters": len(self.text.replace(" ", "")),
            "Method 3: Total Word Count": len(self.words),
            "Method 4: Unique Word Count": len(set(self.words))
        }
        return methods

# Example usage:
example_text = "Apple orange banana apple grape banana apple"
insight = StringInsight(example_text)

print(f"Length of repetitive words: {len(insight)}")
print(f"Top 2 words: {insight.get_most_common(2)}")
print(f"Four counts: {insight.multi_length_count()}")