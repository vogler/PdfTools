PdfTools
========

### Usage

Install [pyPdf](http://pybrary.net/pyPdf/).


compactify.py
-------------

Compacts the input pdfs for printing by removing superflous animated pages.

Usage:

    python compactify.py <inputfile(s)>

Example:

    python compactify.py lecture1.pdf lecture2.pdf

    title = folien.dvi
    lecture1.pdf has 43 pages.
    lecture1-compact.pdf has 22 pages.
    -> removed 21 pages

    title = folien.dvi
    lecture2.pdf has 81 pages.
    lecture2-compact.pdf has 38 pages.
    -> removed 43 pages


crop.py
-------------

Extracts slides from pdfs with multiple slides per page...
Position and dimension of slides on page are defined in the code.

Usage:

    python crop.py <inputfile(s)>
