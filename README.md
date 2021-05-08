# DuPDF: Renaming PDFs by titles in Batch.

Renames PDF files of the same directory based on title.
It relies on `pdftitle` which obtains the title of a file by `pdfminer`.

Run once:

```sh
git clone git@github.com:ruofeidu/DuPDF.git --recurse-submodules
pip install pdftitle
pip install pdfminer
```

Run:

```sh
python dupdf
```

to batch process a directory.
