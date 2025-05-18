PHONY: all setup create-dataset download-model finetune

# Set up dependencies
setup:
	@echo "Installing dependencies"
	pip install -r requirements.txt
	pip install torchvision@https://download.pytorch.org/whl/cu121/torchvision-0.20.1%2Bcu121-cp310-cp310-linux_x86_64.whl
	pip install transformers==4.47.1 unsloth xformers

# Create Hugging Face dataset
create-dataset:
	@echo "Creating HF dataset..."
	python src/rick_llm/dataset.py

# Download the base model
download-model:
	@echo "Downloading model files..."
	python src/rick_llm/download_model.py

# Fine-tune the model
finetune:
	@echo "Fine-tuning Rick LLM..."
	python src/rick_llm/finetune.py