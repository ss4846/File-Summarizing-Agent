# About
The file summarizer agent reads a pdf, docx or any other readable file and creates a short summary(50-100 words), long summary(200-300 words) and key takeaways(5-10 bullet points) of the document. Google's gemini-2.5-flash model was used for generating content.

## Usage
1. Clone the repository
```bash
git clone https://github.com/ss4846/File-Summarizing-Agent
```
2. Change directory to project folder
```bash
cd "\path\to\folder\
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the file
```bash
python main.py <document_to_be_summarized>.<doc_type>
```
