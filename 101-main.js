$(function(){
	$('DIV#add_item').click(()=>$('<li>Item</li>').appendTo('UL.my_list'));
	$('DIV#remove_item').click(()=>$('ul.my_list li: last').remove());
	$('DIV#add_item').click(()=>$('ul.my_list').empty());
});
