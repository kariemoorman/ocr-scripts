import argparse
import json 
import os
import fitz


class ocrPDF:
    def __init__(self, pdf_filepath): 
        self.pdf_filepath = pdf_filepath
        
    def extract_text(self): 
        # Load the PDF file
        pdf_document = fitz.open(self.pdf_filepath)
        # Initialize an empty dictionary to store extracted text
        extracted_text = {'document': self.pdf_filepath}
        # Extract text from each page
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            extracted_text[f'Page_{page_number}'] = page.get_text()
        # Close the PDF document
        pdf_document.close()
        
        # Generate the output file path
        output_filepath = os.path.splitext(self.pdf_filepath)[0] + '.json'
        
        # Write extracted text to a JSON file
        with open(output_filepath, 'w') as json_file:
            json.dump(extracted_text, json_file, indent=4)
        
        print(f"Extracted text saved to: {output_filepath}")

def main():
    parser = argparse.ArgumentParser(description="PDF Text Extractor")
    parser.add_argument('--pdf_filepath', '-f', type=str, help="PDF Filepath")
    args = parser.parse_args()
    
    extractor = ocrPDF(args.pdf_filepath)
    extractor.extract_text()

if __name__ == "__main__":
    main()
