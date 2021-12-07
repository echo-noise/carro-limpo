const buttonPrintOrSaveDocument = document.querySelector(
	".button-print-or-save-document"
);

function printOrSave() {
	window.print();
}

buttonPrintOrSaveDocument.addEventListener("click", printOrSave);