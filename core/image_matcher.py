import os
import requests
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = (
    "https://api-inference.huggingface.co/models/"
    "openai/clip-vit-base-patch32"
)

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

THRESHOLD = 0.85
MARGIN = 0.05

CACHE_FILE = "catalog_embeddings.pkl"


def get_image_embedding(image_path):
    """
    Generate embedding using HuggingFace CLIP API.
    """

    with open(image_path, "rb") as f:

        response = requests.post(
            API_URL,
            headers=headers,
            data=f
        )

    result = response.json()

    return np.array(result)


def compute_catalog_embeddings(catalog_path):
    """
    Generate embeddings for all catalog images.
    """

    catalog_features = {}

    for file in os.listdir(catalog_path):

        path = os.path.join(
            catalog_path,
            file
        )

        embedding = get_image_embedding(path)

        catalog_features[file] = embedding

    return catalog_features


def load_catalog_embeddings(catalog_path):
    """
    Load cached embeddings if available.
    """

    if os.path.exists(CACHE_FILE):

        print("⚡ Loading cached embeddings...")

        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)

    print("⚙️ Computing embeddings...")

    catalog = compute_catalog_embeddings(catalog_path)

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(catalog, f)

    return catalog


def match_image(input_image_path, catalog_features):
    """
    Match customer image with catalog images.
    """

    input_embedding = get_image_embedding(
        input_image_path
    )

    scores = []

    for name, features in catalog_features.items():

        similarity = cosine_similarity(
            [input_embedding],
            [features]
        )[0][0]

        scores.append(
            (name, similarity)
        )

    scores = sorted(
        scores,
        key=lambda x: x[1],
        reverse=True
    )

    best_match, best_score = scores[0]

    second_score = (
        scores[1][1]
        if len(scores) > 1
        else 0
    )

    if (
        best_score < THRESHOLD
        or
        (best_score - second_score) < MARGIN
    ):
        return None, best_score

    return best_match, best_score