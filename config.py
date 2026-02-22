r"""
config.py
-------------------------------------
Centralised configuration file for the IT Support Ticket Analysis project.

This module defines:
- Directory paths for data, notebooks, and supporting outputs
- Auto-creation of subfolders (images, CSVs, models, etc.)
- Consistent references for intermediate artefacts across notebooks
- Modelling parameters (clustering, visualisation, reproducibility)

Usage:
    from config import Config
    df = pd.read_csv(Config.RAW_DATA_PATH)
    plt.savefig(Config.TEXT_IMG_DIR / "stage5_tsne.png")

Project root: C:\Users\David\Desktop\Python_Files\IT-Support-Ticket-Analysis
"""

from pathlib import Path
import os


class Config:
    # ==============================================================
    # 1. Base Paths
    # ==============================================================
    BASE_DIR = Path(r"C:\Users\David\Desktop\Python_Files\IT-Support-Ticket-Analysis")

    DATA_DIR = BASE_DIR / "Data"
    NOTEBOOKS_DIR = BASE_DIR / "Notebooks"
    SUPPORTING_DOCS_DIR = BASE_DIR / "Supporting_Documents"

    # ==============================================================
    # 2. Supporting Documents Substructure
    # ==============================================================
    # Quality Checks
    QC_DIR = SUPPORTING_DOCS_DIR / "00_Quality_Checks"
    QC_OUTPUT_DIR = QC_DIR / "OUTPUTS"

    # Representative Checks
    REP_DIR = SUPPORTING_DOCS_DIR / "01_Representativeness_Checks"
    REP_IMG_DIR = REP_DIR / "Images"
    REP_CSV_DIR = REP_DIR / "CSV"

    # Text Analytics
    TEXT_DIR = SUPPORTING_DOCS_DIR / "02_Text_Analytics"
    TEXT_IMG_DIR = TEXT_DIR / "Images"
    TEXT_CSV_DIR = TEXT_DIR / "CSV"

    # Master output folder for shared artefacts (optional)
    # OUTPUT_DIR = BASE_DIR / "Outputs"
    # MODELS_DIR = OUTPUT_DIR / "Models"
    # LOGS_DIR = OUTPUT_DIR / "Logs"

    # ==============================================================
    # 3. Data Files
    # ==============================================================
    RAW_DATA_PATH = DATA_DIR / "IT_Tickets_Raw.csv"
    CLEAN_CSV_PATH = QC_OUTPUT_DIR / "Tickets_Clean.csv"
    CLEAN_PARQUET_PATH = QC_OUTPUT_DIR / "Tickets_Clean.parquet"

    # Intermediate artefacts
    # TFIDF_MATRIX_PATH = TEXT_CSV_DIR / "tfidf_matrix.pkl"
    # TFIDF_FEATURES_PATH = TEXT_CSV_DIR / "tfidf_features.txt"

    # Clustering outputs
    # KMEANS_METRICS_PATH = TEXT_CSV_DIR / "kmeans_metrics_by_k.csv"
    # OPTIMAL_K_PATH = TEXT_CSV_DIR / "kmeans_optimal_k_by_threshold.csv"
    # CHOSEN_K_PATH = TEXT_CSV_DIR / "chosen_optimal_k.txt"
    # CLUSTER_LABELS_PATH = TEXT_CSV_DIR / "cluster_labels_summary.csv"
    # ACTIONABILITY_PATH = TEXT_CSV_DIR / "cluster_actionability_summary.csv"

    # Visual outputs
    # PCA_FIG_PATH = TEXT_IMG_DIR / "stage5_pca.png"
    # TSNE_FIG_PATH = TEXT_IMG_DIR / "stage5_tsne.png"
    # SILHOUETTE_FIG_PATH = TEXT_IMG_DIR / "stage3_silhouette.png"

    # ==============================================================
    # 4. Clustering Parameters
    # ==============================================================
    RANDOM_STATE = 42
    K_SEARCH_RANGE = range(20, 81)
    THRESHOLD_PERCENTS = [0.01, 0.015, 0.02]
    MAX_FEATURES = 5000
    MIN_DF = 3
    MAX_DF = 0.7

    # ==============================================================
    # 5. Visualisation Parameters
    # ==============================================================
    PCA_COMPONENTS = 2
    TSNE_COMPONENTS = 2
    TSNE_PERPLEXITY = 35
    TSNE_LEARNING_RATE = 200
    TSNE_ITER = 750
    TSNE_METRIC = "cosine"

    # ==============================================================
    # 6. Utility: Ensure folder structure exists
    # ==============================================================
    @classmethod
    def ensure_directories(cls):
        """Create all directories if they don’t already exist."""
        dirs = [
            cls.QC_OUTPUT_DIR,
            cls.REP_IMG_DIR,
            cls.REP_CSV_DIR,
            cls.TEXT_IMG_DIR,
            cls.TEXT_CSV_DIR,
            # cls.OUTPUT_DIR,
            # cls.MODELS_DIR,
            # cls.LOGS_DIR,
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

        print(f"[Config] Verified project directory structure under {cls.BASE_DIR}")


# ----------------------------------------------------------------------
# Auto-run directory check on import (optional but convenient)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Config.ensure_directories()
