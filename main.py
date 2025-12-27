import sys
from agent import DocumentSummarizationAgent

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_document>")
        sys.exit(1)

    document_path = sys.argv[1]
    agent = DocumentSummarizationAgent()
    summary = agent.process(document_path)
    print("Summary:")
    print(summary)