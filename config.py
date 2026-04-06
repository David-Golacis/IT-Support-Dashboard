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
    # 1. Base Paths
    BASE_DIR = Path(r"C:\Users\David\Desktop\Python_Files\IT-Support-Ticket-Analysis")

    DATA_DIR = BASE_DIR / "Data"
    NOTEBOOKS_DIR = BASE_DIR / "Notebooks"
    SUPPORTING_DOCS_DIR = BASE_DIR / "Supporting_Documents"

    # 2. Supporting Documents Substructure
    # Quality Checks
    QC_DIR = SUPPORTING_DOCS_DIR / "00_Quality_Checks"

    # Representative Checks
    REP_DIR = SUPPORTING_DOCS_DIR / "01_Representativeness_Checks"
    REP_IMG_DIR = REP_DIR / "Images"
    REP_SHEETS_DIR = REP_DIR / "Spreadsheets"

    # Lemmatisation
    LEMMA_DIR = SUPPORTING_DOCS_DIR / "02_Lemmatisation"
    LEMMA_IMG_DIR = LEMMA_DIR / "Images"
    LEMMA_SHEETS_DIR = LEMMA_DIR / "Spreadsheets"

    # Clustering
    CLUST_DIR = SUPPORTING_DOCS_DIR / "03_Clustering"
    CLUST_IMG_DIR = CLUST_DIR / "Images"
    CLUST_SHEETS_DIR = CLUST_DIR / "Spreadsheets"

    # 3. Data Files
    RAW_DATA_PATH = DATA_DIR / "IT_Tickets_Raw.csv"

    # Quality checks outputs
    NULL_ANSWERS_PATH = QC_DIR / "01_Null_Answers.csv"
    INVALID_TAGS_PATH = QC_DIR / "02_Invalid_Tags.csv"
    VALIDATED_TAGS_PATH = QC_DIR / "03_Validated_Tags.csv"
    CLEAN_CSV_PATH = QC_DIR / "04_Tickets_Clean.csv"
    CLEAN_PARQUET_PATH = QC_DIR / "04_Tickets_Clean.parquet"

    # Representativeness checks outputs
    ENGLISH_CSV_PATH = REP_SHEETS_DIR / "01_English_Tickets.csv"
    ABSOLUTE_SHIFT_PATH = REP_SHEETS_DIR / "06_Distribution_Shift_Summary.csv"
    VISUAL_PARAMS_PATH = REP_SHEETS_DIR / "07_Visual_Parameters.csv"
    STATISTICAL_SUMMARY_PATH = REP_SHEETS_DIR / "08_Statistical_Summary.csv"
    ENGLISH_PARQUET_PATH = REP_SHEETS_DIR / "01_English_Tickets.parquet"

    # Lemmatisation outputs
    TFIDF_MATRIX_PATH = LEMMA_SHEETS_DIR / "01_TFIDF_Matrix.parquet"
    LEMMATISED_PATH = LEMMA_SHEETS_DIR / "02_Lemmatized.csv"
    LEMMA_SUMMARY_PATH = LEMMA_SHEETS_DIR / "03_Lemma_Summary.csv"
    KDE_PATH = LEMMA_IMG_DIR / "01_Lemma_Similarity_KDE.png"
    RIGHT_TAIL_PATH = LEMMA_IMG_DIR / "02_Right_Tail_Similarity.png"
    CAT_RECURRENCE_CSV_PATH = LEMMA_SHEETS_DIR / "04_Category_Recurrence.csv"
    IMPACT_BARPLOT_PATH = LEMMA_IMG_DIR / "03_Impact_Barplot.png"
    IMPACT_LINEPLOT_PATH = LEMMA_IMG_DIR / "04_Impact_Lineplot.png"
    IMPACT_DOTPLOT_PATH = LEMMA_IMG_DIR / "05_Impact_Dotplot.png"

    # Clustering outputs
    KMEANS_CSV_PATH = CLUST_SHEETS_DIR / "04_KMeans_Clustering_Metrics.csv"
    KMEANS_PARQUET_PATH = CLUST_SHEETS_DIR / "04_KMeans_Clustering_Metrics.parquet"
    OPTIMAL_K_PATH = CLUST_SHEETS_DIR / "05_Optimal_K_By_Threshold.csv"
    SCATTERPLOT_PATH = CLUST_IMG_DIR / "05_Silhouette_Scores_Across_K.png"
    OPTIMAL_SCORE_PATH = CLUST_SHEETS_DIR / "06_Optimal_K_By_Score.csv"
    CLUSTER_LABELS_PATH = CLUST_SHEETS_DIR / "07_Cluster_Labels.csv"

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
            cls.DATA_DIR,
            cls.NOTEBOOKS_DIR,
            cls.SUPPORTING_DOCS_DIR,
            cls.QC_DIR,
            cls.REP_DIR,
            cls.REP_IMG_DIR,
            cls.REP_SHEETS_DIR,
            cls.LEMMA_DIR,
            cls.LEMMA_IMG_DIR,
            cls.LEMMA_SHEETS_DIR,
            cls.CLUST_DIR,
            cls.CLUST_IMG_DIR,
            cls.CLUST_SHEETS_DIR,
        ]
        for d in dirs:
            os.makedirs(d, exist_ok=True)

        print(f"[Config] Verified project directory structure under {cls.BASE_DIR}")


# ----------------------------------------------------------------------
# Auto-run directory check on import (optional but convenient)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    Config.ensure_directories()
