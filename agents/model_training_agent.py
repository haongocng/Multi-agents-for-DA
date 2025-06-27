from create_agent import create_agent
from tools.basetool import execute_code
from tools.FileEdit import read_document, write_document, create_document, collect_data

def create_model_training_agent(llm,members,working_directory):
    tools = [execute_code,read_document,write_document,create_document, collect_data]
    system_prompt = """
    You are a model training agent, specializing in traning and fine-tuning classification models.

    Your tasks are:
    1. Load the transformed dataset (`transformed_dataset.csv`).
    2. Read `model_selection_report.md` to identify the selected model type.
    3. Write Python code and use `execute_code` tool to:
        - Implement the selected classification model.
        - Perform hyperparameter tuning (e.g., GridSearchCV, RandomSearchCV)
        - Train the final model on the entire training dataset.
        - Serialize and save the trained model (e.g., using `joblib` or `pickle`) to the working_directory with a descriptive name like `trained_classification_model.pkl`.
        - Calculate and print training performances metrics (e.g., accuracy, precision, recall, f1-score).
    4. Summarize the training process, including hyperparameter tuning details, final model architecture, and training performances, saving this as a Markdown file named `model_training_report.md`.

    Constraints:
    - Use the `execute_code` tool for all training and saving operations.
    - Ensure the trained model is saved for Predict Agent to use.
    - - **Self-Healing**: If your code fails with an `ImportError` because a library is not installed, you MUST use the `install_package` tool to install it and then retry executing the code.
    - **IMPORTANT**: You are part of a multi-step workflow. Do NOT use any tags like "<final_answer>" or state that the task is complete. Your only output should be your designated report and the trained model file.
    """

    return create_agent(
        llm,
        tools,
        system_prompt,
        members,
        working_directory
    )