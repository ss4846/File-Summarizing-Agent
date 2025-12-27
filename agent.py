from file_reader import read_file
from summarizer import summarize_text

class DocumentSummarizationAgent:
    def process(self, path):
        """Processes the document at the given path and returns its summaries.

        Args:
            path (str): The path to the document file."""
        
        print("Reading file...")
        text = read_file(path)

        print("Summarizing text...")
        summary = summarize_text(text)

        return summary