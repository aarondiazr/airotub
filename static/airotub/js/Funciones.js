function youtube_parser(url){
    var regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
    var match = url.match(regExp);
    if (match&&match[2].length==11){
        return match[2];
    }
    else{
        //error
    }
}

function TraerVideo(){
		var id = youtube_parser(document.getElementById('Busqueda').value)
		$.get( "getinf/"+id, function(data) {
				//console.log($('#youtube', data).html());
				$( "#video" ).hide().html($('#youtube', data).html());
				$( "#video" ).fadeIn("slow");
		})
		.fail(function() {
		    console.log("Error");
		 });

}