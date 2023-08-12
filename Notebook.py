import nbformat

class Notebook:
    '''
    The Notebook class reads a Jupyter Notebook file and extracts the questions, charts, and code snippets.
    The extracted information is organized into slides, each containing a title, question, code, and chart (if present).

    Attributes:
        notebook_path (str) : The path to the Jupyter Notebook file.
        slides        (List[dict]) : A list of slides, each containing a title, question, code, and chart (if present).

    Methods:
        extract_slides : Reads the notebook and extracts the slides.
        get_slides     : Returns the extracted slides.
        __call__       : Reads the notebook, extracts the slides, and returns them.
    '''

    def __init__(self, notebook_path: str):
        self.notebook_path = notebook_path
        self.slides = []

    def extract_slides(self):
        '''
        Reads the notebook and extracts the slides containing the title, question, code, and chart (if present).
        '''

        notebook = nbformat.read(self.notebook_path, as_version=4)
        
        for i, cell in enumerate(notebook.cells[1:]):
            slide = {}
            
            if cell.cell_type == 'code':

                slide['code'] = cell.source
                
                first_line = cell.source.split('\n')[0]
                if first_line.startswith('#'):
                    title_question    = first_line[1:].strip() # Remove the '#' and any leading/trailing whitespace
                    title, question   = title_question.split('.', 1) # Split by the first '.' character

                    if i == 0:
                        slide['title'] = "Dataset Schema"
                    else:
                        slide['title'] = f"Question {title.strip()}"
                        
                    slide['question'] = question.strip()
                
                for output in cell.outputs:
                    if output.output_type == 'display_data':
                        if 'image/png' in output.data:
                            image_data = output.data['image/png']
                            slide['chart'] = image_data
                
                self.slides.append(slide)

    def get_slides(self):
        '''
        Returns the extracted slides.
        '''

        return self.slides

    def __call__(self):
        '''
        Reads the notebook, extracts the slides, and returns them.
        '''

        self.extract_slides()
        return self.get_slides()