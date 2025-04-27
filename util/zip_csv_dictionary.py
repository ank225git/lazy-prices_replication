import shutil

shutil.make_archive(
    base_name="../data/processed/full_docdict",
    format="zip",
    root_dir="../data/processed",
    base_dir="full_docdict.csv"
)
