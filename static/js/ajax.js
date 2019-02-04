$(document).ready(function(){
  $("#form_Buscar_testimonios").submit(function(e){
      e.preventDefault();
      var palabra_buscar = $("#buscar_testimonio").val();
      alert("Entro al evento " + palabra_buscar);
      $.ajax({ 
        type: 'GET', 
        url: '/testimonios_filter', 
         //data: $(this).serialize(), 
        success: function(data){
          $("content_testimonios").html(data);
          console.log(data);
        } 

      }); // end new Ajax.Request 
  });
});