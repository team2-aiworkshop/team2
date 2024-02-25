# EduPill - TeensInAI Team 2

This is an eraly prototype for EduPill, which returns the best paragraphs from the given testfile for answering the user's questions.

## Instructions
1. Run the `main.py` script.
2. Set the location of the input file and press 'Load'. ***NOTE: All input files must be plain text files, with paragraphs delimited by tab characters.***
3. Wait for the program to load the file. This might take some time.
4. Enter a question in the top text edit and press 'Generate'.
5. The application should have displayed three paragraphs in the bottom text box, with *their relevance to the question in ascending order*.

## Dependencies
- [Multilingual-Latent-Dirichlet-Allocation-LDA](https://github.com/ArtificiAI/Multilingual-Latent-Dirichlet-Allocation-LDA/tree/master)
- `levenshtein_distance`
- `nltk`
- `PyQt5`