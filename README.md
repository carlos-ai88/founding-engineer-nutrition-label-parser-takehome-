1. Overview
Purpose: Explains what the project does at a high level.
Content: The system extracts structured nutritional information from messy product label images and normalizes the data.
Why it matters: Shows that you understand the real-world challenge of inconsistent labels and messy input data.
2. Repository Structure
Purpose: Makes it easy for someone to navigate your repo.
Content: Lists all key folders and files, including source_code/, sample_images/, sample_output/, and output/.
Why it matters: Signals that your project is organized, modular, and maintainable.
3. Approach
Purpose: Explains how you solved the problem.
Content: Step-by-step pipeline:
OCR extraction → raw text
Parsing → identify nutrients and amounts
Normalization → map to canonical names and units
Structuring → output CSV
Why it matters: Shows your ability to decompose a messy problem and make deliberate choices.
4. Architecture
Purpose: Visual snapshot of the pipeline.
Content: Diagram-style flow: Images → OCR → Parser → Normalizer → CSV Output
Why it matters: Shows clarity and modularity; easy to scale or swap components.
5. Key Design Decisions & Tradeoffs
Purpose: Explains why you made certain choices instead of trying to handle every edge case.
Examples:
Used rule-based parsing instead of ML → transparent, fast, and easy to debug.
Ignored layout reconstruction → focuses on text extraction for speed and clarity.
Limited normalization → prioritizes high-frequency nutrients.
Why it matters: Demonstrates judgment under ambiguity — one of the most important evaluation criteria.
6. Output Schema
Purpose: Shows exactly what your CSV contains.
Content: Columns:
product_image
nutrient_name_raw
nutrient_name_standard
amount
unit
Why it matters: Makes your output predictable and easy to consume.
7. Limitations
Purpose: Acknowledges what your system does not handle.
Content: OCR noise, multi-line nutrients, irregular table formats, multilingual labels.
Why it matters: Shows honesty and realistic scope — important in take-home assignments.
8. Hardest Parts & Ambiguities
Purpose: Highlights the problem-solving challenges.
Content: Inconsistent nutrient naming, noisy OCR, missing units, layout variations.
Why it matters: Shows critical thinking and awareness of the most complex parts of the task.
9. Future Improvements
Purpose: Shows how you would expand the system if given more time.
Examples: Layout-aware parsing, NLP-based nutrient extraction, unit conversions, multilingual support.
Why it matters: Signals long-term thinking and scalability awareness.
10. How to Run
Purpose: Gives step-by-step instructions to replicate your results.
Content: Install dependencies, add images, run main.py, check output/nutrition_data.csv.
Why it matters: Ensures your project is easy to test and demonstrates professionalism.