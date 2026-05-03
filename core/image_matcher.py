import torch
import clip
from PIL import Image
import os
import pickle

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

THRESHOLD = 0.85
MARGIN = 0.05

CACHE_FILE = "catalog_embeddings.pkl"


def compute_catalog_embeddings(catalog_path):
    catalog_features = {}

    for file in os.listdir(catalog_path):
        path = os.path.join(catalog_path, file)

        image = preprocess(Image.open(path)).unsqueeze(0).to(device)

        with torch.no_grad():
            features = model.encode_image(image)
            features /= features.norm(dim=-1, keepdim=True)

        catalog_features[file] = features.cpu()

    return catalog_features


def load_catalog_embeddings(catalog_path):
    # ✅ Load from cache if exists
    if os.path.exists(CACHE_FILE):
        print("⚡ Loading cached embeddings...")
        with open(CACHE_FILE, "rb") as f:
            return pickle.load(f)

    print("⚙️ Computing embeddings (first time)...")
    catalog = compute_catalog_embeddings(catalog_path)

    with open(CACHE_FILE, "wb") as f:
        pickle.dump(catalog, f)

    return catalog


def match_image(input_image_path, catalog_features):
    image = preprocess(Image.open(input_image_path)).unsqueeze(0).to(device)

    with torch.no_grad():
        input_features = model.encode_image(image)
        input_features /= input_features.norm(dim=-1, keepdim=True)

    input_features = input_features.cpu()

    scores = []

    for name, features in catalog_features.items():
        similarity = (input_features @ features.T).item()
        scores.append((name, similarity))

    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    best_match, best_score = scores[0]
    second_score = scores[1][1] if len(scores) > 1 else 0

    if best_score < THRESHOLD or (best_score - second_score) < MARGIN:
        return None, best_score

    return best_match, best_score