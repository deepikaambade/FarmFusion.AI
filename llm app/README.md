RAG-Powered TinyLlama for Indian States and Districts Data

This project implements a Retrieval-Augmented Generation (RAG) system using the TinyLlama LLM model, enhanced with comprehensive data about Indian states and districts from 1967 to 2019.

   Project Structure

- `output.pdf`: Contains 350,000 rows of data converted into unstructured text.
- `rag-tinyllama-1.py`: Python script implementing the RAG technique with TinyLlama.
- `demo_video.mp4`: Video demonstration of setup and usage.

   Features

- Utilizes data from 1967 to 2019 covering Indian states and districts.
- Implements RAG technique for improved question answering.
- Powered by TinyLlama LLM model.
- Optimized for queries related to Indian geographical and historical data.

   Prerequisites

- Python 3.7+
- Ollama
- TinyLlama model
- Required Python libraries (list them in a requirements.txt file)

   Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/rag-tinyllama-india.git
   cd rag-tinyllama-india
   ```

2. Install required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Download and run the TinyLlama model using Ollama:
   ```
   ollama run tinyllama
   ```

   Usage

1. Ensure the TinyLlama model is running via Ollama.

2. Run the RAG script:
   ```
   python rag-tinyllama-1.py
   ```

3. Start querying the model about Indian states and districts data.

   Demo

Check out our `demo_video.mp4` for a walkthrough of the setup process and example usage of the system.

   Data Source

The `output.pdf` file contains data points from 1967 to 2019, converted from a structured format (likely CSV or similar) into unstructured sentences. This data forms the knowledge base for our RAG system.

   Performance

This system is designed to provide accurate and detailed responses to queries about Indian states and districts, leveraging the comprehensive dataset spanning over five decades.

   Contributing

We welcome contributions to improve the system or expand the dataset. Please submit pull requests or open issues for any enhancements.

   License

GPL 2.O

   Acknowledgements

- TinyLlama model developers
- Ollama project


Would you like me to modify or expand any section of this README?
