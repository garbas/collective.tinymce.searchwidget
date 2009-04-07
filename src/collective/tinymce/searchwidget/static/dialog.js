tinyMCEPopup.requireLangPack();

var SearchWidgetDialog = {
	init : function() {
		var f = document.forms[0];

		// Get the selected contents as text and place it in the input
		//f.someval.value = tinyMCEPopup.editor.selection.getContent({format : 'text'});
		//f.somearg.value = tinyMCEPopup.getWindowArg('some_custom_arg');
	},

	insert : function() {
		// Insert the contents from the input into the document
		tinyMCEPopup.editor.execCommand('mceInsertRawHTML', false, '<img src="folder_icon.gif" />');
		tinyMCEPopup.close();
	}
};

tinyMCEPopup.onInit.add(SearchWidgetDialog.init, SearchWidgetDialog);
