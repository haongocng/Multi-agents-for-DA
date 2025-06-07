# Multi-Agent System for Automated Data Analysis
---
## INTRODUCTIONS:
This project implements a multi-agent system using Python and the LangGraph library to perform a comprehensive, step-by-step data analysis on a given dataset. The system is designed to automate the entire analytical workflow, from initial data exploration to final insight synthesis, by leveraging a team of specialized AI agents.

## Workflow

The analysis is conducted through a predefined pipeline of agents, where the output of one agent becomes the input for the next. This ensures a structured and thorough examination of the data. The workflow is as follows:

1.  **DataExplorer**: Performs an initial exploratory data analysis (EDA) to understand the dataset's structure, data types, and basic statistics.
2.  **DataStatistic**: Conducts detailed statistical tests, such as correlation and distribution analysis.
3.  **DataCluster**: Applies clustering algorithms like K-Means to identify natural groupings within the data.
4.  **DataVisualization**: Generates visual representations (e.g., charts, plots) of the data to highlight trends and patterns.
5.  **HypothesisGenerator**: Formulates specific, answerable questions and hypotheses based on all previous analysis reports.
6.  **Reasoner**: Answers the questions posed by the HypothesisGenerator using data-driven evidence from prior reports.
7.  **QualityReview**: Reviews all previous reports and synthesizes the findings into a single, comprehensive summary.
8.  **Synthesis**: Generates the final high-level, actionable insights based on the complete analysis.

## Technology

* **Framework**: LangChain & LangGraph
* **Language Models**: OpenAI / Google / DeepInfra 
* **Data Manipulation**: Pandas
* **Scientific & Statistical Computing**: Scipy, Scikit-learn
* **Data Visualization**: Matplotlib, Seaborn

---
## INSTRUCTIONS:

### 1. Clone project

```bash
git clone https://github.com/Orjnzz/Multi-agents-for-DA.git
cd Multi-agents-for-DA
```

### 2. Set up environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Create and activate Conda environment:
```bash
conda create -n data_assistant
conda activate data_assistant
```
Note: If system doesn't have Anaconda, only need to install Miniconda for experience

### 4. Install
```bash
pip install -r requirements.txt
```

### 5. Run
```bash
python main.py
```
### Note: rename "sample.env" to ".env" file and fill api_key of LLM, CONDA environment

## Acknowledgements

This project was inspired by and based on the work from the [DataGen repository](https://github.com/MaterializeInc/datagen).
