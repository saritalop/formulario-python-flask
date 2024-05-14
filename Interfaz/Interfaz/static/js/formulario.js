 // Obtener todos los botones de eliminar campo
 var eliminarBotones = document.querySelectorAll('.eliminar-campo');
 // Agregar un evento de clic a cada botón
 eliminarBotones.forEach(function(boton) {
     boton.addEventListener('click', function() {
         // Obtener el campo asociado al botón de eliminar
         var campoId = this.getAttribute('data-campo');
         var campo = document.getElementById('campo_' + campoId);
         // Eliminar el campo y su botón de eliminar del formulario
         campo.parentNode.removeChild(campo);
     });
 });
 
 // Función para agregar campos adicionales al formulario
function agregarNuevoCampo() {
     var nuevoCampoContainer = document.getElementById('nuevo-campo-container');
     // Toggle para mostrar u ocultar el contenedor de nuevo campo
     nuevoCampoContainer.style.display = (nuevoCampoContainer.style.display === 'none') ? 'block' : 'none';
 }

 // Agrega un event listener para el botón "Añadir Nuevo Campo"
 document.getElementById('btn-nuevo-campo').addEventListener('click', agregarNuevoCampo);

// Función para mostrar u ocultar los detalles del formulario
var detalleInfo = document.getElementById('detalle-info');
 document.getElementById('btn-detalle').addEventListener('click', function() {
     if (detalleInfo.style.display === 'none') {
         detalleInfo.style.display = 'block';
     } else {
         detalleInfo.style.display = 'none';
     }
 });
 
 // Función para mostrar alerta cuando se guarde el formulario
 var alertSave = document.getElementById('btn-guardar');
  document.getElementById('btn-guardar').addEventListener('click', function() {
         alert("¡Guardado Correctamente!");
  });