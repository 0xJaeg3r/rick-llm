from datasets import Dataset
import os

# Create dummy ShareGPT-style conversation
dummy_data = [
    {
        "conversations": [
            {"from": "system", "value": "You are Rick Sanchez."},
            {"from": "human", "value": "What's going on, Rick?"},
            {"from": "gpt", "value": "Morty! We gotta go, the Citadel's collapsing!"}
        ]
    }
]

# Create Hugging Face-compatible dataset
dummy_dataset = Dataset.from_list(dummy_data)

# Push to Hugging Face (replace with your username/org + dataset name)
dummy_dataset.push_to_hub(
    "TBBTLovers/test-push-dataset",  # e.g. TBBTLovers/test-rick-chat
    token=os.getenv("HUGGINGFACE_TOKEN")
)